<template>
  <div>
    <h2>회원가입 페이지입니다!</h2> <br>
    
    <h5>아이디를 입력하세요</h5>
      <input type="text" v-model="credentials.username" class="form-control" style="width: 500px">
      <div style="color: red">연속 4개 이상 같은 단어는 사용하지 말아주세요!</div>
      <div style="color: red">영어 또는 영어와 숫자의 조합으로 만들어주세요!</div>
      <br><br>
    <h5>비밀번호를 입력하세요</h5>
      <input type="password" v-model="credentials.password1" class="form-control" style="width: 500px">
      <div style="color: red">연속 4개 이상 같은 단어는 사용하지 말아주세요!</div>
      <div style="color: red">비밀번호는 8글자 이상으로 만들어주세요!</div>
      <br><br>
    <h5>비밀번호를 다시 한번 입력하세요</h5>
      <input type="password" v-model="credentials.password2" class="form-control" style="width: 500px">
      <br><br>
    <h5>생일을 입력하세요</h5>
      <input type="date" v-model="credentials.birthday" ><br><br>
      <button @click="signup">회원가입</button><br>
    
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
        const username = this.credentials.username
        const password1 = this.credentials.password1
        const password2 = this.credentials.password2
        const birthday = this.credentials.birthday
        const SERVER_IP = process.env.VUE_APP_SERVER_IP
        let born = birthday.split('-')[0]

        let currentDateWithFormat = new Date().toJSON().slice(0,10).replace(/-/g,'/').slice(0, 4)
        let age = Number(currentDateWithFormat) - Number(born) + 1

        if (!username || !password1 || !password2 || !birthday) {
          return false
        }

        axios.post(SERVER_IP + '/accounts/signup/', { 'username':username, 'birthday':birthday, 'age':age, 'password1':password1,'password2':password2 })
          .then(res => {

            
            if (res.data.age) {
                // 성공적으로 회원가입이 되었을 경우
              this.$router.push({ name: 'login' })
            // } else {
              // this.$router.push({ name: 'signup' })
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
.form-control {
  margin: 0 auto;
}
</style>