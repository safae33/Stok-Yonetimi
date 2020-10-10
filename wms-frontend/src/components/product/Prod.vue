<template>
  <v-container>
    <v-row>
      <v-col cols="12" lg="6" xl="6">
        <v-row>
          <v-col cols="12">
            <v-row justify="center" align="center">
              <v-img
                :src="this.getAllProducts[this.getActiveProdId].mainUrl"
                max-height="250"
                max-width="400"
              />
            </v-row>
          </v-col>

          <v-col cols="12" class="px-10">
            <v-carousel height="170" hide-delimiter-background>
              <v-carousel-item v-for="(item,i) in items" :key="i" :src="item.src"></v-carousel-item>
            </v-carousel>
          </v-col>
        </v-row>
      </v-col>

      <v-col cols="12" lg="6" xl="6">
        <v-row align="start" justify="end" class="fill-height">
          <v-col cols="12">
            <v-text-field outlined readonly label="Ürün Kodu*" v-model="this.getAllProducts[this.getActiveProdId].code" type="email" required dense></v-text-field>
            <v-text-field :readonly="!isForNew" outlined label="Ürün İsmi" v-model="this.getAllProducts[this.getActiveProdId].name" type="email" required dense></v-text-field>
            <v-text-field :readonly="!isForNew" dense label="Ürün Kategorisi" v-model="this.getAllProducts[this.getActiveProdId].cat"></v-text-field>
          </v-col>
          <v-col cols="12" align-self="end">
            <v-row justify="end">
              <v-btn color="banner" class="white--text">
                Stok Durumuna Git
                <v-icon class="pl-2">mdi-arrow-right-bold</v-icon>
              </v-btn>
            </v-row>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <v-divider />

    <v-card elevation="6" style="border-radius:12px;">
      <v-card-title class="mb-0 pb-0">
        <v-text-field dense v-model="search" append-icon="mdi-magnify" label="Arama"  outlined></v-text-field>
      </v-card-title>
      <v-card-text class="mt-0 pt-0">
        <v-data-table
          fixed-header
          height="50vh"
          :headers="headers"
          :sort-by="[]"
          :sort-desc="[]"
          :search="search"
          multi-sort
        />
      </v-card-text>
    </v-card>

  </v-container>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
  name: "Prod",
  props:{
    isForNew:Boolean
  },
  data: () => ({
    dialog2: false,
    waitSave: false,

    search: "",
    title: "Tüm Kullanıcılar",
    dialog: false,
    valid: false,
    rules: {
      general: [
        (value) => !!value || "Gerekli Alan.",
        (value) => (value && value.length >= 3) || "En az 3 Karakter.",
      ],
      address: [
        (value) => !!value || "Gerekli Alan.",
        (value) => (value && value.length >= 3) || "En az 3 Karakter.",
        (value) => (value && value.length <= 250) || "En Fazla 250 Karakter.",
      ],
      type: [(v) => !!v || "Gerekli Alan."],
      vergi: [
        (value) =>
          (value && value.length == 10) || "Vergi No 10 karakter olmalı.",
      ],
      telNo: [
        (value) =>
          (value && value.length == 10) || "Tel No 10 karakter olmalı.",
      ],
      email: [
        (v) =>
          !v ||
          /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
          "E-Posta uygun olmalı.",
      ],
    },
    types: [
      { text: "Müşteri", value: "false" },
      { text: "Yönetici", value: true },
    ],
    headers: [
      {
        text: "Sıra",
        align: "start",
        sortable: false,
        value: "index",
      },
      { text: "Özellik İsmi", value: "specName" },
      { text: "Özellik Değeri", value: "specValue" },
      { text: "Özellik Birimi", value: "specUnit" },
    ],
    items: [
      {
        src: "https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg",
      },
      {
        src: "https://cdn.vuetifyjs.com/images/carousel/sky.jpg",
      },
      {
        src: "https://cdn.vuetifyjs.com/images/carousel/bird.jpg",
      },
      {
        src: "https://cdn.vuetifyjs.com/images/carousel/planet.jpg",
      },
    ],
  }),
  computed: {
    ...mapGetters(['getAllProducts', 'getActiveProdId'])
  }
};
</script>

<style scoped>
.left {
  background-color: rgba(0, 0, 255, 0.096);
}
.right {
  background-color: rgba(255, 0, 0, 0.226);
}
</style>