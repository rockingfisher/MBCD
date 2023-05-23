<template>
  <div class="border text-start">
    <div class="row">
      <th class="col-3 d-inline">게시글 번호: {{ review.id }}</th>
      <router-link
        :to="{ name: 'ReviewDetailView', params: { review_id: review.id } }"
        class="col-3 d-inline"
      >
        <th>게시글 제목: {{ review.title }}</th>
      </router-link>
      <th class="col-3 d-inline">작성자: {{ review.username }}</th>
      <div class="col-3">
        <button class="col-4" @click.prevent="deleteReview">게시글 삭제</button>
        <button class="col-4" @click.prevent="updateReview">게시글 수정</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ReviewItem",
  props: {
    review: Object,
  },
  methods: {
    deleteReview() {
      axios({
        method: "delete",
        url: `http://127.0.0.1:8000/community/reviews/${this.review.id}/`,
      })
        .then((res) => {
          console.log(res.data);
          this.$router.go();
          // this.$router.push({ name: "CommunityView" });
          // this.comments = res.data;
        })
        .catch((err) => {
          console.log(err);
          // console.log(review_id);
        });
    },
    updateReview() {
      this.$router.push({
        name: "UpdateReviewView",
        params: { review_id: this.review.id },
      });
    },
  },
};
</script>

<style scoped></style>
