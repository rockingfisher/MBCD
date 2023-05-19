<template>
  <div>
    <h1>회원 가입</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>
      <label for="password1">password : </label>
      <input type="password" id="password1" v-model="password1"><br>
      <label for="password2">password confirmation : </label>
      <input type="password" id="password2" v-model="password2"><br>
      <label for="email">e-mail : </label>
      <input type="text" id="email" v-model="email"><br>
      <!-- <label for="lastname">last name : </label>
      <input type="text" id="lastname" v-model="last_name"> | 
      <label for="firstname">first name : </label>
      <input type="text" id="firstname" v-model="first_name"><br> -->
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  
  
  name: 'SignUp',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      email: null,
      // last_name: null,
      // first_name: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const email = this.email
      // const last_name = this.last_name
      // const first_name = this.first_name

      const payload = {
        username, password1, password2, email
      }
      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>

<style>

</style>