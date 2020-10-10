<template>

    <v-col cols="6" :xl="col" :lg="col" md="4">
      <transition name="fade">
  <v-hover style="z-index: 4;">
    <template v-slot:default="{ hover }">
      <v-card class="mx-auto" max-width="344">
        <v-img src="https://cdn.vuetifyjs.com/images/cards/forest-art.jpg"></v-img>

        <v-card-text>
          <h2 class="title primary--text">Patates {{say}}</h2>Beyaz kabuk patates{{say}}
        </v-card-text>

     

        <v-fade-transition>
          <v-overlay v-if="hover" absolute color="myColor">
            <v-btn @click="openDetails(say)">Detay için Tıklayın {{say}}</v-btn>
          </v-overlay>
        </v-fade-transition>
      </v-card>
    </template>
  </v-hover>
      </transition>
    </v-col>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: "ProductListItem",
  props:{
      say:Number,
      col:Number,
  },
  data: () => ({
    overlay: false
  }),
  methods: {
    ...mapActions(["setProdDialog", "setActiveProdId"]),
    openDetails(index) {
      this.setActiveProdId(index);
      this.setProdDialog(true)
    }
  },
  computed:{
    ...mapGetters(["getProdDialog, getActiveProdId"])
  }
};
</script>

<style>
.fade-enter-active {
  transition: opacity 0.75s;
}
.fade-leave-active {
  transition: opacity 0s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>