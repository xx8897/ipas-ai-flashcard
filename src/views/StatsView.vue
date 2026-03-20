<template>
  <div class="space-y-6">
    <h1 class="text-2xl font-bold text-white">📊 統計儀表板</h1>

    <!-- Total summary -->
    <div class="grid grid-cols-3 gap-4">
      <div class="glass p-4 text-center">
        <p class="text-3xl font-black text-white">{{ totalAnswered }}</p>
        <p class="text-slate-400 text-sm mt-1">已作答</p>
      </div>
      <div class="glass p-4 text-center">
        <p class="text-3xl font-black text-green-400">{{ totalCorrect }}</p>
        <p class="text-slate-400 text-sm mt-1">答對</p>
      </div>
      <div class="glass p-4 text-center">
        <p class="text-3xl font-black text-red-400">{{ totalWrong }}</p>
        <p class="text-slate-400 text-sm mt-1">答錯</p>
      </div>
    </div>

    <!-- Accuracy bar -->
    <div v-if="totalAnswered > 0" class="glass p-5 space-y-3">
      <div class="flex justify-between text-sm">
        <span class="text-slate-300">整體正確率</span>
        <span class="text-white font-bold">{{ Math.round(totalCorrect / totalAnswered * 100) }}%</span>
      </div>
      <div class="h-3 rounded-full bg-white/10 overflow-hidden">
        <div class="h-full bg-gradient-to-r from-green-500 to-emerald-400 transition-all duration-700"
          :style="{ width: Math.round(totalCorrect / totalAnswered * 100) + '%' }" />
      </div>
    </div>

    <!-- Per source breakdown -->
    <div class="space-y-3">
      <h2 class="text-lg font-semibold text-slate-300">各題庫來源</h2>
      <div v-for="row in sourceStats" :key="row.source" class="glass p-4 space-y-2">
        <div class="flex justify-between items-center">
          <span class="text-white text-sm font-medium">{{ row.source }}</span>
          <span class="text-xs text-slate-400">{{ row.answered }} / {{ row.total }} 題</span>
        </div>
        <div class="h-2 rounded-full bg-white/10 overflow-hidden">
          <div class="h-full transition-all duration-700"
            :class="row.pct >= 80 ? 'bg-green-500' : row.pct >= 60 ? 'bg-yellow-500' : 'bg-red-500'"
            :style="{ width: row.pct + '%' }" />
        </div>
        <p class="text-xs text-right text-slate-500">正確率 {{ row.pct }}%</p>
      </div>
    </div>

    <!-- No data -->
    <div v-if="totalAnswered === 0" class="glass p-10 text-center text-slate-400">
      尚未作答任何題目。去測驗模式練習看看吧！
    </div>

    <!-- Sync section -->
    <div class="glass p-5 space-y-4">
      <div class="flex items-center gap-3">
        <div class="p-2 bg-blue-500/20 rounded-lg">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4" />
          </svg>
        </div>
        <div>
          <h2 class="text-white font-bold leading-tight">跨裝置同步進度</h2>
          <p class="text-xs text-slate-400 mt-1">您可以將目前的錯題與收藏分享到手機或其他連結。</p>
        </div>
      </div>

      <div class="grid grid-cols-2 gap-3">
        <button 
          @click="copySyncLink"
          class="flex items-center justify-center gap-2 py-2.5 bg-slate-800 hover:bg-slate-700 text-white text-sm rounded-lg transition-all border border-white/5"
        >
          <span>🔗 複製同步連結</span>
        </button>
        <button 
          @click="sendSyncEmail"
          class="flex items-center justify-center gap-2 py-2.5 bg-blue-600 hover:bg-blue-500 text-white text-sm rounded-lg font-bold transition-all shadow-lg shadow-blue-900/20"
        >
          <span>📧 寄送到信箱</span>
        </button>
      </div>
    </div>

    <!-- Reset button -->
    <div class="flex justify-end">
      <button @click="resetAll" class="text-sm text-slate-500 hover:text-red-400 transition-colors">
        重置所有作答記錄
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { store, allQuestions, allSources, clearQuizResults, exportState } from '../store'

const results = computed(() => store.quizResults)

const totalAnswered = computed(() => Object.keys(results.value).length)
const totalCorrect = computed(() => Object.values(results.value).filter(v => v === 'correct').length)
const totalWrong = computed(() => Object.values(results.value).filter(v => v === 'wrong').length)

const sourceStats = computed(() => allSources.map(source => {
  const qs = allQuestions.filter(q => q.source === source)
  const answered = qs.filter(q => results.value[q.id]).length
  const correct = qs.filter(q => results.value[q.id] === 'correct').length
  const pct = answered > 0 ? Math.round(correct / answered * 100) : 0
  return { source, total: qs.length, answered, correct, pct }
}))

function getSyncUrl() {
  const data = exportState()
  const base = window.location.origin + window.location.pathname
  return `${base}#/sync?data=${data}`
}

function copySyncLink() {
  const url = getSyncUrl()
  navigator.clipboard.writeText(url).then(() => {
    alert('同步連結已複製到剪貼簿！請將其傳送到您的其他裝置。')
  })
}

function sendSyncEmail() {
  const email = prompt('請輸入您的電子信箱：')
  if (!email) return

  if (/^\S+@\S+\.\S+$/.test(email)) {
    try {
      const url = getSyncUrl()
      const subject = encodeURIComponent('iPAS AI 應用規劃師 - 學習進度同步')
      const body = encodeURIComponent(`您好！\n\n這是在電腦端產生的學習進度同步連結。\n請在手機或其他裝置點擊下方連結以匯入進度：\n\n${url}\n\n(注意：匯入後會覆蓋該裝置原本的進度)`)
      
      // Attempt to open mail app
      window.location.href = `mailto:${email}?subject=${subject}&body=${body}`
      
      // Provide feedback because mailto is silent
      setTimeout(() => {
        alert('已嘗試開啟您的郵件軟體。如果沒有反應，請改用「複製同步連結」手動傳送。')
      }, 500)
    } catch (e) {
      alert('產生連結時發生錯誤，請聯絡開發者。')
    }
  } else {
    alert('請輸入有效的電子信箱。')
  }
}

function resetAll() {
  if (confirm('確定要重置所有作答記錄嗎？')) clearQuizResults()
}
</script>
