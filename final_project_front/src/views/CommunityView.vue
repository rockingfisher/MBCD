<template>
  <div class="container text-bg-light h-1000px text-center">
    <h1>게시판</h1>
    <div class="row text-start">
      <th class="col-4">게시글 번호</th>
      <th class="col-4">게시글 제목</th>
      <th class="col-4">작성자</th>
    </div>

    <div class="border rounded">
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
<style scoped>
.h-4px {
  height: 4px;
}
.h-1000px {
  height: 1000px;
}
</style>
