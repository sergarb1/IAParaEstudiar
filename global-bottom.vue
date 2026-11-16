<script setup lang="ts">
import { computed, nextTick, ref, watch } from 'vue'
import { useNav } from '@slidev/client'
import configs from '#slidev/configs'

const nav = useNav()
const audioEl = ref<HTMLAudioElement | null>(null)
const enabled = ref(false)
const playing = ref(false)
const failed = ref(false)

const siteBase = import.meta.env.BASE_URL.replace(/presentaciones\/m\d+\/$/, '')
const src = computed(() => {
  const deck = (configs as Record<string, unknown>).narrationBase
  if (!deck)
    return ''
  const page = String(nav.currentPage.value).padStart(2, '0')
  return `${siteBase}audio/${deck}/${page}.mp3`
})

const visible = computed(() => Boolean((configs as Record<string, unknown>).narrationBase))

async function playCurrent() {
  const audio = audioEl.value
  if (!audio)
    return
  failed.value = false
  try {
    await audio.play()
  }
  catch {
    failed.value = true
  }
}

function blurOnPointer(event: PointerEvent) {
  if (event.pointerType === 'mouse')
    (event.currentTarget as HTMLElement | null)?.blur()
}

async function toggle() {
  if (!enabled.value) {
    enabled.value = true
    await nextTick()
    await playCurrent()
    return
  }
  if (playing.value) {
    audioEl.value?.pause()
    enabled.value = false
    return
  }
  await playCurrent()
}

watch(
  () => nav.currentPage.value,
  async () => {
    failed.value = false
    if (!enabled.value || !visible.value)
      return
    await nextTick()
    await playCurrent()
  },
)

const label = computed(() => {
  if (playing.value)
    return 'Pausar narración'
  if (enabled.value)
    return 'Reanudar narración'
  return 'Escuchar narración'
})
</script>

<template>
  <div v-if="visible" class="narration-dock">
    <audio
      ref="audioEl"
      :src="src"
      preload="none"
      @play="playing = true"
      @pause="playing = false"
      @ended="playing = false"
      @error="failed = true"
    />
    <button
      type="button"
      class="narration-button"
      :class="{ 'is-playing': playing, 'is-failed': failed }"
      :aria-label="label"
      :aria-pressed="enabled"
      :title="label"
      @click="toggle"
      @pointerup="blurOnPointer"
    >
      <span class="narration-icon" aria-hidden="true">{{ failed ? '!' : (playing ? 'Ⅱ' : '▶') }}</span>
      <span class="narration-text">{{ failed ? 'Sin audio' : (playing ? 'Pausar' : 'Narración') }}</span>
    </button>
  </div>
</template>
