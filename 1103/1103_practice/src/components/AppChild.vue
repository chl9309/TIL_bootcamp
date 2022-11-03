<template>
  <div>
    <h1>AppChild</h1>
    <input
    type="text"
    @keyup.enter="inChildNum"
    >
    <p>appData:</p>
    <p>parentData:</p>
    <p>childData:</p>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  data () {
    return {

    }
  },
  methods: {
    inChildNum: function () {
      
    }
  }
}
</script>

<style>

</style>