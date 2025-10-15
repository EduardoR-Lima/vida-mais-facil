import { ref } from "vue"
import { useCurrentSession } from "./useCurrentSession"
import { useState } from "./useState"
import { useApiFetch } from "./useApiFetch"
import { useRouter } from "vue-router"
import { HTTPRequestError } from "@/utils/customErrors"

const session = useCurrentSession()

export function useLogin() {
  const loginState = useState()
  const api = useApiFetch()
  const router = useRouter()

  async function sendCredentials(event) {
    const formElement = event.target
    loginState.setToLoading()

    try {
      const sessionData = await api.plainFetch(
        '/auth/token',
        api.addFormBody({method: 'POST'}, new FormData(formElement))
      )
      
      session.registerNewSession(sessionData)
      await router.push('/dashboard')

    } catch(err) {
      formElement.reset()

      // Qualquer falha diferente de 401 será interpretada como falha
      // de comunicação, portanto loginState.isFailed() pode ser utilizado
      // para representar credenciais inválidas 
      if (err instanceof HTTPRequestError && err.status == 401) {
        loginState.setToFailed()
      }
      
    } finally {
      if (!loginState.isFailed()) {
        loginState.setToIdle()
      }
    }
  }

  return {
    sendCredentials,
    loginState
  }
}