<template>
  <div>
    <h1>AppChild</h1>
    <input
    type="text"
    @keyup.enter="inChildNum"
    >
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ ChildData }}</p>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  props:{
    appData: {
      type: String
    },
    parentData: {
      type: String
    },
    childData: {
      type: String
    }
  },
  methods: {
    onInputChangeData(event) {
      this.$emit('parent-input-change', event.target.value)
    }
  },
  data () {
    return {

    }
  },
}
</script>

<style>

</style>