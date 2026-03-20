<template>
  <div class="space-y-6">
    <h1 class="text-2xl font-bold text-white">📌 錯題 / 收藏複習</h1>

    <!-- Tabs -->
    <div class="flex gap-2">
      <button @click="mode = 'wrong'" :class="tabClass(mode === 'wrong', 'red')">
        ❌ 錯題 ({{ wrongList.length }})
      </button>
      <button @click="mode = 'bookmark'" :class="tabClass(mode === 'bookmark', 'yellow')">
        ⭐ 收藏 ({{ bookmarkList.length }})
      </button>
    </div>

    <!-- Empty -->
    <div v-if="displayList.length === 0" class="glass p-10 text-center text-slate-400">
      {{ mode === 'wrong' ? '目前沒有錯題。去測驗模式答答看吧！' : '尚未收藏任何題目。在圖卡或測驗中按 ☆ 收藏。' }}
    </div>

    <!-- List -->
    <div v-else class="space-y-4">
      <div v-for="q in displayList" :key="q.id" class="glass p-5 space-y-3">
        <div class="flex justify-between gap-3">
          <p class="text-white font-medium leading-relaxed flex-1">{{ q.text }}</p>
          <button @click="toggleBookmark(q.id)" class="text-xl shrink-0 hover:scale-125 transition-transform">
            {{ isBookmarked(q.id) ? '⭐' : '☆' }}
          </button>
        </div>
        <div class="space-y-1">
          <div v-for="(label, key) in q.options" :key="key"
            :class="['flex gap-2 text-sm', key === q.answer ? 'text-green-400 font-medium' : 'text-slate-500']">
            <span class="font-mono shrink-0">({{ key }})</span>{{ label }}
          </div>
        </div>
        <p v-if="q.explanation" class="text-slate-400 text-sm border-t border-white/10 pt-2">
          💡 {{ q.explanation }}
        </p>
      </div>
    </div>

    <!-- Clear buttons -->
    <div v-if="displayList.length > 0" class="flex justify-end">
      <button v-if="mode === 'wrong'" @click="clearWrong"
        class="text-sm text-slate-500 hover:text-red-400 transition-colors">
        清除所有錯題記錄
      </button>
      <button v-if="mode === 'bookmark'" @click="clearBookmarks"
        class="text-sm text-slate-500 hover:text-red-400 transition-colors">
        清除所有收藏
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { store, getWrongQuestions, getBookmarkedQuestions, isBookmarked, toggleBookmark, clearQuizResults } from '../store'

const mode = ref('wrong')

const wrongList = computed(() => getWrongQuestions())
const bookmarkList = computed(() => getBookmarkedQuestions())
const displayList = computed(() => mode.value === 'wrong' ? wrongList.value : bookmarkList.value)

function tabClass(active, color) {
  const colors = {
    red: active ? 'bg-red-500/20 border-red-400 text-red-300' : 'border-white/10 text-slate-400',
    yellow: active ? 'bg-yellow-500/20 border-yellow-400 text-yellow-300' : 'border-white/10 text-slate-400',
  }
  return ['px-4 py-2 rounded-xl border text-sm transition-all', colors[color]]
}

function clearWrong() {
  if (confirm('確定要清除所有錯題記錄嗎？')) clearQuizResults()
}

function clearBookmarks() {
  if (confirm('確定要清除所有收藏嗎？')) store.bookmarks = []
}
</script>
