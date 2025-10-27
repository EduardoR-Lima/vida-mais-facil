<script setup>
const props = defineProps({
  id: {
    type: String,
    required: true
  }
})

</script>

<template>
  <div :id class="modal fade" tabindex="-1" :aria-labelledby="id + 'Label'" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" :id="id + 'Label'">
            <slot name="title"></slot>
          </h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fechar">
          </button>
        </div>
        <div class="modal-body d-flex flex-column pt-3 px-4 pb-4">
          <slot></slot>
        </div>
      </div>
    </div>
  </div>
</template>