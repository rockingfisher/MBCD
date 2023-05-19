<template>
  <div class="container">
    <header class="row h-50">
      <!-- {{ carousel_movies }} -->
      <div
        id="carouselExampleSlidesOnly"
        class="carousel slide my-5"
        data-bs-ride="carousel"
      >
        <div class="carousel-inner my-auto">
          <div class="carousel-item active" data-bs-interval="3000">
            <img
              :src="carousel_movies[0]?.URL"
              class="d-block m-auto"
              alt="..."
            />
          </div>
          <div class="carousel-item" data-bs-interval="3000">
            <img
              :src="carousel_movies[1]?.URL"
              class="d-block m-auto"
              alt="..."
            />
          </div>
          <div class="carousel-item" data-bs-interval="3000">
            <img
              :src="carousel_movies[2]?.URL"
              class="d-block m-auto"
              alt="..."
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
    <div class="row my-3 h-50">
      <MovieItem
        v-for="(movie, index) in paginatedData"
        :key="index"
        :movie="movie"
        style="width: 20rem; height: 20rem"
      />
    </div>
    <br />
    <br />
    <br />
    <div class="btn-cover">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
      </button>

      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>

      <button
        :disabled="pageNum >= pageCount - 1"
        @click="nextPage"
        class="page-btn"
      >
        다음
      </button>
    </div>
  </div>
</template>

<script>
import MovieItem from "../components/MovieItem.vue";

export default {
  name: "MovieView",
  data() {
    return {
      pageNum: 0,
      pageSize: 20,
      selectedMovie: [],
      movies: [],
      carousel_movies: [],
      API_URL: "https://image.tmdb.org/t/p/original/",
    };
  },
  components: {
    MovieItem,
  },
  computed: {
    pageCount() {
      let listLeng = this.movies.length,
        listSize = this.pageSize,
        page = Math.floor(listLeng / listSize);

      if (listLeng % listSize > 0) page += 1;
      return page;
    },
    paginatedData() {
      const start = this.pageNum * this.pageSize;
      const end = start + this.pageSize;
      return this.movies.slice(start, end);
    },
  },
  watch: {
    // pageNum() {
    //   this.paginatedData();
    // },
  },
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
      const lst = [];
      var cnt = 0;
      this.movies.forEach((movie) => {
        if (cnt < 3) {
          if (movie.vote_avg > 8) {
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
    nextPage() {
      this.pageNum += 1;
    },
    prevPage() {
      this.pageNum -= 1;
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
</style>
