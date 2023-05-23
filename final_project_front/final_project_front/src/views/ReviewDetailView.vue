<template>
  <div class="ms-3">
    <h1>
      <th>제목 : {{ review?.title }}</th>
    </h1>
    <h4>
      <p>글 번호 : {{ review?.id }}</p>
    </h4>
    <hr />
    <section class="h-500px">
      <p>내용 : {{ review?.content }}</p>
    </section>
    <hr />
    <p>작성시간 : {{ review?.created_at }}</p>
    <!-- <p>수정시간 : {{ review?.updated_at }}</p> -->
    <hr />
    <h4><th>댓글 목록</th></h4>
    <hr />
    <hr />
    <CommentItem
      v-for="(comment, index) in comments"
      :key="index"
      :comment="comment"
      :review_id="review?.id"
    />
    <!-- <div v-for="(comment, index) in comments" :key="index">
      <div v-if="comment.review_id == $route.params.review_id">
        {{ comment.content }}
        <hr />
      </div>
    </div> -->
    <form @submit="createcomment">
      <label for="comment_input">댓글 : </label>
      <input type="text" id="comment_input" v-model="comment_input" />
      <button @submit.prevent="createcomment">submit</button>
    </form>
    <hr />
  </div>
</template>

<script>
import CommentItem from "@/components/CommentItem.vue";
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
  components: {
    CommentItem,
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
      // console.log("댓글 생성");
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

<style>
.h-500px {
  height: 500px;
}
</style>
