<template>
  <div class="container">
    <h3>Alle Songs:</h3>
    <div class="d-flex flex-wrap">

      <div  v-for="item in items" :key="item.id" class="card m-2" style="width: 18rem;">
        <img :src="item.img" class="card-img-top" :alt="item.title">
        <div class="card-body">
            <h5 class="card-title">{{item.title}}</h5>
            <p class="card-text">
              <b>Artist: {{item.artist}}</b><br> 
              Album: {{item.album}}<br> 
              <small class="text-muted">{{item.date}} {{item.time}}  </small>
            </p>
        </div>
        <div class="card-footer">
          <i class="fa-brands fa-spotify "></i>
          <i class="fa-solid fa-tower-broadcast" style="margin-left:15px"></i>
        </div> 
      </div>

    </div>
  </div>
</template>
<script>
import SongCard from '@/components/songs/SongCard.vue'

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