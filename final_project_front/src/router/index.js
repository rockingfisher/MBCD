import Vue from "vue";
import VueRouter from "vue-router";
// import { component } from "vue/types/umd";
import MovieView from "../views/MovieView.vue";
import CommunityView from "../views/CommunityView.vue";
import ReviewDetailView from "@/views/ReviewDetailView";
import SignUpView from "@/views/SignUpView";
import ProfileView from "@/views/ProfileView";
import LogInView from "@/views/LogInView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "MovieView",
    component: MovieView,
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
    path: "/signup",
    name: "SignUpView",
    component: SignUpView,
  },
  {
    path: "/profile",
    name: "ProfileView",
    component: ProfileView,
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
