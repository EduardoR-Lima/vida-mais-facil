import Toastify from 'toastify-js'

export function useToast() {
  function pushToast(level, message, duration = 5000) {
    const className = `bg-${level}-subtle border border-${level}-subtle rounded-2 `
                     + `text-${level}-emphasis`

    Toastify({
      text: message,
      duration: duration,
      close: false,
      gravity: "bottom",
      className: className,
    }).showToast()
  }
  
  return {
    pushToast
  }
}