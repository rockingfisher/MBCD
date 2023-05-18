import Vue from "vue";
import Vuex from "vuex";
// import axios from "axios";

Vue.use(Vuex);
const API_URL = "http://127.0.0.1:8000";
import axios from "axios";
export default new Vuex.Store({
  state: {
    movies: [],
  },
  getters: {},
  mutations: {
    GET_MOVIE(state, movies) {
      // console.log("mutation");
      state.movies = movies;
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
  },
  modules: {},
});
