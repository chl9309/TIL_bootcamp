<template>
  <div>
    <div class="movie-contents">
    <div 
      v-for="(movie,id) in movies"
      :key="id"
      >
      <MovieCard
        :movie="movie"
      />
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/components/MovieCard.vue'

const API_KEY = process.env.VUE_APP_API_KEY

export default {
  name:'MovieView',
  components:{
    MovieCard,
  },
  data() {
    return {
      movies : []
    }
  },
  methods: {
    get_top_reated_movies() {
      const params = {
        api_key: API_KEY,
        language: 'ko-KR',
        page: 1,
      }
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/movie/top_rated',
        params
      })
      .then(res => {
        console.log(res)
        this.movies = res.data.results
      })
      .catch(err => console.log(err))
      },
  },
  created(){
    this.get_top_reated_movies()
  }
}
//https://api.themoviedb.org/3/movie/top_rated?api_key=2a5c5c8d29f6223b7278c7de5b7116b1&language=ko-KR&page=1
</script>

<style>
.movie-contents{
  width:80%;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  justify-content: center;
  padding:10px;
  margin: auto;

}
</style>
 