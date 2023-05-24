import Vue from "vue";
import VueRouter from "vue-router";
// import { component } from "vue/types/umd";
import MoviesView from "../views/MoviesView.vue";
import CommunityView from "../views/CommunityView.vue";
import ReviewDetailView from "@/views/ReviewDetailView";
import MovieDetailView from "@/views/MovieDetailView";
import SignUpView from "@/views/SignUpView";
import ProfileView from "@/views/ProfileView";
import AnotherProfile from "@/views/AnotherProfile";
import LogInView from "@/views/LogInView";
import PasswordChangeView from "@/views/PasswordChangeView";
import CreateReviewView from "@/views/CreateReviewView";
import UpdateReviewView from "@/views/UpdateReviewView";
import RecommendView from "@/views/RecommendView";
import SearchMoviesView from "@/views/SearchMoviesView";
import MovieWarView from "@/views/MovieWarView";

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
  {
    path: "/createReview",
    name: "CreateReviewView",
    component: CreateReviewView,
  },
  {
    path: "/updateReview",
    name: "UpdateReviewView",
    component: UpdateReviewView,
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
    path: "/anotherprofile/:user_id",
    name: "AnotherProfile",
    component: AnotherProfile,
    props: true,
  },
  {
    path: "/login",
    name: "LogInView",
    component: LogInView,
  },
  {
    path: "/pwchange",
    name: "PasswordChangeView",
    component: PasswordChangeView,
  },
  {
    path: "/image-upload",
    name: "ImageUpload",
    component: () => import("@/components/ImageUpload.vue"),
  },
  {
    path: "/recommend",
    name: "RecommendView",
    component: RecommendView,
  },
  {
    path: "/search",
    name: "SearchMoviesView",
    component: SearchMoviesView,
  },
  {
    path: "/moviewar",
    name: "MovieWarView",
    component: MovieWarView,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
