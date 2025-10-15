<script setup lang="ts">
import LoadingSecondaryBtn from '@/components/Buttons/LoadingSecondaryBtn.vue';
import BaseCard from '@/components/Cards/BaseCard.vue';
import ValidatedForm from '@/components/Forms/ValidatedForm.vue';
import ValidatedInput from '@/components/Forms/ValidatedInput.vue';
import SectionTitle from '@/components/Labels/SectionTitle.vue';
import { useLogin } from '@/composables/useLogin';

const { sendCredentials, loginState } = useLogin()
</script>

<template>
  <div class="vstack h-100 py-7 px-4">
    <BaseCard class="container-fluid max-sm m-auto px-4 py-5">
      
      <SectionTitle class="text-center mb-5">
        Bem-vindo de Volta!

        <template #subtitle>
          Informe o e-mail e a senha cadastrados para entrar na
          plataforma
        </template>
      </SectionTitle>

      <BaseCard
        class="bg-body-secondary p-3 border-start border-primary shadow-none
               mb-5 fs-6">
        Ainda não possui cadastro?

        <RouterLink
          to="/cadastro/cliente"
          class="text-secondary fw-bold link-underline link-underline-opacity-0">
          Clique aqui
        </RouterLink>

        para seguir para a página de cadastro
      </BaseCard>

      <p class="text-danger m-0 mb-5" v-if="loginState.isFailed()">
        Credenciais inválidas
      </p>

      <ValidatedForm
        @on-submit="sendCredentials"
        class="vstack gap-5">
        <!-- Campo do E-mail -->
        <div class="vstack gap-3">
          <ValidatedInput
            class="interactive-element"
            name="username"
            type="email"
            required>
            <template #label>
              E-mail
            </template>
            <template #feedback>
              Forneça um e-mail válida com @
            </template>
          </ValidatedInput>

          <!-- Campo da senha -->
          <ValidatedInput
            class="interactive-element"
            name="password"
            type="password"
            required>
            <template #label>
              Senha
            </template>
            <template #feedback>
              Esse campo deve ser preenchido
            </template>
          </ValidatedInput>

        </div>
        <LoadingSecondaryBtn :state="loginState">
          Entrar
        </LoadingSecondaryBtn>
      </ValidatedForm>
    </BaseCard>
  </div>
</template>