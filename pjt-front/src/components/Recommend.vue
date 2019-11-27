<template>
<a data-toggle="collapse" :href="`#recommend-${recommend.id}`" role="button" aria-expanded="true" aria-controls="collapseExample">
  <div>
    <router-link :to="`/RecommendDetail/${recommend.id}`">
    {{ recommend.title }}
    </router-link>
    {{ recommend.discription }}
    
    <button @click="goodRecommend(recommend.id)">좋아요</button>
    <hr>
    <RecommendCollapse :recommend="recommend" />
  </div>
  </a>
</template>

<script>
import axios from 'axios'
import jwtDecode from "jwt-decode";
import RecommendCollapse from '@/components/RecommendCollapse'

export default {
  name: 'Recommend',
  data() {
    return {

    }
  },
  components: {
    RecommendCollapse
  },
  props: {
    recommend: Object
  },
  methods: {
    goodRecommend(recommend_id) {
      console.log(recommend_id)
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      this.$session.start()
      const token = this.$session.get('jwt')
      const user_id = jwtDecode(token).user_id
      const options = {
        headers: {
          Authorization: 'JWT ' + token
        }
      }
      
      axios.post(SERVER_IP + `/movies/likerecommend/${recommend_id}/${user_id}/`, {} ,options)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error);
        })
    },
  }
}
</script>

<style>

</style>