<template>
  <div class="col my-5" style="width: 20rem; height: 20rem">
    <div
      class="card text-bg-dark"
      style="width: 16rem"
      @mouseover="changOverlay"
      @mouseout="changOverlay"
    >
      <!-- 카드에 마우스를 올리면 영화정보가 나오가 나오면 나오지 않게 동작 -->
      <!-- 직관적으로 ture, false로 작동하는 방법도 있음 -->
      <img :src="posterUrl" class="card-img" alt="..." />
      <div class="card-img-overlay" v-show="this.overlay">
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
      posterUrl:
        "https://image.tmdb.org/t/p/original/" + this.movie.poster_path,
    };
  },
  props: {
    movie: Object,
  },
  methods: {
    changOverlay() {
      this.overlay = !this.overlay;
    },
  },
};
</script>

<style></style>
