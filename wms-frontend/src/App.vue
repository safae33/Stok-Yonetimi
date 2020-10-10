<template>
  <router-view></router-view>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "App",

  components: {},

  data: () => ({}),
});
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap");

.banner {
  background: #4398d5;
}

.transparent {
  background-color: #ffffff;
  opacity: 0.8;
}
.thirdBg {
  background-color: #cfd8dc;
}
.fourthBg {
  background-color: #e0f7fa;
}

.submenuBg {
  background: #737373;
}

.btnText {
  font-size: 1.6rem;
  color: white;
  font-family: "Poppins", sans-serif;
}
.sizeUp {
  font-size: 1.9rem;
}
</style>
