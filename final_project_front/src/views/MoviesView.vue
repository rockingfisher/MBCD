<template>
  <div class="container" style="background-color: rgba(214, 230, 245, 96)">
    <!-- rgba(214, 230, 245, 96) -->
    <!-- rgba(245, 232, 213, 96) -->
    <!-- rgba(168, 147, 113, 66) -->

    <header class="row h-50">
      <!-- {{ carousel_movies }} -->
      <div
        id="carouselExampleInterval"
        class="carousel slide my-5"
        data-bs-ride="carousel"
      >
        <div class="carousel-inner my-auto">
          <div class="carousel-item active" data-bs-interval="3000">
            <img
              :src="carousel_movies[0]?.URL"
              class="d-block m-auto w-50 h-50 c carousel_img"
              alt="..."
              style="width: 80rem; height: 80rem"
            />
          </div>
          <div class="carousel-item" data-bs-interval="3000">
            <img
              :src="carousel_movies[1]?.URL"
              class="d-block m-auto w-50 h-50 carousel_img"
              alt="..."
              style="width: 80rem; height: 80rem"
            />
          </div>
          <div class="carousel-item" data-bs-interval="3000">
            <img
              :src="carousel_movies[2]?.URL"
              class="d-block m-auto w-50 h-50 carousel_img"
              alt="..."
              style="width: 80rem; height: 80rem"
            />
          </div>
        </div>
        <button
          class="carousel-control-prev"
          type="button"
          data-bs-target="#carouselExampleInterval"
          data-bs-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button
          class="carousel-control-next"
          type="button"
          data-bs-target="#carouselExampleInterval"
          data-bs-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </header>
    
    <div class="align-text-center"
    style="margin-top: 5rem; text-decoration-color: rgba(43, 137, 224, 88); text-decoration-line: underline; text-decoration-style: double;">
      <h1><th> 장르별 추천영화</th></h1>
    </div>
    <div v-for="genre in genres" :key="genre.id">
      <GenreMovies
        :movies = "movies"
        :genre = genre
        />

    </div>
  </div>
</template>

<script>
import GenreMovies from "@/components/GenreMovies.vue"
export default {
  name: "MovieView",
  data() {
    return {
      search_input: "",
      selectedMovie: [],
      movies: [],
      genres: [],
      searchedMovies: [],
      carousel_movies: [],
      API_URL: "https://image.tmdb.org/t/p/original/",
    };
  },
  components:{GenreMovies},
  computed: {},
  methods: {
    getMovies() {
      // console.log("getMovies");
      this.$store.dispatch("getMovie");
    },
    getgenre() {
      // console.log("장르불러오기");
      this.$store.dispatch("getGenre");
    },
    getCaroselPoster() {
      const lst = [];
      var cnt = 0;
      this.movies.forEach((movie) => {
        if (cnt < 3) {
          if (movie.vote_avg > 7.7) {
            const URL =
              "https://image.tmdb.org/t/p/original/" + movie.poster_path;
            const movie_title = movie.title;
            const data = {
              URL,
              movie_title,
            };
            lst.push(data);
            cnt += 1;
          }
        } else {
          return;
        }
      });
      this.carousel_movies = lst;
    },
    search() {
      if (!this.search_input) {
        this.searchedMovies = this.movies;
        return;
      }

      const searchTerm = this.search_input.toLowerCase();

      this.searchedMovies = this.movies.filter((movie) => {
        if (movie && movie.overview && movie.title) {
          return (
            movie.overview.toLowerCase().includes(searchTerm) ||
            movie.title.toLowerCase().includes(searchTerm)
          );
        }
        return false;
      });

      this.pageNum = 0;
    },
  },
  mounted() {
    this.getMovies();
    // console.log("mounted");
    setTimeout(() => {
      this.searchedMovies = this.movies = this.$store.state.movies;
      // console.log(this.movies);
    }, 100);
    setTimeout(() => {
      this.getCaroselPoster();
    }, 200);
    this.getgenre();
    setTimeout(() => {
      this.genres = this.$store.state.genres;
    }, 200);
  },
};
</script>

<style>
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

.carousel_img {
  border-radius: 11%;
}
</style>
