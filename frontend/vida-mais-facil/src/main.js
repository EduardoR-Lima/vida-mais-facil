// Importando estilos
import "./scss/main.scss"

// Importando dependencias do vue
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Importando dependencias do bootstrap
import { Collapse, Dropdown, Modal } from "bootstrap"

const app = createApp(App)

app.use(router)

app.mount('#app')
