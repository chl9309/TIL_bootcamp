<template>
  <div>
    <h1> AppParent</h1>
    <input
    type="text"
    
    >

    <p>appData:</p>
    <p>childData:</p>
    
    <AppChild/>
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
  name: 'AppParent',
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