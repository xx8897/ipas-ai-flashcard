<template>
  <div class="space-y-6">
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-bold text-white">✍️ 四選一測驗</h1>
        <p class="text-slate-400 text-sm mt-1">第 {{ currentIndex + 1 }} 題 / 共 {{ questions.length }} 題</p>
      </div>
      <div class="flex gap-2 text-sm">
        <span class="px-2 py-1 rounded-lg bg-green-500/20 text-green-400">✅ {{ correctCount }}</span>
        <span class="px-2 py-1 rounded-lg bg-red-500/20 text-red-400">❌ {{ wrongCount }}</span>
      </div>
    </div>

    <!-- Progress bar -->
    <div class="h-1.5 rounded-full bg-white/10 overflow-hidden">
      <div class="h-full bg-gradient-to-r from-purple-500 to-pink-500 transition-all duration-500"
        :style="{ width: progressPct + '%' }" />
    </div>

    <!-- Empty state -->
    <div v-if="questions.length === 0" class="glass p-12 text-center text-slate-400">
      沒有符合條件的題目，請回首頁調整篩選。
    </div>

    <!-- Done state -->
    <div v-else-if="isDone" class="glass p-10 text-center space-y-4">
      <div class="text-5xl">🎉</div>
      <h2 class="text-2xl font-bold text-white">本輪測驗完成！</h2>
      <p class="text-slate-300">
        答對 <span class="text-green-400 font-bold text-xl">{{ correctCount }}</span> /
        {{ questions.length }} 題，正確率
        <span class="text-indigo-400 font-bold text-xl">{{ Math.round(correctCount / questions.length * 100) }}%</span>
      </p>
      <div class="flex justify-center gap-3 pt-2">
        <button @click="restart" class="px-5 py-2 glass rounded-xl hover:border-indigo-400/40 text-white transition-all">🔁 再來一次</button>
        <RouterLink to="/review" class="px-5 py-2 glass rounded-xl hover:border-red-400/40 text-white transition-all">📌 複習錯題</RouterLink>
      </div>
    </div>

    <!-- Question card -->
    <div v-else class="glass p-8 space-y-6">
      <div class="flex justify-between items-start gap-4">
        <p class="text-lg text-white font-medium leading-relaxed flex-1">{{ current.text }}</p>
        <button @click="toggleBookmark(current.id)" class="text-xl shrink-0 hover:scale-125 transition-transform">
          {{ isBookmarked(current.id) ? '⭐' : '☆' }}
        </button>
      </div>

      <div class="space-y-2">
        <button v-for="(label, key) in current.options" :key="key"
          :disabled="!!selected"
          @click="select(key)"
          :class="['option-btn w-full text-left px-4 py-3 rounded-xl border border-white/10 text-slate-200 flex gap-3 items-start',
            selected ? (key === current.answer ? 'correct' : (key === selected ? 'wrong' : 'opacity-40')) : '']">
          <span class="font-mono font-bold text-indigo-300 shrink-0">({{ key }})</span>
          <span>{{ label }}</span>
        </button>
      </div>

      <!-- Explanation -->
      <Transition name="slide-fade">
        <div v-if="selected" class="border-t border-white/10 pt-4 space-y-2">
          <p v-if="current.explanation" class="text-slate-400 text-sm leading-relaxed">💡 {{ current.explanation }}</p>
          <div class="flex justify-end">
            <button @click="next" class="px-5 py-2 bg-indigo-500 hover:bg-indigo-600 text-white rounded-xl font-medium transition-colors">
              下一題 →
            </button>
          </div>
        </div>
      </Transition>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { store, getFilteredQuestions, recordQuizResult, isBookmarked, toggleBookmark } from '../store'

const questions = ref([])
const currentIndex = ref(0)
const selected = ref(null)
const isDone = ref(false)
const correctCount = ref(0)
const wrongCount = ref(0)

function load() {
  questions.value = getFilteredQuestions()
  restart()
}
onMounted(load)

const current = computed(() => questions.value[currentIndex.value] || {})
const progressPct = computed(() =>
  questions.value.length ? ((currentIndex.value) / questions.value.length) * 100 : 0)

function select(key) {
  selected.value = key
  const isCorrect = key === current.value.answer
  if (isCorrect) correctCount.value++
  else wrongCount.value++
  recordQuizResult(current.value.id, isCorrect ? 'correct' : 'wrong')
}

function next() {
  if (currentIndex.value < questions.value.length - 1) {
    currentIndex.value++
    selected.value = null
  } else {
    isDone.value = true
  }
}

function restart() {
  currentIndex.value = 0
  selected.value = null
  isDone.value = false
  correctCount.value = 0
  wrongCount.value = 0
  if (store.shuffle) {
    const qs = [...questions.value]
    for (let i = qs.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [qs[i], qs[j]] = [qs[j], qs[i]]
    }
    questions.value = qs
  }
}
</script>
