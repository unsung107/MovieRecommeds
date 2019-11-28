<template>
  <div>
    <img class="movie--poster--post" :src="movie.post_url" alt=".">
    <span class="content">{{moviecomment.content}}</span>
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
.movie--poster--post {
  width: 200px;
  height: 290px;
}
.content {
  margin-left: 50px;
}
</style>