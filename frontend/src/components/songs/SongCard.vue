<template>
    <div class="card" style="width: 18rem;">
    <img src="{{props.img}}" class="card-img-top" alt="...">
    <div class="card-body">
        <h5 class="card-title">{{props.title}}</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
    </div>
    </div>
</template>

{{props}}
<script>
    //import data from props
 export default {
    props: {
        date: String,
        time: String,
        artist: String,
        title: String,
        img: String,
        album: String,
        spotify: String
    },
}
</script>
