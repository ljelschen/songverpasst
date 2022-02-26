<style scoped>
.header{
  position: relative;
  top: 0px;
  height: 600px;
  width: 100%;

  background-color:#375ABB;
  color: white;
  }

  .bottomCurve{
    position: absolute;
    top: calc(600px - 100px);
    left: 0;
    width: 100%;
    height: 100px;
  }

  .header-info{
    position: relative;
    top: 150px;
  }

  .header-info h1{
    font-size: 50px;
    font-weight: bold;
    margin-bottom: 0px;
  }

  .header-info p{
    font-size: 1.25rem;
    font-weight: 400;
  }
</style>
<template>
  <div class="header ">

    <div class="header-info container">
      <h1>Willkommen bei Songverpass</h1>
      <p class="px-xl-5">
        Hier findest du jeden Radiotitel wieder.
      </p>
      <div class="row px-xl-5">
        <div class="col">
          <a class="btn btn-outline-light">Song Suchen</a>
        </div>
      </div>
    </div>
 
    <svg class="bottomCurve" width="100%" height="96px" viewBox="0 0 100 100" fill="#fff" version="1.1" preserveAspectRatio="none">
        <path d="M0,0 C40,33 66,52 75,52 C83,52 92,33 100,0 L100,100 L0,100 L0,0 Z"></path>
    </svg>
  </div>

</template>

<script>

</script><!-- Add "scoped" attribute to limit CSS to this component only -->
