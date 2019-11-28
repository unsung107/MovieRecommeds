<template>
  <div class="container" style="width:900px">
    <div>
      <div class="title">
        <div>
          <p style="float: left">제목 :</p> 
          <input type="text" class="col-4 row-5" v-model="creationFrom.title" placeholder=" 비오는 날 보기 좋은 영화" style="float:left"/>
        </div>
        <button class="btn btn-secondary" @click="createRecommend" style="float:right">추천리스트 만들기</button>

        <br /><br />
        <p class="d_class">설명 :</p>
        <input type="text" class="col-7 row-5"  v-model="creationFrom.discription" row="4" placeholder="비오는날 보기 좋은 영화 목록입니다~" style="float:left"/>
        <br /><br />
        <button class="btn btn-primary" data-toggle="modal" data-target="#find_movie">영화 추가하기</button>
        <AddMovieInRecommendModal @selectMovie="modalAddMovie" />
        <hr />
      </div>
      <!-- <div> --> 
        <div v-if="selectedMovie.id">
          <div class="d-inline-block" style="width:50% float: left;">
            <img :src="selectedMovie.post_url" alt class="movie--poster--idea"/><br><br>
          </div>
          <div class="d-inline-block" style="width:50%">
            <textarea type="text" v-model="makingMovieComment" class="comment col-9 row-5" />
            <button class="btn btn-secondary" @click="addMovie(selectedMovie)">등록</button>
          </div>
        </div>
      <!-- </div> -->

      <div>
        <div v-for="addedMovie in creationFrom.movies" :key="addedMovie.id">
          <div class="d-inline-block" style="width:50% float:left ml-7 mr-5">
            <img class="movie--poster--idea" :src="addedMovie.movie.post_url"/>
          </div>
          <div class="d-inline-block" style="width:50%">
            <h3 style="float: left">{{addedMovie.movie.title}}</h3> <br><br><br>
            <div style="float: left">{{addedMovie.movieComment}}</div>
          <br />
          </div>
        </div>
      </div><br>
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
.d_class { float: left; }
.movie--poster--idea {
  width: 180px;
  height: 250px;
  margin-top: 10px;
  margin-right: 20px;
  margin-bottom: 15px;
}
</style>