<template>
  <div :id="`recommend-${recommend.id}`">
    <span v-for="movie in recommend.movies" :key="movie.id">
      <img class="movie--poster--re my-3" :src="movie.post_url" alt="">     
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
.movie--poster--re {
  width: 120px;
  height: 175px;
  margin-right: 10px;
  position: relative;
}
</style>