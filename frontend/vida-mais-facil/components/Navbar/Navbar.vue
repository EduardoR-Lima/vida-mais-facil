<script setup lang="ts">
import { useCurrentSession } from '@/composables/useCurrentSession';
import Logo from '../Logo.vue';
import MenuIcon from '../Icons/MenuIcon.vue';
import NavLink from './NavLink.vue';
import CollapseButton from './CollapseButton.vue';

const { isValidSession, removeCurrentSession } = useCurrentSession()
</script>

<template>
  <nav class="navbar navbar-expand-lg py-4">
    <div class="container navbar-min-height">
      <!-- Logo -->
      <div class="navbar-brand p-0">
        <Logo />
      </div>

      <!-- Mostra um botão chamado para a página de login caso o usuário
       esteja deslogado -->
      <template v-if="!isValidSession()">
        <RouterLink
          to="/login"
          class="btn btn-secondary fs-6 fw-bold text-white px-4 py-3 float-end"
        >
          Entrar
        </RouterLink>
      </template>
      
      <!-- Mostra links para navegar entre as páginas quando estiver logado -->
      <template v-else>
        <!-- Os links são colapsados em um menu de hamburguer
         em telas pequenas -->
        <CollapseButton
          target-id="#navbarNav"
          label="Expandir barra de navegação"
          />
        
        <!-- Container responsivo com os links -->
        <div class="collapse navbar-collapse" id="navbarNav">
          <div class="navbar-nav mt-4 mt-lg-0">
            <!-- Link para o Dashboard -->
            <NavLink
              to="/dashboard">
              Dashboard
            </NavLink>

            <!-- Link para os Agendamentos -->
            <NavLink
              to="/agendamento">
              Agendamento
            </NavLink>

            <!-- Link para deslogar -->
            <!-- A solução com o link não é definitiva, pois pode causar
             uma pequena dessincronização entre a navegação e a remoção
             da sessão -->
            <RouterLink
              to="/"
              class="nav-link interactive-element"
              @click="removeCurrentSession"
              role="button">
              Sair
            </RouterLink>
          </div>
        </div>
      </template>

    </div>
  </nav>
</template>