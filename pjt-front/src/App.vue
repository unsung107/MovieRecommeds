<template>
  <div id="app">
    <div id="nav">

      <div v-if="isLoggedIn">
         | 
        <router-link to="/">Home</router-link> | 
        <a @click.prevent="logout" href="/logout">Logout</a> | 
        <router-link to="/createRecommend">추천리스트 작성</router-link> | 
        <router-link to="/RecommendList">추천리스트</router-link> |
        <router-link to="/adminPage">관리페이지</router-link> | 
        <router-link :to="`/userDetail/${user_id}`">마이페이지</router-link> | 
      </div>

      <div v-else>
         | 
        <router-link to="/">Home</router-link> | 
        <router-link to="/login" @login="checkLoggedIn">Login</router-link> | 
        <router-link to="/signup">Signup</router-link>  | 
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
import router from '@/router'
import jwtDecode from 'jwt-decode'

export default {
  name: 'App',
  data() {
    return {
      isLoggedIn: false,
      user_id: '',
    }
  },
  methods: {
    checkLoggedIn(){
      this.$session.start()
      if(this.$session.has('jwt')) {
        this.isLoggedIn = true
      }
    },
    logout() {
      this.$session.destroy()
      this.isLoggedIn = false
      router.push('/login')
      
    }
  },
  mounted() {
    this.checkLoggedIn()
    if (this.isLoggedIn) {
      const token = this.$session.get('jwt')
      this.user_id = jwtDecode(token).user_id
    }
  },
  updated() {
    this.checkLoggedIn()
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
