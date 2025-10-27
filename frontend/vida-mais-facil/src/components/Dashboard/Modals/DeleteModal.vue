<script setup>
import LoadingSecondaryBtn from '@/components/Buttons/LoadingSecondaryBtn.vue';
import BaseModal from '@/components/Modals/BaseModal.vue';
import { useFormatter } from '@/composables/useFormatter';

const model = defineModel()
const emit = defineEmits(['submit'])

const props = defineProps({
  id: {
    type: String,
    required: true
  },
  isLoading: {
    type: Boolean,
    required: true
  }
})

const { isoDateToBr } = useFormatter()

</script>

<template>
  <BaseModal :id>
    <template #title>
      Confirmar exclusão
    </template>

    <p class="text-center m-0 mb-5">
      Você tem certeza de que gostaria de remover o indicador de
      <span class="text-secondary fw-bold">
        {{ model.tipo }}
      </span>
      do dia
      <span class="text-primary fw-bold">
        {{ isoDateToBr(model.data_registro) }}
      </span>
    </p>

    <LoadingSecondaryBtn :is-loading @click="() => emit('submit')">
      Confirmar
    </LoadingSecondaryBtn>
    
  </BaseModal>
</template>