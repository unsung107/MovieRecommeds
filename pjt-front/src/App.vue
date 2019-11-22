<template>
  <div id="app">
    <button @click="movieUpdate">실험</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  
  name: 'app',
  components: {
  },
  methods: {
    movieUpdate() {
      axios.get('http://127.0.0.1:8000/movies/movieupdate/')
      .then(response => {
        console.log(response)
      })
      
    }
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
  margin-top: 60px;
}
</style>
