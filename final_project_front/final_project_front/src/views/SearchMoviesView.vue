<template>
  <div class="container" style="background-color: rgba(214, 230, 245, 96)">
    <!-- rgba(214, 230, 245, 96) -->
    <!-- rgba(245, 232, 213, 96) -->
    <!-- rgba(168, 147, 113, 66) -->
    <div class="text-center mt-3">
      <h1 v-if="search_output" style="color:white; text-shadow: 1px 1px 1px black;">
        '{{ search_output }}' 로 검색한 결과
        <div v-if="searchedMovies==''" class="my-5">
          검색 결과가 없습니다
        </div>
      </h1>
    </div>
    <!-- 영화 16개 표시 -->
    <div class="row h-50">
      <MovieItem
        v-for="(movie, index) in paginatedData"
        :key="index"
        :movie="movie"
        style="height: 20rem"
      />
    </div>
    <br />
    <br />
    <form @submit.prevent="search" class="d-flex justify-center" role="search">
        <input
          v-model="search_input"
          class="form-control"
          type="search"
          placeholder="Search"
          aria-label="Search"
          style="width: 30%; margin-left: 30%;"
        />
        <button class="btn btn-outline-info" type="submit">
          Search
        </button>
          </form>
    <!-- 페이지 이동 -->
    <div class="btn-cover">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn btn btn-primary">
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
    <!-- 영화검색 -->
  </div>
</template>

<script>
import MovieItem from "../components/MovieItem.vue";

export default {
  name: "SearchMovieView",
  data() {
    return {
      pageNum: 0,
      pageSize: 16,
      search_input: "",
      search_output: "",
      selectedMovie: [],
      movies: [],
      searchedMovies: [],
      carousel_movies: [],
      API_URL: "https://image.tmdb.org/t/p/original/",
    };
  },
  components: {
    MovieItem,
  },
  computed: {
    pageCount() {
      let listLeng = this.searchedMovies.length,
        listSize = this.pageSize,
        page = Math.floor(listLeng / listSize);

      if (listLeng % listSize > 0) page += 1;
      return page;
    },
    paginatedData() {
      const start = this.pageNum * this.pageSize;
      const end = start + this.pageSize;
      return this.searchedMovies.slice(start, end);
    },
  },
  methods: {
    getMovies() {
      // console.log("getMovies");
      this.$store.dispatch("getMovie");
    },

    nextPage() {
      this.pageNum += 1;
    },
    prevPage() {
      this.pageNum -= 1;
    },
    search() {
      if (!this.search_input) {
        this.searchedMovies = this.movies;
        this.search_output = ''
        return;
      }

      const searchTerm = this.search_input.toLowerCase();
      this.search_output = searchTerm
      this.search_input = ''
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
      this.search_input = this.$route.params.search_input
      this.search()
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
