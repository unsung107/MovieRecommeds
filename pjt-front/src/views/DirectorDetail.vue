<template>
  <div>
    <h4 class="directordetail" >{{director.name}}</h4><br><br>
    <img :src="director.image_url" alt="">
    <br><br> <br><br>
    <div class="row">
    <span v-for="movie in director.movies" :key="movie.id" class="border-0 card col-3">
      <router-link :to="`/movie/${movie.id}`">
      <img class="movie--poster-- my-3" style="width:180px height:250px" :src="movie.post_url" :alt="movie.title"><br>
      {{ movie.title }}
      </router-link>
    </span>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'directorDetail',
  data() {
    return {
      director: {},
      director_id: this.$route.params.director_id,
    }
  },
  methods: {
    getMovieInfo() {

      const SERVER_IP = process.env.VUE_APP_SERVER_IP + `/movies/api/v1/directorDetail/${this.director_id}`;

      axios.get(SERVER_IP)
      .then(response => {
        
        this.director = response.data
      })
    }
  },
  mounted() {
    this.getMovieInfo()
  },
}
</script>

<style>
.directordetail {
  margin-left: 660px
}
</style>