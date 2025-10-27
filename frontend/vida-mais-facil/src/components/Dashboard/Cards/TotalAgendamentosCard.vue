<script setup>
import BaseCard from '@/components/Cards/BaseCard.vue';
import { useApiFetch } from '@/composables/useApiFetch';

const api = useApiFetch()

const totalAgendamentos = await api.secureFetch('/agendamentos/total')

</script>

<template>
<BaseCard>
    <div class="px-5 py-3 hstack gap-4 justify-content-around">
      <p class="m-0 fs-1 fw-bold text-primary">
        {{ totalAgendamentos.total }}
      </p>
      <p class="m-0 text-center">
        Agendamentos realizados no total
      </p>
    </div>
  </BaseCard>
</template>