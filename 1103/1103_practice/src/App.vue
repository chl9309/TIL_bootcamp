<template>
  <div id="app">
    <h1> App </h1>
    <input
    type="text"
    v-model="appData"
    @input="onInputChangeData"
    >

    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    
    <AppParent
      :app-data="appData"
      :parent-data="parentData"
    />
  </div>
</template>

<script>
import AppParent from '@/components/AppParent'

export default {
  name: 'App',
  data() {
    return {
      appData: null,
      parentData: null,
      childData: null,
    }
  },
  components: {
    AppParent,
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
