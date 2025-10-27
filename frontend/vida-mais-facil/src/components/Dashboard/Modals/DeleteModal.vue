<script setup>
import LoadingSecondaryBtn from '@/components/Buttons/LoadingSecondaryBtn.vue';
import BaseModal from '@/components/Modals/BaseModal.vue';
import { useApiFetch } from '@/composables/useApiFetch';
import { useFormatter } from '@/composables/useFormatter';
import { useToast } from '@/composables/useToast';
import { Modal } from 'bootstrap';

const model = defineModel()
const emit = defineEmits(['success'])

const props = defineProps({
  id: {
    type: String,
    required: true
  }
})

const { isoDateToBr } = useFormatter()

// Lógica de comunicação com a api. Por enquanto está acoplada diretamente
// no modal por ser muito especifica, mas o ideal é generalizar ou mover
// ela para fora do componente
const api = useApiFetch()
const toast = useToast()

async function onSubmit(event) {
  try {
    await api.secureFetch(
      `/indicadores/${model.value.id_indicador}`,
      {method: 'DELETE'}
    )

    toast.pushToast('success', 'Indicador removido com sucesso')
    emit('success', model.value)
  
  } finally {
    Modal.getOrCreateInstance(`#${props.id}`).hide()
  }
}

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

    <LoadingSecondaryBtn
      :is-loading="api.fetchState.isLoading()"
      @click="onSubmit">
      Confirmar
    </LoadingSecondaryBtn>
    
  </BaseModal>
</template>