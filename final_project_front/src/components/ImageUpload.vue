<template>
  <div>
    <h1>Image Upload</h1>
    <form @submit.prevent="uploadImage">
      <input type="file" accept="image/*" @change="handleFileChange" />
      <button type="submit">Upload</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ImageUpload",
  data() {
    return {
      file: null,
    };
  },
  methods: {
    handleFileChange(event) {
      this.file = event.target.files[0];
    },
    uploadImage() {
      const token = this.token;
      const headers = {
        Authorization: `Token ${token}`,
      };
      const formData = new FormData();
      formData.append("picture", this.file);

      axios
        .post(
          `http://127.0.0.1:8000/account/profile/${this.user.pk}/`,
          formData,
          { headers }
        )
        .then((res) => {
          console.log(res);
          const userProfile = res.data;
          console.log("userProfile");
          console.log(userProfile);
        })
        .catch((err) => {
          console.log("여긴가");
          console.log(err);
          console.log(this.token);
        });
    },
  },
  computed: {
    token() {
      return this.$store.state.token;
    },
    user() {
      return this.$store.state.user;
    },
  },
};
</script>

<style></style>
