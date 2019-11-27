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
        <button v-if="token" @click="goodMovie(movie.id)">좋아요</button>
      </span>
    </div>

  </div>
</template>

<script>
import axios from "axios";
import jwtDecode from "jwt-decode";
// import MovieDetail from "@/components/MovieDetail.vue";
// @ is an alias to /src

export default {
  name: "home",
  data() {
    return {
      movies: [],
      searchKey: "",
      user: "",
    };
  },
  components: {
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
    },
    goodMovie(movie_id) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      this.$session.start();
      const options = {
        headers: {
          Authorization: "JWT " + this.token
        }
      };

      axios
        .post(
          SERVER_IP + `/movies/likemovie/${movie_id}/${this.user_id}/`,
          {},
          options
        )
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  mounted() {},
  computed: {
    token() {
      return this.$session.get('jwt')
    },
    movieList() {
      return this.movies;
    },
    user_id() {
      return jwtDecode(this.token).user_id;
    }
  },
};
</script>

<style>
</style>