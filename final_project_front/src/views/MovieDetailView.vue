<template>
  <div>
    <div class="row" style="height: 50%">
      <header class="col-6">
        <img :src="posterUrl" class="card-img border rounded-4 m-3" alt="..." />
      </header>
      <section class="col-5 m-3">
        <h1>제목: {{ movie?.title }}</h1>
        <h2 class="my-4">
          <span class="text-warning">{{ star }}</span> : {{ movie?.vote_avg }}
        </h2>
        <h3>개봉일: {{ movie?.released_date }}</h3>
        <div class="rating"></div>

        <br />
        <h5>
          <th>줄거리: {{ movie?.overview }}</th>
        </h5>
        <br />
        <hr />
        <div class="youtube"></div>
      </section>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MovieDetailView",
  data() {
    return {
      movies: [],
      movie: null,
      posterUrl: null,
      star: "",
    };
  },
  methods: {
    getMovie() {
      this.movies.forEach((movie) => {
        if (movie.title == this.$route.params.movie_title) {
          this.movie = movie;
          return;
        }
      });
      setTimeout(() => {
        if (this.movie) {
          this.posterUrl =
            "https://image.tmdb.org/t/p/original/" + this.movie.poster_path;
          this.makeStar();
        }
      }, 100);
    },
    makeStar() {
      let tmp = "";
      const N = 5;
      const full_star = (this.movie.vote_avg + 1) / 2;
      for (let index = 1; index < N + 1; index++) {
        if (index < full_star) {
          tmp += "★";
        } else {
          tmp += "☆";
        }
      }
      this.star = tmp;
    },
    getVideoUrl() {
      const youtube = document.querySelector(".youtube");
      if (!youtube) {
        return;
      }

      const api_key = "cce60a874fcd4eaaa877cdc5211c1d3c";
      axios({
        method: "get",
        url: `https://api.themoviedb.org/3/movie/${this.movie.id}/videos?api_key=${api_key}`,
        data: {
          api_key,
        },
      })
        .then((res) => {
          let output = "<h3>예고편을 불러오는 중입니다.</h3>";
          if (res.data.results.length > 0) {
            const youtubeId = res.data.results[0].key;
            output = `<iframe width="100%" height="100%" src="https://www.youtube.com/embed/${youtubeId}?autoplay=1"></iframe>`;
          } else {
            output = '<h3 class="noVideo">재생할 예고편이 없습니다.</h3>';
          }
          youtube.innerHTML = output;
        })
        .catch((err) => {
          console.log(err);
          youtube.innerHTML =
            '<h3 class="noVideo">예고편을 가져오는 도중 오류가 발생했습니다.</h3>';
        });
    },
    getgenre() {
      // this.$store.dispatch(getGenre);
    },
  },
  mounted() {
    this.getMovie();
    setTimeout(() => {
      this.getVideoUrl();
    }, 200);
  },
  created() {
    this.movies = this.$store.state.movies;
  },
};
</script>

<style scoped>
.youtube {
  margin: auto;
  height: 600px;
}

iframe {
  display: block;
}
</style>
