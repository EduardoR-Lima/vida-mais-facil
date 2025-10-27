<script setup>
import LoadingSecondaryBtn from '@/components/Buttons/LoadingSecondaryBtn.vue';
import ValidatedForm from '@/components/Forms/ValidatedForm.vue';
import ValidatedInput from '@/components/Forms/ValidatedInput.vue';
import ValidatedTextarea from '@/components/Forms/ValidatedTextarea.vue';
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
    const updatedEntity = await api.secureFetch(
      `/indicadores/${model.value.id_indicador}`,
      api.addJsonBody(
        {method: 'PUT'},
        model.value
      )
    )

    toast.pushToast('success', 'Indicador atualizado com sucesso')
    emit('success', updatedEntity)
  
  } finally {
    Modal.getOrCreateInstance(`#${props.id}`).hide()
  }
}

</script>

<template>
  <BaseModal :id>
    <template #title>
      {{ isoDateToBr(model.data_registro) }}
    </template>
    
    <ValidatedForm class="vstack" @submit="onSubmit">
      <div class="hstack gap-4 mb-3">
        <ValidatedInput
          name="tipo"
          v-model="model.tipo"
          maxlength="45">
          <template #label>
            Tipo
          </template>
        </ValidatedInput>
        <ValidatedInput
          name="valor"
          v-model="model.valor"
          maxlength="15">
          <template #label>
            Valor
          </template>
        </ValidatedInput>
      </div>

      <ValidatedTextarea
        class="mb-5"
        name="observacoes"
        rows="4"
        v-model="model.observacoes">
        <template #label>
          Observações
        </template>
      </ValidatedTextarea>

      <LoadingSecondaryBtn :is-loading="api.fetchState.isLoading()">
        Atualizar
      </LoadingSecondaryBtn>
    </ValidatedForm>

  </BaseModal>
</template>