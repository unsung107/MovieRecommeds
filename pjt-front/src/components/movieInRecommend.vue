<template>
  <div>
    <img class="movie--poster" :src="movie.post_url" alt=".">
    {{moviecomment.content}}
  </div>
</template>

<script>
export default {
  name: 'movieInRecommend',
  props: {
    movie: Object,
    moviecomment: Object
  }
}
</script>

<style>

</style>