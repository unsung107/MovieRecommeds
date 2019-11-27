<template>
  <div>
    <Recommend v-for="recommend in recommends" :key="recommend.id" :recommend="recommend"/>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
import Recommend from '@/components/Recommend'

export default {
  name: 'RecommendList',
  data() {
    return {
      recommends: []
    }
  },
  components: {
    Recommend,
  },
  methods: {
    getRecommend() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP + `/movies/api/v1/recommendList/0/`;

      axios.get(SERVER_IP)
      .then(response => {
        this.recommends = response.data.recommends
      })
    },
  },
  mounted() {
    this.getRecommend()
  }

  
}
</script>

<style>

</style>