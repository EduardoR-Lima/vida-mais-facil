<script setup>
import LoadingSecondaryBtn from '@/components/Buttons/LoadingSecondaryBtn.vue';
import ValidatedForm from '@/components/Forms/ValidatedForm.vue';
import ValidatedInput from '@/components/Forms/ValidatedInput.vue';
import ValidatedTextarea from '@/components/Forms/ValidatedTextarea.vue';
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
      {{ isoDateToBr(model.data_registro) }}
    </template>
    
    <ValidatedForm class="vstack" @submit="(e) => emit('submit', e)">
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

      <LoadingSecondaryBtn :is-loading>
        Atualizar
      </LoadingSecondaryBtn>
    </ValidatedForm>

  </BaseModal>
</template>