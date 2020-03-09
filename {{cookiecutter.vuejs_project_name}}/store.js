import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    version: null,
    example: ""
  },
  mutations: {
    loadVersion(state, version) {
      state.version = version;
    },
    loadExample(state, example) {
      state.example = example;
    }
  },
  actions: {},
  modules: {}
});
