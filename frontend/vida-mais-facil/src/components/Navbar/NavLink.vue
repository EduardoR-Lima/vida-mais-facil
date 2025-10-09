<script setup>
import { useRoute } from 'vue-router';

const props = defineProps({
  to: {
    type: String,
    required: true
  }
})

const route = useRoute()
</script>

<template>
  <RouterLink
    :to
    class="nav-link interactive-element"
    :class="{'active': route.path == to}">
    <slot></slot>
  </RouterLink>
</template>