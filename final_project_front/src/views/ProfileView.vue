<template>
  <div>
    <hr>
    <h1>{{ user?.username }}'s profile</h1>
    <p>email : {{ user?.email }}</p>
    <img :src="profileImageUrl" class="img-thumbnail" alt="err"><br>
    <button @click="openImageUpload">Upload Image</button>
    <hr/>
    <h4>my review</h4>
    <ul v-for="review in my_reviews" :key="review.id">
      <li v-if="review.username === user.username">
        <a :href="MyMyReview(review.id)">{{ review.title }}</a>
      </li>
    </ul>
    <hr/>
    <button @click="logOut">LogOut</button>
    <button @click="pwchange">password change</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'ProFile',
  data() {
    return {
      initialLoad: true, // 초기 로드 여부
      my_reviews: [], // 리뷰 전체
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
      this.$store.dispatch("getProfile", userPk);
    },
    pwchange() {
      this.$router.push("/pwchange");
    },
    openImageUpload() {
      this.$router.push('/image-upload')
    },
    getMyReview() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/reviews/`
      })
        .then((res)=>{
          console.log('my')
          console.log(res)
          this.my_reviews = res.data;
        })
        .catch((err)=>{console.log(err)})
    },
    MyMyReview(id) {
      return `/reviewdetail/${id}`
    }
  },
  created() {
    this.getUser()
    this.getProfile()
    this.getMyReview()
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
    profileImageUrl() {
      const imageName = this.userprofile.picture;
      return `http://127.0.0.1:8000${imageName}`;
    },
    my_reviews_item() {
      const userName = this.user.username
      return this.my_reviews.filter(review => review.username === userName)
    }
  },
};
</script>

<style></style>