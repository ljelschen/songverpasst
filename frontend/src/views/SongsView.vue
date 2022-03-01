<style>

:root{
  /* settings */
  --cardHeight: 280px;

  /* fixed Value */
  --infoHeight: 80px; 
}

.info{
  padding: 5px;
  padding-left: 10px;
  position:relative;
  top: calc(var(--cardHeight) - var(--infoHeight));
  z-index: 10;
  height: 80px;
  background-color: #375ABB;
  opacity: 95%;
  width: 100%;
  transition: all 0.3s linear;
}

.cover{
  height: var(--cardHeight);
  width: auto;
  color: #ffF;
  transition: all 0.5s ease;
  cursor: pointer;
}


.cover:hover{
  transform: scale(1.1);
  backdrop-filter: brightness(30%);
}


.cover:hover .info{
  z-index: 20;
  /*color: #375ABB;*/
}
</style>

<template>
  <div class="container">
    <h3>Alle Songs:</h3>
    <div class="d-flex flex-wrap">

      <div  v-for="item in items" :key="item.id" class="cover m-2 border shadow" style="width: 18rem;" v-bind:style="{ 'background-image': 'url(' + item.img + ')' }">
      
        <div class="info">  
            <span>{{item.title}}</span><br>   
            <b>{{item.artist}}</b><br>
            <small>{{item.date}} {{item.time}}</small>
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
        //.get(this.$hostname + 'getSongsByStation?station=Bremen Next')
        .get(this.$hostname + 'getAllSongs')
        .then(response => {
        this.items = response.data
        //console.log(this.items)
        })

    
  }

}
</script>
<style scoped></style>