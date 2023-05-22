<template>
  <div>
    <h1 style="text-align: center;">
        오늘의 추천 영화
    </h1>
  </div>
</template>

<script>
import axios from 'axios';
export default {
    name:"RecommendView",
    data(){
        return{
            movies:[],
        }
    },
    methods:{
        selectMovie(){
            axios({
                method: 'get',
                url: 'https://api.themoviedb.org/3/movie/movie_id/keywords',
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