<template>
  <div>

    내가 좋아하는 배우가 나오는 영화
    <div class="row">
      <span class="border-0 card col-3 my-3" v-for="movie in movies.actors" :key="`actor-${movie.id}`">
        <router-link :to="`/movie/${movie.id}`">
          <img class="movie--poster my-3" :src="movie.post_url" :alt="movie.title" />
        </router-link>
        {{ movie.title }}
      </span>
    </div>

    <hr>

    내가 좋아하는 배우가 나오는 영화
    <div class="row">
      <span class="border-0 card col-3 my-3" v-for="movie in movies.directors" :key="`director-${movie.id}`">
        <router-link :to="`/movie/${movie.id}`">
          <img class="movie--poster my-3" :src="movie.post_url" :alt="movie.title" />
        </router-link>
        {{ movie.title }}
      </span>
    </div>
    <hr>

    내가 좋아한 영화를 좋아하는 유저들이 좋아하는 영화
     <div class="row">
      <span class="border-0 card col-3 my-3" v-for="movie in movies.users" :key="`user-${movie.id}`">
        <router-link :to="`/movie/${movie.id}`">
          <img class="movie--poster my-3" :src="movie.post_url" :alt="movie.title" />
        </router-link>
        {{ movie.title }}
      </span>
    </div>
  </div>
</template>

<script>
import jwtDecode from 'jwt-decode'
import axios from 'axios'


export default {
  name: 'MovieForYou',
  data() {
    return {
      movies: {},
      SERVER_IP: process.env.VUE_APP_SERVER_IP
    }
  },
  computed: {
    token() {
      return this.$session.get('jwt')
    },
    user_id() {
      return jwtDecode(this.token).user_id;
    },
  },
  methods: {
    getMovieForYou() {
      console.log(this.SERVER_IP)
      axios.get(this.SERVER_IP + `/movies/api/v1/movieForUser/${this.user_id}/`)  
      .then(response => {
        this.movies = response.data
      })
    }
  },
  mounted() {
    this.getMovieForYou()
  }
}
</script>

<style>

</style>