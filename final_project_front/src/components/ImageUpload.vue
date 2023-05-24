<template>
  <div class="container">
    <div v-if="profileCreated">
      <hr>
      <h1 class="mx-5 my-4">프로필 이미지 변경</h1>
      <hr>
      <form @submit.prevent="uploadImage" class="my-5">
        <div v-if="file">
          <img :src="previewURL" alt="Selected Image" style="max-width: 300px; max-height: 300px;">
        </div>
        <input type="file" accept="image/*" @change="handleFileChange"><br>
        <button type="submit" class="mt-3 btn btn-outline-info">Upload</button>
      </form>
    </div>
    <div v-else>
      <h1>프로필 이미지 생성</h1>
      <div v-if="file">
        <img :src="previewURL" alt="Selected Image" style="max-width: 300px; max-height: 300px;">
      </div>
      <form @submit.prevent="createImage">
        <input type="file" accept="image/*" @change="handleFileChange">
        <button type="submit" class="mt-3 btn btn-outline-info">create</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters  } from 'vuex';
import { mapMutations } from 'vuex';

export default {
  name: 'ImageUpload',
  data() {
    return {
      file: null,
      previewURL: null,
    };
  },
  methods: {
    ...mapMutations(['GET_PROFILE']),
    handleFileChange(event) {
      this.file = event.target.files[0];
      this.previewURL = URL.createObjectURL(this.file);
    },
    uploadImage() {
    const token = this.token
    const headers = {
      Authorization: `Token ${token}`,
    }
      const formData = new FormData();
      formData.append('picture', this.file);

      axios.post(`http://127.0.0.1:8000/account/profile/${this.user.pk}/`, formData, { headers })
      .then((res)=>{
        console.log(res)
        const userProfile = res.data
        console.log(userProfile)
        this.$router.push('/profile')
      })
      .catch((err)=>{
        console.log(err)
    })
    },
    createImage() {
    const token = this.token
    const headers = {
      Authorization: `Token ${token}`,
    }
      const formData = new FormData();
      formData.append('picture', this.file);

      axios.post(`http://127.0.0.1:8000/account/profilecreate/${this.user.pk}/`, formData, { headers })
      .then((res)=>{
        console.log(res)
        const userProfile = res.data
        console.log(userProfile)
        this.GET_PROFILE(userProfile)
        this.$router.push('/')
      })
      .catch((err)=>{
        console.log(err)
    })
    },
    getUserAlone() {
      this.$store.dispatch('getUserAlone')
    },
  },
  computed: {
      token() {
      return this.$store.state.token
      },
      user() {
      return this.$store.state.user
      },
      ...mapGetters(['profileCreated'])
  },
  created() {
    this.getUserAlone()
  },
  mounted() {
    this.getUserAlone()
  }
};
</script>

<style>
</style>





