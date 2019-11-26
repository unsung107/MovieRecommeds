<template>
  <div>
    {{ userInfo }}
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'userDetail',
  data() {
    return {
      userInfo: {},
      user_id: this.$route.params.user_id,
    }
  },

  methods: {
    getUser() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP + `/movies/api/v1/userDetail/${this.user_id}/`; 

      axios.get(SERVER_IP)
      .then(response => {
        this.userInfo = response.data
        console.log(response.data)
      })
    }
  },

  mounted() {
    this.getUser()
  }
}
</script>

<style>

</style>