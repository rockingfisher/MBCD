import Vue from "vue";
import Vuex from "vuex";
// import axios from "axios";
import router from "@/router";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);
const API_URL = "http://127.0.0.1:8000";
import axios from "axios";
export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    movies: [],
    genres: [],
    token: null,
    user: null,
    userprofile: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false;
    },
    profileCreated(state) {
      return state.userprofile ? true : false;
    },
  },
  mutations: {
    GET_MOVIE(state, movies) {
      state.movies = movies;
    },
    SAVE_TOKEN(state, token) {
      state.token = token;
    },
    GET_USER(state, data) {
      state.user = data;
    },
    GET_PROFILE(state, data) {
      state.userprofile = data;
    },
    LOG_OUT(state) {
      state.token = null;
      state.user = null;
      state.userprofile = null;
      router.push({ name: "LogInView" });
    },
    GET_GENRE(state, genres) {
      // console.log(genres);
      state.genres = genres;
    },
  },
  actions: {
    getMovie(context) {
      axios({
        method: "get",
        url: `${API_URL}/movies/home/`,
      })
        .then((res) => {
          // console.log("actton");
          context.commit("GET_MOVIE", res.data);
        })
        .catch((err) => console.log(err));
    },
    signUp(context, payload) {
      const username = payload.username;
      const password1 = payload.password1;
      const password2 = payload.password2;
      const email = payload.email;
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/signup/",
        data: {
          username,
          password1,
          password2,
          email,
        },
      })
        .then((res) => {
          // console.log(res);
          context.commit("SAVE_TOKEN", res.data.key);
        })
        .then(() => {
          router.push("/image-upload");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    logIn(context, payload) {
      const { username, password } = payload;

      axios({
        method: "post",
        url: `http://127.0.0.1:8000/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          context.commit("SAVE_TOKEN", res.data.key);
        })
        .then(() => {
          context.dispatch("getUser");
        })
        .catch((err) => {
          console.log(err);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    logOut(context) {
      axios.post("http://127.0.0.1:8000/accounts/logout/").then(() => {
        context.commit("LOG_OUT");
      });
    },
    getUser(context) {
      const token = this.state.token;
      const headers = {
        Authorization: `Token ${token}`,
      };
      axios
        .get("http://127.0.0.1:8000/accounts/userprofile/", { headers })
        .then((res) => {
          const userData = res.data;
          // console.log("userData")
          // console.log(userData)
          context.commit("GET_USER", userData);
          return userData;
        })
        .then((userPk) => {
          context.dispatch("getProfile", userPk.pk);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getUserAlone(context) {
      const token = this.state.token;
      const headers = {
        Authorization: `Token ${token}`,
      };
      axios
        .get("http://127.0.0.1:8000/accounts/userprofile/", { headers })
        .then((res) => {
          const userData = res.data;
          // console.log("userData")
          // console.log(userData)
          context.commit("GET_USER", userData);
          return userData;
        })
        .catch((err) => {
          console.log(err);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getProfile(context, payload) {
      const userpk = payload;
      const token = this.state.token;
      const headers = {
        Authorization: `Token ${token}`,
      };

      axios
        .get(`http://127.0.0.1:8000/account/profile/${userpk}`, { headers })
        .then((res) => {
          // console.log(res);
          const userProfile = res.data;
          // console.log("userProfile");
          // console.log(userProfile);
          context.commit("GET_PROFILE", userProfile);
        })
        .catch((err) => {
          // console.log('여긴가')
          console.log(err);
          router.push({ name: "ImageUpload" });
        });
    },
    passwordChange(context, payload) {
      const { new_password1, new_password2 } = payload;
      const token = this.state.token;
      const headers = {
        Authorization: `Token ${token}`,
      };

      axios({
        method: "post",
        url: `http://127.0.0.1:8000/password/change/`,
        headers: headers,
        data: {
          new_password1,
          new_password2,
        },
      })
        .then((res) => {
          context.commit("SAVE_TOKEN", res.data.key);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getGenre(context) {
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/`,
      })
        .then((res) => {
          context.commit("GET_GENRE", res.data);
        })
        .catch((err) => console.log(err));
    },
  },
  modules: {},
});
