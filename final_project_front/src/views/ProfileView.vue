<template>
  <div class="profileheader">
    <hr />
    <header class="text-center">
      <h1>
        <span style="text-shadow: 1px 1px 1px gray; font-size: 3rem">{{
          user.username
        }}</span
        >'s profile
      </h1>
    </header>
    <section class="justify-center text-center shadow-sm">
      <img
        class="shadow-lg"
        style="border-radius: 50%; width: 30%; height: 30%"
        :src="profileImageUrl"
        alt="자비좀"
      />
      <p class="my-3">Email : {{ user.email }}</p>
      <div class="btn btn-secondary mb-4" @click="openImageUpload">
        Upload Image
      </div>
    </section>

    <hr />
    <span
      class="text-center m-3 text-primary"
      style="text-decoration-line: underline"
    >
      <h2><p>선호하는 장르를 선택해주세요</p></h2>
    </span>
    <div
      class="row shadow-sm mx-3"
      style="border-radius: 20px; text-shadow: 1px 1px 4px grey"
    >
      <div
        class="d-inline btn btn-primary col-2 my-3"
        style="margin-left: 3.2rem; margin-right: 3.2rem; border-radius: 20px"
        v-for="(genre, idx) in genres"
        :class="{ deactive: !userprofile[GENRES[genre.id] + '_key'] }"
        :key="idx"
        @click.prevent="activeBtn(genre)"
      >
        {{ genre.name }}
      </div>
      <!-- {{ userprofile }} -->
      <hr />
      <footer class="row my-3">
        <div class="btn btn-secondary col-2 mx-auto" @click="logOut">
          LogOut
        </div>
        <div class="btn btn-secondary col-2 mx-auto" @click="pwchange">
          password change
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ProFile",
  data() {
    return {
      GENRES: {
        28: "action",
        12: "adventure",
        16: "animation",
        35: "comedy",
        80: "crime",
        99: "documentary",
        18: "drama",
        10751: "family",
        14: "fantasy",
        36: "history",
        27: "horror",
        10402: "music",
        9648: "mystery",
        10749: "romance",
        878: "science_fiction",
        10770: "tv_movie",
        53: "thriller",
        10752: "war",
        37: "western",
      },
    };
  },
  methods: {
    getUser() {
      this.$store.dispatch("getUser");
    },
    logOut() {
      this.$store.dispatch("logOut");
    },
    getProfile() {
      const userPk = this.user.pk;
      console.log(userPk);
      this.$store.dispatch("getProfile", userPk);
    },
    pwchange() {
      this.$router.push("/pwchange");
    },
    openImageUpload() {
      window.open("/image-upload", "_blank");
    },
    activeBtn(genre) {
      // console.log(this.user.pk);
      // console.log(genre.id);
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/account/profile/togglecount/${this.user.pk}/${genre.id}/`,
      })
        .then((res) => {
          console.log(res);
          this.getProfile();
        })
        .catch((err) => console.log(err));
    },
  },
  created() {
    this.getUser();
  },
  mounted() {
    this.getProfile();
  },
  computed: {
    user() {
      return this.$store.state.user;
    },
    userprofile() {
      return this.$store.state.userprofile;
    },
    movie() {
      return this.$store.state.movie;
    },
    profileImageUrl() {
      const imageName = this.userprofile.picture;
      return `http://127.0.0.1:8000${imageName}`;
    },
    genres() {
      return this.$store.state.genres;
    },
  },
};
</script>

<style>
.deactive {
  background-color: gainsboro;
}
.profileheader {
  margin-left: 20rem;
  margin-right: 20rem;
}
</style>
