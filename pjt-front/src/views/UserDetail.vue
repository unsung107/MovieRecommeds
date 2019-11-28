<template>
  <div>
    {{ userInfo.username }}
    {{userInfo.birthday}}
    <br>
    <router-link :to="`/UserRecommend/${user_id}`"> {{userInfo.username}} 님이 추천하는 영화 </router-link>
    <hr>
    <br>
    {{userInfo.username}} 님이 좋아하는 영화
    <br>
     <br>
    <div v-for="movie in userInfo.like_movies" :key="`movie-${movie.id}`" class="d-inline-block mr-5"> 
    <router-link :to="`/movie/${movie.id}`">
        <img
          :src="movie.post_url"
          :alt="movie.title"
          :key="movie.id"
          class="person--poster rounded-circle"
        /></router-link>
      {{movie.title}}
    </div>
    <hr>
    {{userInfo.username}} 님이 좋아하는 배우
    <br>
 <br>
    <div v-for="actor in userInfo.like_actors" :key="actor.id" class="d-inline-block mr-5">
      <router-link :to="`/actor/${actor.id}`">
        <img
          :src="actor.image_url"
          :alt="actor.name"
          :key="actor.id"
          class="person--poster rounded-circle"
        /></router-link>
        <br>
        {{ actor.name }}
      
    </div>
    <hr>
    {{userInfo.username}} 님이 좋아하는 감독
    <br>
    <div v-for="director in userInfo.like_directors" :key="director.id" class="d-inline-block mr-5">
      <router-link :to="`/director/${director.id}`">
        <img
          :src="director.image_url"
          :alt="director.name"
          :key="director.id"
          class="person--poster rounded-circle"
        />
        <br></router-link>
        {{ director.name }}
      
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