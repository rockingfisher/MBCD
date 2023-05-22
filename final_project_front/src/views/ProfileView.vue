<template>
  <div>
    <hr>
    <h1>{{ user.username }}'s profile</h1>
    <p>email : {{ user.email }}</p>
    <img :src="profileImageUrl" alt="자비좀">
    <button @click="openImageUpload">Upload Image</button>
    <hr>
    <hr>
    <button @click="logOut">LogOut</button>
    <button @click="pwchange">password change</button>
  </div>
</template>

<script>
export default {
  name: 'ProFile',
  methods: {
    getUser() {
      this.$store.dispatch('getUser')
    },
    logOut() {
      this.$store.dispatch('logOut')
    },
    getProfile() {
      const userPk = this.user.pk
      console.log(userPk)
      this.$store.dispatch('getProfile', userPk)
    },
    pwchange() {
      this.$router.push('/pwchange')
    },
    openImageUpload() {
      window.open('/image-upload', '_blank');
    },
  },
  created() {
    this.getUser()
  },
  mounted() {
    this.getProfile()
  },
  computed: {
    user() {
      return this.$store.state.user
    },
    userprofile() {
      return this.$store.state.userprofile
    },
    movie() {
      return this.$store.state.movie
    },
    profileImageUrl() {
      const imageName = this.userprofile.picture
      return `http://127.0.0.1:8000${imageName}`
    }
  }
}
</script>

<style>

</style>