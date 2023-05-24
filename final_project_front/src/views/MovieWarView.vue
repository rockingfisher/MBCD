<template>
  <div class="row align-content-between">
    <div class="text-center" style="font-size: 5rem; color: black">
      <p v-if="round > 1">{{ round }}강</p>
      <div v-else>
        <p>최후의 영화는</p>
      </div>
    </div>
    <!-- {{ stack2 }}
    {{ two_movies }} -->
    <section class="row">
      <div
        v-for="(movie, idx) in two_movies"
        :key="idx"
        class="col-5 d-inline p-0 mx-auto"
        style="height: 35rem; width: 30rem"
        @click.prevent="push_stack2(movie)"
      >
        <MovieWarItem :movie="movie" />
      </div>
    </section>
    <div class="text-center mt-0" style="font-size: 10rem; color: red">
      <p v-if="round > 1">VS</p>
    </div>
    <div v-if="round < 2" class="text-center">
      <router-link
        :to="{
          name: 'MovieDetailView',
          params: { movie_title: stack2[0].title },
        }"
      >
        최후의 영화를 자세히 보려면 클릭
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MovieWarItem from "@/components/MovieWarItem.vue";
import _ from "lodash";
export default {
  name: "MovieWarView",
  data() {
    return {
      movies: [],
      // 뽑아오는 리스트
      stack1: [],
      // 선택된 영화를 저장하는 리스트
      stack2: [],
      // 2개 뽑아온 영화 리스트
      two_movies: [],
      round: 32,
    };
  },
  components: {
    MovieWarItem,
  },
  methods: {
    getMovies() {
      this.$store.dispatch("getMovie");
    },
    push_movies() {
      this.movies = this.$store.state.movies;
    },
    set_32_movies() {
      // console.log(this.movies);
      this.stack1 = _.sampleSize(this.movies, 32);
    },
    change_stack1_and_stack2() {
      this.stack1 = this.stack2;
    },
    get_stack1() {
      if (this.stack1.length > 0) {
        this.two_movies.push(this.stack1.pop());
        this.two_movies.push(this.stack1.pop());
      } else if (this.stack2.length % 2 == 0) {
        setTimeout(() => {
          this.round = this.round / 2;
          this.stack1 = this.stack2;
          console.log(this.stack1);
          this.stack2 = [];
          console.log(this.stack1);
        }, 100);
        setTimeout(() => {
          this.two_movies.push(this.stack1.pop());
          this.two_movies.push(this.stack1.pop());
        }, 300);
      } else if (this.stack2.length == 1) {
        // 1개 남았을 때 필요사항 작성하는곳
        // stack2에 1개 들어있음
        this.round = this.round / 2;
        this.two_movies.push(this.stack1.pop());
        this.push_score_lst();
      }
    },
    push_stack2(movie) {
      // console.log(movie)
      if (this.round > 1) {
        this.stack2.push(movie);
        this.two_movies = [];
        this.get_stack1();
      }
    },
    push_score_lst() {
      this.stack2[0].genres.forEach((genre_id) => {
        axios({
          method: "get",
          url: `http://127.0.0.1:8000/account/profile/increasecount/option/${this.user.pk}/${genre_id}/5/`,
        })
          .then((res) => {
            console.log(res);
          })
          .catch((err) => console.log(err));
      });
    },
  },
  computed: {
    user() {
      return this.$store.state.user;
    },
  },
  mounted() {
    this.getMovies();
    setTimeout(() => {
      this.push_movies();
    }, 100);
    setTimeout(() => {
      this.set_32_movies();
    }, 200);
    setTimeout(() => {
      this.get_stack1();
    }, 300);
  },
  created() {},
};
</script>

<style></style>
