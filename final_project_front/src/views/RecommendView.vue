<template>
  <div>
    <header>
        <h1 style="text-align: center; margin-top: 2rem; color: rgba(43, 137, 224, 88); text-decoration-color: rgba(43, 137, 224, 88); text-decoration-line: underline; text-decoration-style: double;">
            오늘의 추천 영화
        </h1>
    </header>
    <section class="text-center m-5">
        <form @submit.prevent="selectMovie">
            <label for="keyword_input"><h3>키워드를 입력하세요 : </h3> </label>
            <input type="text" id="keyword_input" v-model="keyword_input">
        </form>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
export default {
    name:"RecommendView",
    data(){
        return{
            movies:[],
            keyword_input:'',
        }
    },
    methods:{
        selectMovie(){
            axios({
                method: 'get',
                url: 'https://api.themoviedb.org/3/movie/411/keywords&language=ko',
                headers: {
 accept: 'application/json',
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjY2U2MGE4NzRmY2Q0ZWFhYTg3N2NkYzUyMTFjMWQzYyIsInN1YiI6IjYzZDMyNWQ2MDMxYTFkMDA4M2EwOWJjYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.5CmcI77Vn7YcxR3V814PZLoC9jyIJxeAuTp-8UYKx8c'
  }
            })
            .then((res)=>{
                console.log(res)
            })
            .catch(err=>console.log(err))

        }

    },
    mounted(){
        this.movies = this.$store.state.movies;
    }
}
</script>

<style>

</style>