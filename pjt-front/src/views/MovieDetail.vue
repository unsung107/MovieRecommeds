<template>
  <div class="container">
    <!-- movie poster -->
    <div class="d-inline-block" style="width:30%">
      <img class="movie--poster my-3" :src="movie.post_url" alt />
    </div>
    <!-- movie title discription -->
    <div class="d-inline-block" style="width:70%">
      <!-- {{ movie }} -->
      <h3>{{ movie.title }}</h3>
      {{ movie.discription }}
    </div>
    <!-- movie 평점 관객수 좋아요누른사람 -->
    <div class="d-inline-block">
      <h6>평점: {{ movie.score }}</h6>
    </div>
    <div class="d-inline-block">
      <h6>관객 수: {{ movie.audience }}</h6>
      <i class="fas fa-heart fa-lg" style="color:red">좋아요</i>
    </div>
    <div class="d-inline-block">
      <h3>좋아요누른사람for문돌리면서 이름뽑기</h3>
    </div>
    <!-- 감독, 배우 -->
    <div class="row">
      감독
      <span v-for="director in movie.directors" :key="director.id">
        <router-link :to="`/director/${director.id}`">
          <br />
          <img
            :src="director.image_url"
            :alt="director.name"
            :key="director.id"
            class="person--poster rounded-circle"
          />
          <br/>
          {{ director.name }}
          <button v-if="token" @click="goodDirector(director.id)">좋아요</button>
        </router-link>
      </span><hr>
      배우
      <span v-for="actor in movie.actors" :key="actor.id">
        <router-link :to="`/actor/${actor.id}`">
          <img
            :src="actor.image_url"
            :alt="actor.name"
            :key="actor.id"
            class="person--poster rounded-circle"
          />
          <br />
          {{ actor.name }}
          <button v-if="token" @click="goodActor(actor.id)">좋아요</button>
        </router-link>
      </span>
    </div>
    <hr>
    <!-- vedio -->
    <div class="d-inline-block" style="width:40%">
    <iframe :src="movie.video_url" frameborder="0" width="400px" height="300px" style="position:relative"></iframe>
    </div>
    <!-- snapshot -->
    <div class="d-inline-block test" style="width:60%">
    <div style="width:80%" id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
      <ol class="carousel-indicators">
        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
        <li v-for="idx in movie.snapshot_url.length" :key="idx" data-target="#carouselExampleIndicators" :data-slide-to="idx"></li>
      </ol>
        <div class="carousel-inner">
        <div class="carousel-item active">
          <img class="d-block w-100" :src="movie.snapshot_url[0]" alt="First slide">
        </div>
        <div v-for="idx in movie.snapshot_url.length - 1" :key="`snapshot-${idx}`" class="carousel-item">
          <img class="d-block w-100" :src="movie.snapshot_url[idx]" alt="Second slide">
        </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
    </div>
    <hr>
    <!-- review -->
    <div v-if="token">
      <input type="text" v-model="review.content" />
      <input type="number" v-model="review.score" />
      <button @click="createReview">작성</button>
    </div>
    <div>
      <span v-for="review in reviews" :key="review.id">{{review.username}} : {{review.content}}  {{review.id}}
        <button v-if="token && user_id === review.user_id" @click="deleteReview(review.id)">x</button>
        <br><br><br><br>
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
.test { height: 300px !important; overflow: hidden; }
/* .test div, .test ol, .test img{ height: 300px !important;  } */
</style>