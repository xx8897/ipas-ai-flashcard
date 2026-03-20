<template>
  <div class="min-h-screen pt-20 px-4 flex items-center justify-center">
    <div class="glass-card max-w-md w-full p-8 text-center">
      <div class="mb-6">
        <div class="w-20 h-20 bg-blue-500/20 rounded-full flex items-center justify-center mx-auto mb-4">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4" />
          </svg>
        </div>
        <h2 class="text-2xl font-bold mb-2">同步學習進度</h2>
        <p class="text-slate-400">偵測到來自其他裝置的學習記錄（錯題、收藏等）。</p>
      </div>

      <div class="space-y-4">
        <div class="p-4 bg-yellow-500/10 border border-yellow-500/30 rounded-lg text-sm text-yellow-200 text-left">
          ⚠️ 注意：匯入後將會<strong>覆蓋</strong>此裝置目前的學習進度。
        </div>

        <button 
          @click="confirmSync"
          class="w-full py-3 bg-blue-600 hover:bg-blue-500 text-white rounded-xl font-bold transition-all shadow-lg shadow-blue-900/20"
        >
          確認匯入並開啟
        </button>

        <button 
          @click="$router.push('/')"
          class="w-full py-3 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl transition-all"
        >
          取消
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { importState } from '../store'

const route = useRoute()
const router = useRouter()

const confirmSync = () => {
  const data = route.query.data
  if (data) {
    const success = importState(data)
    if (success) {
      alert('進度匯入成功！')
      router.push('/')
    } else {
      alert('無效的同步連結。')
    }
  } else {
    router.push('/')
  }
}
</script>
