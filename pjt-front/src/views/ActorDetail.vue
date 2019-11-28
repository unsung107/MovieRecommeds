<template>
  <div>
  
    <span :href="actor.image_url">
      <h4 class="actordetail" >{{actor.name}}</h4><br><br>
      <img :src="actor.image_url" alt="">
    </span><br>
    <br><br> <br><br>
    <div class="row">
    <span v-for="movie in actor.movies" :key="movie.id" class="border-0 card col-3">
      <router-link :to="`/movie/${movie.id}`">
      <img class="movie--poster-- my-3" style="width:180px height:250px" :src="movie.post_url" :alt="movie.title"><br>
      {{ movie.title }}
      </router-link>
    </span>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ActorDetail',
  data() {
    return {
      actor: {},
      actor_id: this.$route.params.actor_id,
    }
  },
  methods: {
    getMovieInfo() {

      const SERVER_IP = process.env.VUE_APP_SERVER_IP + `/movies/api/v1/actorDetail/${this.actor_id}`;

      axios.get(SERVER_IP)
      .then(response => {
        
        this.actor = response.data
      })
    }
  },
  mounted() {
    this.getMovieInfo()
  },
}
</script>

<style>
.actordetail {
  margin-left: 660px
}
</style>