function isoDateToBr(date) {
  return new Date(date).toLocaleDateString('pt-br')
}

export function useFormatter() {
  return {
    isoDateToBr
  }
}