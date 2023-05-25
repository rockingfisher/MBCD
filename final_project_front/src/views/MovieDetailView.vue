<template>
  <div class="container">
    <hr>
    <div class="row my-auto justify-content-between">
      <header class="col-6">
        <img :src="posterUrl" class="card-img border rounded-4 m-3 img-fluid" alt="..." />
      </header>
      <section class="col-5 m-3 d-flex flex-column justify-content-between">
          <div>
            <h1 class="mt-3">
              <th>제목: {{ movie?.title }}</th>
            </h1>
            <div class="my-4">
              <h2>
                <th class="text-warning" style="display: inline">{{ star }}</th>
                <th style="display: inline">: {{ movie?.vote_avg }}</th>
              </h2>
            </div>
            <div class="my-3">
              <h4 style="display: inline"><th>장르 :</th></h4>
              <span v-for="(genreName, idx) in genreNames" :key="idx" class="my-3">
                <h5 style="display: inline" class="text-primary">
                  <th class="">[{{ genreName }}]</th>
                </h5>
              </span>
            </div>
            <h4>
              <th>개봉일 : {{ movie?.released_date }}</th>
            </h4>
            <div class="rating"></div>
            <hr />
            <h5>
              <th>{{ movie?.overview }}</th>
            </h5>
          </div>
          <div>
            <hr>
            <div class="d-flex">
              <p class="heart fs-4 ms-5">♥ : {{ likecount }}</p>
              <div class="button mt-0 mb-0" @click="likeIt">
                <p v-if="Liked" class="btnText">싫어요!</p>
                <p v-else class="btnText">좋아요!</p>
                <div class="btnTwo">
                  <p class="btnText2">♥</p>
              </div>
            </div>
        </div>
          </div>
      </section>
      <hr />
      <div class="youtube"></div>
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
      genres: [],
      genreNames: [],
      movie: null,
      posterUrl: null,
      star: "",
      likecount: 0,
      Liked: null,
    };
  },
  methods: {
    getMovie() {
      this.movies.forEach((movie) => {
        if (movie.title == this.$route.params.movie_title) {
          this.movie = movie;
          axios.get(`http://127.0.0.1:8000/movies/${this.movie.id}/likes/`)
            .then((res) => {
              this.likecount = res.data.like_user.length;
            })
            .catch((err) => {
              console.log(err);
            });
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
        url: `https://api.themoviedb.org/3/movie/${this.movie?.id}/videos?api_key=${api_key}`,
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
      // console.log("장르불러오기");
      this.$store.dispatch("getGenre");
    },
    getGenreNames() {
      let genreNames = [];
      this.movie.genres.forEach((genre_id) => {
        // console.log(genre_id);
        const genre = this.genres.find((genre) => genre.id === genre_id);
        if (genre) {
          genreNames.push(genre.name);
        }
      });
      this.genreNames = genreNames;
    },
    likeIt() {
      const payload = this.movie.id
      const user = this.user
      const token = this.$store.state.token;
      const headers = {
        Authorization: `Token ${token}`,
      }
      axios.post(`http://127.0.0.1:8000/movies/${payload}/likes/`, user, {headers})
        .then((res)=>{
          this.likecount = res.data.like_user.length
          return res.data.like_user
        })
        .then((like_user)=>{
          const userId = this.user.pk;
          const userLiked = like_user.some((user) => user.id === userId);
          if (userLiked) {
            // 사용자가 좋아요를 누른 경우
            this.Liked = true
          } else {
            // 사용자가 좋아요를 누르지 않은 경우
            this.Liked = false
          }
        })
        .catch(err=>console.log(err))
    },
    checkIfUserLiked() {
      if (this.movie && this.movie.like_user) {
        const userId = this.user.pk; // 사용자 식별자를 지정해야 합니다.
        const userLiked = this.movie.like_user.some((user) => user.id === userId);
        console.log(userId)
        console.log(userLiked)
        if (userLiked) {
          // 사용자가 좋아요를 누른 경우
          console.log('사용자가 좋아요를 눌렀습니다.');
          this.Liked = true
        } else {
          // 사용자가 좋아요를 누르지 않은 경우
          console.log('사용자가 좋아요를 누르지 않았습니다.');
          this.Liked = false
        }
      }
    },
    increaseCount() {
      if (this.movie) {
        this.movie.genres.forEach((genre_id) => {
          axios({
            method: "get",
            url: `http://127.0.0.1:8000/account/profile/increasecount/${this.user.pk}/${genre_id}/`,
          })
            .then(() => {
              // console.log(res);
              this.getProfile();
            })
            .catch((err) => console.log(err));
        });
      }
    },
  },
  computed: {
    user() {
      return this.$store.state.user;
    },
  },
  mounted() {
    this.getMovie();
    setTimeout(() => {
      this.getVideoUrl();
    }, 200);
    this.getgenre();
    setTimeout(() => {
      this.genres = this.$store.state.genres;
    }, 200);
  },
  created() {
    this.movies = this.$store.state.movies;
    setTimeout(() => {
      this.getGenreNames();
    }, 300);
    setTimeout(() => {
      this.increaseCount();
    }, 300);
    setTimeout(()=>{
      this.checkIfUserLiked()
    }, 300)
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
.heartbox {
  height: 30px;
}

.heart {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
