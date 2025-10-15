<template>
  <div class="max-md">
    <p class="fw-bold fs-3 text-primary m-0 mb-2">
      <slot></slot>
    </p>
    <p class="m-0" v-if="$slots.subtitle">
      <slot name="subtitle"></slot>
    </p>
  </div>
</template>