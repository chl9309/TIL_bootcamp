<template>
  <div id="app">
    <header>
      <h1>My First PJT</h1>
      <TheSearchBar
        @input-change="onInputChange"
      />
    </header>
    
    <section>
      <VideoList
        :videos="videos"
      />

    </section>
  </div>
</template>

<script>
import TheSearchBar from '@/components/TheSearchBar'
import VideoList from '@/components/VideoList'
import axios from 'axios'
const API_KEY = process.env.VUE_APP_API_KEY

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList
  },
  data() {
    return {
      inputValue: null,
      vidos: []
    }
  },
  methods: {
    onInputChange(inputText) {
        this.inputValue = inputText
        console.log(inputText)

      const params= {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue,
      }

      axios({
        method:'GET',
        url: 'https://www.googleapis.com/youtube/v3/search',
        params
        // params= {
        // key: API_KEY,
        // part: 'snippet;',
        // type: 'video',
        // q: this.inputValue
        // params: params
      })
      .then(res => console.log(res))
      .catch(err => console.log(err))
    }
  },
  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
