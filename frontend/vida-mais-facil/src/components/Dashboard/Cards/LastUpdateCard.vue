<script setup>
import BaseCard from '@/components/Cards/BaseCard.vue';
import CheckCircleIcon from '@/components/Icons/CheckCircleIcon.vue';
import ExclamationCircleIcon from '@/components/Icons/ExclamationCircleIcon.vue';
import ExclamationTriangleIcon from '@/components/Icons/ExclamationTriangleIcon.vue';
import { useApiFetch } from '@/composables/useApiFetch';
import { computed } from 'vue';

const api = useApiFetch()

const indicadores = await api.secureFetch('/indicadores')
const hasData = computed(() => !!indicadores.length)

// Específico desse componente. Não há necessidade de criar um composable
// próprio
const DAY_MILLISECONDS = 24 * 60 * 60 * 1000
const lastUpdate = computed(() => {
  const lastDate = new Date(indicadores[0].data_registro)
  return Math.floor((new Date() - lastDate)/DAY_MILLISECONDS)
})

</script>

<template>
  <BaseCard>
    <div class="px-5 py-3 hstack gap-4 justify-content-around">
      <!-- Caso haja registro de indicadores -->
      <template v-if="hasData">
        <!-- Indicadores atualizados nos últimos 3 dias -->
        <CheckCircleIcon
          class="fs-1 fw-bold text-success"
          v-if="lastUpdate < 3"/>
        
        <!-- Indicadores atualizados nos últimos 5 dias -->
        <ExclamationTriangleIcon
          class="fs-1 fw-bold text-warning"
          v-else-if="lastUpdate < 5"/>
        
        <!-- Indicadores atualizados há mais de 5 dias -->
        <ExclamationCircleIcon
          class="fs-1 fw-bold text-secondary"
          v-else/>

        <p class="m-0 text-center">
          <template v-if="lastUpdate < 3">
            Seus indicadores estão todos em dia. Continue assim
          </template>

          <template v-else>
            Os indicadores não são atualizados há {{ lastUpdate }} dias
          </template>
        </p>
      </template>

      <!-- Caso indicadores seja uma lista vazia -->
      <template v-else>
        <p class="m-0 text-center">
          Nenhum indicador registrado
        </p>
      </template>
    </div>
  </BaseCard>
</template>