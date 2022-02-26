import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import * as Vue from 'vue' // in Vue 3
import axios from 'axios'
import VueAxios from 'vue-axios'

const app = createApp(App)
app.config.globalProperties.$hostname = "http://127.0.0.1:5000/"
app.use(router)
app.use(VueAxios, axios)
app.mount('#app')
