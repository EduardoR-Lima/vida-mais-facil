<script setup>
import PlusCircleIcon from '@/components/Icons/PlusCircleIcon.vue';
import BaseTable from '@/components/Tables/BaseTable.vue';
import TableCell from '@/components/Tables/TableCell.vue';
import { useApiFetch } from '@/composables/useApiFetch';
import { useFormatter } from '@/composables/useFormatter';
import DeleteModal from '../Modals/DeleteModal.vue';
import { ref } from 'vue';
import ViewModal from '../Modals/ViewModal.vue';
import CreateModal from '../Modals/CreateModal.vue';
import UpdateModal from '../Modals/UpdateModal.vue';

const { isoDateToBr } = useFormatter()
const api = useApiFetch()

const indicadores = await api.secureFetch('/indicadores')

const modelTest = ref(indicadores[0])

</script>

<template>
  <BaseTable :rows="4.25" v-bind="$attrs">
    <template #header>
      <p class="m-0 fs-4 fw-bold text-primary">
        Histórico de Indicadores
      </p>
      <PlusCircleIcon
        class="fs-3 text-primary"
        role="button"
        data-bs-toggle="modal"
        data-bs-target="#indCreateModal"/>
    </template>

    <TableCell v-for="i in indicadores">
      <!-- Primeira coluna -->
      <div
        class="flex-grow-1"
        role="button"
        data-bs-toggle="modal"
        data-bs-target="#indViewModal">
        <p class="m-0 fw-bold text-primary">
          {{ isoDateToBr(i.data_registro) }}
        </p>
        <p class="m-0 fs-6">
          {{ i.tipo }}
        </p>
      </div>

      <div
        class="fw-bold text-primary interactive-element"
        style="align-content: center;"
        role="button"
        data-bs-toggle="modal"
        data-bs-target="#indUpdateModal">
        Editar
      </div>

      <div
        class="fw-bold text-secondary interactive-element"
        style="align-content: center;"
        role="button"
        data-bs-toggle="modal"
        data-bs-target="#indDeleteModal">
        Excluir
      </div>

    </TableCell>
    
    <p class="m-3 text-center text-body-secondary" v-if="!indicadores.length">
      Nenhum indicador registrado
    </p>
  </BaseTable>
  
  <CreateModal
    id="indCreateModal"
    :is-loading="false"
    v-model="modelTest"
    @submit="() => console.log('confirmado')"/>

  <DeleteModal
    id="indDeleteModal"
    :is-loading="false"
    v-model="modelTest"
    @submit="() => console.log('confirmado')"/>

  <ViewModal
    id="indViewModal"
    v-model="modelTest"/>

  <UpdateModal
    id="indUpdateModal"
    :is-loading="false"
    v-model="modelTest"
    @submit="() => console.log('confirmado')"/>
</template>