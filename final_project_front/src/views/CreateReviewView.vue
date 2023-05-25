<template>
  <form @submit="createReview">
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
      <div>
        <label for="movie_title_input" class="ms-3 custom">영화제목 : </label>
        <input
          @input="searchMovie"
          type="text"
          class="ms-3 form-control"
          id="movie_title_input"
          style="width: 800px"
          v-model="movie_title_input"
        />
        <ul
          v-if="showMovies"
          style="border-radius: 20px; padding-start: 20px; width: 810px"
        >
          <div
            v-for="movie in selctedMovies"
            :key="movie"
            class="shadow-sm"
            @click="inputMovieTitle(movie.title)"
          >
            <p class="mb-0 m-2">
              {{ movie.title }}
            </p>
          </div>
        </ul>
      </div>
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
          style="min-height: 500px"
          v-model="content_input"
        />
      </div>
    </section>
    <div class="button" @click="createReview">
      <p class="btnText">리뷰 등록</p>
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
  name: "CreateReviewView",
  data() {
    return {
      title_input: null,
      content_input: null,
      movie_title_input: null,
      rank_input: null,
      selctedMovies: [],
      showMovies: false,
    };
  },
  methods: {
    createReview() {
      // const username =
      const title = this.title_input;
      const content = this.content_input;
      const rank = this.rank_input;
      const movie_title = this.movie_title_input;
      const user_pk = this.user.pk;

      if (!title) {
        alert("제목을 입력해주세요");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/community/reviews/`,
        data: {
          title,
          content,
          rank,
          movie_title,
          user_pk,
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
    searchMovie() {
      if (this.movie_title_input.length > 0) {
        this.selctedMovies = this.movies.filter((movie) => {
          return movie.title.includes(this.movie_title_input.trim());
        });
        this.showMovies = true;
      } else {
        this.selctedMovies = [];
        this.showMovies = false;
      }
    },
    inputMovieTitle(title) {
      this.movie_title_input = title;
      this.showMovies = false;
    },
  },
  computed: {
    user() {
      return this.$store.state.user;
    },
    movies() {
      return this.$store.state.movies;
    },
  },
};
</script>

<style>
.custom {
  width: 75px;
}
.button {
  background: #3d4c53;
  margin: 20px auto;
  width: 200px;
  height: 40px;
  overflow: hidden;
  text-align: center;
  transition: 0.2s;
  cursor: pointer;
  border-radius: 3px;
  box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.2);
}
.btnTwo {
  position: relative;
  width: 200px;
  height: 100px;
  margin-top: -100px;
  padding-top: 2px;
  background: rgba(43, 137, 224, 88);
  left: -250px;
  transition: 0.3s;
}
.btnText {
  margin-top: 9px;
  color: white;
  transition: 0.3s;
}
.btnText2 {
  margin-top: 59px;
  margin-right: -130px;
  color: #fff;
}
.button:hover .btnTwo {
  /*When hovering over .button change .btnTwo*/
  left: -130px;
}
.button:hover .btnText {
  /*When hovering over .button change .btnText*/
  margin-left: 65px;
}
.button:active {
  /*Clicked and held*/
  box-shadow: 0px 5px 6px rgba(0, 0, 0, 0.3);
}
</style>
