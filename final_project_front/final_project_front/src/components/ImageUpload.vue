<template>
  <div>
    <div v-if="profileCreated">
      <h1>Image Upload</h1>
      <form @submit.prevent="uploadImage">
        <input type="file" accept="image/*" @change="handleFileChange">
        <button type="submit">Upload</button>
      </form>
    </div>
    <div v-else>
      <h1>Image Create</h1>
      <form @submit.prevent="createImage">
        <input type="file" accept="image/*" @change="handleFileChange">
        <button type="submit">create</button>
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
    };
  },
  methods: {
    ...mapMutations(['GET_PROFILE']),
    handleFileChange(event) {
      this.file = event.target.files[0];
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





