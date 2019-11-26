<template>
  <div>
    <!-- {{recommend}} -->
    {{recommend.title}}
    {{recommend.discription}}
    <span v-for="movie in recommend.movies" :key="movie.id">{{movie.title}}
      <img :src="movie.post_url">
    </span>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'RecommendDetail',
  data() {
    return{
      recommend_id: this.$route.params.recommend_id,
      recommend: {},
    }
  },
  props:{
  },
  methods: {
    getRecommend() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP + `/movies/api/v1/recommendDetail/${this.recommend_id}`;
      axios.get(SERVER_IP)
      .then(response =>{ 
        this.recommend = response.data
      })
    }
  },
  mounted() {
    
    this.getRecommend()
  }
}
</script>

<style>

</style>