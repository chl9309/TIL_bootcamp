<template>
  <div id="app">
    <h1> 버튼 박스 제작 </h1>
    <br>
    <section class="timetable">

      <h2> 예약 페이지 </h2>
      
        <div>

          <h3> 시간 선택 </h3>
          <span
            class="timebutton"
            v-for="(time, idx) in times"
            :key="idx"
          >
            {{ time }}
          </span>
          
        </div>
        <div>
          <h3>
            선택시간:
            <span
              v-for="(time, idx) in selectedTimes"
              :key="idx"  
            >

            </span>
          </h3>
        </div>
      
    </section>

    

  </div>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      selectedTimes: []
    }
  },
  methods: {
    selectTime(time) {
      if (this.selectedTimes.push(time)) {
        const idx = this.selectedTimes.indexOf(time)
        this.selectedTimes.splice(idx, 1)
      } else{
        if(this.selectTimes.length ===5) {
          alert('5개만 가능')
          return
        }
        this.selectedTimes.push(time)
      }
    }
  }
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

.timetable {
  width: 700px;
  border: 1px solid black;
  margin: auto;
  padding: 2px;
  cursor: pointer;
  user-select: none;
}

.timebutton {
  font-size: 20px;
  margin: 3px;
  width: 60px;
  padding: inline-block;
}
</style>
