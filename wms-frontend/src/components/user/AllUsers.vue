<template>
  <v-container>
    <v-card elevation="12">
      <v-card-title class="mb-0 pb-0">
        <v-row justify="space-between">
          <v-col cols="12">
            <Banner />
          </v-col>
          <v-col cols="11">
            <v-text-field
              dense
              dark
              v-model="search"
              append-icon="mdi-magnify"
              label="Arama"
              outlined
              hide-details
            ></v-text-field>
          </v-col>
          <v-col cols="1">
            <v-btn
              elevation="18"
              style="z-index: 1;"
              class="banner"
              dark
              outlined
              @click="firmDialog = true"
              :loading="firmDialog"
            >
              <v-icon>mdi-plus</v-icon>Yeni Kayıt
            </v-btn>
          </v-col>
        </v-row>
      </v-card-title>

      <v-card-text class="mt-6 pr-0 pl-0">
        <v-row justify="center" align="center">
          <v-col cols="12">
            <v-data-table
              class="mr-0 ml-0 pl-0 pr-0"
              fixed-header
              height="60vh"
              :headers="headers"
              :sort-by="[]"
              :sort-desc="[]"
              :search="search"
              multi-sort
            >
              <!-- <template #item.index="{item}">
                <v-chip color="myColor" dark>{{ item.index }}</v-chip>
              </template>

              <template #item.actions="{item}">
                <v-icon @click="delete_us(item.id)" color="black">mdi-delete</v-icon>
              </template> -->
            </v-data-table>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

        <!-- ######################################### DİALOG BAŞLANGICI ######################################### -->
    <v-row>
      <v-col >
        <v-dialog v-model="firmDialog" persistent scrollable width="80vw" >
          <v-form v-model="valid" ref="dialogCard">
            <v-card style="border-radius:12px;" height="90vh">
              <v-card-title class="white--text" style="background-color: rgb(43,43,43)">
                <v-row align="center" justify="space-between" class="px-2">
                  <v-chip class="ma-2" color="white" outlined pill>
                    Firma
                    <v-icon right>mdi-home</v-icon>
                  </v-chip>

                  <v-btn color="banner" dark class="white--text" @click="firmDialog = false">
                    <v-icon>mdi-close</v-icon>Kapat
                  </v-btn>
                </v-row>
              </v-card-title>
              <v-card-text>
                <User />
          
              </v-card-text>
              <v-card-actions style="background-color: rgb(43,43,43)">
                <v-spacer></v-spacer>
                <v-btn
                  color="banner"
                  :disabled="!valid"
                  dark
                  class="white--text"
                 
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
  </v-container>
</template>

<script>
import User from "@/components/user/User"
import Banner from "@/components/layout/Banner";
export default {
  name: "AllUsers",
  components: {
    User,
    Banner,
  },
  data() {
    return {
        firmDialog: false,
        valid: false,
      search: "",
      newUserDialog: false,
      headers: [
        {
          text: "Sıra",
          align: "start",
          sortable: false,
          value: "index",
        },
        { text: "Ürün  ", value: "product" },
        { text: "Adet", value: "quantity" },
        { text: "Firma İsmi", value: "firm" },
        { text: "İşlem Tarihi", value: "transactionDate" },
        { text: "Eylemler", value: "actions", sortable: false },
      ],
    };
  },
  methods: {},
};
</script>

<style>
</style>