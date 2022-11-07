<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <input type="text"
    @keyup.enter="changeMessage"
    v-model="inputData">
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      inputData: null,
    }
  },
  components: {

  },
  computed: {
    message() {
      return this.$store.state.message
    }
  },
  methods: {
    changeMessage() {
      const newMessage = this.inputData
      this.$shote.dispatch('chageMessage', newMessage) {
        
        ontest.commit(amulatinon 메서즈 ㄱ새ㅓ')
      }
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
