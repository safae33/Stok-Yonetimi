<template>
  <v-container class="ml-auto mr-auto" style="width:100vw;">
    <v-layout class="mt-4 fourthBg" style="border-radius:10px;">
      <v-row justify="start">
        <v-col cols="12" lg="4" xl="4">
          <v-row justify="center" align="center" class="fill-height">
            <v-card elevation="24" width="350px" color="success">
              <v-row justify="center" align="center">
                <v-btn
                  depressed
                  x-large
                  class="transparent btnText"
                  width="350px"
                  height="180px"
                  :loading="loading1"
                  @click="loading1 = !loading1"
                >
                  <v-icon large>mdi-plus</v-icon>Ürün Satış
                  <template v-slot:loader>
                    <span class="custom-loader">
                      <v-icon light x-large>mdi-cached</v-icon>
                    </span>
                  </template>
                </v-btn>
              </v-row>
            </v-card>
          </v-row>
        </v-col>
        <v-col cols="12" lg="8" xl="8">
          <v-card elevation="0" class="mr-2">
            <v-card-title
              class="fourthBg pt-0 pb-0 rounded-0 chipText elevation-4"
              style="border:0px;"
            >
              <v-row>
                <v-col cols="12">
                  <span>Aylık Gelir Bilgileri</span>
                </v-col>
                <v-col v-if="!isMobile" cols="12">
                  <v-divider></v-divider>
                </v-col>
              </v-row>
            </v-card-title>

            <v-card-text class="fourthBg elevation-4">
              <v-row justify="center">
                <v-col class="text-center" cols="12" xl="3" lg="3" md="3" sm="3">
                  <v-row>
                    <v-col align-self="center" cols="5" xl="12" lg="12" md="12" sm="12">
                      <span class="chipText mb-1 mr-2" pill>Toplam Gelir</span>
                    </v-col>
                    <v-col align-self="center" cols="7" xl="12" lg="12" md="12" sm="12">
                      <v-progress-circular
                        rotate="360"
                        size="180"
                        width="25"
                        value="40"
                        color="success"
                        class="btnText"
                      >980 ₺</v-progress-circular>
                    </v-col>
                  </v-row>
                </v-col>
                <v-col v-if="isMobile" class="text-center" cols="1">
                  <v-divider vertical></v-divider>
                </v-col>
                <v-col class="text-center" cols="12" xl="3" lg="3" md="3" sm="3">
                  <v-row>
                    <v-col align-self="center" cols="5" xl="12" lg="12" md="12" sm="12">
                      <span class="chipText mb-1 mr-2" pill>Gecikmiş Gelir</span>
                    </v-col>
                    <v-col align-self="center" cols="7" xl="12" lg="12" md="12" sm="12">
                      <v-progress-circular
                        rotate="360"
                        size="180"
                        width="25"
                        value="10"
                        color="error"
                        class="btnText"
                      >640 ₺</v-progress-circular>
                    </v-col>
                  </v-row>
                </v-col>
                <v-col v-if="isMobile" class="text-center" cols="1">
                  <v-divider vertical></v-divider>
                </v-col>
                <v-col class="text-center" cols="12" xl="3" lg="3" md="3" sm="3">
                  <v-row>
                    <v-col align-self="center" cols="5" xl="12" lg="12" md="12" sm="12">
                      <span class="chipText mb-1 mr-2" pill>Beklenen Gelir</span>
                    </v-col>
                    <v-col align-self="center" cols="7" xl="12" lg="12" md="12" sm="12">
                      <v-progress-circular
                        rotate="360"
                        size="180"
                        width="25"
                        value="86"
                        color="teal"
                        class="btnText"
                      >1.840 ₺</v-progress-circular>
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-layout>
    <v-row justify="center">
      <v-col cols="10">
        <v-divider></v-divider>
      </v-col>
    </v-row>
    <v-layout class="fourthBg" style="border-radius:10px;">
      <v-row justify="start">
        <v-col cols="12" lg="4" xl="4">
          <v-row justify="center" align="center" class="fill-height">
            <v-card elevation="24" width="350px" color="second">
              <v-row justify="center" align="center">
                <v-btn
                  depressed
                  x-large
                  class="transparent btnText"
                  width="350px"
                  height="180px"
                  :loading="loading2"
                  @click="loading2 = !loading2"
                >
                  <v-icon large>mdi-plus</v-icon>Ürün Alış
                  <template v-slot:loader>
                    <span class="custom-loader">
                      <v-icon light x-large>mdi-cached</v-icon>
                    </span>
                  </template>
                </v-btn>
              </v-row>
            </v-card>
          </v-row>
        </v-col>
        <v-col cols="12" lg="8" xl="8">
          <v-card elevation="0" class="mr-2">
            <v-card-title
              class="fourthBg pt-0 pb-0 rounded-0 chipText elevation-4"
              style="border:0px;"
            >
              <v-row>
                <v-col cols="12">
                  <span>Aylık Ödeme Bilgileri</span>
                </v-col>
                <v-col v-if="!isMobile" cols="12">
                  <v-divider></v-divider>
                </v-col>
              </v-row>
            </v-card-title>
            <v-card-text class="fourthBg elevation-4">
              <v-row justify="center">
                <v-col class="text-center" cols="12" xl="3" lg="3" md="3">
                  <v-row>
                    <v-col align-self="center" cols="5" xl="12" lg="12" md="12" sm="12">
                      <span class="chipText mb-1 mr-2" pill>Toplam Ödeme</span>
                    </v-col>
                    <v-col align-self="center" cols="7" xl="12" lg="12" md="12" sm="12">
                      <v-progress-circular
                        rotate="360"
                        size="180"
                        width="25"
                        value="90"
                        color="success"
                        class="btnText"
                      >475 ₺</v-progress-circular>
                    </v-col>
                  </v-row>
                </v-col>
                <v-col v-if="isMobile" class="text-center" cols="1">
                  <v-divider vertical></v-divider>
                </v-col>

                <v-col class="text-center" cols="12" xl="3" lg="3" md="3">
                  <v-row>
                    <v-col align-self="center" cols="5" xl="12" lg="12" md="12" sm="12">
                      <span class="chipText mb-1 mr-2" pill>Toplam Ödeme</span>
                    </v-col>
                    <v-col align-self="center" cols="7" xl="12" lg="12" md="12" sm="12">
                      <v-progress-circular
                        rotate="360"
                        size="180"
                        width="25"
                        value="62"
                        color="error"
                        class="btnText"
                      >249 ₺</v-progress-circular>
                    </v-col>
                  </v-row>
                </v-col>
                <v-col v-if="isMobile" class="text-center" cols="1">
                  <v-divider vertical></v-divider>
                </v-col>
                <v-col class="text-center" cols="12" xl="3" lg="3" md="3">
                  <v-row>
                    <v-col align-self="center" cols="5" xl="12" lg="12" md="12" sm="12">
                      <span class="chipText mb-1 mr-2" pill>Beklenen Ödeme</span>
                    </v-col>
                    <v-col align-self="center" cols="7" xl="12" lg="12" md="12" sm="12">
                      <v-progress-circular
                        rotate="360"
                        size="180"
                        width="25"
                        value="27"
                        color="teal"
                        class="btnText"
                      >3.251 ₺</v-progress-circular>
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-layout>
    <v-row justify="center">
      <v-col cols="10">
        <v-divider></v-divider>
      </v-col>
    </v-row>
    <v-layout class="fourthBg" style="border-radius:10px;">
      <v-row justify="start">
        <v-col cols="12">
          <v-card elevation="0" class="mr-2">
            <v-card-title
              class="fourthBg pt-0 pb-0 rounded-0 chipText elevation-4"
              style="border:0px;"
            >
              <v-row>
                <v-col cols="12">
                  <span>Net Durum</span>
                </v-col>
                <v-col v-if="!isMobile" cols="12">
                  <v-divider></v-divider>
                </v-col>
              </v-row>
            </v-card-title>
            <v-card-text class="fourthBg elevation-4">
              <v-row justify="center">
                <v-col class="text-center" cols="12" xl="2" lg="2" md="2">
                  <v-row>
                    <v-col align-self="center" cols="5" xl="12" lg="12" md="12" sm="12">
                      <span class="chipText mb-1 mr-2" pill>Toplam Ödeme</span>
                    </v-col>
                    <v-col align-self="center" cols="7" xl="12" lg="12" md="12" sm="12">
                      <v-progress-circular
                        rotate="360"
                        size="180"
                        width="25"
                        value="90"
                        color="success"
                        class="btnText"
                      >475 ₺</v-progress-circular>
                    </v-col>
                  </v-row>
                </v-col>
                <v-col v-if="isMobile" class="text-center" cols="1">
                  <v-divider vertical></v-divider>
                </v-col>
                <v-col class="text-center" cols="12" xl="2" lg="2" md="2">
                  <v-row>
                    <v-col align-self="center" cols="5" xl="12" lg="12" md="12" sm="12">
                      <span class="chipText mb-1 mr-2" pill>Toplam Ödeme</span>
                    </v-col>
                    <v-col align-self="center" cols="7" xl="12" lg="12" md="12" sm="12">
                      <v-progress-circular
                        rotate="360"
                        size="180"
                        width="25"
                        value="90"
                        color="success"
                        class="btnText"
                      >475 ₺</v-progress-circular>
                    </v-col>
                  </v-row>
                </v-col>
                <v-col v-if="isMobile" class="text-center" cols="1">
                  <v-divider vertical></v-divider>
                </v-col>
                <v-col class="text-center" cols="12" xl="2" lg="2" md="2">
                  <v-row>
                    <v-col align-self="center" cols="5" xl="12" lg="12" md="12" sm="12">
                      <span class="chipText mb-1 mr-2" pill>Toplam Ödeme</span>
                    </v-col>
                    <v-col align-self="center" cols="7" xl="12" lg="12" md="12" sm="12">
                      <v-progress-circular
                        rotate="360"
                        size="180"
                        width="25"
                        value="90"
                        color="success"
                        class="btnText"
                      >475 ₺</v-progress-circular>
                    </v-col>
                  </v-row>
                </v-col>
                <v-col v-if="isMobile" class="text-center" cols="1">
                  <v-divider vertical></v-divider>
                </v-col>
                <v-col class="text-center" cols="12" xl="2" lg="2" md="2">
                  <v-row>
                    <v-col align-self="center" cols="5" xl="12" lg="12" md="12" sm="12">
                      <span class="chipText mb-1 mr-2" pill>Toplam Ödeme</span>
                    </v-col>
                    <v-col align-self="center" cols="7" xl="12" lg="12" md="12" sm="12">
                      <v-progress-circular
                        rotate="360"
                        size="180"
                        width="25"
                        value="90"
                        color="success"
                        class="btnText"
                      >475 ₺</v-progress-circular>
                    </v-col>
                  </v-row>
                </v-col>

                <v-col class="text-center" cols="12" xl="2" lg="2" md="2">
                  <v-row>
                    <v-col align-self="center" cols="5" xl="12" lg="12" md="12" sm="12">
                      <span class="chipText mb-1 mr-2" pill>Toplam Ödeme</span>
                    </v-col>
                    <v-col align-self="center" cols="7" xl="12" lg="12" md="12" sm="12">
                      <v-progress-circular
                        rotate="360"
                        size="180"
                        width="25"
                        value="62"
                        color="error"
                        class="btnText"
                      >249 ₺</v-progress-circular>
                    </v-col>
                  </v-row>
                </v-col>
                <v-col v-if="isMobile" class="text-center" cols="1">
                  <v-divider vertical></v-divider>
                </v-col>
                <v-col class="text-center" cols="12" xl="2" lg="2" md="2">
                  <v-row>
                    <v-col align-self="center" cols="5" xl="12" lg="12" md="12" sm="12">
                      <span class="chipText mb-1 mr-2" pill>Beklenen Ödeme</span>
                    </v-col>
                    <v-col align-self="center" cols="7" xl="12" lg="12" md="12" sm="12">
                      <v-progress-circular
                        rotate="360"
                        size="180"
                        width="25"
                        value="27"
                        color="teal"
                        class="btnText"
                      >3.251 ₺</v-progress-circular>
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-layout>
    <v-row justify="center">
      <v-col cols="10">
        <v-divider></v-divider>
      </v-col>
    </v-row>
    <v-layout class="fourthBg" style="border-radius:10px;">
      <v-row justify="center">
        <v-col cols="12" lg="4" xl="4">
          <v-row justify="center" align="center" class="fill-height">
            <v-card elevation="24" width="350px" color="second">
              <v-row justify="center" align="center">
                <v-btn
                  depressed
                  x-large
                  class="transparent btnText"
                  width="350px"
                  height="180px"
                  :loading="loading2"
                  @click="loading2 = !loading2"
                >
                  <v-icon large>mdi-plus</v-icon>Farklı Ürün Ekleme
                  <template v-slot:loader>
                    <span class="custom-loader">
                      <v-icon light x-large>mdi-cached</v-icon>
                    </span>
                  </template>
                </v-btn>
              </v-row>
            </v-card>
          </v-row>
        </v-col>
        <v-col cols="12" xl="8" lg="8" class="fourthBg">
          <v-card class="mt-4 mr-4" elevation="0">
            <v-card-title class="fourthBg elevation-4">
              <span>Nakit Akış Tablosu</span>
            </v-card-title>
            <v-sheet class="v-sheet--offset mx-auto fourthBg" color="cyan" elevation="12">
              <v-sparkline
                :labels="labels"
                :value="value"
                color="white"
                line-width="2"
                padding="16"
              ></v-sparkline>
            </v-sheet>

            <v-card-text class="pt-10 fourthBg elevation-4">
              <div class="title font-weight-light mb-2">3 Aylık Nakit Akış Talonuz</div>
              <div
                class="subheading font-weight-light grey--text"
              >Tekrarlanan İşlemler Üzerine Oluşturuldu</div>
              <v-divider class="my-2"></v-divider>
              <v-icon class="mr-2" small>mdi-clock</v-icon>
              <span class="caption grey--text font-weight-light">son işlem 26 dk. önce</span>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: "Dashboard",
  data() {
    return {
      labels: ["12am", "3am", "6am", "9am", "12pm", "3pm", "6pm", "9pm"],
      value: [200, 675, 410, 390, 310, 460, 250, 240],
      loading1: false,
      loading2: false,
    };
  },
  methods: {},
  computed: {
    isMobile() {
      if (this.$vuetify.breakpoint.smAndUp) return true;
      else return false;
    },
  },
};
</script>

<style scoped>
.chipText {
  font-size: 1.2rem;
  color: black;
  font-family: "Poppins", sans-serif;
}
.custom-loader {
  animation: loader 1s infinite;
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