<template>
    <tr>
        <th scope="row">{{tid}}</th>
        <td>{{date}}</td>
        <td>{{time}}</td>
        <td>{{artist}}</td>
        <td>{{song}}</td>
    </tr>
</template>


<script>
export default {
    name: 'songsTable',

    props: {
        tid: Number,
        date: String,
        time: String,
        artist: String,
        song: String,
  }
}
</script>