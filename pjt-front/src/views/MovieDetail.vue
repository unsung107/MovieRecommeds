<template>
  <div class="container">
    <img class="movie--poster my-3" :src="movie.post_url" alt />
    <button @click="goodMovie(movie.id)">좋아요</button>
    review

    <div class="row">
      <span class="card col-3 my-3" v-for="director in movie.directors" :key="director.id">
        감독
        <router-link :to="`/director/${director.id}`">
        <br>
          <img :src="director.image_url" :alt="director.name" :key="director.id" class="movie--poster rounded-circle" /><br>

          {{ director.name }}
          <button @click="goodDirector(director.id)">좋아요</button>
          
        </router-link>
      </span>
      <span class="card col-3 my-3" v-for="actor in movie.actors" :key="actor.id">
        배우
        <router-link :to="`/actor/${actor.id}`">
          <img :src="actor.image_url" :alt="actor.name" :key="actor.id" class="movie--poster rounded-circle" /><br>
          {{ actor.name }}
          <button @click="goodActor(actor.id)">좋아요</button>
        </router-link>
      </span>
    </div>

  </div>
</template>

<script>
import axios from "axios";
import jwtDecode from "jwt-decode";

export default {
  name: "detail",
  data() {
    return {
      movie: {},
      movie_id: this.$route.params.movie_id
    };
  },
  methods: {
    getMovieInfo(movie_id) {
      const SERVER_IP =
        process.env.VUE_APP_SERVER_IP +
        `/movies/api/v1/movieDetail/${movie_id}`;

      axios.get(SERVER_IP).then(response => {
        this.movie = response.data;
      });
    },
    goodMovie(movie_id) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      this.$session.start()
      const token = this.$session.get('jwt')
      const user_id = jwtDecode(token).user_id
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      
      axios.post(SERVER_IP + `/movies/likemovie/${movie_id}/${user_id}/`, {} ,options)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error);
        })
    },
    goodDirector(director_id) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      this.$session.start()
      const token = this.$session.get('jwt')
      const user_id = jwtDecode(token).user_id
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      
      axios.post(SERVER_IP + `/movies/likedirector/${director_id}/${user_id}/`, {} ,options)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error);
        })
    },
    goodActor(actor_id) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      this.$session.start()
      const token = this.$session.get('jwt')
      const user_id = jwtDecode(token).user_id
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      
      axios.post(SERVER_IP + `/movies/likeactor/${actor_id}/${user_id}/`, {} ,options)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error);
        })
    },
  },
  mounted() {
    this.getMovieInfo(this.movie_id);
  }
};
</script>

<style>
</style>