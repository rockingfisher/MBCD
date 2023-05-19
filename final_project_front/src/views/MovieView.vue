<template>
  <div class="row my-3">
    <MovieItem
      v-for="(movie, index) in movies"
      :key="index"
      :movie="movie"
      style="width: 20rem; height: 20rem"
    />
  </div>
</template>

<script>
import axios from "axios";
import MovieItem from "../components/MovieItem.vue";

export default {
  name: "MovieView",
  data() {
    return {
      movies: [],
    };
  },
  components: {
    MovieItem,
  },
  computed: {},
  methods: {
    getMovies() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/movies/home/",
      })
        .then((res) => {
          console.log(res.data);
          this.movies = res.data;
        })
        .catch((err) => console.log(err));
    },
  },
  created() {
    this.getMovies();
  },
};
</script>

<style></style>
