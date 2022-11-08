<template>
  <div id="app">
    <h3 ref="appText"> {{ text }}</h3>
    <button @click="increase">Update Data</button>
    <h3 ref="appNumber"> {{ number }}</h3>
    <hr>
    <ChildItem/>
  </div>
</template>

<script>
import ChildItem from '@components/ChildItem'

export default {
  name: 'App',
  components: {
    ChildItem
  },
  data() {
    return {
      text: '초기 데이터',
      number : 0,
      isActive: false,
    }
  },
  methods: {
    increase() {
      this.number++
    }
  },
  beforeCreate() {
    console.log('--- beforeCreate App.vue ---')
    console.log(`this.text 호출 ${ this.text }`)
    this.text = 'App.vue가 생성 된 직후입니다.'
    alert(this.text)
  },
  created() {
    console.clear() //beforeCreate에서 호출한 console 정리
    console.log('%c  --- createApp.vue ---', "color:pink")
    this.text = 'App.vue가 created 된 시점' // data 접근 가능
    console.log(this.text)

    this.increase() // method 호출도 정상 작동
    console.log(this.$refs.appText) // Dom 접근 불가능
    alert(this.text)
  },
  beforeMount() {
    // mount 되기 직전에 호출
    console.clear()
    console.log('--- beforeMount App.vue ---')
    console.log(this.$refs.appText)
  },
  mounted() {
    console.clear()
    console.log('--- mounted App.vue ---')
    console.log(this.$refs.appText) // Dom 접근 가능
    this.text = 'App.vue가 mounted 된 시점'
    alert(this.text)
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
