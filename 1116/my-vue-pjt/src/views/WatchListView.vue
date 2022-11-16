<template>
  <div class="watch-list-div">
    <h1>Search Movie</h1>
    <WatchListForm @create-watch="createWatch"/>
    <WatchListItem @complete-watch="completeWatch" v-for="(watch, index) in watchs" :key="index" :watch="watch"/>
  </div>
</template>

<script>
import WatchListItem from '@/components/WatchListItem'
import WatchListForm from '@/components/WatchListForm'

export default {
  name: 'WatchListView',
  components: {
    WatchListItem,
    WatchListForm,
  },
  data: function () {
    return {
      watchs: [],
    }
  },
  methods: {
    createWatch: function (watchTitle) {
      const watch = {
        title: watchTitle
      }
      this.watchs.push(watch)
      console.log(watch)
    },
    completeWatch: function () {
      
    }
  },
}
</script>

<style>
@import url(//fonts.googleapis.com/css?family=IBM+Plex+Sans+KR);
.watch-list-div{
  font: 400 1.5vh "IBM Plex Sans KR";
  color: rgb(207, 217, 214);
}
</style>
