import { computed, ref } from "vue"

const IDLE_STATE = 1
const LOADING_STATE = 2
const FAILED_STATE = 0

export function useState(initialState = IDLE_STATE) {
  const state = ref(initialState)

  const setToLoading = () => { state.value = LOADING_STATE }
  const setToIdle = () => { state.value = IDLE_STATE }
  const setToFailed = () => { state.value = FAILED_STATE }

  const isLoading = computed(() => state.value == LOADING_STATE)
  const isIdle = computed(() => state.value == IDLE_STATE)
  const isFailed = computed(() => state.value == FAILED_STATE)

  return {
    state,
    setToLoading,
    setToIdle,
    setToFailed,
    isLoading,
    isIdle,
    isFailed
  }
}
