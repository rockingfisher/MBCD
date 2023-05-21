<template>
  <div id="app container">
    <nav class="navbar bg-dark" data-bs-theme="dark">
      <router-link :to="{ name: 'MoviesView' }">Movies</router-link>
      <router-link :to="{ name: 'CommunityView' }">Community</router-link>
      <router-link :to="{ name: 'RecommendView' }">Recommend</router-link>
    </nav>
    <router-view />
  </div>
</template>

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
