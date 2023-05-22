<template>
  <div
    class="col-3 m-3"
    style="width: 18rem; height: 20rem; border-radius: 11%"
  >
    <div
      style="width: 18rem; height: 20rem; border-radius: 11%"
      @click="getMovieDetail"
      class="card text-bg-dark"
      @mouseover="changOverlay"
      @mouseout="changOverlay"
    >
      <!-- 카드에 마우스를 올리면 영화정보가 나오가 나오면 나오지 않게 동작 -->
      <img
        :src="PosterUrl"
        class="card-img"
        alt="..."
        style="width: 18rem; height: 20rem; border-radius: 11%"
      />
      <div
        class="card-img-overlay"
        v-show="this.overlay"
        style="width: 18rem; height: 20rem; border-radius: 11%"
      >
        <h5 class="card-title">{{ movie.title }}</h5>
        <p class="card-text">
          <small>{{ movie.overview }}</small>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieItem",
  data() {
    return {
      overlay: false,
    };
  },
  props: {
    movie: Object,
  },
  methods: {
    changOverlay() {
      this.overlay = !this.overlay;
    },
    getMovieDetail() {
      this.$router.push({
        name: "MovieDetailView",
        params: { movie_title: this.movie.title },
      });
    },
  },
  computed: {
    PosterUrl() {
      return "https://image.tmdb.org/t/p/original/" + this.movie.poster_path;
    },
  },
};
</script>

<style></style>
