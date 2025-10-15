<script setup>
import { useFormValidation } from '@/composables/useFormValidation';

const emit = defineEmits([
  'onSubmit',
])

const { validateForm } = useFormValidation(e => emit('onSubmit', e))
</script>

<template>
  <form novalidate @submit.prevent="validateForm">
    <slot></slot>
  </form>
</template>