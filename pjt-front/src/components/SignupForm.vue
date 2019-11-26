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
    <button @click="signup">제출</button><br>
    
    <!-- <span v-for="error in errors[0].username" :key="error">{{error}}</span>
    <span v-for="error in errors[0].password1" :key="error">{{error}}</span>
    <span v-for="error in errors[0].password2" :key="error">{{error}}</span> -->
  </div>

</template>

<script>
  import axios from 'axios'
  // import date from 'date'

  export default {
    name: 'Signup',
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
          birthday: new Date().toJSON().slice(0,10).replace(/-/g,'-'),
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

        let currentDateWithFormat = new Date().toJSON().slice(0,10).replace(/-/g,'/').slice(0, 4)
        let age = Number(currentDateWithFormat) - Number(born) + 1

        if (!id || !password1 || !password2 || !birthday) {
          return false
        }

        axios.post('http://127.0.0.1:8000/accounts/signup/', { 'username':id, 'birthday':birthday, 'age':age, 'password1':password1,'password2':password2 })
          .then(res => {

            
            if (res.data.age) {
                // 성공적으로 회원가입이 되었을 경우
              this.$router.push({ name: 'home' })
            // } else {
            //   this.$router.push({ name: 'signup' })
            } else {
              this.errors.push(res.data)
              console.log(this.errors[0])
            }
        })
      }
    }
  }
</script>

<style>

</style>