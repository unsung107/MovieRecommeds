<template>
  <div>

  </div>
</template>

<script>
import jwtDecode from 'jwt-decode'

export default {
  name: 'MovieForYou',
  data() {

  },
  computed: {
    token() {
      return this.$session.get('jwt')
    },
    user_id() {
      return jwtDecode(this.token).user_id;
    },
  },
}
</script>

<style>

</style>