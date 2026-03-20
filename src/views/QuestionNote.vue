<template>
  <div class="mt-4">
    <div v-if="!isEditing" @click="isEditing = true" 
      class="group cursor-pointer flex items-start gap-2 p-3 rounded-xl bg-white/5 border border-white/5 hover:border-blue-500/30 transition-all"
    >
      <div class="mt-0.5 text-slate-400 group-hover:text-blue-400">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
        </svg>
      </div>
      <div class="flex-1">
        <p v-if="note" class="text-sm text-slate-300 italic">「 {{ note }} 」</p>
        <p v-else class="text-sm text-slate-500 italic">點擊新增個人筆記或解題心得...</p>
      </div>
    </div>

    <div v-else class="space-y-2">
      <textarea
        v-model="tempNote"
        ref="textareaRef"
        rows="3"
        class="w-full bg-slate-900/80 border border-blue-500/50 rounded-xl p-3 text-sm text-white placeholder-slate-600 focus:outline-none focus:ring-1 focus:ring-blue-500 transition-all font-sans"
        placeholder="在此輸入您的筆記..."
        @blur="handleSave"
      ></textarea>
      <div class="flex justify-between items-center px-1">
        <span class="text-[10px] text-slate-500">自動儲存內容</span>
        <button @click="handleSave" class="text-xs text-blue-400 font-bold hover:text-blue-300">完成編輯</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, nextTick } from 'vue'
import { getNote, saveNote } from '../store'

const props = defineProps({
  questionId: {
    type: Number,
    required: true
  }
})

const isEditing = ref(false)
const note = ref(getNote(props.questionId))
const tempNote = ref(note.value)
const textareaRef = ref(null)

const handleSave = () => {
  saveNote(props.questionId, tempNote.value)
  note.value = tempNote.value
  isEditing.value = false
}

watch(() => props.questionId, (newId) => {
  note.value = getNote(newId)
  tempNote.value = note.value
  isEditing.value = false
})

onMounted(() => {
  watch(isEditing, (val) => {
    if (val) {
      nextTick(() => {
        textareaRef.value?.focus()
      })
    }
  })
})
</script>
