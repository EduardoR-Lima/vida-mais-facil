import { HTTPRequestError } from "@/utils/customErrors"
import { useCurrentSession } from "./useCurrentSession"
import { useRouter } from "vue-router"
import { useState } from "./useState"
import { useToast } from "./useToast"

const apiUrlRoot = "http://localhost:8000/api"

const { sessionToken } = useCurrentSession()

function addHeaderProperty(options, property) {
  // Garante que o headers exista e aplica a autorização
  options.headers = options.headers ?? {}
  Object.assign(options.headers, property)

  return options
}

function addJsonBody(options, object) {
  options.body = JSON.stringify(object)
  return addHeaderProperty(options, {'Content-Type': 'application/json'})
}

function addFormBody(options, object) {
  options.body = new URLSearchParams(object)
  return addHeaderProperty(options, {'Content-Type': 'application/x-www-form-urlencoded'})
}

export function useApiFetch() {
  const fetchState = useState()
  const router = useRouter()
  const toast = useToast()

  // Realiza o fetch e possui um estado de loading
  async function plainFetch(endpoint, options = {}) {
    fetchState.setToLoading()

    try {
      const response = await fetch(
        apiUrlRoot + endpoint,
        options
      )

      if (!response.ok) {
        throw new HTTPRequestError(
          response.status,
          await response.json()
        )
      }

      if (response.headers.get('Content-Type') == 'application/json') {
        return await response.json()
      }

      return null

    } catch (err) {
      fetchState.setToFailed()
      // Automaticamente notifica o usuário de que houve um problema no servidor
      if (!(err instanceof HTTPRequestError) || err.status >= 500) {
        toast.pushToast(
          'danger',
          'Ocorreu um erro ao tentar comunicar com o servidor'
        )
      }

      // Lança o erro novamente para que o fluxo seja interrompido
      throw err

    } finally {
      fetchState.setToIdle()
    }
  }

  // Adiciona o header de autorização para o fetch
  async function secureFetch(endpoint, options = {}) {
    addHeaderProperty(options, {'Authorization': 'Bearer ' + sessionToken.value})
    
    try {
      return await plainFetch(
        endpoint, 
        options
      )
    } catch (err) {
      if (err instanceof HTTPRequestError && err.status == 401) {
        await router.push('/login')
      }
    }
  }


  return {
    fetchState,
    plainFetch,
    secureFetch,
    addFormBody,
    addJsonBody
  }
}
