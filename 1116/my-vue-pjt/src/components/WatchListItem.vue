<template>
  <div class="list-container">
    <div @click="completeWatch" class=" watch-list ">
      <div class=" del-movie ">
        <del v-if="comp1"> {{ watch.title }} </del>
      </div>
      <div>
        <a v-if="comp2"> {{ watch.title }} </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WatchList',
  props: {
    watch: Object,
  
  },
  data: function () {
    return{
      comp1: false,
      comp2: true
    }
  },
  methods: {
    completeWatch: function () {
      this.$emit('complete-watch', this.watch)
      
      if (this.comp1) {
        this.comp1 = false
        this.comp2 = true
      } else {
        this.comp1 = true
        this.comp2 = false
      }
    }
  }
}
</script>

<style>
@import url(//fonts.googleapis.com/css?family=IBM+Plex+Sans+KR);

.watch-list{
  font: 400 2vh "IBM Plex Sans KR";
}
.del-movie {
  width: 100%;
  background-color:rgba(212, 212, 212, 0.471);
  color: rgb(173, 173, 173);
}
</style>