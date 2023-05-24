<template>
  <div>
    <hr />
    <h1>{{ user.username }}'s profile</h1>
    <p>email : {{ user.email }}</p>
    <img :src="profileImageUrl" alt="자비좀" />
    <button @click="openImageUpload">Upload Image</button>
    <hr />
    <hr />
    <button @click="logOut">LogOut</button>
    <button @click="pwchange">password change</button>
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
        class="d-inline btn btn-primary col-1 m-4"
        v-for="(genre, idx) in genres"
        :class="{ deactive: !userprofile[GENRES[genre.id] + '_key'] }"
        :key="idx"
        @click.prevent="activeBtn(genre)"
      >
        {{ genre.name }}
      </div>
      <!-- {{ userprofile }} -->
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
</style>
