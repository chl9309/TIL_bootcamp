<template>
  <div>
    <h1> AppParent</h1>
    <input
    type="text"
    :value="parentdata"
    >

    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    
    <AppChild/>
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
  name: 'AppParent',
  props:{
    appData: {
      type: String
    },
    parentData: {
      type: String
    },
  },
  methods: {
    onInputChangeData(event) {
      this.$emit('parent-input-change', event.target.value)
    },
    onInputChildData(event) {
      this.$emit('parent-input-change', event.target.value)
    }
  },
  data () {
    return {
     
    }
  },
  components: {
    AppChild,
  }
}
</script>

<style>

</style>