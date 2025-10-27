<script setup>
import { useFormValidation } from '@/composables/useFormValidation';

const emit = defineEmits([
  'submit',
])

const { validateForm } = useFormValidation(e => emit('submit', e))
</script>

<template>
  <form novalidate @submit.prevent="validateForm">
    <slot></slot>
  </form>
</template>