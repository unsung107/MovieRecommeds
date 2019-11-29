<template>
<div class="container">
  <div>
    <h3>[ {{recommend.title}} ]  
    <i
      v-if="token"
      @click="goodRecommend(recommend.id, recommend)"
      :class="(recommend.liked_users && recommend.liked_users.indexOf(user_id) !== -1) ?'fas fa-heart' : 'far fa-heart'"
    ></i></h3><br>
    <div>>{{recommend.discription}}</div>
    <button v-if="token && recommend.user === user_id" @click="deleteRecommend" class="list_app btn btn-secondary">리스트 삭제</button>
    
    
    
    <br />
    <span>
      <movieInRecommend :movie="recommend.movies[0]" :moviecomment="recommend.moviecomments[0]" />
    </span>
    <hr >
    <div class="review-div">
      
      <div v-if="recommend.movies.length > 1">
        <span v-for="idx in recommend.movies.length - 1" :key="`movieinrecommend-${idx}`">
          <movieInRecommend
            :movie="recommend.movies[idx]"
            :moviecomment="recommend.moviecomments[idx]"
          />
          <hr />
        </span>
      </div>
      <h5 class="review">Review</h5>
      <div v-if="token">
        <input type="text" v-model="review.content" />
        <button class="btn btn-secondary" style="ml-2" @click="createReview">작성</button><br><br>
      </div>
      <div>
      
        <span v-for="review in recommend_reviews" :key="review.id">
          <router-link :to="`/UserDetail/${review.user}`">{{review.username}}</router-link>
          : {{review.content}}
          <button
            v-if="token && user_id === review.user_id"
            @click="deleteReview(review.id)"
            class="btn--review btn-secondary"
          > review 삭제</button>
          <br />
        </span>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import jwtDecode from "jwt-decode";
import router from "@/router";
import movieInRecommend from "@/components/movieInRecommend";

export default {
  name: "RecommendDetail",
  data() {
    return {
      recommend_id: this.$route.params.recommend_id,
      recommend: {},
      token: this.$session.get("jwt"),
      review: {
        content: ""
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
      axios
        .get(
          this.SERVER_IP + `/movies/api/v1/recommendDetail/${this.recommend_id}`
        )
        .then(response => {
          this.recommend = response.data;
          this.recommend_reviews = this.recommend.recommend_reviews;
        });
    },
    createReview() {
      axios
        .post(
          this.SERVER_IP +
            `/movies/api/v1/createRecommendReview/${this.user_id}/${this.recommend_id}/`,
          this.review,
          this.options
        )
        .then(response => {
          this.recommend_reviews.push(response.data);
        });
    },
    deleteReview(review_id) {
      axios
        .post(
          this.SERVER_IP + `/movies/api/v1/deleteRecommendReview/${review_id}/`,
          {},
          this.options
        )
        .then(response => {
          console.log(response);
          this.recommend_reviews = this.recommend_reviews.filter(
            review => review.id != review_id
          );
        });
    },
    goodRecommend(recommend_id, recommend) {
      axios
        .post(
          this.SERVER_IP +
            `/movies/likerecommend/${recommend_id}/${this.user_id}/`,
          {},
          this.options
        )
        .then(response => {
          if (response.data.liked) {
            recommend.liked_users.push(this.user_id);
          } else {
            recommend.liked_users = recommend.liked_users.filter(
              user => user !== this.user_id
            );
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    deleteRecommend() {
      axios
        .post(
          this.SERVER_IP +
            `/movies/api/v1/deleteRecommend/${this.recommend_id}/`,
          {},
          this.options
        )
        .then(response => {
          response;
          router.push("/RecommendList");
        });
    }
  },
  mounted() {
    this.getRecommend();
  }
};
</script>

<style>
.list_app {
  position: relative;
  left: 350px;
  top: 10px
}
.review {
  position: relative;
  right: 300px;
  top: 10px
}
/* .review-div {
  margin-left: 200px;
} */
.btn--review {
  height: 30px;
}
</style>