import Vue from 'vue'
import Router from 'vue-router'
//import von views
import home from '@/views/home'
import admin from '@/views/admin'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/admin',
      name: 'admin',
      component: admin
    }
  ]
})