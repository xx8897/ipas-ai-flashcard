import { reactive, watch } from 'vue'

// Load questions
import questionsRaw from './data/questions.json'

const STORAGE_KEY = 'ipas_flashcard_store'

function loadFromStorage() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    if (raw) return JSON.parse(raw)
  } catch {}
  return null
}

function defaultState() {
  return {
    // Filter state
    selectedSources: [],   // empty = all
    selectedSubjects: [],  // empty = all
    shuffle: false,
    // Session progress (quiz mode)
    quizResults: {},       // { [id]: 'correct' | 'wrong' }
    // Bookmarks
    bookmarks: [],         // [id, id, ...]
  }
}

const saved = loadFromStorage()
export const store = reactive(saved ? { ...defaultState(), ...saved } : defaultState())

watch(store, (val) => {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(val))
}, { deep: true })

// Derived helpers
export const allQuestions = questionsRaw

export function getFilteredQuestions() {
  let qs = [...questionsRaw]
  if (store.selectedSources.length > 0) {
    qs = qs.filter(q => store.selectedSources.includes(q.source))
  }
  if (store.selectedSubjects.length > 0) {
    qs = qs.filter(q => store.selectedSubjects.includes(q.subject))
  }
  if (store.shuffle) {
    for (let i = qs.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [qs[i], qs[j]] = [qs[j], qs[i]]
    }
  }
  return qs
}

export function getWrongQuestions() {
  const wrongIds = Object.entries(store.quizResults)
    .filter(([, v]) => v === 'wrong')
    .map(([id]) => Number(id))
  return questionsRaw.filter(q => wrongIds.includes(q.id))
}

export function getBookmarkedQuestions() {
  return questionsRaw.filter(q => store.bookmarks.includes(q.id))
}

export function toggleBookmark(id) {
  const idx = store.bookmarks.indexOf(id)
  if (idx === -1) store.bookmarks.push(id)
  else store.bookmarks.splice(idx, 1)
}

export function isBookmarked(id) {
  return store.bookmarks.includes(id)
}

export function recordQuizResult(id, result) {
  store.quizResults[id] = result
}

export function clearQuizResults() {
  store.quizResults = {}
}

// Sync functionality
export function exportState() {
  const data = {
    quizResults: store.quizResults,
    bookmarks: store.bookmarks
  }
  // Use btoa safely for short data (JSON stringified)
  const json = JSON.stringify(data)
  // btoa doesn't like non-latin chars, but IDs and status should be fine.
  // To be super safe, use encodeURIComponent + btoa
  return btoa(encodeURIComponent(json))
}

export function importState(encodedData) {
  try {
    const json = decodeURIComponent(atob(encodedData))
    const data = JSON.parse(json)
    if (data.quizResults) store.quizResults = data.quizResults
    if (data.bookmarks) store.bookmarks = data.bookmarks
    return true
  } catch (e) {
    console.error('Import failed', e)
    return false
  }
}

// Unique sources / subjects for filter UI
export const allSources = [...new Set(questionsRaw.map(q => q.source))]
export const allSubjects = [...new Set(questionsRaw.map(q => q.subject))]
