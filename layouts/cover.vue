<template>
  <div class="slidev-layout cover">
    <div class="cover-mark">IA para estudiar</div>
    <div class="cover-content">
      <slot />
    </div>
    <div class="cover-author">
      <p>{{ author }}</p>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client/context.ts'

const props = defineProps({
  author: {
    type: String,
    default: '',
  },
})

const { $frontmatter } = useSlideContext()

const author = computed(
  () => props.author || $frontmatter?.value?.author || $frontmatter?.author || 'Sergi García Barea',
)
</script>
