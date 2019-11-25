<template>
  <div>
    <h1>Signup Form</h1>
    
    <input type="text" v-model="credentials.id">
    <input type="password" v-model="credentials.password1">
    <input type="password" v-model="credentials.password2">
    <input type="number" v-model="credentials.age">
    <button @click="signup">제출</button>
    
    <!-- <form @submit.prevent="signup">
      <b-form-group label="Enter your id">
        <b-form-input type="text" v-model="id" aria-placeholder="아이디를 입력하세요"></b-form-input>
      </b-form-group>

      <b-form-group label="Enter your password">
        <b-form-input type="password" v-model="password" aria-placeholder="비밀번호를 입력하세요"></b-form-input>
      </b-form-group>

      <b-form-group label="Enter your birthday">
        <b-form-input type="date" v-model="birthday" aria-placeholder="생년월일을 입력하세요"></b-form-input>
      </b-form-group>

      <b-button size="lg" variant="success" type="submit">Signup</b-button>
    </form> -->
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Signup',
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
          age:0,
        },
      loading: false,
      errors: [],
      }
    },
    methods: {
      signup () {
        const id = this.credentials.id
        const password1 = this.credentials.password1
        const password2 = this.credentials.password2
        const age = this.credentials.age

        if (!id || !password1 || !password2 || !age) {
            return false
        }

        axios.post('http://127.0.0.1:8000/accounts/signup/', { 'username':id, 'password1':password1,'password2':password2, 'age':age })
            .then(res => {
              console.log(res)
                if (res.status === 200) {
                    // 성공적으로 회원가입이 되었을 경우
                    this.$router.push({ name: 'Signin' })
                }
            })
      }
    }
  }
</script>

<style>

</style>