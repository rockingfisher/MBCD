<template>
  <div class="container text-bg-light h-1000px text-center">
    <h1>게시판</h1>
    <div class="row text-start">
      <th class="col-3">게시글 번호</th>
      <th class="col-3">게시글 제목</th>
      <th class="col-3">작성자</th>
      <th class="col-3"></th>
    </div>

    <div class="border rounded">
      <ReviewItem
        v-for="(review, index) in selected_reviews"
        :key="index"
        :review="review"
      />
    </div>
    <div class="m-2">
      <router-link :to="{ name: 'CreateReviewView' }">
        <button>글쓰기</button>
      </router-link>
    </div>
    <form @submit.prevent="search">
      <select name="select_value" id="select_value">
        <option value="title">제목</option>
        <option value="content">내용</option>
        <option value="title_and_content">제목+내용</option>
      </select>
      <input type="text" id="serchReview" v-model="search_input">
      <button @click.prevent="search">검색</button>
    </form>
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
      selected_reviews:[],
      search_input: "",
    };
  },
  components: {
    ReviewItem,
  },
  methods: {
    getReviews() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/community/reviews/",
      })
        .then((res) => {
          this.reviews = res.data;
          this.selected_reviews = res.data;
        })
        .catch((err) => console.log(err));
    },
    search() {
    if (!this.search_input) {
      // 검색어가 입력되지 않은 경우 모든 게시글을 보여줍니다.
      this.getReviews();
      return;
    }

    const option = document.getElementById('select_value').value;
    const searchTerm = this.search_input.toLowerCase();

    this.selected_reviews = this.reviews.filter((review) => {
      if (option === 'title') {
        // 게시글 제목으로 검색
        return review.title.toLowerCase().includes(searchTerm);
      } else if (option === 'content') {
        // 게시글 내용으로 검색
        return review.content.toLowerCase().includes(searchTerm);
      } else if(option === 'title_and_content'){
        return review.content.toLowerCase().includes(searchTerm) || review.title.toLowerCase().includes(searchTerm) ;
        // 게시글 제목 + 내용으로 검색
      }
    });
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