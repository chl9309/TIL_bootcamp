<template>
  <div>
    <h1>SearchBar</h1>
    <input type="text"
    v-model="searchInputData"
    @keyup.enter="searchInput">
  </div>
</template>

<script>
export default {
  name:'SearchBar',
  data: function(){
    return{
      searchInputData: null,
    }
  },
  methods: {
    searchInput() {
      this.$emit('search-input', this.searchInputData)
      this.searchInputData = ""
    }
  },
}
</script>

<style>

</style>