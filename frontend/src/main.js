import { createApp, VueElement } from 'vue'
import ArcoVue from '@arco-design/web-vue/es/arco-vue'
import ArcoVueIcon from '@arco-design/web-vue/es/icon'
import App from './App.vue'
import router from './router'
import '@arco-design/web-vue/dist/arco.css'

import './assets/main.css'

const app = createApp(App)

app.use(router)
app.use(ArcoVue)
app.use(ArcoVueIcon)
app.mount('#app')