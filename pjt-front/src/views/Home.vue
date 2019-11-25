<template>
  <div class="container">
    <button @click="getMovie(1)">범죄</button>
    <button @click="getMovie(2)">드라마</button>
    <button @click="getMovie(3)">액션</button>
    <button @click="getMovie(5)">SF</button>
    <button @click="getMovie(11)">판타지</button>
    <br />

    <input type="text" v-model="searchKey" @input="searching(searchKey)" />

    <div class="row">
      <span class="card col-3 my-3" v-for="movie in movies" :key="movie.id">
        <router-link :to="`/movie/${movie.id}`">
          <img class="movie--poster my-3" :src="movie.post_url" :alt="movie.title" />
        </router-link>
        {{ movie.title }}
      </span>
    </div>
  </div>
</template>

<script>
import axios from "axios";
// import MovieDetail from "@/components/MovieDetail.vue";
// @ is an alias to /src

export default {
  name: "home",
  data() {
    return {
      movies: [],
      searchKey: ""
    };
  },
  components: {
    // MovieDetail
  },
  methods: {
    getMovie(genre_id) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(SERVER_IP + `/movies/api/v1/${genre_id}/`)
        .then(response => {
          this.movies = response.data.movies;
        })
        .catch(error => {
          console.error(error);
        });
    },

    searching(movie_nm) {
      if (!movie_nm) {
        movie_nm = " ";
      }
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(SERVER_IP + `/movies/api/v1/searchNm/${movie_nm}/`)
        .then(response => {
          this.movies = response.data.movies;
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  mounted() {},
  computed: {
    movieList() {
      return this.movies;
    }
  }
};
</script>

<style>
</style>