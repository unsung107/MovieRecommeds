<template>
  <div class="home">
    <button @click="getMovie(1)">범죄</button>
    <button @click="getMovie(2)">드라마</button>
    <button @click="getMovie(3)">액션</button>
    <button @click="getMovie(5)">SF</button>
    <button @click="getMovie(11)">판타지</button>
    <br>

    <input type="text" v-model="searchKey" @input="searching(searchKey)">
    
    <div v-for="movie in movieList" :key="movie.id">{{movie.title}}</div>
  </div>
</template>

<script>
import axios from "axios";
// @ is an alias to /src

export default {
  name: "home",
  data() {
    return {
      movies: [],
      searchKey: '',
    };
  },
  components: {},
  methods: {
    getMovie(genre_id) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(SERVER_IP + `/movies/api/v1/${genre_id}/`)
        .then(response => {
          console.log(response.data);
          this.movies = response.data.movies
          console.log(this.movies)
        })
        .catch(error => {
          console.error(error);
        });
    },

    searching(movie_nm) {
      if (!movie_nm) {
        movie_nm = ' '
      }
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(SERVER_IP + `/movies/api/v1/searchNm/${movie_nm}/`)
        .then(response => {
          this.movies = response.data.movies
          
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  mounted() {
    
  },
  computed: {
    movieList() {
      return this.movies
    }
  }
};
</script>
