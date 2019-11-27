<template>
  <div>
    <router-link :to="`/RecommendDetail/${recommend.id}`">
    {{ recommend.title }}
    </router-link>
    {{ recommend.discription }}
    <span v-for="movie in recommend.movies" :key="movie.id">
      <img class="movie--poster my-3" :src="movie.post_url" alt="">     
    </span>
    <button @click="goodRecommend(recommend.id)">좋아요</button>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from "jwt-decode";

export default {
  name: 'Recommend',
  data() {
    return {

    }
  },
  components: {

  },
  props: {
    recommend: Object
  },
  methods: {
    goodRecommend(recommend_id) {
      console.log(recommend_id)
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      this.$session.start()
      const token = this.$session.get('jwt')
      const user_id = jwtDecode(token).user_id
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      
      axios.post(SERVER_IP + `/movies/likerecommend/${recommend_id}/${user_id}/`, {} ,options)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error);
        })
    },
  }
}
</script>

<style>

</style>