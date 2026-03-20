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
import { store, allQuestions, allSources, clearQuizResults } from '../store'

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

function resetAll() {
  if (confirm('確定要重置所有作答記錄嗎？')) clearQuizResults()
}
</script>
