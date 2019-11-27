<template>
  <div>
    {{ userInfo.username }}
    {{userInfo.birthday}}
    <router-link :to="`/UserRecommend/${user_id}`"> {{userInfo.username}} 님의 추천리스트 보러가기 </router-link>
    <br>
    <span v-for="movie in userInfo.like_movies" :key="`movie-${movie.id}`"> 
      {{movie.title}}
    </span>
    <hr>
    내가 좋아하는 배우
    <br>
    <span v-for="actor in userInfo.like_actors" :key="actor.id">
      <router-link :to="`/actor/${actor.id}`">
        <img
          :src="actor.image_url"
          :alt="actor.name"
          :key="actor.id"
          class="person--poster rounded-circle"
        />
        {{ actor.name }}
      </router-link>
    </span>
    <hr>
    내가 좋아하는 감독
    <br>
    <span v-for="director in userInfo.like_directors" :key="director.id">
      <router-link :to="`/director/${director.id}`">
        <img
          :src="director.image_url"
          :alt="director.name"
          :key="director.id"
          class="person--poster rounded-circle"
        />
        {{ director.name }}
      </router-link>
    </span>
    
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