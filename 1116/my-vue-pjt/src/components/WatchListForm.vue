<template>
  <div class="watch-list-form">
    <input
    type="text"
    v-model="watchTitle"
    @keyup.enter="createWatch"
    >
    <button @click="createWatch" class="btn-11 " id="neon-text">Add</button>
  </div>
</template>

<script>
export default {
  name: 'WatchListForm',
  data: function () {
    return {
      watchTitle: null,
    }
  },
  methods: {
    createWatch: function() {
      this.$emit('create-watch', this.watchTitle)
      this.watchTitle = null
    }
  }
}
</script>

<style>
.watch-list-form{
  margin: 20px;
}

input {
  border-radius: 5px;
  width:35%;
  height: 30px;
  font-size:20px;
  border: 1px solid #b1ebff;
}


input:focus {
  outline: 2px solid #00a092;
}

.btn-11 {
  margin-left:8px;
  width: 60px;
  height: 30px;
  border: 1px solid #b1ebff;
  border-radius: 5px;
  color:#b3a7b2;
  box-shadow: 0 0 5px #efefef, 0 0 5px #ffffff inset;
  transition: all 0.3s ease;
}
.btn-11:hover{
   text-shadow:
    0 0 20px #21ebff,
    0 0 50px rgba(33, 235, 255, .9),
    0 0 75px rgba(33, 235, 255, .8),
    0 0 76px rgba(33, 235, 255, .7),
    0 0 77px rgba(33, 235, 255, .6),
    0 0 78px rgba(33, 235, 255, .5),
    0 0 79px rgba(33, 235, 255, .4),
    0 0 80px rgba(33, 235, 255, .3),
    0 0 85px rgba(33, 235, 255, .2),
     0 0 99px rgba(33, 235, 255, .1);
}


</style>