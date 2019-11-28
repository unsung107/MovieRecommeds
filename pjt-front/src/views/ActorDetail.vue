<template>
  <div>
  <a :href="actor.image_url">
    <img :src="actor.image_url" alt="">
    </a>
    {{actor.name}}
    
    <div class="row">
    <span v-for="movie in actor.movies" :key="movie.id" class="border-0 card col-3">
      <router-link :to="`/movie/${movie.id}`">
      <img class="movie--poster my-3" :src="movie.post_url" :alt="movie.title"><br>
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

</style>