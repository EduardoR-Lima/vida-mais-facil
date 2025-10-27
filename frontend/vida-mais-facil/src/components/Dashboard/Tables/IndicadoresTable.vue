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

const indicadores = ref(await api.secureFetch('/indicadores'))
const currentInd = ref({})

function setCurrentInd(indicador) {
  currentInd.value = {...indicador}
}

function addInd(indicador) {
  indicadores.value.push(indicador)
}

function removeInd(indicador) {
  indicadores.value = indicadores.value.filter(ind => {
    return ind.id_indicador !== indicador.id_indicador 
  })
}

function updateInd(indicador) {
  const idx = indicadores.value.findIndex(ind => {
    return ind.id_indicador == indicador.id_indicador
  })

  if (idx > 0) {
    Object.assign(indicadores.value[idx], indicador)
  }
}

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
        data-bs-target="#indCreateModal"
        @click="() => setCurrentInd({})"/>
    </template>

    <div class="d-flex gap-3 flex-column-reverse">
      <TableCell
        v-for="i in indicadores"
        @click="() => setCurrentInd(i)">
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
    </div>
    
    <p class="m-3 text-center text-body-secondary" v-if="!indicadores.length">
      Nenhum indicador registrado
    </p>
  </BaseTable>
  
  <CreateModal
    id="indCreateModal"
    v-model="currentInd"
    @success="ind => addInd(ind)"/>

  <DeleteModal
    id="indDeleteModal"
    v-model="currentInd"
    @success="ind => removeInd(ind)"/>

  <ViewModal
    id="indViewModal"
    v-model="currentInd"/>

  <UpdateModal
    id="indUpdateModal"
    v-model="currentInd"
    @success="ind => updateInd(ind)"/>
</template>