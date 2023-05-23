<template>
  <div
    class="col-3 align-content-center"
    style="width: 30rem; height: 35rem; border-radius: 11%; margin: 1rem"
  >
    <div
      class="card shadow"
      style="
        width: 30rem;
        height: 35rem;
        border-radius: 11%;
        margin: 1rem;
        color: white;
      "
      @click="getMovieDetail"
      @mouseover="changOverlay"
      @mouseout="changOverlay"
    >
      <!-- 카드에 마우스를 올리면 영화정보가 나오가 나오면 나오지 않게 동작 -->
      <img
        :src="PosterUrl"
        class="card-img shadow"
        alt="..."
        style="width: 30rem; height: 35rem; border-radius: 11%"
      />
      <div
        class="card-img-overlay shadow"
        v-show="this.overlay"
        style="width: 30rem; height: 35rem; border-radius: 11%"
      >
        <h4 class="card-title" style="text-shadow: 1px 1px 2px black">
          {{ movie.title }}
        </h4>
        <h4>
          <span style="color: gold; text-shadow: 1px 1px 2px black">
            {{ Star }} :
          </span>
          <span style="color: white; text-shadow: 1px 1px 2px black">
            {{ movie.vote_avg }}
          </span>
        </h4>
        <p class="card-text" style="text-shadow: 1px 1px 2px black">
          <small>{{ movie.overview.slice(0, 100) }}...</small>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieWarItem",
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
      if (this.$route.path !== "/moviewar") {
        this.$router.push({
          name: "MovieDetailView",
          params: { movie_title: this.movie.title },
        });
      }
    },
  },
  computed: {
    PosterUrl() {
      return "https://image.tmdb.org/t/p/original/" + this.movie.poster_path;
    },
    Star() {
      let star = "";
      const N = 5;
      const full_star = (this.movie.vote_avg + 1) / 2;
      for (let index = 1; index < N + 1; index++) {
        if (index < full_star) {
          star += "★";
        } else {
          star += "☆";
        }
      }
      return star;
    },
  },
};
</script>

<style></style>
