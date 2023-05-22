<template>
  <form @submit="updateReview">
    <header class="mt-3">
      <label for="title_input" class="ms-3"> 제&nbsp;&nbsp;목 : </label>
      <input
        type="text"
        class="ms-3"
        id="title_input"
        style="width: 800px"
        v-model="title_input"
      />
      <hr />
      <label for="movie_title_input" class="ms-3">영화제목 : </label>
      <input
        type="text"
        class="ms-3"
        id="movie_title_input"
        style="width: 800px"
        v-model="movie_title_input"
      />
    </header>
    <hr />
    <section>
      <label for="rank_input" class="ms-3"> 내 평점 : </label>
      <input
        type="number"
        min="0"
        max="10"
        class="ms-3"
        id="rank_input"
        v-model="rank_input"
      />
      <hr />
      <label for="content_input"> 내용 : </label>
      <textarea
        id="content_input"
        class="m-2 w-100"
        style="width: 1200px; height: 800px"
        v-model="content_input"
      />
    </section>
    <button class="align-self-end">수정</button>
  </form>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
export default {
  name: "UpdateReviewView",
  data() {
    return {
      title_input: null,
      content_input: null,
      movie_title_input: null,
      rank_input: null,
      review_id: 0,
    };
  },
  methods: {
    updateReview() {
      if (!this.$route.params.review_id) {
        this.moveCommunity();
      }

      const title = this.title_input;
      const content = this.content_input;
      const rank = this.rank_input;
      const movie_title = this.movie_title_input;

      if (!title) {
        alert("제목을 입력해주세요");
        return;
      }
      if (!content) {
        alert("내용을 입력해주세요");
        return;
      }

      if (!rank) {
        alert("평점을 입력해주세요");
        return;
      }
      if (!movie_title) {
        alert("영화제목을 입력해주세요");
        return;
      }

      axios({
        method: "put",
        url: `${API_URL}/community/reviews/${this.review_id}/`,
        data: {
          title,
          content,
          rank,
          movie_title,
        },
      })
        .then((res) => {
          console.log(res);
          this.$router.push({
            name: "CommunityView",
          });
          // this.comment_input = "";
          // this.getcomments();
        })
        .catch((err) => console.log(err));
    },
    getdetail() {
      if (!this.$route.params.review_id) {
        this.moveCommunity();
      }
      // console.log(this.$route.params.review_id);
      axios({
        method: "get",
        url: `${API_URL}/community/reviews/${this.$route.params.review_id}/`,
        // url: `http://127.0.0.1:8000/community/reviews/`,
      })
        .then((res) => {
          // console.log(res.data);
          // this.review = res.data;
          this.title_input = res.data.title;
          this.content_input = res.data.content;
          this.movie_title_input = res.data.movie_title;
          this.rank_input = res.data.rank;
          this.review_id = this.$route.params.review_id;
        })
        .catch((err) => {
          console.log(err);
          // console.log(review_id);
        });
    },
    moveCommunity() {
      this.$router.push({
        name: "CommunityView",
      });
    },
  },
  mounted() {
    // console.log(this.$route.params.review_id);
    this.getdetail();
  },
};
</script>

<style></style>
