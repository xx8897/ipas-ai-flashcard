import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import './style.css'

import HomeView from './views/HomeView.vue'
import FlashcardView from './views/FlashcardView.vue'
import QuizView from './views/QuizView.vue'
import ReviewView from './views/ReviewView.vue'
import StatsView from './views/StatsView.vue'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/', component: HomeView },
    { path: '/flashcard', component: FlashcardView },
    { path: '/quiz', component: QuizView },
    { path: '/review', component: ReviewView },
    { path: '/stats', component: StatsView },
  ]
})

createApp(App).use(router).mount('#app')
