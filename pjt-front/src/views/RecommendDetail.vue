<template>
  <div>
    {{recommend.title}}
    {{recommend.discription}}
    {{recommend.user}}
    <button v-if="token" @click="goodRecommend(recommend.id)">좋아요</button><br>
    <span>
      <movieInRecommend :movie="recommend.movies[0]" :moviecomment="recommend.moviecomments[0]"/>
    </span>
    <hr>
    <span
      v-for="idx in recommend.movies.length - 1"
      :key="`movieinrecommend-${idx}`"
    >
      <movieInRecommend :movie="recommend.movies[idx]" :moviecomment="recommend.moviecomments[idx]"/>
      <hr>
    </span>

    <div v-if="token">
      <input type="text" v-model="review.content" />
      <button @click="createReview">작성</button>
    </div>
    <div>
      <span v-for="review in recommend_reviews" :key="review.id">
        <router-link :to="`/UserDetail/${review.user}`">{{review.username}}</router-link> : {{review.content}} {{review.id}}
        <button
          v-if="token && user_id === review.user_id"
          @click="deleteReview(review.id)"
        >x</button>
        <br />
      </span>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import jwtDecode from 'jwt-decode'
import movieInRecommend from '@/components/movieInRecommend'

export default {
  name: "RecommendDetail",
  data() {
    return {
      recommend_id: this.$route.params.recommend_id,
      recommend: {},
      token: this.$session.get("jwt"),
      review: {
        content: "",
      },
      recommend_reviews: [],
      SERVER_IP: process.env.VUE_APP_SERVER_IP
    };
  },
  components: {
    movieInRecommend
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
    getRecommend() {
      axios.get(this.SERVER_IP + `/movies/api/v1/recommendDetail/${this.recommend_id}`).then(response => {
        this.recommend = response.data;
        this.recommend_reviews = this.recommend.recommend_reviews
      });
    },
    createReview() {
      axios
        .post(this.SERVER_IP + `/movies/api/v1/createRecommendReview/${this.user_id}/${this.recommend_id}/`, this.review, this.options)
        .then(response => {
          this.recommend_reviews.push(response.data)
        })
    },
    deleteReview(review_id) {
      axios.post(this.SERVER_IP + `/movies/api/v1/deleteRecommendReview/${review_id}/`, {}, this.options)
      .then(response => {
        console.log(response)
        this.recommend_reviews = this.recommend_reviews.filter(review => review.id != review_id)
      })
    },
    goodRecommend(recommend_id) {
      axios
        .post(
          this.SERVER_IP + `/movies/likerecommend/${recommend_id}/${this.user_id}/`,
          {},
          this.options
        )
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  mounted() {
    this.getRecommend();
  }
};
</script>

<style>
</style>