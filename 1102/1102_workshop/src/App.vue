<template>
  <div id="app">
    <TheLunch v-on:get-menu="getMenu" />
    <p>App: {{ lunchMenu }}</p>
    <hr>
    <TheLotto v-if="lunchMenu" :lunch-menu="lunchMenu"/>
  </div>
</template>

<script>
import TheLunch from '@/components/TheLunch'
import TheLotto from '@/components/TheLotto'

export default {
  name: 'App',
  components: {
    TheLunch,
    TheLotto,
  },
  data() {
    return {
      lunchMenu: null,
    }
  },
  methods: {
    getMenu(menu) {
      this.lunchMenu = menu
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
  margin-top: 60px;
}
</style>
