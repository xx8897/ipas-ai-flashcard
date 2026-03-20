<template>
  <div class="min-h-screen">
    <nav class="glass sticky top-0 z-50 mx-4 mt-4 px-6 py-3 flex items-center justify-between rounded-2xl">
      <RouterLink to="/" class="flex items-center gap-2 text-indigo-300 font-bold text-lg hover:text-white transition-colors">
        <span class="text-2xl">🧠</span>
        <span class="hidden sm:block">iPAS AI 圖卡</span>
      </RouterLink>
      <div class="flex items-center gap-1 text-sm">
        <RouterLink to="/" class="nav-link">首頁</RouterLink>
        <RouterLink to="/flashcard" class="nav-link">圖卡</RouterLink>
        <RouterLink to="/quiz" class="nav-link">測驗</RouterLink>
        <RouterLink to="/review" class="nav-link">錯題</RouterLink>
        <RouterLink to="/stats" class="nav-link">統計</RouterLink>
      </div>
    </nav>
    <main class="container mx-auto px-4 py-6 max-w-4xl">
      <RouterView v-slot="{ Component }">
        <Transition name="slide-fade" mode="out-in">
          <component :is="Component" />
        </Transition>
      </RouterView>
    </main>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
@reference "tailwindcss";
.nav-link {
  @apply px-3 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-white/10 transition-all;
}
.router-link-active.nav-link {
  @apply text-indigo-300 bg-indigo-500/20;
}
</style>
