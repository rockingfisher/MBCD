<template>
  <form @submit="updateReview">
    <header class="mt-3">
      <label for="title_input" class="ms-3 custom"> 리뷰제목 : </label>
      <input
        type="text"
        class="ms-3 form-control"
        id="title_input"
        style="width: 800px"
        v-model="title_input"
      />
      <hr />
      <label for="movie_title_input" class="ms-3 custom">영화제목 : </label>
      <input
        type="text"
        class="ms-3 form-control"
        id="movie_title_input"
        style="width: 800px"
        v-model="movie_title_input"
      />
    </header>
    <hr />
    <section>
      <label for="rank_input" class="ms-3 custom"> 내 평점 : </label>
      <input
        type="number"
        min="0"
        max="10"
        class="ms-3 form-control custom"
        id="rank_input"
        v-model="rank_input"
      />
      <hr />
      <label for="content_input" class="ms-3"> 리뷰내용 : </label>
      <div class="m-2">
        <textarea
          id="content_input"
          class="w-100 form-control"
          style="min-height: 500px;"
          v-model="content_input"
        />
      </div>
    </section>
    <div class="button" @click="updateReview">
        <p class="btnText">리뷰 수정</p>
        <div class="btnTwo">
          <p class="btnText2">GO!</p>
        </div>
    </div>
  </form>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
export default {
  name: "UpdateReviewView",
  data() {
    return {
      title_input: null,
      content_input: null,
      movie_title_input: null,
      rank_input: null,
      review_id: 0,
    };
  },
  methods: {
    updateReview() {
      if (!this.$route.params.review_id) {
        this.moveCommunity();
      }

      const title = this.title_input;
      const content = this.content_input;
      const rank = this.rank_input;
      const movie_title = this.movie_title_input;

      if (!title) {
        alert("제목을 입력해주세요");
        return;
      }
      if (!content) {
        alert("내용을 입력해주세요");
        return;
      }

      if (!rank) {
        alert("평점을 입력해주세요");
        return;
      }
      if (!movie_title) {
        alert("영화제목을 입력해주세요");
        return;
      }

      axios({
        method: "put",
        url: `${API_URL}/community/reviews/${this.review_id}/`,
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
    getdetail() {
      if (!this.$route.params.review_id) {
        this.moveCommunity();
      }
      // console.log(this.$route.params.review_id);
      axios({
        method: "get",
        url: `${API_URL}/community/reviews/${this.$route.params.review_id}/`,
        // url: `http://127.0.0.1:8000/community/reviews/`,
      })
        .then((res) => {
          // console.log(res.data);
          // this.review = res.data;
          this.title_input = res.data.title;
          this.content_input = res.data.content;
          this.movie_title_input = res.data.movie_title;
          this.rank_input = res.data.rank;
          this.review_id = this.$route.params.review_id;
        })
        .catch((err) => {
          console.log(err);
          // console.log(review_id);
        });
    },
    moveCommunity() {
      this.$router.push({
        name: "CommunityView",
      });
    },
  },
  mounted() {
    // console.log(this.$route.params.review_id);
    this.getdetail();
  },
};
</script>

<style>
.custom {
  width: 75px;
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
</style>