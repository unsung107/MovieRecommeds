<template>
  <div>
    <movieInRecommend />
    {{recommends}}
    <button v-if="token" @click="goodRecommend(recommend.id)">좋아요</button>
    
  </div>
</template>

<script>
import axios from 'axios'
import movieInRecommend from '@/components/movieInRecommend'
import jwtDecode from "jwt-decode";

export default {
  name: 'RecommendDetail',
  data() {
    return {
      recommends: [],
      user_id: this.$route.params.user_id,
    }
  },
  components: {
    movieInRecommend
  },
  methods: {
    getRecommend() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP + `/movies/api/v1/recommendList/${this.user_id}/`;

      axios.get(SERVER_IP)
      .then(response => {
        this.recommends = response.data.recommends
      })
    },
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
  },
  mounted() {
    this.getRecommend()
  }

  
}
</script>

<style>

</style>