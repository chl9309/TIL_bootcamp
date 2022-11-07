import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store',
  },
  getters: {
  },
  mutations: {
  },
  actions: {
    changeMessage(context, newMessage) {
      console.log(context)
      console.log(newMessage)
    }
  },
  modules: {
  }
})
