<template>
  <div class="border text-start">
    <div class="row">
      <th class="col-3 d-flex align-items-center"> No: {{ review.id }}</th>
      <router-link
        :to="{ name: 'ReviewDetailView', params: { review_id: review.id } }"
        class="col-3 d-flex align-items-center" style="text-decoration: none"
      >
        <th>{{ review.title }}</th>
      </router-link>
      <router-link :to="{ name:'AnotherProfile', params: { user_id: review.user_id }}" class="col-3 d-flex align-items-center" style="text-decoration: none">
        <th>{{ review.username }}</th>
      </router-link>
      <div class="col-3 d-flex justify-content-evenly">
        <button class="btn btn-outline-danger " @click.prevent="deleteReview">삭제</button>
        <button class="btn btn-outline-warning custom-color" @click.prevent="updateReview">수정</button>
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

<style scoped>
.custom-color {
  border-color: rgba(224, 155, 43, 88);
}
</style>
