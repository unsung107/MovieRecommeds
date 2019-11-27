<template>
  <div>
    {{ userInfo.username }}
    {{userInfo.birthday}}
    <div v-for="movie in userInfo.like_movies" :key="`movie-${movie.id}`"> 
      {{movie.title}}
    </div>
    <div v-for="recommend in userInfo.recommends" :key="`recommend-${recommend.id}`"> 
      {{recommend.title}}
      {{recommend.discription}}
      
      <div v-for="movie in recommend.movies" :key="`recommendmovie-${movie.id}`">
        <img :src="movie.post_url" alt="">
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'userDetail',
  data() {
    return {
      userInfo: {},
      user_id: this.$route.params.user_id,
    }
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