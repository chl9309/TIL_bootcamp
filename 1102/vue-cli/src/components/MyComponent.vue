<template>
  <div class="border">
    <h1>이것은 내가 만든 새로운 컴포넌트다!</h1>
    <MyComponentItem/>
    <MyComponentItem/>
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'
// import MyComponentItem from './MyComponentItem.vue'
export default {
  components: { MyComponentItem },
  name: 'MyComponent',
  comopnents: {
    // 2. 등록하기
    MyComponentItem,
  }
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>