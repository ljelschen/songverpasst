<template>
  <div class="home">
    <h1>Add Station</h1>
    <addStation></addStation>
  </div>
</template>

<script>
//include addStation.vue
import addStation from '@/components/admin/addStation.vue'

export default {
    name: 'admin',
    components: {
        addStation
    },
    data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script><!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>