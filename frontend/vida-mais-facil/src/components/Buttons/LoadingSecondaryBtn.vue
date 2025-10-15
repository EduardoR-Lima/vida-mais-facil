<script setup>
const props = defineProps({
  state: {
    type: Object,
    required: true
  }
})

</script>

<template>
  <button
    class="btn btn-secondary px-4 py-3 fw-bold text-white fs-6"
    :disabled="state.isLoading()">
    
    <template v-if="state.isLoading()">
      <span
        class="spinner-border spinner-border-sm me-1"
        aria-hidden="true">
      </span>
      <span role="status">
        <slot name="fallback">
          Enviando...
        </slot>
      </span>
    </template>

    <template v-else>
      <slot></slot>
    </template>
  </button>
</template>