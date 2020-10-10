<template>
  <v-container>
    <v-row>
      <v-col cols="12" lg="6" xl="6">
        <v-row>
          <v-col cols="12">
            <v-row justify="center" align="center">
              <v-img
                :src="newProd.mainUrl"
                max-height="250"
                max-width="400"
                lazy-src="@/assets/placeholder.jpg"
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
            <v-text-field outlined  label="Ürün Kodu*" persistent-hint hint="Belirtilmezse otomatik oluşturulacaktır." v-model="newProd.code" type="email" required dense></v-text-field>
            <v-text-field outlined label="Ürün İsmi" v-model="newProd.name" type="email" required dense></v-text-field>
            <v-text-field dense label="Ürün Kategorisi" v-model="newProd.cat"></v-text-field>
          </v-col>
          <v-col cols="12" align-self="end">
            <v-row justify="end">
              <v-btn color="banner" dark class="white--text">
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
        <v-spacer />
        <v-dialog v-model="newDialog" max-width="500px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="banner"
              dark
              class="white--text"
              v-bind="attrs"
              v-on="on"
              :loading="newDialog"
            ><v-icon>mdi-plus</v-icon>Ekle</v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">Yeni Özellik</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" xl="4" lg="4" md="4">
                      <v-select :items="['Renk', 'Uzunluk', 'Kilo', 'yarak', 'kürek']" v-model="newSpec.name" label="Özellik İsmi"></v-select>
                  </v-col>
                  
                  <v-col cols="12" xl="4" lg="4" md="4">
                      <v-select :items="['20', '30', '40', '50', '90', 'Kırmızı']" v-model="newSpec.value" label="Özellik Değeri"></v-select>
                  </v-col>
                  <v-col cols="12" xl="4" lg="4" md="4">
                      <v-select :items="['Metre', 'Adet', 'Kg', 'Lt', 'kürek', 'Sıfat']" v-model="newSpec.unit" label="Özellik Birimi"></v-select>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="banner" text @click="closeNewSpec()">İptal</v-btn>
              <v-btn color="banner" text @click="saveNewSpec()">Kaydet</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        
      </v-card-title>
      <v-card-text class="mt-0 pt-0">
        <v-data-table
          fixed-header
          height="50vh"
          :items="newProd.specs"
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

export default {
  name: "NewProd",
  methods:{
      closeNewSpec() {
          this.newDialog = false;
          this.resetNewSpec();
      },
      saveNewSpec(){
          this.newProd.specs.push({...this.newSpec});
          this.resetNewSpec();
          this.newDialog = false;
      },
      resetNewSpec(){
          this.newSpec.name = "";
          this.newSpec.unit = "";
          this.newSpec.value = "";
      }

  },
  data: () => ({
    newDialog: false,
    dialog2: false,
    waitSave: false,
    newSpec:{
        name: "",
        unit: "",
        value: "",
    },
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
    headers: [

      { text: "Özellik İsmi", value: "name" },
      { text: "Özellik Değeri", value: "value" },
      { text: "Özellik Birimi", value: "unit" },
    ],
    newProd: {
        code: "",
        name: "",
        cat: "",
        mainUrl: "https://wolper.com.au/wp-content/uploads/2017/10/image-placeholder.jpg",
        specs: [
            
        ]
    },
    items: [
        {src: "https://wolper.com.au/wp-content/uploads/2017/10/image-placeholder.jpg"}
    ]
  }),
  computed: {
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