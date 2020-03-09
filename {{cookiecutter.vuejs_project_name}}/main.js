import Vue from "vue";
import router from "./router";
import store from "./store";

import axios from "axios";
import "./scss/entry.scss";

//////////
// Load font awesome
//////////
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(fas);
library.add(far);
Vue.component("fa", FontAwesomeIcon);

//////////
// Load api url from django
//////////
// eslint-disable-next-line
let apiUrl = document.head.querySelector("meta[name=\"url\"]").content;

axios.defaults.baseURL = apiUrl;
Vue.prototype.$http = axios;

//////////
// Load git version from django
//////////
try {
  // eslint-disable-next-line
  let version = JSON.parse(document.head.querySelector("meta[name=\"version\"]").content);

  store.commit("loadVersion", version);
} catch (err) {
  // eslint-disable-next-line no-console
  console.log("Error loading version");
}

//////////
// Load example data from django view
//////////
// eslint-disable-next-line
let example = JSON.parse(document.head.querySelector("meta[name=\"example\"]").content);

store.commit("loadExample", example);


Vue.config.productionTip = false;

new Vue({
  router,
  store
}).$mount("#app");
