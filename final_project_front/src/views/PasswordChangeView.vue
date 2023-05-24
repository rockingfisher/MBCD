<template>
    <div class="container">
      <div style="border-top: 1px solid gray; border-bottom: 1px  solid gray; margin-top: 1rem;">
        <h1 class="my-3">암호변경</h1>
      </div> 
      <form @submit.prevent="passwordChange" class="d-flex justify-content-evenly"
      style="border-bottom: 1px  solid gray;">
        <!-- <label for="oldpassword">old password : </label>
        <input type="text" id="oldpassword" v-model="oldpassword"><br> -->
          <div class="row" style="width: 40rem">
            <div class="mt-3 mb-3 d-flex">
              <label for="password1" class="custom2" style="text-align:center"> new password : </label>
              <input class="form-control" style="width: 23rem" type="password" id="password1" v-model="password1"><br>
            </div>
            <div class="mt-3 mb-3 d-flex">
              <label for="password2" class="custom2" style="text-align:center">password confirmation : </label>
              <input class="form-control" style="width: 23rem;" type="password" id="password2" v-model="password2"><br>
            </div>
          </div>
          <input type="submit" class="but btnBorder btnBlueGreen">
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

<style scoped>
.custom2 {
  width: 15rem;
  display: flex;
  align-items: center;
  justify-content: end;
}

.but {
  width: 120px;
  padding: 0;
  margin: 10px 20px 10px 0;
  font-weight: 600;
  text-align: center;
  line-height: 50px;
  color: #FFF;
  border-radius: 5px;
  transition: all 0.2s ;
}

.btnBlueGreen {
  background: rgba(43, 137, 224, 88);
}
/* BORDER */
.btnBlueGreen.btnBorder {
  box-shadow: 0px 0px 0px 0px rgba(74, 167, 255, 100);
}

.btnBlueGreen.btnBorder:hover {
  box-shadow: 0px 0px 0px 5px rgba(74, 167, 255, 100);
}
</style>