<template>
  <div class="login-div">

    <div v-if='loading' role="status">
      <span>loading</span>
    </div>

    <div class="login-form">

      <div v-if="errors.length">
        <h4>다음의 오류를 해결해주세요!</h4>
        <hr>
        <div v-for="(error, idx) in errors" v-bind:key="idx">{{ error }}</div>
      </div>

      <div class="form-group">
        <label for="id">ID </label>
        <input type="text" id="id" placeholder="아이디를 입력해주세요" v-model="credentials.username">
      </div>

      <div class="form-group">
        <label for="password">password</label>
        <input type="password" id="password" placeholder="비밀번호를 입력해주세요" v-model="credentials.password">
      </div>

      <div>
        <button v-on:click="login">Login</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'

export default {
  name: 'LoginForm',
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      },
      loading: false,
      errors: [],
    }
  },
  props:{
  },
  methods: {
    login() {
      if (this.checkForm()) {
        this.loading = true
        const SERVER_IP = process.env.VUE_APP_SERVER_IP

        axios.post(SERVER_IP + '/api-token-auth/', this.credentials)
          .then(response => {
            this.$session.start()
            this.$session.set('jwt', response.data.token)
            this.loading = false
            // console.log(response)
            router.push('/')
          })
          .catch(error => {
            console.log(error)
            this.loading = false
          })
      }
    },
    checkForm() {
      this.errors = []
      if (!this.credentials.username) {
        this.errors.push('아이디를 입력해주세요')
      }
      if (this.credentials.password < 8) {
        this.errors.push('비밀번호는 8글자 이상 입력해주세요')
      }
      if (this.errors.length === 0) {
        return true
      }
    },
  },

}
</script>

<style>

</style>