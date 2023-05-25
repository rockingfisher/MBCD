<template>
  <div id="app container">
    <div class="sidebar" v-show="this.$route.path != '/recommend'">
      <div class="container">
        <div class="text-center row mt-3">
          <img
            style="height: 3.5rem"
            :src="require('@/assets/images/home.png')"
            alt="로고"
            @click="goToHome"
          />
          <p style="color: white">home</p>
        </div>
        <div class="text-center row">
          <img
            style="height: 3.5rem"
            :src="require('@/assets/images/search.png')"
            alt="로고"
            @click="goToSearch"
          />
          <p style="color: white">search</p>
        </div>

        <div class="text-center row">
          <img
            style="height: 3.5rem"
            :src="require('@/assets/images/war.png')"
            alt="로고"
            @click="goToMovieWar"
          />
          <p style="color: white">war</p>
        </div>
        <div class="text-center row">
          <img
            style="height: 3.5rem"
            :src="require('@/assets/images/up.png')"
            alt="로고"
            @click="scrollToTop"
          />
          <p style="color: white">UP</p>
        </div>
      </div>
    </div>
    <nav
      class="navbar navbar-expand-lg shadow-sm"
      style="background-color: rgba(43, 137, 224, 88)"
    >
      <div class="container-fluid">
        <a
          class="navbar-brand"
          href="#"
          style="
            color: rgba(214, 230, 245, 96);
            text-shadow: 1px 1px 2px rgba(74, 167, 255, 100);
          "
        >
          <router-link
            class="logo"
            style="text-decoration: none"
            :to="{ name: 'MoviesView' }"
          >
            <img
              style="height: 3.5rem"
              :src="require('@/assets/images/logo.png')"
              alt="로고"
            />
          </router-link>
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarTogglerDemo02"
          aria-controls="navbarTogglerDemo02"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">
                <router-link class="no_text_deco" :to="{ name: 'MoviesView' }"
                  >Home</router-link
                >
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">
                <router-link
                  class="no_text_deco"
                  :to="{ name: 'CommunityView' }"
                  >Community</router-link
                >
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link">
                <router-link
                  class="no_text_deco"
                  :to="{ name: 'RecommendView' }"
                  >Recommend</router-link
                ></a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link">
                <router-link
                  class="no_text_deco"
                  :to="{ name: 'SearchMoviesView' }"
                  >SearchMovies</router-link
                ></a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link">
                <router-link class="no_text_deco" :to="{ name: 'MovieWarView' }"
                  >MovieWar</router-link
                ></a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link">
                <router-link
                  class="no_text_deco"
                  v-if="isLogin"
                  :to="{ name: 'ProfileView' }"
                  >my profile</router-link
                ><router-link
                  class="no_text_deco"
                  v-else
                  :to="{ name: 'LogInView' }"
                  >Login</router-link
                >
              </a>
            </li>
          </ul>
          <div>
            <img
              v-show="isMobile === false"
              v-if="profileCreated"
              :src="profileImageUrl"
              class="img"
              alt="err"
            />
          </div>
          <!-- {{ search_input }} -->
          <form
            v-if="this.$route.path !== '/search'"
            @submit.prevent="searchMovie"
            class="d-flex"
            role="search"
          >
            <input
              v-model="search_input"
              class="form-control me-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
            />
            <button class="btn btn-outline-info" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    user() {
      return this.$store.state.user;
    },
    userprofile() {
      return this.$store.state.userprofile;
    },
    profileImageUrl() {
      const imageName = this.userprofile.picture;
      return `http://127.0.0.1:8000${imageName}`;
    },
    isMobile() {
      return this.windowWidth <= 991; // 기준 넓이보다 작거나 같으면 true 반환
    },
    ...mapGetters(["isLogin"]),
    ...mapGetters(["profileCreated"]),
  },
  data() {
    return {
      search_input: "",
      windowWidth: 0,
    };
  },
  methods: {
    searchMovie() {
      console.log(this.$route.path);
      if (this.$route.path !== "/search") {
        this.$router.push({
          name: "SearchMoviesView",
          params: { search_input: this.search_input },
        });
        this.search_input = "";
      }
    },
    handleResize() {
      this.windowWidth = window.innerWidth;
    },
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: "smooth", // 부드러운 스크롤을 원한다면 추가합니다.
      });
    },
    goToMovieWar() {
      if (this.$route.path !== "/moviewar") {
        this.$router.push({
          name: "MovieWarView",
        });
      } else {
        this.$router.go();
      }
    },
    goToHome() {
      if (this.$route.path !== "/") {
        this.$router.push({
          name: "MoviesView",
        });
      } else {
        this.$router.go();
      }
    },
    goToSearch() {
      if (this.$route.path !== "/search") {
        this.$router.push({
          name: "SearchMoviesView",
        });
      } else {
        this.$router.go();
      }
    },
  },
  mounted() {
    window.addEventListener("resize", this.handleResize);
    this.handleResize(); // 초기화시 한 번 호출
  },
};
</script>

<style>
#app {
  font-family: TMONBlack, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: rgba(214, 230, 245, 96);
  background-color: rgba(214, 230, 245, 96);
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: rgba(214, 230, 245, 96);
}

nav a.router-link-exact-active:not(.logo) {
  color: rgba(224, 155, 43, 88);
}

.img {
  width: 40px;
  height: 40px;
  border-radius: 100%;
  overflow: hidden;
  margin-right: 10px;
}

router-link {
  color: rgba(214, 230, 245, 96);
  text-decoration: none;
}

.no_text_deco {
  text-decoration: none;
}

.sidebar {
  position: fixed;
  top: 30%;
  right: 5%;
  width: 6rem;
  height: 25rem;
  border-radius: 20px;
  box-shadow: 1px 1px 4px gray;
  background-color: rgba(43, 137, 224, 88);
}
</style>
