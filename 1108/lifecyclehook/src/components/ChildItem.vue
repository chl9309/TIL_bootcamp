<template>
  <div>
    <h1>{{childText}}</h1>
  </div>
</template>

<script>
export default {
  name: 'ChildItem',
  components: {
   
  },
  data( ) {
    return {
      childText: '자식 초기 데이터'
    }
  }
}
</script>

<style>

</style>