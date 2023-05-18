import Vue from "vue";
import VueRouter from "vue-router";
// import { component } from "vue/types/umd";
import MoviesView from "../views/MoviesView.vue";
import CommunityView from "../views/CommunityView.vue";
import ReviewDetailView from "@/views/ReviewDetailView";
import MovieDetailView from "@/views/MovieDetailView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "MoviesView",
    component: MoviesView,
  },
  {
    path: "/communiy",
    name: "CommunityView",
    component: CommunityView,
  },
  {
    path: "/reviewdetail/:review_id",
    name: "ReviewDetailView",
    component: ReviewDetailView,
    props: true,
  },
  {
    path: "/moviedetail/",
    name: "MovieDetailView",
    component: MovieDetailView,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
