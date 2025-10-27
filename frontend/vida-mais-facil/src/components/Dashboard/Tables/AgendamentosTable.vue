<script setup>
import BaseTable from '@/components/Tables/BaseTable.vue';
import TableCell from '@/components/Tables/TableCell.vue';
import { useApiFetch } from '@/composables/useApiFetch';
import { useFormatter } from '@/composables/useFormatter';

const api = useApiFetch()
const { isoDateToBr } = useFormatter()

const agendamentos = await api.secureFetch('/agendamentos')

</script>

<template>
  <BaseTable>
    <template #header>
      <p class="m-0 fs-4 fw-bold text-primary">
        Próximos agendamentos
      </p>
    </template>

    <TableCell v-for="a in agendamentos">
      <div>
        <p class="m-0 fw-bold text-primary">
          {{ a.profissional.nome }}
        </p>
        <p class="m-0 fs-6">
          {{ a.profissional.especialidade.nome }}
        </p>
      </div>

      <p class="m-0">{{ isoDateToBr(a.data) }}</p>
    </TableCell>

    <p class="m-3 text-center text-body-secondary" v-if="!agendamentos.length">
      Nenhum agendamento pendente
    </p>
  </BaseTable>
</template>