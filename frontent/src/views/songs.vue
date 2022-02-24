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
    <tbody>

    </tbody>
      <songsTable v-for="(song, index) in songs" :tid="index" :date="songs[index]['1']" :time="songs[index]['1']" :artist="songs[index]['1']" :song="songs[index]['1']"></songsTable>    
    </table>
</template>
<script>

import songsTable from '@/components/songs/songsTable.vue'

export default {
  name: 'songs',
  components: {
    songsTable
  },

  data () {
    return {
      songs: ''
    }
  },

  mounted () {
      this.axios
        .get(this.$hostname + 'getSongsByStation?station=Bremen Next')
        .then(response => {
        this.songs = response
        console.log(this.songs)
        })

    
  }

}
</script>
<style scoped></style>