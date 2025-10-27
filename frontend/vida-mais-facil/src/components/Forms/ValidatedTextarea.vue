<script setup>
const model = defineModel()
const props = defineProps({
  name: {
    type: String,
    required: true,
  }
})

defineOptions({
  inheritAttrs: false,
})
</script>

<template>
  <div>
    <label :for="name" class="form-label">
      <slot name="label"></slot>
    </label>
    <textarea
      class="form-control interactive-element"
      v-bind="$attrs"
      v-model="model"
      :id="name"
      :name>
    </textarea>
    <p class="invalid-feedback m-0" v-if="$slots.feedback">
      <slot name="feedback"></slot>
    </p>
  </div>
</template>