<template>
  <v-container>
    <v-card elevation="12">
      <v-row>
        <v-col cols="12" class="text-left">
          <v-btn
            elevation="18"
            style="z-index: 1;"
            class="white--text"
            outlined
            @click="dialog = true"
            :loading="dialog"
          >
            <v-icon>mdi-plus</v-icon>ürün
          </v-btn>
        </v-col>
        <v-col cols="12" class="text-left">
          <v-btn
            elevation="18"
            style="z-index: 1;"
            class="white--text"
            outlined
            @click="dialogUser = true"
            :loading="dialogUser"
          >
            <v-icon>mdi-plus</v-icon>user
          </v-btn>
        </v-col>
      </v-row>
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
            mobile-breakpoint="1600"
            fixed-header
            height="50vh"
            :headers="headers1"
            :items="this.getAllUsers"
            :sort-by="[]"
            :sort-desc="[]"
            :search="search"
            multi-sort
          >
           
          </v-data-table>
        </v-col>
      </v-row>
    </v-card>

    <!-- ######################################### DİALOG BAŞLANGICI ######################################### -->
    <v-row>
      <v-col >
        <v-dialog v-model="dialog" persistent scrollable width="75vw" >
          <v-form v-model="valid" ref="dialogCard">
            <v-card style="border-radius:12px;" height="90vh">
              <v-card-title class="myColor white--text">
                <v-row align="center" justify="space-between" class="px-2">
                  <v-chip class="ma-2" color="white" outlined pill>
                    Yeni Ürün
                    <v-icon right>mdi-folder-outline</v-icon>
                  </v-chip>

                  <v-btn color="banner" class="white--text" @click="closeDialog()">
                    <v-icon>mdi-close</v-icon>Kapat
                  </v-btn>
                </v-row>
              </v-card-title>
              <v-card-text>
                <Prod />
          
              </v-card-text>
              <v-card-actions style="background-color: #363062">
                <v-spacer></v-spacer>
                <v-btn
                  color="banner"
                  :disabled="!valid"
                  dark
                  class="white--text"
                  @click="save()"
                >Kaydet</v-btn>
              </v-card-actions>
            </v-card>
          </v-form>
          <v-fade-transition>
            <v-overlay v-if="waitSave" z-index="9999">
              <v-progress-circular indeterminate size="64"></v-progress-circular>
            </v-overlay>
          </v-fade-transition>
        </v-dialog>
      </v-col>
    </v-row>

    <!-- ######################################### DİALOG SONU ######################################### -->

    <!-- ######################################### DİALOG USER BAŞLANGICI ######################################### -->
    <v-row>
      <v-col >
        <v-dialog v-model="dialogUser" persistent scrollable width="75vw" >
          <v-form v-model="valid" ref="dialogCard">
            <v-card style="border-radius:12px;" height="90vh">
              <v-card-title class="myColor white--text">
                <v-row align="center" justify="space-between" class="px-2">
                  <v-chip class="ma-2" color="white" outlined pill>
                    Yeni User
                    <v-icon right>mdi-folder-outline</v-icon>
                  </v-chip>

                  <v-btn color="banner" class="white--text" @click="dialogUser = false;">
                    <v-icon>mdi-close</v-icon>Kapat
                  </v-btn>
                </v-row>
              </v-card-title>
              <v-card-text>
                <User />
          
              </v-card-text>
              <v-card-actions style="background-color: #363062">
                <v-spacer></v-spacer>
                <v-btn
                  color="banner"
                  :disabled="!valid"
                  dark
                  class="white--text"
                  @click="save()"
                >Kaydet</v-btn>
              </v-card-actions>
            </v-card>
          </v-form>
          <v-fade-transition>
            <v-overlay v-if="waitSave" z-index="9999">
              <v-progress-circular indeterminate size="64"></v-progress-circular>
            </v-overlay>
          </v-fade-transition>
        </v-dialog>
      </v-col>
    </v-row>

    <!-- ######################################### DİALOG SONU ######################################### -->

    <!-- ######################################### DİALOG BAŞLANGICI ######################################### -->
    <v-row>
      <v-col>
        <v-dialog v-model="dialog2"  scrollable width="75vw" class="mb-10">
          <v-form v-model="valid" ref="dialogCard">
            <v-row>
              <ProductListItem v-for="i in [1,2,3,4,5,6,7,8,9]" :key="i" :say="i" />
            </v-row>
          </v-form>
          <v-fade-transition>
            <v-overlay v-if="waitSave" z-index="9999">
              <v-progress-circular indeterminate size="64"></v-progress-circular>
            </v-overlay>
          </v-fade-transition>
        </v-dialog>
      </v-col>
    </v-row>

    <!-- ######################################### DİALOG SONU #########################################   -->

    <v-snackbar
      v-model="snackSuccess"
      :timeout="snackTimeout"
      color="success"
      class="white--text"
    >Kullanıcı Başarıyla Eklendi!</v-snackbar>
    <v-snackbar
      v-model="snackError"
      :timeout="snackTimeout"
      color="error"
      class="white--text"
    >Kullanıcı Başarıyla Silindi!</v-snackbar>

<!-- ######################################### kayan menü şeysi #########################################   -->
    <v-list
      dense
      rounded
      style="white-space: nowrap; border: 2px solid #ccc; position: sticky; top: 0px"
      class="overflow-y-auto d-flex"
      max-height="120px"
    >
      <v-list-item-group color="black" active-class="exactItem v-ripple__animation--enter">
        <template v-for="item in liste">
          <v-list-item
            :key="item"
            exact
            dense
            class="d-inline-flex mr-2"
            style="border: 2px solid #ccc"
          >
            <v-list-item-avatar>
              <v-img src="https://cdn.vuetifyjs.com/images/lists/1.jpg"></v-img>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title>{{item}}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list-item-group>
    </v-list>

    
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import Banner from "@/components/layout/Banner";
import ProductListItem from "@/components/product/ProductListItem";
import Prod from "@/components/product/Prod";
import User from "@/components/user/User";
export default {
  name: "Dashboard",
  components: {
    Banner,
    ProductListItem,
    Prod,
    User,
  },
  data() {
    return {
      liste: [
        "ali",
        "veri",
        "49",
        "50",
        "yarak",
        "kürek",
        "asdasd",
        "qweqweqw",
        "kahvaltılıklardan",
      ],
      dialog2: false,
      dialogUser: false,
      snackTimeout: 3500,
      snackSuccess: false,
      snackError: false,
      waitSave: false,
      headers1: [
        {
          text: "Sıra",
          align: "start",
          sortable: false,
          value: "index",
        },
        { text: "İsim", value: "companyName" },
        { text: "Adres", value: "companyAddress" },
        { text: "E-Posta", value: "mail" },
        { text: "Vergi Numarası", value: "taxNo" },
        { text: "Tel No", value: "telNo" },
        { text: "Eylemler", value: "actions", sortable: false },
      ],
      desserts: [
        {
          name: "Frozen Yogurt",
          calories: 200,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: "1%",
        },
        {
          name: "Ice cream sandwich",
          calories: 200,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: "1%",
        },
        {
          name: "Eclair",
          calories: 300,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: "7%",
        },
        {
          name: "Cupcake",
          calories: 300,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          iron: "8%",
        },
        {
          name: "Gingerbread",
          calories: 400,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          iron: "16%",
        },
        {
          name: "Jelly bean",
          calories: 400,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          iron: "0%",
        },
        {
          name: "Lollipop",
          calories: 400,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          iron: "2%",
        },
        {
          name: "Honeycomb",
          calories: 400,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          iron: "45%",
        },
        {
          name: "Donut",
          calories: 500,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
          iron: "22%",
        },
        {
          name: "KitKat",
          calories: 500,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          iron: "6%",
        },
      ],
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
      user: {
        companyName: "",
        companyAddress: "",
        mail: "",
        passwd: "",
        taxNo: "",
        telNo: "",
        isAdmin: "",
      },
    };
  },
  computed: {
    ...mapGetters(["getApplyArr", "getAllUsers"]),
    getDiaWidth() {
      if (this.$vuetify.breakpoint.lgAndUp) return true;
      else return false;
    },
  },
  methods: {
    ...mapActions(["setApplyListApi", "get_users", "save_user", "delete_user"]),
    getColor(id) {
      if (id <= 3) return "red";
      else if (id <= 6) return "orange";
      else return "green";
    },
    closeDialog() {
      this.dialog = !this.dialog;
      this.$refs.dialogCard.reset();
    },
    save() {
      if (this.valid) {
        this.waitSave = true;
        this.save_user(this.user).then(() => {
          this.waitSave = false;
          this.get_users();
          this.closeDialog();
        });
      }
      this.snackSuccess = true;
    },
    delete_us(id) {
      this.waitSave = true;
      this.delete_user(id).then(() => {
        this.waitSave = false;
        this.get_users();
      });
      this.snackError = true;
    },
  },
  mounted() {},
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