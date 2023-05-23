<template>
  <form @submit="createReview">
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
    <button class="align-self-end">게시글 작성</button>
  </form>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
export default {
  name: "CreateReviewView",
  data() {
    return {
      title_input: null,
      content_input: null,
      movie_title_input: null,
      rank_input: null,
    };
  },
  methods: {
    createReview() {
      // const username =
      const title = this.title_input;
      const content = this.content_input;
      const rank = this.rank_input;
      const movie_title = this.movie_title_input;

      if (!title) {
        alert("제목을 입력해주세요");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/community/reviews/`,
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
  },
};
</script>

<style></style>
