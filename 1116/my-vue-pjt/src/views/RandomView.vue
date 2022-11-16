<template>
  <div>
    <div class="weather-guide">
       <p>    {{ weather }} 한 날씨에는 이런 영화는 어떠세요? </p>
    </div>
    <div class="movie-card-container">
      <img 
        :src="poster_url"
        class="movie-poster"
      >
      <p class="text-title"> {{ movie_title }} </p>
      <p class="text-overview"> {{ movie_overview }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

const API_KEY = process.env.VUE_APP_API_KEY
const WEATEHR_API_KEY = process.env.VUE_APP_WEATHER_API_KEY

const clouds_movies = [10749,10752,37]
const rain_movies = [80,18,14]
const clear_movies = [28,12,16,35]
const idx_list = []


export default {
  name:'RandomView',
  data() {
    return {
      weather:null,
      movie : null,
      movie_title: null,
      movie_overview: null,
      poster_url: null,
    }
  },
  computed:{
  },
  methods:{
   get_weather_api(){
     const parameters = {
        q:'Busan',
        appid: WEATEHR_API_KEY,
      }
      axios({
        method: 'get',
        url: `https://api.openweathermap.org/data/2.5/weather?q=${parameters.q}&appid=${parameters.appid}`,
        parameters
      })
      .then(res => {
        this.weather = res.data.weather[0].main
      })
      .catch(err => console.log(err))
    },
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
        if(this.weather === 'Clouds'){
          for(let i=0;i<20;i++){
            const now_movie_gernes = res.data.results[i].genre_ids
            if(now_movie_gernes.filter(x=> clouds_movies.includes(x)) !== []){
              idx_list.push(i)
            }
          }
          this.movie = res.data.results[idx_list[_.random(0,idx_list.length)]]

        }
        else if(this.weather === 'Rain'){
          for(let i=0;i<20;i++){
            const now_movie_gernes = res.data.results[i].genre_ids
          
            if(now_movie_gernes.filter(x=> rain_movies.includes(x)) !== []){
              idx_list.push(i)
            }
          }
          this.movie = res.data.results[idx_list[_.random(0,idx_list.length)]]
        }
        else if(this.weather === 'Clear'){
          for(let i=0;i<20;i++){
            const now_movie_gernes = res.data.results[i].genre_ids
            if(now_movie_gernes.filter(x=> clear_movies.includes(x)) !== []){
              idx_list.push(i)
            }
          }
          this.movie = res.data.results[idx_list[_.random(0,idx_list.length)]]
        }
        else{
          this.movie = res.data.results[_.random(0,19)]
        }
        this.movie_title = this.movie.original_title
        this.movie_overview = this.movie.overview
        this.poster_url = 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2' + this.movie.poster_path     
      })
      
      .catch(err => console.log(err))
    },

  },
  created(){
      this.get_weather_api()
  },
  watch: {
    weather() {
      this.get_top_reated_movies()
    }
  }
  
}
</script>

<style>
@import url(//fonts.googleapis.com/css?family=IBM+Plex+Sans+KR);

.weather-guide{
  color: #fff;
  font: 400 2vh "IBM Plex Sans KR";
}

.movie-card-container{
  display: inline-block;
  width:400px;
  border: 2px solid transparent;
  border-radius: 5px;
  padding: 1px;
  background-image: linear-gradient(#fff, #fff), 
  linear-gradient(to bottom, rgb(171, 153, 158) 0%,  rgb(54, 101, 79) 100%);
  box-shadow: inset 0 0 0.5em 0 rgb(232, 255, 243), 0 0 0.5em 0 rgb(173, 255, 195);
  background-origin: border-box;
  background-clip: content-box, border-box;
  margin:20px;

}

.movie-poster{
  width:100%;
}

.text-title{
  font: 400 2vh "IBM Plex Sans KR";
  font-weight: bolder;
}

.text-overview{
  font: 400 1.5vh "IBM Plex Sans KR";
  padding-left:20px;
  padding-right: 20px;
  padding-bottom: 10px;
}

</style>