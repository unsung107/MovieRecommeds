<template>
  <div>
    {{ recommend.title }}
    {{ recommend.discription }}
    <span v-for="movie in recommend.movies" :key="movie.id">
      <img :src="movie.post_url" alt="">
      
    </span>
    <hr>
  </div>
</template>

<script>


export default {
  name: 'Recommend',
  data() {
    return {

    }
  },
  components: {

  },
  props: {
    recommend: Object
  },
}
</script>

<style>

</style>