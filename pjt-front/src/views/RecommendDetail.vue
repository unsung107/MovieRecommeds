<template>
  <div>
    <movieInRecommend />
    {{recommends}}
    
  </div>
</template>

<script>
import axios from 'axios'
import movieInRecommend from '@/components/movieInRecommend'

export default {
  name: 'RecommendDetail',
  data() {
    return {
      recommends: [],
      user_id: this.$route.params.user_id,
    }
  },
  components: {
    movieInRecommend
  },
  methods: {
    getRecommend() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP + `/movies/api/v1/recommendList/${this.user_id}/`;

      axios.get(SERVER_IP)
      .then(response => {
        this.recommends = response.data.recommends
      })
    }
  },
  mounted() {
    this.getRecommend()
  }

  
}
</script>

<style>

</style>