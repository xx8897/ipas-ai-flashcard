<template>
  <div class="space-y-6">
    <!-- Header -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-bold text-white">🃏 圖卡翻轉模式</h1>
        <p class="text-slate-400 text-sm mt-1">題目 {{ currentIndex + 1 }} / {{ questions.length }}</p>
      </div>
      <div class="flex gap-2">
        <button @click="toggleShuffle" :class="['px-3 py-1.5 rounded-lg text-sm transition-all border',
          store.shuffle ? 'bg-indigo-500/30 border-indigo-400 text-indigo-300' : 'border-white/10 text-slate-400']">
          🔀
        </button>
        <button @click="restart" class="px-3 py-1.5 rounded-lg text-sm border border-white/10 text-slate-400 hover:text-white transition-all">
          ↩ 重置
        </button>
      </div>
    </div>

    <!-- Progress bar -->
    <div class="h-1.5 rounded-full bg-white/10 overflow-hidden">
      <div class="h-full bg-gradient-to-r from-indigo-500 to-purple-500 transition-all duration-500"
        :style="{ width: progressPct + '%' }" />
    </div>

    <!-- Empty state -->
    <div v-if="questions.length === 0" class="glass p-12 text-center text-slate-400">
      目前沒有符合篩選條件的題目，請回首頁調整篩選。
    </div>

    <!-- Flashcard -->
    <div v-else class="perspective cursor-pointer select-none" @click="flip" style="height: 380px;">
      <div :class="['flip-card relative w-full h-full', isFlipped ? 'flipped' : '']">
        <!-- Front -->
        <div class="flip-card-front glass absolute inset-0 p-8 flex flex-col justify-between">
          <div class="flex justify-between items-start">
            <span class="text-xs px-2 py-1 rounded-full bg-indigo-500/20 text-indigo-300">{{ current.source }}</span>
            <button @click.stop="toggleBookmark(current.id)"
              class="text-xl transition-transform hover:scale-125"
              :title="isBookmarked(current.id) ? '取消收藏' : '加入收藏'">
              {{ isBookmarked(current.id) ? '⭐' : '☆' }}
            </button>
          </div>
          <div class="flex-1 flex items-center justify-center text-center">
            <p class="text-xl text-white leading-relaxed font-medium">{{ current.text }}</p>
          </div>
          <p class="text-center text-slate-500 text-sm animate-pulse">點擊翻轉查看答案</p>
        </div>

        <!-- Back -->
        <div class="flip-card-back glass absolute inset-0 p-8 flex flex-col gap-4 overflow-y-auto">
          <div class="text-center">
            <span class="text-4xl font-black text-indigo-400">{{ current.answer }}</span>
            <p class="text-green-400 font-semibold mt-1">✅ {{ current.options[current.answer] }}</p>
          </div>
          <div class="text-slate-300 text-sm space-y-1 leading-relaxed">
            <div v-for="(label, key) in current.options" :key="key"
              :class="['flex gap-2', key === current.answer ? 'text-green-400' : 'text-slate-500']">
              <span class="font-mono font-bold shrink-0">({{ key }})</span>
              <span>{{ label }}</span>
            </div>
          </div>
          <div v-if="current.explanation" class="text-slate-400 text-sm border-t border-white/10 pt-3">
            💡 {{ current.explanation }}
          </div>
        </div>
      </div>
    </div>

    <!-- Navigation -->
    <div class="flex justify-between items-center">
      <button @click="prev" :disabled="currentIndex === 0"
        class="px-5 py-2.5 glass rounded-xl text-slate-300 hover:text-white disabled:opacity-30 disabled:cursor-not-allowed transition-all">
        ← 上一題
      </button>
      <span class="text-slate-500 text-sm">{{ doneCount }} / {{ questions.length }} 已翻閱</span>
      <button @click="next" :disabled="currentIndex === questions.length - 1"
        class="px-5 py-2.5 glass rounded-xl text-slate-300 hover:text-white disabled:opacity-30 disabled:cursor-not-allowed transition-all">
        下一題 →
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { store, getFilteredQuestions, isBookmarked, toggleBookmark } from '../store'

const questions = ref([])
const currentIndex = ref(0)
const isFlipped = ref(false)
const seenSet = ref(new Set())

function load() {
  questions.value = getFilteredQuestions()
  currentIndex.value = 0
  isFlipped.value = false
  seenSet.value = new Set()
}
onMounted(load)

const current = computed(() => questions.value[currentIndex.value] || {})
const progressPct = computed(() => questions.value.length
  ? ((currentIndex.value + 1) / questions.value.length) * 100 : 0)
const doneCount = computed(() => seenSet.value.size)

function flip() {
  isFlipped.value = !isFlipped.value
  if (isFlipped.value) seenSet.value.add(current.value.id)
}

function next() {
  if (currentIndex.value < questions.value.length - 1) {
    currentIndex.value++
    isFlipped.value = false
  }
}

function prev() {
  if (currentIndex.value > 0) {
    currentIndex.value--
    isFlipped.value = false
  }
}

function restart() {
  load()
}

function toggleShuffle() {
  store.shuffle = !store.shuffle
  load()
}
</script>
