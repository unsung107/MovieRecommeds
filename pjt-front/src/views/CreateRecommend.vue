<template>
  <div class="container">
    <div>
      title :
      <input type="text" v-model="creationFrom.title" />
      <br />discription :
      <textarea type="text" class="col-7 row-5"  v-model="creationFrom.discription" row="4" />
      <br />
      <button class="btn btn-primary" data-toggle="modal" data-target="#find_movie">영화 추가하기</button>
      <AddMovieInRecommendModal @selectMovie="modalAddMovie" />
      <hr />
      <div v-if="selectedMovie.id">
        <img :src="selectedMovie.post_url" alt class="movie--poster" />
        <input type="text" v-model="makingMovieComment" />
        <button class="btn btn-secondary" @click="addMovie(selectedMovie)">등록</button>
      </div>
      <div>
        <span v-for="addedMovie in creationFrom.movies" :key="addedMovie.id">
          {{addedMovie.movie.title}}
          <img class="movie--poster" :src="addedMovie.movie.post_url" />
          {{addedMovie.movieComment}}
          <br />
        </span>
      </div>
      <button class="btn btn-secondary" @click="createRecommend">제출하기</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import jwtDecode from "jwt-decode";
import router from "@/router";
import AddMovieInRecommendModal from "@/components/AddMovieInRecommendModal";

export default {
  name: "CreateRecommend",
  components: {
    AddMovieInRecommendModal
  },
  data() {
    return {
      creationFrom: {
        user_id: "",
        title: "",
        discription: "",
        movies: []
      },
      makingMovieComment: "",
      token: "",
      selectedMovie: {}
    };
  },
  methods: {
    checkLoggedIn() {
      this.$session.start();
      if (!this.$session.has("jwt")) {
        router("/login");
      } else {
        this.token = this.$session.get("jwt");
        this.creationFrom.user_id = jwtDecode(this.token).user_id;
      }
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
    },

    createRecommend() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;

      const options = {
        headers: {
          Authorization: "JWT " + this.token
        }
      };
      console.log(options);
      axios
        .post(
          SERVER_IP +
            `/movies/api/v1/createRecommend/${this.creationFrom.user_id}/`,
          this.creationFrom,
          options
        )
        .then(response => {
          response
          router.push('/RecommendList')
        });
    },

    modalAddMovie(selectedMovie) {
      console.log(selectedMovie)
      this.selectedMovie = selectedMovie
    }
  },
  mounted() {
    this.checkLoggedIn();
  }
};
</script>

<style>
</style>