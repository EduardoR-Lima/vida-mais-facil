<script setup lang="ts">
import BaseCard from '../Cards/BaseCard.vue';

const props = defineProps({
  rows: {
    type: Number,
    required: false,
    default: 3
  }
})

</script>

<template>
  <BaseCard>
    <div class="vstack pb-3 p-2">
      <div class="hstack justify-content-between p-3">
        <slot name="header"></slot>
      </div>
      
      <!-- A altura de cada row é calculada considerando um componente
       TableCell com uma única linha. Os valores utilizados (como 3.5)
       são aproximações e foram obtidos através de experimentação -->
      <div
        class="vstack p-3 gap-3 overflow-auto"
        :style="{'height': `${1.5 + 3.5*rows}rem`}">
        <slot></slot>
      </div>

    </div>
  </BaseCard>
</template>