<template>
  <div class="container">
    <div>
      title :
      <input type="text" v-model="creationFrom.title" />
      <br />discription :
      <input type="text" v-model="creationFrom.discription" />
      <br />

      <hr />
      <div v-if="selectedMovie.id">
        <img :src="selectedMovie.post_url" alt class="movie--poster" />
        <input type="text" v-model="makingMovieComment" />
        <button class="btn btn-secondary" @click="addMovie(selectedMovie)">추가하기</button>
      </div>
      <div>
        <input type="text" v-model="searchKey" @input="searching(searchKey)" />
        <div class="row">
          <span
            class="card col-3 my-3"
            v-for="movie in movies"
            :key="movie.id"
            @click="selectMovie(movie)"
          >
            <img class="movie--poster my-3" :src="movie.post_url" :alt="movie.title" />
            {{ movie.title }}
          </span>
        </div>
        <span v-for="addedMovie in creationFrom.movies" :key="addedMovie.id">
          {{addedMovie.movie.title}}
          <img class="movie--poster" :src="addedMovie.movie.post_url" />
          {{addedMovie.movieComment}}
          <br />
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CreateRecommend",
  data() {
    return {
      creationFrom: {
        title: "",
        discription: "",
        movies: []
      },
      searchKey: "",
      movies: [],
      selectedMovie: {},
      makingMovieComment: ""
    };
  },
  methods: {
    searching(movie_nm) {
      if (!movie_nm) {
        movie_nm = " ";
      }
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(SERVER_IP + `/movies/api/v1/searchNm/${movie_nm}/`)
        .then(response => {
          this.movies = response.data.movies;
          console.log(this.movies);
        })
        .catch(error => {
          console.error(error);
        });
    },

    selectMovie(movie) {
      this.selectedMovie = movie;
      this.movies = [];
      this.searchKey = "";
    },

    addMovie(movie) {
      if (this.makingMovieComment) {
        this.creationFrom.movies.push({
          movie: movie,
          movieComment: this.makingMovieComment
        });
        this.selectedMovie = {};
        this.makingMovieComment = "";
      }
      console.log(this.creationFrom);
    }
  }
};
</script>

<style>
</style>