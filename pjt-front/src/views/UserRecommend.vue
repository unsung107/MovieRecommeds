<template>
  <div>
    
    <Recommend v-for="recommend in recommends" :key="recommend.id" :recommend="recommend" />
  </div>
</template>

<script>
import axios from 'axios'
import Recommend from '@/components/Recommend'
import jwtDecode from "jwt-decode";

export default {
  name: 'UserRecommend',
  data() {
    return {
      recommends: [],
      user_id: this.$route.params.user_id,
    }
  },
  components: {
    Recommend
  },
  computed: {
    token() {
      return this.$session.get('jwt')
    }
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