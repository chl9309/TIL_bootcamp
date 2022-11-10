<template>
  <div>
    <input
      type="text"
      v-on:keydown.enter="onInputKeyword"
      >
  </div>
</template>

<script>
export default {
  name:'TheSearchBar',
  methods: {
    onInputKeyword: function(event) {
      console.log(event.target.value)
      this.$emit('input-change', event.target.value)
    }
  },

}
</script>

<style>

</style>