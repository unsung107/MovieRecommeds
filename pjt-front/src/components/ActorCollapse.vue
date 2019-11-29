<template>
  <div class="collapse panel-collapse" :id="`actor-${actor.id}`" role="tabpanel">
    <!-- {{actor}} -->
    <span v-for="movie in actor.movies" :key="movie.id">
      <img class="movie--poster--mini my-3" :src="movie.post_url" alt="">     
    </span>
  </div>
</template>

<script>

export default {
  name: 'ActorCollapse',
  data() {
    return{
    }
  },
  props: {
    actor: Object
  }
}
</script>

<style>

</style>