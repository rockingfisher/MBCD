<template>
  <div v-if="genreMovies.length>4"
    class=""
    style="margin-top: 8rem; margin-bottom: 8rem;">
    <h2 style="margin-left: 1rem; 
    margin-bottom: 1rem; margin-top: 1rem; color: white; 
    text-shadow: 1px 1px 4px rgba(43, 137, 224, 88);
    "><th># {{ genre.name }}</th></h2>
    <div class="movie-row" style="background-color: rgba(43, 137, 224, 88); border-radius: 9%;">
      <MovieItem v-for="movie in genreMovies.slice(0, 4)" 
      :key="movie.id" :movie="movie"
      style="box-shadow: 10%;" />
    </div>
  </div>
</template>

<script>
import MovieItem from "./MovieItem.vue";
export default {
  name: "GenreMovies",
  props: {
    movies: Array,
    genre: Object
  },
  components: {
    MovieItem,
  },
  data() {
    return {
      genreMovies: [],
    };
  },
  methods: {
    selectGenreMovie() {
      this.genreMovies = this.movies.filter((movie) =>
        movie.genres.includes(this.genre.id)
      );
      // 리스트를 섞어 줍니다
      this.genreMovies.sort(() => Math.random() - 0.5);
    },
  },
  mounted() {
    setTimeout(() => {
      this.selectGenreMovie();
    }, 300);
  },
};
</script>

<style>
.movie-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
</style>
