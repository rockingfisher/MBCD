<template>
  <div class="container text-bg-light h-1000px text-center">
    <h1 class="m-3 mt-5">리뷰 게시판</h1>
    <div class="row text-start" id="board">
      <th class="col-3">게시글 번호</th>
      <th class="col-3">게시글 제목</th>
      <th class="col-3">작성자</th>
      <th class="col-3">영화제목</th>
    </div>

    <div class="border rounded">
      <ReviewItem
        v-for="(review, index) in paginatedData"
        :key="index"
        :review="review"
      />
    </div>
    <div class="m-2">
      <router-link :to="{ name: 'CreateReviewView' }" style="text-decoration: none">
        <div class="button">
            <p class="btnText">리뷰 작성</p>
            <div class="btnTwo">
              <p class="btnText2">GO!</p>
            </div>
        </div>
      </router-link>
    </div>
    <form @submit.prevent="search" id="search_form">
      <select name="select_value" id="select_value" class="search_opt">
        <option value="title">제목</option>
        <option value="content">내용</option>
        <option value="title_and_content">제목+내용</option>
      </select>
      <input type="text" id="serchReview" v-model="search_input">
      <button class="btn btn-outline-info btn-sm" @click.prevent="search" id="selcet_btn">search</button>
    </form>
     <div class="btn-cover">
      <button
        :disabled="pageNum === 0"
        @click="prevPage"
        class="page-btn btn btn-primary"
      >
        Prev
      </button>

      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} Page</span>

      <button
        :disabled="pageNum >= pageCount - 1"
        @click="nextPage"
        class="page-btn btn btn-primary"
      >
        Next
      </button>
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
      pageNum: 0,
      pageSize: 20,
      reviews: [],
      selected_reviews:[],
      search_input: "",
    };
  },
  components: {
    ReviewItem,
  },
  computed: {
    pageCount() {
      let listLeng = this.reviews.length
      let listSize = this.pageSize
      let page = Math.floor(listLeng / listSize);

      if (listLeng % listSize > 0) page += 1;
      return page;
    },
    paginatedData() {
      const start = this.pageNum * this.pageSize;
      const end = start + this.pageSize;
      return this.reviews.slice(start, end);
    },
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
    nextPage() {
      this.pageNum += 1;
    },
    prevPage() {
      this.pageNum -= 1;
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
.button {
  background: #3D4C53;
  margin : 20px auto;
  width : 200px;
  height : 40px;
  overflow: hidden;
  text-align : center;
  transition : .2s;
  cursor : pointer;
  border-radius: 3px;
  box-shadow: 0px 1px 2px rgba(0,0,0,.2);
}
.btnTwo {
  position : relative;
  width : 200px;
  height : 100px;
  margin-top: -100px;
  padding-top: 2px;
  background : rgba(43, 137, 224, 88);
  left : -250px;
  transition : .3s;
}
.btnText {
  margin-top: 9px;
  color : white;
  transition : .3s;
}
.btnText2 {
  margin-top : 59px;
  margin-right : -130px;
  color : #FFF;
}
.button:hover .btnTwo{ /*When hovering over .button change .btnTwo*/
  left: -130px;
}
.button:hover .btnText{ /*When hovering over .button change .btnText*/
  margin-left : 65px;
}
.button:active { /*Clicked and held*/
  box-shadow: 0px 5px 6px rgba(0,0,0,0.3);
}
.search_opt {
  appearance: none;
  height: 32px;
  width: 95px;
  /* 추가적인 스타일링을 위한 속성들 */
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #fff;
  color: #333;
  /* 기타 스타일링 속성들 */
  text-align: center;
}
.btn-cover {
  margin-top: 1.5rem;
  text-align: center;
}
.btn-cover .page-btn {
  width: 5rem;
  height: 2rem;
  letter-spacing: 0.5px;
}
.btn-cover .page-count {
  padding: 0 1rem;
}

#board {
  margin: 0px 0px 0px;
  border: 1px solid black;
  background-color: #e2eef3c7;
}
#search_form {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
}
#selcet_btn{
  margin-inline-end: 37px;
}
</style>
