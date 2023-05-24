<template>
  <div class="container">
    <hr>
    <h1>회원 가입</h1>
    <hr>
    <form @submit.prevent="signUp">
      <div class="mt-3 mb-3 d-flex">
      <label for="username" class="custom2" style="text-align:center">username  </label>
      <input type="text" id="username" v-model="username"  class="form-control me-4">
      </div>
      <div class="mt-3 mb-3 d-flex">
      <label for="password1" class="custom2" style="text-align:center">password  </label>
      <input type="password" id="password1" v-model="password1"  class="form-control me-4">
      </div>
      <div class="mt-3 mb-3 d-flex">
      <label for="password2" class="custom2" style="text-align:center">password confirmation </label>
      <input type="password" id="password2" v-model="password2"  class="form-control me-4">
      </div>
      <div class="mt-3 mb-3 d-flex">
      <label for="email" class="custom2" style="text-align:center">e-mail  </label>
      <input type="text" id="email" v-model="email"  class="form-control me-4">
      </div>
      <hr>
      <input type="submit" value="SignUp" class="btn btn-outline-info btn-sm">
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
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const email = this.email
      
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