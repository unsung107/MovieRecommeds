<template>
  <div class="container">
    <!-- movie poster -->
    <div class="d-inline-block" style="width:30%">
      <a :href="movie.post_url">
        <img class="movie--poster my-3" :src="movie.post_url" alt />
      </a>
    </div>
    <!-- movie title discription -->
    <div class="d-inline-block" style="width:70%">
      <!-- {{ movie }} -->
      <h3>
        {{ movie.title }}
        <i
          v-if="token"
          @click="goodMovie(movie.id, movie)"
          :class="(movie.liked_users && movie.liked_users.indexOf(user_id) !== -1) ?'fas fa-heart' : 'far fa-heart'"
        ></i>
      </h3>
      {{ movie.discription }}
    </div>
    <div class="ml-5 d-inline-block" style="width: 250px">
      <h5 style="float:right">평점: {{ movie.score }}  관객수: {{ movie.audience }}</h5>
    </div>
    <div>
      <a
        data-toggle="collapse"
        :href="`#user-collapse`"
        role="button"
        aria-expanded="false"
        aria-controls="collapseExample"
      >이 영화를 좋아하는 사람들</a>
      <div class="collapse" id="user-collapse">
        <span v-for="user in movie.liked_users_info" :key="`user-${user.id}`">
          <router-link :to="`/UserDetail/${user.id}`">{{ user.username }}</router-link>
        </span>
      </div>
    </div>
    <hr />
    <!-- movie 평점 관객수 좋아요누른사람 -->

    <!-- 감독, 배우 -->
    <h4>감독</h4>
    <div class="row">
      <span class="border-0 card col-2 my-3" v-for="director in movie.directors" :key="director.id">
        <router-link :to="`/director/${director.id}`">
          <br />
          <img
            :src="director.image_url"
            :alt="director.name"
            :key="director.id"
            class="person--poster rounded-circle"
          />
        </router-link>
        <br />
        {{ director.name }}
        <i
          v-if="token"
          @click="goodDirector(director.id, director)"
          :class="(director.liked_users && director.liked_users.indexOf(user_id) !== -1) ?'fas fa-heart' : 'far fa-heart'"
        ></i>
      </span>
    </div>
    <hr />
    <h4>배우</h4>
    <div class="row">
      <span class="border-0 card col-2 my-3" v-for="actor in movie.actors" :key="actor.id">
        <router-link :to="`/actor/${actor.id}`">
          <img
            :src="actor.image_url"
            :alt="actor.name"
            :key="actor.id"
            class="person--poster rounded-circle"
          />
        </router-link>
        <a
          data-toggle="collapse"
          :href="`#actor-${actor.id}`"
          role="button"
          aria-expanded="false"
          aria-controls="collapseExample"
        >영화보기</a>
        <ActorCollapse :actor="actor" />
        <br />
        {{ actor.name }}
        <i
          v-if="token"
          @click="goodActor(actor.id, actor)"
          :class="(actor.liked_users && actor.liked_users.indexOf(user_id) !== -1) ?'fas fa-heart' : 'far fa-heart'"
        ></i>
      </span>
    </div>

    <hr />
    <div style="text-align: left;">
      <h4>예고편 및 스냅샷</h4>
      <br />
      <br />
    </div>
    <!-- vedio -->
    <div class="d-inline-block" style="width:40%">
      <iframe
        :src="movie.video_url"
        frameborder="0"
        width="400px"
        height="300px"
        style="position:relative"
      ></iframe>
    </div>
    <!-- snapshot -->
    <div class="d-inline-block test" style="width:60%">
      <div
        style="width:80%"
        id="carouselExampleIndicators"
        class="carousel slide"
        data-ride="carousel"
      >
        <ol class="carousel-indicators">
          <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
          <li
            v-for="idx in movie.snapshot_url.length - 1"
            :key="idx"
            data-target="#carouselExampleIndicators"
            :data-slide-to="idx"
          ></li>
        </ol>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img class="d-block w-100" :src="movie.snapshot_url[0]" alt="First slide" />
          </div>

          <div
            v-for="idx in movie.snapshot_url.length - 1"
            :key="`snapshot-${idx}`"
            class="carousel-item"
          >
            <img class="d-block w-100" :src="movie.snapshot_url[idx]" alt="Second slide" />
          </div>
        </div>
        <a
          class="carousel-control-prev"
          href="#carouselExampleIndicators"
          role="button"
          data-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a
          class="carousel-control-next"
          href="#carouselExampleIndicators"
          role="button"
          data-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
    </div>
    <hr />
    <!-- review -->
    <h4>Reveiw</h4><br><br>
    <div v-if="token" style="float:left ml-2">
      <input type="text" v-model="review.content" />
      <i
        v-for="idx in [1,2,3,4,5]"
        :class="(review.score >= idx)? 'fas fa-star' :'far fa-star'"
        :key="`star-${idx}`"
        @mouseover="getScore(idx)"
        @click="fixScore(idx)"
        :id="`star-${idx}`"
      ></i>
      <button @click="createReview">작성</button>
    </div>
    <br />
    <div>
      <hr>
      <div v-for="review in reviews" :key="review.id" style="text-align: left;">
        <router-link :to="`/UserDetail/${review.user_id}`">{{review.username}}</router-link>
        : {{review.content}}
        <i
          v-for="idx in [1,2,3,4,5]"
          :class="(review.score >= idx)? 'fas fa-star' :'far fa-star'"
          :key="`star-${idx}`"
          id="review-star"
        ></i>
        <i
          v-if="token && user_id === review.user_id"
          @click="deleteReview(review.id)"
          class="fas fa-times"
        ></i>
        <hr>
      </div>
           
    </div>
    <span v-if="user_id === 1">
    <router-link :to="`/MovieUpdate/${movie.id}`">
    영화수정하기
    </router-link>
    </span>
  </div>
</template>
<script>
import axios from "axios";
import jwtDecode from "jwt-decode";
import ActorCollapse from "@/components/ActorCollapse";

export default {
  name: "detail",
  components: {
    ActorCollapse
  },
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
      isFixxed: false
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
    fixScore(score) {
      this.review.score = score;
      this.isFixxed = !this.isFixxed;
    },
    getScore(score) {
      if (!this.isFixxed) {
        this.review.score = score;
      }
    },
    getMovieInfo(movie_id) {
      axios
        .get(this.SERVER_IP + `/movies/api/v1/movieDetail/${movie_id}/`)
        .then(response => {
          this.movie = response.data;
          this.reviews = response.data.reviews;
          this.loading = false;
        });
    },
    goodMovie(movie_id, movie) {
      axios
        .post(
          this.SERVER_IP + `/movies/likemovie/${movie_id}/${this.user_id}/`,
          {},
          this.options
        )
        .then(response => {
          if (response.data.liked) {
            movie.liked_users.push(this.user_id);
          } else {
            movie.liked_users = movie.liked_users.filter(
              user => user !== this.user_id
            );
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    goodDirector(director_id, director) {
      axios
        .post(
          this.SERVER_IP +
            `/movies/likedirector/${director_id}/${this.user_id}/`,
          {},
          this.options
        )
        .then(response => {
          if (response.data.liked) {
            director.liked_users.push(this.user_id);
          } else {
            director.liked_users = director.liked_users.filter(
              user => user !== this.user_id
            );
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    goodActor(actor_id, actor) {
      axios
        .post(
          this.SERVER_IP + `/movies/likeactor/${actor_id}/${this.user_id}/`,
          {},
          this.options
        )
        .then(response => {
          if (response.data.liked) {
            actor.liked_users.push(this.user_id);
          } else {
            actor.liked_users = actor.liked_users.filter(
              user => user !== this.user_id
            );
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    createReview() {
      axios
        .post(
          this.SERVER_IP +
            `/movies/api/v1/createMovieReview/${this.user_id}/${this.movie_id}/`,
          this.review,
          this.options
        )
        .then(response => {
          this.reviews.push(response.data);
        });
    },
    deleteReview(review_id) {
      axios
        .post(
          this.SERVER_IP + `/movies/api/v1/deleteRevieReview/${review_id}/`,
          {},
          this.options
        )
        .then(response => {
          console.log(response);
          this.reviews = this.reviews.filter(review => review.id != review_id);
        });
    }
  },
  mounted() {
    this.movie_id = this.$route.params.movie_id;
    this.getMovieInfo(this.movie_id);
  }
};
</script>
<style>
.test {
  height: 300px !important;
  overflow: hidden;
}
/* .test div, .test ol, .test img{ height: 300px !important;  } */
h4 {
  float: left;
}
</style>