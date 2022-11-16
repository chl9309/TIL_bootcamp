<template>
  <div class="movie-cards-container">
    <img 
      :src="poster_url"
      class="movie-poster"
    >
    <p class="text-title"> {{ movie_title }} </p>
    <p class="text-overviews"> {{ movie_overview }}</p>
    <!-- <p v-html="video.snippet.title"></p> -->
    <!--{{ video.snippet.title | stringUnescape }}-->
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: Object
  },
  data(){
    return{
      movie_title: this.movie.original_title,
      movie_overview: this.movie.overview
    }
  },
  computed:{
    poster_url(){
      return 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2' + this.movie.poster_path
    },
  }
}
</script>

<style>
@import url(//fonts.googleapis.com/css?family=IBM+Plex+Sans+KR);

.movie-cards-container{
  display: inline-block;
  border: 2px solid transparent;
  border-radius: 5px;
  padding: 1px;
  background-image: linear-gradient(#fff, #fff), 
  linear-gradient(to bottom, rgb(255, 255, 255) 0%,  rgb(114, 255, 213) 100%);
  box-shadow: inset 0 0 0.5em 0 rgb(255, 223, 244), 0 0 0.5em 0 rgb(13, 78, 43);
  background-origin: border-box;
  background-clip: content-box, border-box;
  margin:20px;
}

.movie-cards-container:hover{
  color:rgb(0, 110, 94);
  background-image: linear-gradient(#fff, #fff), 
  linear-gradient(to bottom, rgb(255, 217, 217) 0%,  rgb(38, 209, 169) 100%);
  filter: hue-rotate(700deg) contrast(130%) opacity(80%);
  box-shadow: 0 0 10px rgb(211, 255, 242),
              0 0 20px rgb(199, 255, 238),
              0 0 40px rgb(114, 255, 213),
              0 0 80px rgb(114, 255, 213);

}

.movie-poster{

}

.text-title{
  font: 400 2vh "IBM Plex Sans KR";
  font-weight: bolder;
  height: 30px;
  overflow : hidden;
  text-overflow : ellipsis;
  
}

.text-overviews{
  font: 400 1.5vh "IBM Plex Sans KR";
  padding-left:20px;
  padding-right: 20px;
  padding-bottom: 10px;
  height: 40px;
  overflow : hidden;
  text-overflow : ellipsis;
}

</style>