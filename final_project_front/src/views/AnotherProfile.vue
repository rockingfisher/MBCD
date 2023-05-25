<template>
  <div class="mx-20rem">
    <header
      class="text-center"
      style="
        margin-top: 2rem;
        margin-bottom: 5rem;
        border-top: 5px solid gray;
        border-bottom: 5px solid gray;
      "
    >
      <h1 class="my-5">
        <span style="text-shadow: 1px 1px 1px gray; font-size: 3rem">{{
          userprofile.user?.username
        }}</span
        >'s profile
      </h1>
    </header>
    <section
      class="justify-center text-center shadow-sm"
      style="border-bottom: 2px solid gray"
    >
      <img
        class="shadow-lg"
        style="border-radius: 50%; width: 30%; height: 30%"
        :src="profileImageUrl"
        alt="자비좀"
      />
      <p class="my-3">Email : {{ userprofile.user?.email }}</p>
    </section>

    <footer
      class="row shadow-sm mx-3"
      style="
        border-radius: 20px;
        border: 1px solid gray;
        margin-top: 3rem;
        margin-bottom: 5rem;
      "
    >
      <span
        class="text-center m-3 text-primary"
        style="text-decoration-line: underline"
      >
        <h2>
          <p>{{ userprofile.user?.username }}이(가) 선호하는 장르</p>
        </h2>
      </span>
      <div
        v-for="(genre, idx) in genres"
        :key="idx"
        class="btn btn-primary my-3 col-2"
        v-show="userprofile[GENRES[genre.id] + '_key']"
        style="margin-left: 3.2rem; margin-right: 3.2rem; border-radius: 20px"
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
  </div>
</template>

<!-- <template>
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
</template> -->

<script>
import axios from "axios";

export default {
  name: "AnotherProFile",
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
  props: ["user_id"],
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
        method: "get",
        url: `http://127.0.0.1:8000/community/reviews/`,
      })
        .then((res) => {
          console.log("my");
          console.log(res);
          this.my_reviews = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    MyMyReview(id) {
      return `/reviewdetail/${id}`;
    },
  },
  created() {
    console.log(this.user_id);
    // console.log(this.$router.params.user_id)
    this.getProfile();
    this.getMyReview();
  },
  watch: {
    profileImageUrl(newValue, oldValue) {
      if (newValue !== oldValue) {
        location.reload();
      }
    },
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
      const userName = this.userprofile.user.username;
      return this.my_reviews.filter((review) => review.username === userName);
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
.mx-20rem {
  margin-left: 20rem;
  margin-right: 20rem;
}
.mx-23rem {
  margin-left: 23rem;
  margin-right: 23rem;
}
</style>
