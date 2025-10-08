import { computed, ref } from "vue"

const EXPIRE_MARGIN = 5 * 60 * 1000
const SESSION_STORAGE_KEY = 'vmf-session-data-key'

function persistSession(sessionData) {
  const stringfied = JSON.stringify(sessionData)
  localStorage.setItem(SESSION_STORAGE_KEY, stringfied)
}

function retrieveSessionData() {
  const data = localStorage.getItem(SESSION_STORAGE_KEY)
  return data? JSON.parse(data) : null
}

function registerNewSession(sessionData) {
  persistSession(sessionData)
  Object.assign(currentSession.value, sessionData)
}

function removeCurrentSession() {
  localStorage.removeItem(SESSION_STORAGE_KEY)
  currentSession.value = {}
}

const currentSession = ref(
  retrieveSessionData() || {}
)

const userId = computed(() => currentSession.value.cliente?.id_cliente || '')
const userName = computed(() => currentSession.value.cliente?.nome || '')
const sessionToken = computed(() => currentSession.value.access_token || '')

function isExpiredToken() {
  const remaining = new Date(currentSession.value.exp) - new Date()
  return remaining < EXPIRE_MARGIN
}

function isValidSession() {
  if (!sessionToken.value) {
    return false
  }

  if (isExpiredToken()) {
    removeCurrentSession()
    return false
  }

  return true
}

export function useCurrentSession() {
  return {
    userId,
    userName,
    sessionToken,
    registerNewSession,
    removeCurrentSession,
    isValidSession,
  }
}