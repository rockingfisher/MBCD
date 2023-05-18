<template>
  <div class="row">
    <header class="col">
      <img :src="posterUrl" class="card-img border rounded-4 m-3" alt="..." />
    </header>
    <section class="col mt-5">
      <h1>제목 : {{ movie?.title }}</h1>
      <h2 class="my-4">
        <span class="text-warning">{{ star }}</span> : {{ movie?.vote_avg }}
      </h2>
      <h3>개봉일 : {{ movie.released_date }}</h3>
      <div class="rating"></div>

      <br />
      <h4>줄거리 : {{ movie?.overview }}</h4>
    </section>
  </div>
</template>

<script>
export default {
  name: "MovieDetailView",
  data() {
    return {
      movies: [],
      movie: null,
      posterUrl: null,
      star: "",
    };
  },
  computed: {
    // movies() {
    //   return this.$store.state.movies;
    // },
  },
  methods: {
    getMovie() {
      this.movies.forEach((movie) => {
        if (movie.title == this.$route.params.movie_title) {
          this.movie = movie;
          return;
        }
      });
      setTimeout(() => {
        this.posterUrl =
          "https://image.tmdb.org/t/p/original/" + this.movie.poster_path;
        this.makeStar();
      }, 100);
      // console.log(this.movie.posterUrl);
      // console.log(this.movie);
    },
    makeStar() {
      var tmp = "";
      const N = 5;
      const full_star = (this.movie.vote_avg + 1) / 2;
      console.log(full_star);
      for (let index = 1; index < N + 1; index++) {
        if (index < full_star) {
          tmp += "★";
        } else {
          tmp += "☆";
        }
      }
      console.log(tmp);
      this.star = tmp;
    },
  },
  mounted() {
    this.getMovie();
  },
  created() {
    this.movies = this.$store.state.movies;
  },
};
</script>

<style></style>
