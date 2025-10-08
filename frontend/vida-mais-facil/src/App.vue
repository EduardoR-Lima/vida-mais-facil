<script setup>
import { useRoute } from 'vue-router';
import Navbar from '../components/Navbar/Navbar.vue';


const route = useRoute()
</script>

<template>
  <header
    v-if="route.meta.hasNavbar"
    class="position-absolute top-0 start-0 end-0 bg-white shadow-sm z-1">
    <Navbar />
  </header>

  <div class="page-container page-bg-gradient overflow-hidden
              d-flex flex-column vh-100">
    <main
      class="flex-fill overflow-y-auto smooth-scroll rm-scrollbar"
      :class="{'navbar-margin': route.meta.hasNavbar}">
      <RouterView />
    </main>
  </div>
</template>

