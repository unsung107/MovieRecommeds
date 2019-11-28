<template>
  <div>
    <h2> 영화 수정하기 </h2>
    <hr>
    제목 : <input type="text" :value="form.title" id="title"><br><hr>
    설명 : <textarea :value="form.discription" id="discription"></textarea><br><hr>
    관객 : <input type="number" :value="form.audience" id="audience"><br><hr>
    평점 : <input type="number" :value="form.score" id="score"><br><hr>
    예고 : <textarea :value="form.video_url" id="video_url"></textarea><br><hr>
    스냅 : <textarea :value="form.snapshot_url" id="snapshot_url" ></textarea><br><hr>
    <button class="btn btn-primary" @click="updateMove">수정하기</button>
    <button class="btn btn-warning" @click="deleteMovie">삭제하기</button>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'

export default {
  name: 'movieUpdate',
  data() {
    return{
      movie_id: this.$route.params.movie_id,
      SERVER_IP: process.env.VUE_APP_SERVER_IP,
      form: {},
    token: this.$session.get("jwt"),
    data: {
        title: '',
        discription: '',
        audience: '',
        video_url: '',
        snapshot_url: '',
    }
 
    }
  },
  computed: {
    options() {
      return {
        headers: {
          Authorization: "JWT " + this.token
        }
      };
    }
  },
  props: {
    movieForm: Object,
  },
  mounted() {
      this.getForm()
  },
  methods: {
    getForm() {
        axios.get(this.SERVER_IP + `/movies/api/v1/updateMovie/${this.movie_id}/`, this.options)
        .then(response =>{
            this.form = response.data.form
        })
    },
    deleteMovie() {
        axios.post(this.SERVER_IP + `/movies/api/v1/deleteMovie/${this.movie_id}/`, {}, this.options)
        .then(response =>{
            console.log(response)
            router.push('/')
        })
    },
    updateMove() {
        const data = {
            title: this.form.title,
        discription: this.form.discription,
        audience: this.form.audience,
        video_url: this.form.video_url,
        snapshot_url: this.form.snapshot_url,
        }
        console.log(data)
        axios.post(this.SERVER_IP + `/movies/api/v1/updateMovie/${this.movie_id}/`, data, this.options)
        .then(response =>{
            console.log(response)
            router.push(`/movie/${this.movie_id}`)
        })
    }
  }
}
</script>

<style>

</style>