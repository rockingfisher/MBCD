<template>
  <div>
    <hr>
    <h1>{{ userprofile.user?.username }}'s profile</h1>
    <p>email : {{ userprofile.user?.email }}</p>
    <img :src="profileImageUrl" class="img-thumbnail" alt="err"><br>
    <hr/>
    <h4>my review</h4>
    <ul v-for="review in my_reviews" :key="review.id">
      <li v-if="review.username === userprofile.user.username">
        <a :href="MyMyReview(review.id)">{{ review.title }}</a>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'AnotherProFile',
  data() {
    return {
      initialLoad: true, // 초기 로드 여부
      my_reviews: [], // 리뷰 전체
    }
  },
  props:['user_id'],
  methods: {
    logOut() {
      this.$store.dispatch("logOut");
    },
    getProfile() {
      const userPk = this.user_id;
      this.$store.dispatch("getAnotherProfile", userPk);
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
    console.log(this.user_id)
    // console.log(this.$router.params.user_id)
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
    userprofile() {
      return this.$store.state.anotheruserprofile;
    },
    profileImageUrl() {
      const imageName = this.userprofile.picture;
      return `http://127.0.0.1:8000${imageName}`;
    },
    my_reviews_item() {
      const userName = this.userprofile.user.username
      return this.my_reviews.filter(review => review.username === userName)
    }
  },
};
</script>

<style></style>