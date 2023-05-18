<template>
  <div class="align-middle">
    <div class="text-bg-light p-3 border rounded w-75 h-75">
      <ReviewItem
        v-for="(review, index) in reviews"
        :key="index"
        :review="review"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ReviewItem from "../components/ReviewItem.vue";

export default {
  name: "CommunityView",
  data() {
    return {
      reviews: [],
    };
  },
  components: {
    ReviewItem,
  },
  computed: {},
  methods: {
    getReviews() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/community/reviews/",
      })
        .then((res) => {
          // console.log(res.data);
          this.reviews = res.data;
        })
        .catch((err) => console.log(err));
    },
  },
  created() {
    this.getReviews();
  },
};
</script>

<style></style>
