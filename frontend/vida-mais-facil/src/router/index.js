import { useCurrentSession } from '@/composables/useCurrentSession'
import { createRouter, createWebHistory } from 'vue-router'

const { isValidSession } = useCurrentSession()

function requiresLogin(to) {
  if (!isValidSession()) {
    return { path: '/login' }
  }

  return true
}

function requiresLogout(to) {
  if (isValidSession()) {
    return { path: '/dashboard' }
  }

  return true
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: () => import('../views/LandingPageView.vue'),
    },
    {
      path: '/login',
      component: () => import('../views/LoginView.vue'),
      beforeEnter: [requiresLogout],
    },
    {
      path: '/cadastro/cliente',
      component: () => import('../views/CadastroClienteView.vue'),
    },
    {
      path: '/cadastro/profissional',
      component: () => import('../views/CadastroProfissionalView.vue'),
    },
    {
      path: '/dashboard',
      component: () => import('../views/DashboardView.vue'),
      beforeEnter: [requiresLogin],
    },
    {
      path: '/agendamento',
      component: () => import('../views/AgendamentoView.vue'),
      beforeEnter: [requiresLogin],
    }
  ],
})

export default router
