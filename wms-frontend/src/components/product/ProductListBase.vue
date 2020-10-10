<template>
  <v-layout class="mx-6 fourthBg" style="border-radius:20px;">
    <!-- ######################################### kayan menü şeysi #########################################   -->
    <!-- <v-list
      dense
      rounded
      style="white-space: nowrap; border: 2px solid #ccc; position: sticky; top: 50px; z-index: 5;"
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
    </v-list>-->
    <!-- ######################################### kayan menü şeysi sonu #########################################   -->
    <v-card color="#eeeeee" elevation="0">
      <v-card-title class="card-title rounded-top pt-0">
        <v-row align="start">
          <v-col cols="12" class="text-right">
            <span class="mr-4" depressed @click="prodStyle()">
              <v-icon color="fifth" :class="clickedAgenda">mdi-view-agenda</v-icon>
            </span>

            <v-btn
              elevation="18"
              style="z-index: 1;"
              color="fifth"
              retain-focus-on-click
              class="white--text"
              @click="newProduct = true"
              :loading="newProduct"
            >
              <v-icon>mdi-plus</v-icon>Yeni Ürün Ekle
            </v-btn>
          </v-col>
        </v-row>
      </v-card-title>
      <v-card-text>
        <v-row>
          <ProductListItem @click="openDetails(i)" v-for="i in 19" :key="i" :say="i" :col="col" />
        </v-row>
      </v-card-text>
    </v-card>

    <!-- ######################################### DİALOG BAŞLANGICI ######################################### -->
    <v-row>
      <v-col>
        <v-dialog v-model="newProduct" persistent scrollable width="70vw">
          <v-form ref="dialogCard">
            <v-card style="border-radius:12px;" height="90vh">
              <v-card-title class="banner">
                <v-row align="center" justify="space-between" class="px-2">
                  <v-chip class="ma-2" color="white" outlined pill>
                    Yeni Ürün
                    <v-icon right>mdi-folder-outline</v-icon>
                  </v-chip>

                  <v-btn color="banner" dark class="white--text" @click="closeDialog()">
                    <v-icon>mdi-close</v-icon>Kapat
                  </v-btn>
                </v-row>
              </v-card-title>
              <v-card-text>
                <NewProd />
              </v-card-text>
              <v-card-actions class="banner">
                <v-spacer></v-spacer>
                <v-btn color="banner" dark class="white--text" @click="save()">Kaydet</v-btn>
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
        <v-dialog v-model="this.getProdDialog" persistent scrollable width="75vw">
          <v-form v-model="valid" ref="dialogCard">
            <v-card style="border-radius:12px;" height="90vh">
              <v-card-title class="myColor white--text">
                <v-row align="center" justify="space-between" class="px-2">
                  <v-chip class="ma-2" color="white" outlined pill>
                    Yeni Ürün
                    <v-icon right>mdi-folder-outline</v-icon>
                  </v-chip>

                  <v-btn color="banner" dark class="white--text" @click="closeDialog()">
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
  </v-layout>
</template>

<script>
import ProductListItem from "./ProductListItem.vue";
import Prod from "@/components/product/Prod";
import NewProd from "@/components/product/NewProd";
import { mapGetters, mapActions } from "vuex";
export default {
  name: "ProductListBase",
  components: { ProductListItem, Prod, NewProd },
  data() {
    return {
      clickedAgenda: String,
      col: 3,
      prodDialog: false,
      activeProdId: null,
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
      newProduct: false,
      waitSave: false,
      valid: false,
    };
  },
  methods: {
    ...mapActions(["setProdDialog"]),
    closeDialog() {
      this.waitSave = true;
      setTimeout(() => {
        this.waitSave = false;
        this.newProduct = false;
        this.setProdDialog(false);
      }, 1000);
    },
    openDetails(i) {
      console.log("yaraak");
      this.activeProdId = i;
      this.prodDialog = true;
    },
    prodStyle() {
      this.clickedAgenda = "custom-agenda";
      setTimeout(() => {
        this.clickedAgenda = "";
      }, 1000);
      if (this.col == 6) this.col = 2;
      else if (this.col == 2) this.col = 3;
      else if (this.col == 3) this.col = 6;
    },
  },
  computed: {
    ...mapGetters(["getAllProducts", "getActiveProdId", "getProdDialog"]),
  },
};
</script>

<style>
.card-title {
  position: sticky;
  top: 64px;
  z-index: 5;
  height: 56px;
}

.custom-agenda {
  animation: loader 1s;
  display: flex;
}
@-moz-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@-webkit-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@-o-keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
@keyframes loader {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>