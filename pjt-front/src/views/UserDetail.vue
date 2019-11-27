<template>
  <div>
    {{ userInfo.username }}
    {{userInfo.birthday}}
    <div v-for="movie in userInfo.like_movies" :key="`movie-${movie.id}`"> 
      {{movie.title}}
    </div>
    <router-link :to="`/UserRecommend/${user_id}`"> 추천리스트 보러가기 </router-link>
  </div>
</template>

<script>
import axios from 'axios'
// import Recommend from '@/components/Recommend'
export default {
  name: 'userDetail',
  data() {
    return {
      userInfo: {},
      user_id: this.$route.params.user_id,
    }
  },
  components: {
    // Recommend
  },
  methods: {
    getUser() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP + `/movies/api/v1/userDetail/${this.user_id}/`; 

      axios.get(SERVER_IP)
      .then(response => {
        this.userInfo = response.data
      })
    }
  },

  mounted() {
    this.getUser()
  }
}
</script>

<style>

</style>