<template>
  <v-container>
    <v-card elevation="12">
      
      <Banner />
      <v-card-title class="pb-0 mb-0">
        <v-text-field
          dense
          dark
          v-model="search"
          append-icon="mdi-magnify"
          label="Arama"
          single-line
          outlined
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-row class="data-row d-inline">
        <v-col class="data-col" cols="12">
          <v-data-table

            fixed-header
            height="60vh"
            :headers="headers"
            :items="this.getApplyArr"
            :sort-by="[]"
            :sort-desc="[]"
            :search="search"
            multi-sort
            class="elevation-18"
            @click:row="handleClick"
          >
            
          </v-data-table>
        </v-col>
      </v-row>
    </v-card>
    
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import Banner from "@/components/layout/Banner";
export default {
  name: "Dashboard",
  components: {
    Banner,
  },
  data() {
    return {
      st:1,
      dialog: false,
      headers: [
        {
          text: "Sıra",
          align: "start",
          sortable: false,
          value: "index"
        },
        { text: "Yetkili Ad-Soyad", value: "authNameSurname" },
        { text: "Yetkili Tel No", value: "authTelNo" },
        { text: "Yetkili Tc No", value: "authTc" },
        { text: "Onay Durumu", value: "isApproved" },
        { text: "Durum", value: "state" }
      ],
      search: "",
      title: "Tüm Başvurular",
      valid: false,
      rules: {
        general: [
          value => !!value || "Gerekli Alan.",
          value => (value && value.length >= 3) || "En az 3 Karakter."
        ],
        address: [
          value => !!value || "Gerekli Alan.",
          value => (value && value.length >= 3) || "En az 3 Karakter.",
          value => (value && value.length <= 250) || "En Fazla 250 Karakter."
        ],
        type: [val => (val || "").length > 0 || "Gerekli Alan."],
        vergi: [
          value =>
            (value && value.length == 10) || "Vergi No 10 karakter olmalı."
        ],
        telNo: [
          value => (value && value.length == 10) || "Tel No 10 karakter olmalı."
        ],
        email: [
          v =>
            !v ||
            /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
            "E-Posta uygun olmalı."
        ]
      },
      types: ["Müşteri", "Yönetici"],
      clickedApply: "",
      
    };
  },

  computed: {
    ...mapGetters(["getApplyArr", "getDataHere", "getIsAdmin"])
  },
  methods: {
    ...mapActions(["setApplyListApi"]),
    isApprovedColor(check) {
      if (check) return "success";
      else return "grey";
    },
    stateColor(item) {
      if (item.isNew) return "success";
      else {
        if (item.isEnd) return "grey";
        else return "headerColor";
      }
    },
    stateText(item) {
      if (item.isNew) return "YENİ";
      else {
        if (item.isEnd) return "Tamamlanmış.";
        else return "Aktif Durumda";
      }
    },
    handleClick(value) {
      this.clickedApply = value;
      this.dialog = true;
    },
    changee1(i){
      this.st = i;
    }
  },
  mounted() {
    this.setApplyListApi();
  }
};
</script>

<style >
.top-col {
  position: fixed;
  height: 30vh;
  border-radius: 10px;
}

.data-col {
  position: relative;
}

.v-icon {
  color: black;
}
</style>