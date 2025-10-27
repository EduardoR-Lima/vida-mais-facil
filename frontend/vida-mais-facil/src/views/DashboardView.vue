<script setup>
import PlaceholderCard from '@/components/Cards/PlaceholderCard.vue';
import LastUpdateCard from '@/components/Dashboard/Cards/LastUpdateCard.vue';
import TotalAgendamentosCard from '@/components/Dashboard/Cards/TotalAgendamentosCard.vue';
import AgendamentosTable from '@/components/Dashboard/Tables/AgendamentosTable.vue';
import IndicadoresTable from '@/components/Dashboard/Tables/IndicadoresTable.vue';
import SectionTitle from '@/components/Labels/SectionTitle.vue';
import { useCurrentSession } from '@/composables/useCurrentSession';
import { computed } from '@vue/reactivity';
import { Suspense } from 'vue';

const session = useCurrentSession()

const firstName = computed(() => session.userName.value.split(' ').at(0))

</script>

<template>
  <div class="container vstack px-4 py-5 gap-6" style="min-height: 100%;">
    <!-- Título da página -->
    <SectionTitle>
      Olá, {{ firstName }}! Tudo bem?

      <template #subtitle>
        Fique atento para manter os seus indicadores em dia
      </template>
    </SectionTitle>

    <div class="vstack flex-lg-row gap-6">
      <div class="vstack gap-6 col-lg-8">
        <Suspense>
          <LastUpdateCard />
          <template #fallback>
            <PlaceholderCard style="height: 5rem;"/>
          </template>
        </Suspense>
        <Suspense>
          <TotalAgendamentosCard />
          <template #fallback>
            <PlaceholderCard style="height: 5rem;"/>
          </template>
        </Suspense>
        <Suspense>
          <IndicadoresTable class="flex-grow-1"/>
          <template #fallback>
            <PlaceholderCard style="height: 10rem;"/>
          </template>
        </Suspense>
      </div>
      
      <div class="d-flex col-lg-4">
        <Suspense>
          <AgendamentosTable class="flex-grow-1" />
          <template #fallback>
            <PlaceholderCard style="height: 10rem;"/>
          </template>
        </Suspense>
      </div>
    </div>


  </div>
</template>