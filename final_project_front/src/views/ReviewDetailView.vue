<template>
  <div>
    <h1>ReviewDetail</h1>
    <hr />
    {{ review_id }}
    <p>글 번호 : {{ review?.id }}</p>
    <p>제목 : {{ review?.title }}</p>
    <p>내용 : {{ review?.content }}</p>
    <p>작성시간 : {{ review?.created_at }}</p>
    <p>수정시간 : {{ review?.updated_at }}</p>
    <hr />
    <div v-for="(comment, index) in comments" :key="index">
      <div v-if="comment.review_id == review_id">
        {{ comment.content }}
      </div>
    </div>
    <div>
      <label for="comment">댓글</label>
      <input type="text" id="comment" v-model="comment_input" />
      <button @submit="createcomment">제출</button>
    </div>
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
          console.log(res);
          // this.movies = res.data;
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
      const content = this.comment_input;
      const review_id = this.review_id;
      console.log("작동");
      axios({
        method: "post",
        url: `${API_URL}/reviews/${this.$route.params.review_id}/comments/`,
        data: {
          content,
          review_id,
        },
      })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => console.log(err));
    },
  },
  props: {
    // review_id: Number,
    review_id: String,
  },
  mounted() {
    // this.getdetail();
    // this.getcomments();
  },
};
</script>

<style></style>
