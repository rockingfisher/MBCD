import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import router from "@/router";
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
    username: null,
    user_pk: null,
  },
  getters: {},
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name:'ProfileView' })
    },
    GET_USER(state, data) {
      state.username = data.username
      state.user_pk - data.user_pk
    }
  },
  actions: {
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      const email = payload.email
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: {
          username, password1, password2, email
        }
      })
        .then((res) => {
          console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logIn(context, payload) {
      const {username, password} = payload;

      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res)=>{
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err)=> {
          console.log(err)
        })
    },
    getUser(context) {
      const token = this.state.token
      const headers = {
        Authorization: `Token ${token}`,
      }
      axios.get('http://127.0.0.1:8000/accounts/userprofile/', { headers })
        .then((res)=>{
          const userData = res.data
          console.log(userData)
          context.commit('GET_USER', userData)
        })
          .catch((err)=>{
          console.log(err)
        })
    },
  },
  modules: {},
});
