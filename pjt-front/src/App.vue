<template>
  <div id="app">
        <div id="navbb">
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="#">NavBar</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#">Link</b-nav-item>
        <b-nav-item href="#" disabled>Disabled</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>

        <!-- <b-nav-item-dropdown text="Lang" right>
          <b-dropdown-item href="#">EN</b-dropdown-item>
          <b-dropdown-item href="#">ES</b-dropdown-item>
          <b-dropdown-item href="#">RU</b-dropdown-item>
          <b-dropdown-item href="#">FA</b-dropdown-item>
        </b-nav-item-dropdown> -->

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <em>User</em>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>

    <div id="nav">
      <div v-if="isLoggedIn">
        |
        <router-link to="/">Home</router-link>|
        <a @click.prevent="logout" href="/logout">Logout</a> |
        <router-link to="/createRecommend">추천리스트 작성</router-link>|
        <router-link to="/RecommendList">추천리스트</router-link>|
        <router-link to="/adminPage">관리페이지</router-link>|
        <router-link :to="`/userDetail/${user_id}`">마이페이지</router-link>|
        <router-link :to="`/MovieForYou`">MovieForYou</router-link>|
      </div>

      <div v-else>
        |
        <router-link to="/">Home</router-link>|
        <router-link to="/login" @login="checkLoggedIn">Login</router-link>|
        <router-link to="/signup">Signup</router-link>|
      </div>
    </div>
    <router-view />
  </div>
</template>

<script>
import router from "@/router";
import jwtDecode from "jwt-decode";

export default {
  name: "App",
  data() {
    return {
      isLoggedIn: false,
      user_id: ""
    };
  },
  methods: {
    checkLoggedIn() {
      this.$session.start();
      if (this.$session.has("jwt")) {
        this.isLoggedIn = true;
        const token = this.$session.get("jwt");
        this.user_id = jwtDecode(token).user_id;
      }
    },
    logout() {
      this.$session.destroy();
      this.isLoggedIn = false;
      router.push("/login");
    }
  },
  mounted() {
    this.checkLoggedIn();
  },
  updated() {
    this.checkLoggedIn();
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
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
