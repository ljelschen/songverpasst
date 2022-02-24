import Vue from 'vue'
import Router from 'vue-router'
//import von views
import home from '@/views/home'
import admin from '@/views/admin'
import songs from '@/views/songs'

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
    }, 
    {
      path: '/songs',
      name: 'songs',
      component: songs
    }
  ]
})