<template>
  <div>
    <input type="text" v-model="searchKey">
    <button @click="findMovieUpdate">추가하기</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      searchKey: ''
    }
  },
  methods: {
    findMovieUpdate() {
      if (this.searchKey) {
        console.log('start')
        const API_URL = `http://127.0.0.1:8000/movies/movieupdate/`
        axios.get(API_URL)
        .then(response =>{
          console.log(response)
          this.searchKey = ''
        })
      }
    }
  }
}
</script>

<style>

</style>