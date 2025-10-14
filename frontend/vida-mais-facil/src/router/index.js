import { useCurrentSession } from '@/composables/useCurrentSession'
import { useToast } from '@/composables/useToast'
import { createRouter, createWebHistory } from 'vue-router'

const { isValidSession, isExpiredToken } = useCurrentSession()
const { pushToast } = useToast()

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
      name: 'Home',
      component: () => import('../views/LandingPageView.vue'),
      meta: {
        hasNavbar: true,
      },
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('../views/LoginView.vue'),
      beforeEnter: [requiresLogout],
      meta: {
        hasNavbar: false,
      },
    },
    {
      path: '/cadastro/cliente',
      name: 'CadastroCliente',
      component: () => import('../views/CadastroClienteView.vue'),
      meta: {
        hasNavbar: false,
      },
    },
    {
      path: '/cadastro/profissional',
      name: 'CadastroProfissional',
      component: () => import('../views/CadastroProfissionalView.vue'),
      meta: {
        hasNavbar: false,
      },
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: () => import('../views/DashboardView.vue'),
      beforeEnter: [requiresLogin],
      meta: {
        hasNavbar: true,
      },
    },
    {
      path: '/agendamento',
      name: 'Agendamento',
      component: () => import('../views/AgendamentoView.vue'),
      beforeEnter: [requiresLogin],
      meta: {
        hasNavbar: true,
      },
    }
  ],
})

router.afterEach((to, from) => {
  // Informar que a sessão expirou em casos de redirect para a página de login
  if (to.name == 'Login' && isExpiredToken()) {
    pushToast('warning', 'A sessão expirou')
  }
})

export default router
