<template>
  <div class="row align-content-between">
    <MovieWarItem
      v-for="(movie, idx) in two_movies"
      :key="idx"
      :movie="movie"
      class="mx-auto"
    />
    <div class="text-center" style="font-size: 10rem; color: red">
      <p>VS</p>
    </div>
  </div>
</template>

<script>
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
      two_movies: [],
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
      if (this.stack1) {
        this.two_movies.push(this.stack1.pop());
        this.two_movies.push(this.stack1.pop());
      }
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
