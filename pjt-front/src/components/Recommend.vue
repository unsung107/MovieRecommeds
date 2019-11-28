<template>
<a data-toggle="collapse" :href="`#recommend-${recommend.id}`" role="button" aria-expanded="false" aria-controls="collapseExample">
  <div> <br>
    <router-link :to="`/RecommendDetail/${recommend.id}`">
    <h5 style="">[ {{ recommend.title }} ]</h5>
    </router-link><br>
    {{ recommend.discription }}
    
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
  computed: {
    token() {
      return this.$session.get('jwt')
    },
    user_id() {
      return jwtDecode(this.token).user_id;
    }
  },
  methods: {
    goodRecommend(recommend_id, recommend) {
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
          if (response.data.liked) {
            recommend.liked_users.push(this.user_id)
          } else{
            recommend.liked_users = recommend.liked_users.filter(user => user !== this.user_id)
          }
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