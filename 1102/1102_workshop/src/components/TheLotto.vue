<template>
  <div>
    <h1>{{ lunchMenu }} 먹고 로또</h1>
    <button @click="getLuckyNumbers"> get Lucky Numbers</button>
    <p>{{ lottonums }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  props: {
    lunchMenu: String
  },
  data () {
    return {
      lottoNums: null,
    }
  },
  methods: {
    getLuckyNumbers() {
      const numbers = _.range(1, 46)
      this.lottonums = _.sampleSize(numbers, 6)
    }
  }
}
</script>

<style>

</style>