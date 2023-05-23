<template>
  <div>
    <hr>
    <h1>{{ user?.username }}'s profile</h1>
    <p>email : {{ user?.email }}</p>
    <img :src="profileImageUrl" alt="err">
    <button @click="openImageUpload">Upload Image</button>
    <hr />
    <hr />
    <button @click="logOut">LogOut</button>
    <button @click="pwchange">password change</button>
  </div>
</template>

<script>
export default {
  name: 'ProFile',
  data() {
    return {
    initialLoad: true, // 초기 로드 여부
    }
  },
  methods: {
    getUser() {
      this.$store.dispatch("getUser");
    },
    logOut() {
      this.$store.dispatch("logOut");
    },
    getProfile() {
      const userPk = this.user.pk;
      console.log(userPk);
      this.$store.dispatch("getProfile", userPk);
    },
    pwchange() {
      this.$router.push("/pwchange");
    },
    openImageUpload() {
      this.$router.push('/image-upload')
    },

  },
  created() {
    this.getUser()
    this.getProfile()
  },
  // beforeMount() {
  //   if (this.initialLoad) {
  //     this.initialLoad = false; // 초기 로드 이후에는 새로고침 중지
  //     location.reload();
  //   }
  // },
  mounted() {
  // if (this.refreshCount < this.maxRefreshCount) {
  //   location.reload();
  //   console.log(this.refreshCount)
  //   this.refreshCount++;
  // }
  },
  updated() {
    // this.getProfile()
  },
  watch: {
    profileImageUrl(newValue, oldValue) {
      if (newValue !== oldValue) {
        location.reload();
      }
    }
  },
  computed: {
    user() {
      return this.$store.state.user;
    },
    userprofile() {
      return this.$store.state.userprofile;
    },
    movie() {
      return this.$store.state.movie;
    },
    profileImageUrl() {
      const imageName = this.userprofile.picture;
      return `http://127.0.0.1:8000/${imageName}`;
    },
  },
};
</script>

<style></style>