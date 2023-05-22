<template>
  <div class="container" style="background-color: rgba(214, 230, 245, 96)">
    <!-- rgba(214, 230, 245, 96) -->
    <!-- rgba(245, 232, 213, 96) -->
    <!-- rgba(168, 147, 113, 66) -->

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
    <form @submit.prevent="search" class="text-center">
      <div class="d-inline mx-auto">
        <input type="text" id="serchReview" v-model="search_input" />
        <button @click.prevent="search">검색</button>
      </div>
    </form>
    <!-- 페이지 이동 -->
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
    <!-- 영화검색 -->
  </div>
</template>

<script>
import MovieItem from "../components/MovieItem.vue";

export default {
  name: "MovieView",
  data() {
    return {
      pageNum: 0,
      pageSize: 16,
      search_input: "",
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

    nextPage() {
      this.pageNum += 1;
    },
    prevPage() {
      this.pageNum -= 1;
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
