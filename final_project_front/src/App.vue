<template>
  <div id="app container">
    <nav class="navbar bg-dark" data-bs-theme="dark">
      <router-link :to="{ name: 'MoviesView' }">Movies</router-link>
      <router-link :to="{ name: 'CommunityView' }">Community</router-link>
      <router-link v-if="isLogin" :to="{ name: 'ProfileView' }">my profile</router-link>
      <router-link v-else :to="{ name: 'LogInView' }">Login</router-link>
      <router-link :to="{ name: 'RecommendView' }">Recommend</router-link>
      <img v-if="profileCreated" :src="profileImageUrl" alt="err">

    </nav>
    <router-view />
  </div>
</template>

<script>
  import { mapGetters } from 'vuex';

  export default {
    computed: {
      user() {
        return this.$store.state.user
      },
      userprofile() {
        return this.$store.state.userprofile
      },
      profileImageUrl() {
        const imageName = this.userprofile.picture
        return `http://127.0.0.1:8000${imageName}`
      },
      ...mapGetters(['isLogin']),
      ...mapGetters(['profileCreated']),
    },
  }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
