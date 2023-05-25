<template>
  <div class="profileheader">
    <header class="text-center"
    style=" margin-top: 2rem; margin-bottom: 5rem; border-top: 5px solid gray; border-bottom: 5px solid gray;">
      <h1 class='my-5'>
        <span style="text-shadow: 1px 1px 1px gray; font-size: 3rem">{{
          user.username
        }}</span
        >'s profile
      </h1>
    </header>
    <section class="justify-center text-center shadow-sm"
    style="border-bottom: 2px solid gray;">
      <img
        class="shadow-lg"
        style="border-radius: 50%; width: 30%; height: 30%"
        :src="profileImageUrl"
        alt="자비좀"
      />
      <p class="my-3">Email : {{ user.email }}</p>
      <div class="btn btn-secondary mb-4" @click="openImageUpload">
        Upload Image
      </div>
    </section>

    <footer
    class="row shadow-sm mx-3"
    style="border-radius: 20px; border: 1px solid gray; margin-top: 3rem; margin-bottom: 5rem;"
    >
    <span
      class="text-center m-3 text-primary"
      style="text-decoration-line: underline"
    >
      <h2><p>선호하는 장르를 선택해주세요</p></h2>
    </span>
      <div
        class="d-inline btn btn-primary col-2 my-3"
        style="margin-left: 3.2rem; margin-right: 3.2rem; border-radius: 20px"
        v-for="(genre, idx) in genres"
        :class="{ deactive: !userprofile[GENRES[genre.id] + '_key'] }"
        :key="idx"
        @click.prevent="activeBtn(genre)"
      >
        {{ genre.name }}
      </div>
      <!-- {{ userprofile }} -->
    </footer>
    <div
      class="mx-3"
      style="
        border-radius: 20px;
        border: 1px solid gray;
        margin-top: 3rem;
        margin-bottom: 5rem;
      "
    >
      <h4
        class="text-center"
        style="
          border-bottom: 1px solid gray;
          margin-top: 1rem;
          padding-bottom: 1rem;
        "
      >
        {{ userprofile.user?.username }}이(가) 작성한 리뷰 목록
      </h4>
      <div
        class="row text-start mx-2 pb-1"
        style="border-bottom: 1px solid gray"
      >
        <th class="col-2">게시글번호</th>
        <th class="col-4">게시글 제목</th>
        <th class="col-3">영화 제목</th>
        <th class="col-2">작성일</th>
      </div>
      <ul v-for="review in my_reviews" :key="review.id">
        <div
          v-if="review.username === userprofile.user.username"
          class="row text-start ms-2 mt-1"
        >
          <th class="col-1">{{ review.id }}</th>
          <th class="col-4">
            <a :href="MyMyReview(review.id)">{{ review.title }}</a>
          </th>
          <th class="col-3">{{ review.movie_title }}</th>
          <th class="col-2">{{ review.created_at.slice(0, 10) }}</th>
        </div>
      </ul>
    </div>
    <hr>
    <div class="row mt-3 mb-4">
      <div class="btn btn-outline-primary col-2 ms-auto" @click="logOut">
        LogOut
      </div>
      <div class="btn btn-outline-primary col-2 ms-5" @click="pwchange">
        password change
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ProFile",
  data() {
    return {
      initialLoad: true, // 초기 로드 여부
      my_reviews: [], // 리뷰 전체
      GENRES: {
        28: "action",
        12: "adventure",
        16: "animation",
        35: "comedy",
        80: "crime",
        99: "documentary",
        18: "drama",
        10751: "family",
        14: "fantasy",
        36: "history",
        27: "horror",
        10402: "music",
        9648: "mystery",
        10749: "romance",
        878: "science_fiction",
        10770: "tv_movie",
        53: "thriller",
        10752: "war",
        37: "western",
      },
    };
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
      window.open("/image-upload", "_blank");
    },
    activeBtn(genre) {
      // console.log(this.user.pk);
      // console.log(genre.id);
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/account/profile/togglecount/${this.user.pk}/${genre.id}/`,
      })
        .then((res) => {
          console.log(res);
          this.getProfile();
        })
        .catch((err) => console.log(err));
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
    this.getUser();
    this.getMyReview()
  },
  mounted() {
    this.getProfile();
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
      return `http://127.0.0.1:8000${imageName}`;
    },
    genres() {
      return this.$store.state.genres;
    },
  },
};
</script>

<style>
.deactive {
  background-color: gainsboro;
}
.profileheader {
  margin-left: 20rem;
  margin-right: 20rem;
}
</style>
