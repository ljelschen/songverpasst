<template>
  <div id="app">
    <!-- include the Navigation -->
    <navigation></navigation>
    <router-view/>
    <footnav></footnav>

  </div>
</template>

<script>
import navigation from './components/navigation.vue'
import footnav from'./components/footer.vue'



export default {

  name: 'App',
  components: {
    navigation, 
    footnav
  }
}
</script><style>
#app {
  
}
</style>