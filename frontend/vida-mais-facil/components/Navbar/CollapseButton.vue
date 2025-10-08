<script setup>
import MenuIcon from '../Icons/MenuIcon.vue';

const props = defineProps({
  targetId: {
    type: String,
    required: true
  },
  label: {
    type: String,
    required: true
  }
})

const id = props.targetId.replace('#', '')

</script>

<template>
  <button
    class="navbar-toggler border-0"
    type="button"
    data-bs-toggle="collapse"
    :data-bs-target="'#' + id"
    :aria-controls="id"
    aria-expanded="false"
    :aria-label="label">
    <MenuIcon class="fs-2 text-primary"/>
  </button>
</template>