<template>
  <div
    class="modal-size modal fade"
    tabindex="-1"
    role="dialog"
    aria-hidden="true"
    id="find_movie"
  >
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">영화 검색</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
                  <input type="text" v-model="searchKey" @input="searching(searchKey)" />
    <div class="row container">
      <span
        class="card border-0 col-4 my-3 mx-2.7"
        v-for="movie in movies"
        :key="movie.id"
        @click="selectMovie(movie)"
      >
        <img class="movie--poster--modal my-3" :src="movie.post_url" :alt="movie.title" />
        <!-- {{ movie.title }} -->
      </span>
    </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">취소</button>
          <button type="button" class="btn btn-primary" @click="addMovie" data-dismiss="modal">추가</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      searchKey: "",
      movies: {},
      selectedMovie: {}
    };
  },
  props:{
    user: Number
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
      this.movies = {movie}
    },
    addMovie() {
      this.$emit("selectMovie", this.selectedMovie);
      this.searchKey = ''
      this.movies = {}
    },
  }
};
</script>

<style>
.movie--poster--modal {
  width: 120px;
  height: 180px;
}
</style>