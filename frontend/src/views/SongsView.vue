<template>
  <table class="table table-striped">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Datum</th>
        <th scope="col">Zeit</th>
        <th scope="col">Artist</th>
        <th scope="col">Song</th>
      </tr>
    </thead>
    <tbody v-if="items !=''">
      <tr v-for="item in items" :key="item.id">
          <th scope="row">{{item.id}}</th>
          <td>{{item.date}}</td>
          <td>{{item.time}}</td>
          <td>{{item.artist}}</td>
          <td>{{item.title}}</td>
      </tr>
    </tbody>
    </table>
</template>
<script>


export default {
  name: 'songs',


  data () {
    return {
      items: ''
    }
  },

  mounted () {
      this.axios
        .get(this.$hostname + 'getSongsByStation?station=Bremen Next')
        .then(response => {
        this.items = response.data
        //console.log(this.items)
        })

    
  }

}
</script>
<style scoped></style>