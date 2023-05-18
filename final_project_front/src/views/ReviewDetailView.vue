<template>
  <div>
    <h1><th>ReviewDetail</th></h1>
    <hr />
    <p>글 번호 : {{ review?.id }}</p>
    <p>제목 : {{ review?.title }}</p>
    <p>내용 : {{ review?.content }}</p>
    <p>작성시간 : {{ review?.created_at }}</p>
    <p>수정시간 : {{ review?.updated_at }}</p>
    <hr />
    <h4><th>댓글 목록</th></h4>
    <hr />
    <div v-for="(comment, index) in comments" :key="index">
      <div v-if="comment.review_id == $route.params.review_id">
        {{ comment.content }}
        <hr />
      </div>
    </div>
    <form @submit="createcomment">
      <label for="comment">댓글 : </label>
      <input type="text" id="comment" v-model="comment_input" />
      <!-- <button @submit.prevent="createcomment">제출</button> -->
    </form>
    <hr />
    {{ comment_input }}
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
export default {
  name: "ReviewDetailView",
  data() {
    return {
      review: null,
      comments: [],
      comment_input: "",
    };
  },
  computed: {},
  methods: {
    getdetail() {
      axios({
        method: "get",
        url: `${API_URL}/community/reviews/${this.$route.params.review_id}/`,
        // url: `http://127.0.0.1:8000/community/reviews/`,
      })
        .then((res) => {
          // console.log(res);
          this.review = res.data;
        })
        .catch((err) => {
          console.log(err);
          // console.log(review_id);
        });
    },
    getcomments() {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/community/comments/`,
      })
        .then((res) => {
          // console.log(res.data);
          this.comments = res.data;
        })
        .catch((err) => {
          console.log(err);
          // console.log(review_id);
        });
    },
    createcomment() {
      // const username =
      const content = this.comment_input;
      const review_id = this.$route.params.review_id;
      console.log("댓글 생성");
      axios({
        method: "post",
        url: `${API_URL}/community/reviews/${this.$route.params.review_id}/comments/`,
        data: {
          content,
          review_id,
        },
      })
        .then((res) => {
          console.log(res);
          this.comment_input = "";
          // this.getcomments();
        })
        .catch((err) => console.log(err));
    },
  },
  props: {
    // review_id: Number,
    // review_id: String,
  },
  mounted() {
    this.getdetail();
    this.getcomments();
  },
};
</script>

<style></style>
