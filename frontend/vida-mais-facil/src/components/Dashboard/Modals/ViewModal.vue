<script setup>
import ValidatedInput from '@/components/Forms/ValidatedInput.vue';
import ValidatedTextarea from '@/components/Forms/ValidatedTextarea.vue';
import BaseModal from '@/components/Modals/BaseModal.vue';
import { useFormatter } from '@/composables/useFormatter';

const model = defineModel()

const props = defineProps({
  id: {
    type: String,
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
    
    <div class="vstack gap-3">
      <div class="hstack gap-4">
        <ValidatedInput name="tipo" v-model="model.tipo" disabled>
          <template #label>
            Tipo
          </template>
        </ValidatedInput>
        <ValidatedInput name="valor" v-model="model.valor" disabled>
          <template #label>
            Valor
          </template>
        </ValidatedInput>
      </div>

      <ValidatedTextarea name="observacoes" rows="4" v-model="model.observacoes" disabled>
        <template #label>
          Observações
        </template>
      </ValidatedTextarea>
    </div>

  </BaseModal>
</template>