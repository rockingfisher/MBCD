<template>
  <div>
    <header>
      <div
        v-for="(movie, idx) in carousel_movies"
        :key="idx"
        id="carouselExampleSlidesOnly"
        class="carousel slide"
        data-bs-ride="carousel"
      >
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img
              src="API_URL+movie.poster_path"
              class="d-block w-100"
              alt="..."
            />
          </div>
          <div class="carousel-item">
            <img src="" class="d-block w-100" alt="..." />
          </div>
          <div class="carousel-item">
            <img src="" class="d-block w-100" alt="..." />
          </div>
        </div>
      </div>
    </header>
    <div class="row my-3">
      <MovieItem
        v-for="(movie, index) in movies"
        :key="index"
        :movie="movie"
        style="width: 20rem; height: 20rem"
      />
    </div>
  </div>
</template>

<script>
import MovieItem from "../components/MovieItem.vue";

export default {
  name: "MovieView",
  data() {
    return {
      movies: [],
      carousel_movies: [],
      API_URL: "https://image.tmdb.org/t/p/original/",
    };
  },
  components: {
    MovieItem,
  },
  computed: {},
  // "https://image.tmdb.org/t/p/original/" + this.movie.poster_path
  // select30Movies(){
  //   this.movies.filter((movie) => {
  // }
  // });
  methods: {
    getMovies() {
      // console.log("getMovies");
      this.$store.dispatch("getMovie");
    },
    getCaroselPoster() {
      this.movies.forEach((movie) => {
        if (movie.id <= 3) {
          this.carousel_movies.push(movie);
        }
      });
    },
  },
  // created() {
  //   console.log("created");
  //   this.getMovies();
  // },
  mounted() {
    this.getMovies();
    // console.log("mounted");
    setTimeout(() => {
      this.movies = this.$store.state.movies;
      // console.log(this.movies);
    }, 100);
    setTimeout(() => {
      this.getCaroselPoster();
    }, 200);
  },
};
</script>

<style></style>
