<template>
  <div class="collapse" :id="`recommend-${recommend.id}`">
    <span v-for="movie in recommend.movies" :key="movie.id">
      <img class="movie--poster my-3" :src="movie.post_url" alt="">     
    </span>
  </div>
</template>

<script>

export default {
  name: 'RecommendCollapse',
  data() {
    return{
    }
  },
  props: {
    recommend: Object
  }
}
</script>

<style>

</style>