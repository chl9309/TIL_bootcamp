<template>
  <div id="app">
    <SearchBar
      @search-input="getSearchData"
    />
    <VideoDetail/>
    <VideoList/>
    <router-view/>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
import VideoDetail from '@/components/VideoDetail'
import VideoList from '@/components/VideoList'

export default {
  name: 'VideoList',
  components: {
    SearchBar,
    VideoDetail,
    VideoList,
  },
  methods: {
    getSearchData: function(InputData) {
      console.log(`${InputData}`)
    }
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
