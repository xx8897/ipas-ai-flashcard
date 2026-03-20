<template>
  <div class="space-y-8">
    <!-- Hero -->
    <div class="text-center py-10">
      <div class="text-6xl mb-4">🧠</div>
      <h1 class="text-4xl font-bold text-white mb-3">iPAS AI 應用規劃師</h1>
      <p class="text-slate-400 text-lg">互動式題庫複習系統 — <span class="text-indigo-400">{{ allQuestions.length }}</span> 道題目</p>
    </div>

    <!-- Filter Panel -->
    <div class="glass p-6 space-y-5">
      <h2 class="text-lg font-semibold text-indigo-300 flex items-center gap-2">
        <span>⚙️</span> 篩選設定
      </h2>

      <!-- Source filter -->
      <div>
        <p class="text-sm text-slate-400 mb-2">題庫來源</p>
        <div class="flex flex-wrap gap-2">
          <button v-for="s in allSources" :key="s"
            @click="toggleSource(s)"
            :class="['px-3 py-1.5 rounded-full text-sm border transition-all',
              store.selectedSources.includes(s)
                ? 'bg-indigo-500/30 border-indigo-400 text-indigo-200'
                : 'border-white/10 text-slate-400 hover:border-white/30']">
            {{ s }}
          </button>
        </div>
      </div>

      <!-- Subject filter -->
      <div>
        <p class="text-sm text-slate-400 mb-2">科目</p>
        <div class="flex flex-wrap gap-2">
          <button v-for="s in allSubjects" :key="s"
            @click="toggleSubject(s)"
            :class="['px-3 py-1.5 rounded-full text-sm border transition-all',
              store.selectedSubjects.includes(s)
                ? 'bg-purple-500/30 border-purple-400 text-purple-200'
                : 'border-white/10 text-slate-400 hover:border-white/30']">
            {{ s }}
          </button>
        </div>
      </div>

      <!-- Options row -->
      <div class="flex items-center gap-4">
        <label class="flex items-center gap-2 cursor-pointer">
          <div @click="store.shuffle = !store.shuffle"
            :class="['w-11 h-6 rounded-full transition-colors relative', store.shuffle ? 'bg-indigo-500' : 'bg-white/10']">
            <div :class="['absolute top-0.5 w-5 h-5 rounded-full bg-white transition-transform', store.shuffle ? 'translate-x-5' : 'translate-x-0.5']" />
          </div>
          <span class="text-sm text-slate-300">🔀 隨機出題</span>
        </label>
        <span class="text-slate-500 text-sm ml-auto">已選 {{ filteredCount }} 題</span>
        <button @click="resetFilters" class="text-xs text-slate-500 hover:text-red-400 transition-colors">重置</button>
      </div>
    </div>

    <!-- Quick Actions -->
    <div class="flex gap-4">
      <RouterLink to="/quiz?mode=bookmarked" v-if="bookmarkCount > 0"
        class="flex-1 glass p-4 flex items-center justify-between group hover:border-yellow-400/40 transition-all">
        <div>
          <h3 class="font-bold text-white">⭐ 收藏星號題</h3>
          <p class="text-xs text-slate-400">目前共有 {{ bookmarkCount }} 題</p>
        </div>
        <div class="text-yellow-400 group-hover:translate-x-1 transition-transform">→</div>
      </RouterLink>

      <RouterLink to="/quiz?mode=wrong" v-if="wrongCount > 0"
        class="flex-1 glass p-4 flex items-center justify-between group hover:border-red-400/40 transition-all">
        <div>
          <h3 class="font-bold text-white">🔥 弱點重測 (錯題)</h3>
          <p class="text-xs text-slate-400">目前共有 {{ wrongCount }} 題</p>
        </div>
        <div class="text-red-400 group-hover:translate-x-1 transition-transform">→</div>
      </RouterLink>
    </div>

    <!-- Mode Cards -->
    <div class="grid sm:grid-cols-2 gap-4">
      <RouterLink to="/flashcard" class="glass p-6 hover:border-indigo-400/40 transition-all group block">
        <div class="text-4xl mb-3">🃏</div>
        <h3 class="text-xl font-bold text-white mb-1">圖卡翻轉模式</h3>
        <p class="text-slate-400 text-sm">點擊卡片翻轉查看解答，可標記不熟的題目</p>
        <div class="mt-4 text-indigo-400 text-sm group-hover:text-indigo-300">開始 →</div>
      </RouterLink>

      <RouterLink to="/quiz" class="glass p-6 hover:border-purple-400/40 transition-all group block">
        <div class="text-4xl mb-3">✍️</div>
        <h3 class="text-xl font-bold text-white mb-1">四選一測驗模式</h3>
        <p class="text-slate-400 text-sm">即時顯示正確/錯誤，自動記錄錯題</p>
        <div class="mt-4 text-purple-400 text-sm group-hover:text-purple-300">開始 →</div>
      </RouterLink>

      <RouterLink to="/review" class="glass p-6 hover:border-amber-400/40 transition-all group block">
        <div class="text-4xl mb-3">📌</div>
        <h3 class="text-xl font-bold text-white mb-1">錯題 / 收藏複習</h3>
        <p class="text-slate-400 text-sm">
          錯題 <span class="text-red-400">{{ wrongCount }}</span> 道・收藏 <span class="text-yellow-400">{{ bookmarkCount }}</span> 道
        </p>
        <div class="mt-4 text-amber-400 text-sm group-hover:text-amber-300">開始 →</div>
      </RouterLink>

      <RouterLink to="/stats" class="glass p-6 hover:border-green-400/40 transition-all group block">
        <div class="text-4xl mb-3">📊</div>
        <h3 class="text-xl font-bold text-white mb-1">統計儀表板</h3>
        <p class="text-slate-400 text-sm">查看各題庫的答題正確率</p>
        <div class="mt-4 text-green-400 text-sm group-hover:text-green-300">查看 →</div>
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { RouterLink } from 'vue-router'
import {
  store, allQuestions, allSources, allSubjects,
  getFilteredQuestions, getWrongQuestions, getBookmarkedQuestions
} from '../store'

const filteredCount = computed(() => getFilteredQuestions().length)
const wrongCount = computed(() => getWrongQuestions().length)
const bookmarkCount = computed(() => getBookmarkedQuestions().length)

function toggleSource(s) {
  const idx = store.selectedSources.indexOf(s)
  if (idx === -1) store.selectedSources.push(s)
  else store.selectedSources.splice(idx, 1)
}

function toggleSubject(s) {
  const idx = store.selectedSubjects.indexOf(s)
  if (idx === -1) store.selectedSubjects.push(s)
  else store.selectedSubjects.splice(idx, 1)
}

function resetFilters() {
  store.selectedSources = []
  store.selectedSubjects = []
}
</script>
