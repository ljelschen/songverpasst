<template>
    <form action="">
        <div class="mb-3">
            <label for="name" class="form-label">Name</label>
            <input v-model="name" type="text" class="form-control" id="name" placeholder="beste Station ever">
        </div>
        <div class="mb-3">
            <label for="type" class="form-label">Type</label>
            <select v-model="type" class="form-control" id="type" aria-label="Default select example">
                <option value="get" selected>Get</option>
                <option value="html">HTML</option>
            </select>
        </div>
        <div class="mb-3">
            <label for="url" class="form-label">Url</label>
            <input v-model="url" type="text" class="form-control" id="url" placeholder="http://...........">
        </div>
        <button @click="getInfo" class="btn btn-success">Speichern</button>
        <div v-if="response">
            {{response}}
        </div>

        <span>{{url}}</span>
    </form>


</template>

<script>
export default {
    name: 'addStation',
    data (){
        return {
            name: "",
            type: "",
            url: "",
            response: "",
        }
  },
  methods: {
    getInfo() {
        this.axios
        .post(this.$hostname + 'getStations',{
        name: this.name,
        type: this.type,
        url: this.url,
    })
        .then(response => (this.response = response))
    }
  },
  mounted () {

  }

}
</script>