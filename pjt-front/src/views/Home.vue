<template>
    <div class="container">
      <button type="button" class="btn btn-outline-info" @click="getMovie(0)">   최신   </button>
      <button type="button" class="btn btn-outline-info" @click="getMovie(1)">   애니메이션   </button>
      <button type="button" class="btn btn-outline-info" @click="getMovie(2)">  범죄  </button>
      <button type="button" class="btn btn-outline-info" @click="getMovie(3)">   드라마   </button>
      <button type="button" class="btn btn-outline-info" @click="getMovie(5)">    어드벤처    </button>
      <button type="button" class="btn btn-outline-info" @click="getMovie(10)">  코미디  </button>
    <br /><br />

    <!-- search bar -->
    <form class="form-inline md-form form-sm mt-0 search-box">
      <div class="searchWrap">
      <i class="fas fa-search" aria-hidden="true"></i>
      <input class="search-box-inner form-control form-control-sm w-75" type="text" placeholder="Search" aria-label="Search" v-model="searchKey" @input="searching(searchKey)">
      </div>
    </form>

    <!--  -->
    <div class="row">
      <span class="border-0 card col-3 my-3" v-for="movie in movies" :key="movie.id">
        <router-link :to="`/movie/${movie.id}`">
          <img class="movie--poster my-3" :src="movie.post_url" :alt="movie.title" />
        </router-link>
        {{ movie.title }} <i v-if="token" @click="goodMovie(movie.id, movie)" :class="(movie.liked_users && movie.liked_users.indexOf(user_id) !== -1) ?'fas fa-heart' : 'far fa-heart'"></i>
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
    goodMovie(movie_id, movie) {
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
          if (response.data.liked) {
            movie.liked_users.push(this.user_id)
          } else{
            movie.liked_users = movie.liked_users.filter(user => user !== this.user_id)
          }
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
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
  mounted() {
    this.getMovie(0)
  },
};
</script>

<style>

.btn-outline-info {
  margin-right: 5px;
  position: relative;
	width: 11%;
}
container {
  position: relative;
  margin: 0 auto;
}

.search-box { text-align: center; }
.fas {padding: 5px; }
.searchWrap { width: 970px; margin: 0 auto; }

</style>