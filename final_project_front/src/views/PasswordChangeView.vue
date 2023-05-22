<template>
    <div>
      <h1>암호변경</h1>
      <form @submit.prevent="passwordChange">
        <!-- <label for="oldpassword">old password : </label>
        <input type="text" id="oldpassword" v-model="oldpassword"><br> -->
  
        <label for="password1"> new password : </label>
        <input type="password" id="password1" v-model="password1"><br>

        <label for="password2">password confirmation : </label>
        <input type="password" id="password2" v-model="password2"><br>
  
        <input type="submit">
      </form>
    </div>
  </template>

<script>
export default {
    
  name: 'PasswordChange',
  data() {
    return {
    //   oldpassword: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    passwordChange() {
    //   const oldpassword = this.oldpassword
      const new_password1 = this.password1
      const new_password2 = this.password2

      const payload = {
        new_password1, new_password2
      }
      this.$store.dispatch('passwordChange', payload)
    }
  }
}
</script>

<style>
</style>