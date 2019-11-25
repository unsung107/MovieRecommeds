<template>
  <div>
    <h1>Signup Form</h1>
    <div>Enter your id</div>
    <input type="text" v-model="credentials.id"><br><br>
    <div>Enter your password</div>
    <input type="password" v-model="credentials.password1"><br><br>
    <div>Enter your password again</div>
    <input type="password" v-model="credentials.password2"><br><br>
    <div>Enter your birthday</div>
    <input type="date" v-model="credentials.birthday"><br><br>
    <button @click="signup">제출</button>
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
          birthday: 0,
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
        const birthday = this.credentials.birthday

        let born = birthday.split('-')[0]
        console.log(born)

        if (!id || !password1 || !password2 || !birthday) {
            return false
        }

        axios.post('http://127.0.0.1:8000/accounts/signup/', { 'username':id, 'password1':password1,'password2':password2, 'birthday':birthday })
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