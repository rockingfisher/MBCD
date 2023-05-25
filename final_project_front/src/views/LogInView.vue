<template>
  <div class="container">
    <hr>
    <h1>로그인</h1>
    <hr>
    <form @submit.prevent="login" class="d-flex justify-content-evenly">
      <div>
        <div class="mt-3 mb-3 d-flex" >
          <label for="username" class="custom2" style="text-align:center">username : </label>
          <input class="form-control" type="text" id="username" v-model="username"><br>
        </div>
        <div class="mt-3 mb-3 d-flex" >
          <label for="password" class="custom2" style="text-align:center"> password : </label>
          <input class="form-control" type="password" id="password" v-model="password"><br>
        </div>
      </div>
      <input type="submit" value="logIn" class="but btnBorder btnBlueGreen">
    </form>
    <hr>
    <span class="fs-6 text-black-50 me-2">회원이 아니십니까? MBCD의 회원으로 가입하면 다양한 서비스를 이용할 수 있습니다!</span>
    <button @click="signup" class="btn btn-outline-info btn-sm">signup</button>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password  
      }
      this.$store.dispatch('logIn', payload)
      setTimeout(()=>{
        if (this,this.$store.state.user){
          this.$router.push('/')
        }
        else {
          alert('아이디 혹은 비밀번호가 틀렸습니다')
          this.username = ''
          this.password = ''
        }
      }, 500)
      // this.$router.push('/profile')
    }, 
    signup() {
      this.$router.push({ name:'SignUpView' })
    }
  }
}
</script>

<style>
.custom2 {
  width: 150px;
  display: flex;
  align-items: center;
  justify-content: center;
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
