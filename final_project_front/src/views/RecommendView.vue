<template>
  <div>
    <header class="text-center">
      <h1
        style="
          text-align: center;
          margin-top: 2rem;
          color: rgba(43, 137, 224, 88);
          text-decoration-color: rgba(43, 137, 224, 88);
          text-decoration-line: underline;
          text-decoration-style: double;
        "
      >
        오늘의 추천 영화
      </h1>
      <button
        @click.prevent="sort_movies"
        @click="movie_on"
        class="btn btn-primary"
      >
        오늘의 영화 뽑기
      </button>
      <div
        v-if="movie_flag"
        class="row mt-5 shadow-lg"
        style="
          background-color: #f03e02;
          background: radial-gradient(#f03e02, #19181d);
        "
      >
        <!-- #F03E02
        #ef035e -->
        <MovieItem
          v-for="(movie, idx) in selected_movies"
          :key="idx"
          :movie="movie"
          class="mx-auto mb-5"
        />
      </div>
      <!-- <div
        class="bg-black"
        style="background-color: black; height: 30rem; float: inline-start"
      ></div> -->
    </header>
    <section class="text-center m-5"></section>
  </div>
</template>

<script>
import MovieItem from "@/components/MovieWarItem.vue";
import _ from "lodash";
export default {
  name: "RecommendView",
  data() {
    return {
      movie_flag: false,
      selected_movies: [],
      movies_scored: [],
      keyword_input: "",
      GENRES: {
        28: "action",
        12: "adventure",
        16: "animation",
        35: "comedy",
        80: "crime",
        99: "documentary",
        18: "drama",
        10751: "family",
        14: "fantasy",
        36: "history",
        27: "horror",
        10402: "music",
        9648: "mystery",
        10749: "romance",
        878: "science_fiction",
        10770: "tv_movie",
        53: "thriller",
        10752: "war",
        37: "western",
      },
    };
  },
  components: {
    MovieItem,
  },
  methods: {
    getUser() {
      this.$store.dispatch("getUser");
    },
    getProfile() {
      const userPk = this.user.pk;
      //   console.log(userPk);
      this.$store.dispatch("getProfile", userPk);
    },
    sort_movies() {
      this.genres.forEach((genre) => {
        this.userprofile[this.GENRES[genre.id] + "_cnt"];
        this.movies_scored.forEach((movie) => {
          movie.total_score = 0;
          movie.genres.forEach((genre) => {
            movie.total_score =
              movie.total_score + this.userprofile[this.GENRES[genre] + "_cnt"];
          });
        });
      });
      //   점수를 먼저 비교해서 정렬하고 다음으로 total score를 기반으로 정렬
      this.movies_scored.sort(function (a, b) {
        if (a.total_score > b.total_score) return -1;
        if (a.total_score < b.total_score) return 1;

        if (a.vote_avg > b.vote_avg) return -1;
        if (a.vote_avg < b.vote_avg) return 1;
      });
      //   this.movies_scored.sort(function (a, b) {
      //     return b.vote_avg - a.vote_avg || b.total_score - a.total_score;
      //   });
      //   this.movies_scored.sort(function (a, b) {
      //     return b.total_score - a.total_score;
      //   });
      const lst = [];
      for (let index = 0; index < 10; index++) {
        lst.push(this.movies_scored[index]);
      }
      this.selected_movies = _.sampleSize(lst, 3);
    },
    movie_on() {
      this.movie_flag = true;
    },
  },
  computed: {
    user() {
      return this.$store.state.user;
    },
    userprofile() {
      return this.$store.state.userprofile;
    },
    movies() {
      return this.$store.state.movies;
    },
    genres() {
      return this.$store.state.genres;
    },
  },
  mounted() {
    this.getUser();
    this.getProfile();
    this.movies_scored = this.$store.state.movies;
  },
};
</script>

<style></style>
