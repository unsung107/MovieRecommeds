<template>
  <div class="container">
    <img class="movie--poster my-3" :src="movie.post_url" alt />
    <button v-if="token" @click="goodMovie(movie.id)">좋아요</button>
    review
    <div v-if="token">
      <input type="text" v-model="review.content" />
      <input type="number" v-model="review.score" />
      <button @click="createReview">작성</button>
    </div>
    <div>
      <span v-for="review in reviews" :key="review.id">{{review.username}} : {{review.content}}  {{review.id}}
        <button v-if="token && user_id === review.user_id" @click="deleteReview(review.id)">x</button>
        <br>
      
      </span>
    </div>

    <div class="row">
      <span class="card col-3 my-3" v-for="director in movie.directors" :key="director.id">
        감독
        <router-link :to="`/director/${director.id}`">
          <br />
          <img
            :src="director.image_url"
            :alt="director.name"
            :key="director.id"
            class="movie--poster rounded-circle"
          />
          <br />
          {{ director.name }}
          <button v-if="token" @click="goodDirector(director.id)">좋아요</button>
        </router-link>
      </span>
      <span class="card col-3 my-3" v-for="actor in movie.actors" :key="actor.id">
        배우
        <router-link :to="`/actor/${actor.id}`">
          <img
            :src="actor.image_url"
            :alt="actor.name"
            :key="actor.id"
            class="movie--poster rounded-circle"
          />
          <br />
          {{ actor.name }}
          <button v-if="token" @click="goodActor(actor.id)">좋아요</button>
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
      movie_id: this.$route.params.movie_id,
      token: this.$session.get("jwt"),
      review: {
        content: "",
        score: 0
      },
      reviews: [],
      SERVER_IP: process.env.VUE_APP_SERVER_IP,
    };
  },
  computed: {
    user_id: function() {
      return jwtDecode(this.token).user_id;
    },
    options() {
      return {
        headers: {
          Authorization: "JWT " + this.token
        }
      };
    }
  },
  methods: {
    getMovieInfo(movie_id) {
      axios
        .get(this.SERVER_IP + `/movies/api/v1/movieDetail/${movie_id}/`)
        .then(response => {
          this.movie = response.data;
          this.reviews = response.data.reviews
          this.loading = false;
        });
    },
    goodMovie(movie_id) {
      axios
        .post(
          this.SERVER_IP + `/movies/likemovie/${movie_id}/${this.user_id}/`,
          {},
          this.options
        )
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.log(error);
        });
    },
    goodDirector(director_id) {
      axios
        .post(
          this.SERVER_IP +
            `/movies/likedirector/${director_id}/${this.user_id}/`,
          {},
          this.options
        )
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.log(error);
        });
    },
    goodActor(actor_id) {
      axios
        .post(
          this.SERVER_IP + `/movies/likeactor/${actor_id}/${this.user_id}/`,
          {},
          this.options
        )
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.log(error);
        });
    },
    createReview() {
      axios
        .post(this.SERVER_IP + `/movies/api/v1/createMovieReview/${this.user_id}/${this.movie_id}/`, this.review, this.options)
        .then(response => {
          this.reviews.push(response.data)
        })
    },
    deleteReview(review_id) {
      axios.post(this.SERVER_IP + `/movies/api/v1/deleteRevieReview/${review_id}/`, {}, this.options)
      .then(response => {
        console.log(response)
        this.reviews = this.reviews.filter(review => review.id != review_id)
      })
    },
  },
  mounted() {
    this.movie_id = this.$route.params.movie_id;
    this.getMovieInfo(this.movie_id);
  },
};
</script>

<style>
</style>