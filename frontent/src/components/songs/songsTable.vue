<template>
    <tr>
        <th scope="row">{{item.id}}</th>
        <td>{{item.date}}</td>
        <td>{{item.time}}</td>
        <td>{{item.artist}}</td>
        <td>{{item.title}}</td>
    </tr>
</template>


<script>
export default {
    name: 'songsTable',
}
</script>