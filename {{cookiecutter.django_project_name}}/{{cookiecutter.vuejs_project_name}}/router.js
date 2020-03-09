import Vue from "vue";
import VueRouter from "vue-router";

import ExampleView from "@views/ExampleView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "example-view",
    component: ExampleView
  }
];

const router = new VueRouter({
  // mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
