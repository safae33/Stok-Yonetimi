<template>
  <v-container
    class="mx-lg-6 mx-xl-6 px-lg-4 px-xl-4 mx-md-6 px-md-6 mt-10 fourthBg"
    style="border-radius:10px;"
  >
    <v-row justify="center" align="center">
      <v-card elevation="24" width="95%" class>
        <v-card-title class="thirdBg" style="border-radius:10px 10px 0 0;">
          <v-row justify="space-between" dense>
            <v-col cols="10">
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
            <v-col cols="2" class="pr-0">
              <v-btn
                elevation="18"
                style="z-index: 1;"
                class="banner"
                dark
                outlined
                @click="newStock = true"
                :loading="dialog"
              >
                <v-icon>mdi-plus</v-icon>Yeni Kayıt
              </v-btn>
            </v-col>
          </v-row>
        </v-card-title>

        <v-card-text>
          <v-expansion-panels popout focusable hover>
            <v-expansion-panel>
              <v-expansion-panel-header class="pt-0 pb-0">
                <template v-slot:default="{ open }">
                  <v-fab-transition>
                    <v-row v-if="!open" justify="center" align="center" class="mt-0 mb-0">
                      <v-col cols="1" class="mt-0 mb-0">
                        <v-row justify="center" class="mt-0 mb-0">
                          <v-row justify="center" class="mt-0 mb-0">
                            <v-avatar size="64px">
                              <img
                                alt="Avatar"
                                src="https://avatars0.githubusercontent.com/u/9064066?v=4&s=460"
                              />
                            </v-avatar>
                          </v-row>
                        </v-row>
                      </v-col>
                      <v-col cols="5">
                        <v-row justify="center">
                          <v-label>Örnek Ürün</v-label>
                        </v-row>
                      </v-col>
                      <v-col cols="6">
                        <v-row justify="center">
                          <v-chip outlined>Örnek Ürün</v-chip>
                        </v-row>
                      </v-col>
                    </v-row>
                    <v-row v-else justify="center" align="center" class="thirdBg">
                      <v-col cols="2">
                        <v-chip pill outlined color="thirdBg">Örnek Ürün</v-chip>
                      </v-col>
                    </v-row>
                  </v-fab-transition>
                </template>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-row class="thirdBg">
                  <v-col cols="12" xl="6" lg="6" md="6">
                    <v-row
                      justify="center"
                      align="center"
                      align-lg="start"
                      align-xl="start"
                      align-md="start"
                    >
                      <v-col cols="8" xl="4" lg="4" md="4" sm="6">
                        <v-row>
                          <v-img src="https://cdn.vuetifyjs.com/images/parallax/material.jpg" />
                        </v-row>
                      </v-col>
                      <v-col cols="12" xl="8" lg="8" md="8" class="pt-0 mt-0">
                        <v-row>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Firma Adı"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Firma Tel No"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Vergi Dairesi"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Vergi No"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-col>
                    </v-row>
                  </v-col>
                  <v-col cols="12" xl="6" lg="6" md="6">
                    <v-textarea label="Firma Adres*" counter="250" outlined></v-textarea>
                    <!-- ######################################### SEVKİYAT ADRESLERİ BAŞI ######################################### -->
                    <v-card elevation="3">
                      <v-card-title class="mt-0 mb-0 pb-0 pt-0">
                        <v-chip class="ma-2" outlined color="headerColor">
                          Sevkiyat Adresleri
                          <v-icon right>mdi-map-marker</v-icon>
                        </v-chip>
                      </v-card-title>
                      <v-tabs v-model="tab" background-color="headerColor" dark>
                        <v-tab v-for="n in 3" :key="n">Adres {{ n }}</v-tab>
                        <v-tab @click="yaz()">
                          <v-icon>mdi-map-marker-plus</v-icon>
                        </v-tab>
                      </v-tabs>
                      <v-card-text class="text-center">
                        <v-tabs-items v-model="tab">
                          <v-tab-item v-for="i in 3" :key="i">
                            <v-card flat>
                              <v-card-text>{{ i }}.</v-card-text>
                            </v-card>
                          </v-tab-item>
                        </v-tabs-items>
                      </v-card-text>
                    </v-card>
                    <!-- ######################################### SEVKİYAT ADRESLERİ SONU ######################################### -->
                  </v-col>
                </v-row>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
              <v-expansion-panel-header class="pt-0 pb-0">
                <template v-slot:default="{ open }">
                  <v-fab-transition>
                    <v-row v-if="!open" justify="center" align="center" class="mt-0 mb-0">
                      <v-col cols="1" class="mt-0 mb-0">
                        <v-row justify="center" class="mt-0 mb-0">
                          <v-img
                            class="mt-0 mb-0"
                            aspect-ratio="4/3"
                            height="64px"
                            src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
                          />
                        </v-row>
                      </v-col>
                      <v-col cols="5">
                        <v-row justify="center">
                          <v-label>Örnek Ürün</v-label>
                        </v-row>
                      </v-col>
                      <v-col cols="6">
                        <v-row justify="center">
                          <v-chip outlined>Örnek Ürün</v-chip>
                        </v-row>
                      </v-col>
                    </v-row>
                    <v-row v-else class="text-center">
                      <v-col cols="2">
                        <v-chip pill outlined color="thirdBg">Örnek Ürün</v-chip>
                      </v-col>
                    </v-row>
                  </v-fab-transition>
                </template>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-row>
                  <v-col cols="12" xl="6" lg="6" md="6">
                    <v-row
                      justify="center"
                      align="center"
                      align-lg="start"
                      align-xl="start"
                      align-md="start"
                    >
                      <v-col cols="8" xl="4" lg="4" md="4" sm="6">
                        <v-row>
                          <v-img src="https://cdn.vuetifyjs.com/images/parallax/material.jpg" />
                        </v-row>
                      </v-col>
                      <v-col cols="12" xl="8" lg="8" md="8" class="pt-0 mt-0">
                        <v-row>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Firma Adı"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Firma Tel No"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Vergi Dairesi"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Vergi No"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-col>
                    </v-row>
                  </v-col>
                  <v-col cols="12" xl="6" lg="6" md="6">
                    <v-textarea label="Firma Adres*" counter="250" outlined></v-textarea>
                    <!-- ######################################### SEVKİYAT ADRESLERİ BAŞI ######################################### -->
                    <v-card elevation="3">
                      <v-card-title class="mt-0 mb-0 pb-0 pt-0">
                        <v-chip class="ma-2" outlined color="headerColor">
                          Sevkiyat Adresleri
                          <v-icon right>mdi-map-marker</v-icon>
                        </v-chip>
                      </v-card-title>
                      <v-tabs v-model="tab" background-color="headerColor" dark>
                        <v-tab v-for="n in 3" :key="n">Adres {{ n }}</v-tab>
                        <v-tab @click="yaz()">
                          <v-icon>mdi-map-marker-plus</v-icon>
                        </v-tab>
                      </v-tabs>
                      <v-card-text class="text-center">
                        <v-tabs-items v-model="tab">
                          <v-tab-item v-for="i in 3" :key="i">
                            <v-card flat>
                              <v-card-text>{{ i }}.</v-card-text>
                            </v-card>
                          </v-tab-item>
                        </v-tabs-items>
                      </v-card-text>
                    </v-card>
                    <!-- ######################################### SEVKİYAT ADRESLERİ SONU ######################################### -->
                  </v-col>
                </v-row>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
              <v-expansion-panel-header class="pt-0 pb-0">
                <template v-slot:default="{ open }">
                  <v-fab-transition>
                    <v-row v-if="!open" justify="center" align="center" class="mt-0 mb-0">
                      <v-col cols="1" class="mt-0 mb-0">
                        <v-row justify="center" class="mt-0 mb-0">
                          <v-row justify="center" class="mt-0 mb-0">
                            <v-img
                              class="mt-0 mb-0"
                              aspect-ratio="4/3"
                              height="64px"
                              src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
                            />
                          </v-row>
                        </v-row>
                      </v-col>
                      <v-col cols="5">
                        <v-row justify="center">
                          <v-label>Örnek Ürün</v-label>
                        </v-row>
                      </v-col>
                      <v-col cols="6">
                        <v-row justify="center">
                          <v-chip outlined>Örnek Ürün</v-chip>
                        </v-row>
                      </v-col>
                    </v-row>
                    <v-row v-else class="text-center">
                      <v-col cols="2">
                        <v-chip pill outlined color="thirdBg">Örnek Ürün</v-chip>
                      </v-col>
                    </v-row>
                  </v-fab-transition>
                </template>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-row>
                  <v-col cols="12" xl="6" lg="6" md="6">
                    <v-row
                      justify="center"
                      align="center"
                      align-lg="start"
                      align-xl="start"
                      align-md="start"
                    >
                      <v-col cols="8" xl="4" lg="4" md="4" sm="6">
                        <v-row>
                          <v-img src="https://cdn.vuetifyjs.com/images/parallax/material.jpg" />
                        </v-row>
                      </v-col>
                      <v-col cols="12" xl="8" lg="8" md="8" class="pt-0 mt-0">
                        <v-row>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Firma Adı"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Firma Tel No"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Vergi Dairesi"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Vergi No"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-col>
                    </v-row>
                  </v-col>
                  <v-col cols="12" xl="6" lg="6" md="6">
                    <v-textarea label="Firma Adres*" counter="250" outlined></v-textarea>
                    <!-- ######################################### SEVKİYAT ADRESLERİ BAŞI ######################################### -->
                    <v-card elevation="3">
                      <v-card-title class="mt-0 mb-0 pb-0 pt-0">
                        <v-chip class="ma-2" outlined color="headerColor">
                          Sevkiyat Adresleri
                          <v-icon right>mdi-map-marker</v-icon>
                        </v-chip>
                      </v-card-title>
                      <v-tabs v-model="tab" background-color="headerColor" dark>
                        <v-tab v-for="n in 3" :key="n">Adres {{ n }}</v-tab>
                        <v-tab @click="yaz()">
                          <v-icon>mdi-map-marker-plus</v-icon>
                        </v-tab>
                      </v-tabs>
                      <v-card-text class="text-center">
                        <v-tabs-items v-model="tab">
                          <v-tab-item v-for="i in 3" :key="i">
                            <v-card flat>
                              <v-card-text>{{ i }}.</v-card-text>
                            </v-card>
                          </v-tab-item>
                        </v-tabs-items>
                      </v-card-text>
                    </v-card>
                    <!-- ######################################### SEVKİYAT ADRESLERİ SONU ######################################### -->
                  </v-col>
                </v-row>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
              <v-expansion-panel-header class="pt-0 pb-0">
                <template v-slot:default="{ open }">
                  <v-fab-transition>
                    <v-row v-if="!open" justify="center" align="center" class="mt-0 mb-0">
                      <v-col cols="1" class="mt-0 mb-0">
                        <v-row justify="center" class="mt-0 mb-0">
                          <v-row justify="center" class="mt-0 mb-0">
                            <v-img
                              class="mt-0 mb-0"
                              aspect-ratio="4/3"
                              height="64px"
                              src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
                            />
                          </v-row>
                        </v-row>
                      </v-col>
                      <v-col cols="5">
                        <v-row justify="center">
                          <v-label>Örnek Ürün</v-label>
                        </v-row>
                      </v-col>
                      <v-col cols="6">
                        <v-row justify="center">
                          <v-chip outlined>Örnek Ürün</v-chip>
                        </v-row>
                      </v-col>
                    </v-row>
                    <v-row v-else class="text-center">
                      <v-col cols="2">
                        <v-chip pill outlined color="thirdBg">Örnek Ürün</v-chip>
                      </v-col>
                    </v-row>
                  </v-fab-transition>
                </template>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-row>
                  <v-col cols="12" xl="6" lg="6" md="6">
                    <v-row
                      justify="center"
                      align="center"
                      align-lg="start"
                      align-xl="start"
                      align-md="start"
                    >
                      <v-col cols="8" xl="4" lg="4" md="4" sm="6">
                        <v-row>
                          <v-img src="https://cdn.vuetifyjs.com/images/parallax/material.jpg" />
                        </v-row>
                      </v-col>
                      <v-col cols="12" xl="8" lg="8" md="8" class="pt-0 mt-0">
                        <v-row>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Firma Adı"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Firma Tel No"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Vergi Dairesi"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Vergi No"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-col>
                    </v-row>
                  </v-col>
                  <v-col cols="12" xl="6" lg="6" md="6">
                    <v-textarea label="Firma Adres*" counter="250" outlined></v-textarea>
                    <!-- ######################################### SEVKİYAT ADRESLERİ BAŞI ######################################### -->
                    <v-card elevation="3">
                      <v-card-title class="mt-0 mb-0 pb-0 pt-0">
                        <v-chip class="ma-2" outlined color="headerColor">
                          Sevkiyat Adresleri
                          <v-icon right>mdi-map-marker</v-icon>
                        </v-chip>
                      </v-card-title>
                      <v-tabs v-model="tab" background-color="headerColor" dark>
                        <v-tab v-for="n in 3" :key="n">Adres {{ n }}</v-tab>
                        <v-tab @click="yaz()">
                          <v-icon>mdi-map-marker-plus</v-icon>
                        </v-tab>
                      </v-tabs>
                      <v-card-text class="text-center">
                        <v-tabs-items v-model="tab">
                          <v-tab-item v-for="i in 3" :key="i">
                            <v-card flat>
                              <v-card-text>{{ i }}.</v-card-text>
                            </v-card>
                          </v-tab-item>
                        </v-tabs-items>
                      </v-card-text>
                    </v-card>
                    <!-- ######################################### SEVKİYAT ADRESLERİ SONU ######################################### -->
                  </v-col>
                </v-row>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
              <v-expansion-panel-header class="pt-0 pb-0">
                <template v-slot:default="{ open }">
                  <v-fab-transition>
                    <v-row v-if="!open" justify="center" align="center" class="mt-0 mb-0">
                      <v-col cols="1" class="mt-0 mb-0">
                        <v-row justify="center" class="mt-0 mb-0">
                          <v-row justify="center" class="mt-0 mb-0">
                            <v-img
                              class="mt-0 mb-0"
                              aspect-ratio="4/3"
                              height="64px"
                              src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
                            />
                          </v-row>
                        </v-row>
                      </v-col>
                      <v-col cols="5">
                        <v-row justify="center">
                          <v-label>Örnek Ürün</v-label>
                        </v-row>
                      </v-col>
                      <v-col cols="6">
                        <v-row justify="center">
                          <v-chip outlined>Örnek Ürün</v-chip>
                        </v-row>
                      </v-col>
                    </v-row>
                    <v-row v-else class="text-center">
                      <v-col cols="2">
                        <v-chip pill outlined color="thirdBg">Örnek Ürün</v-chip>
                      </v-col>
                    </v-row>
                  </v-fab-transition>
                </template>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-row>
                  <v-col cols="12" xl="6" lg="6" md="6">
                    <v-row
                      justify="center"
                      align="center"
                      align-lg="start"
                      align-xl="start"
                      align-md="start"
                    >
                      <v-col cols="8" xl="4" lg="4" md="4" sm="6">
                        <v-row>
                          <v-img src="https://cdn.vuetifyjs.com/images/parallax/material.jpg" />
                        </v-row>
                      </v-col>
                      <v-col cols="12" xl="8" lg="8" md="8" class="pt-0 mt-0">
                        <v-row>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Firma Adı"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Firma Tel No"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Vergi Dairesi"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Vergi No"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-col>
                    </v-row>
                  </v-col>
                  <v-col cols="12" xl="6" lg="6" md="6">
                    <v-textarea label="Firma Adres*" counter="250" outlined></v-textarea>
                    <!-- ######################################### SEVKİYAT ADRESLERİ BAŞI ######################################### -->
                    <v-card elevation="3">
                      <v-card-title class="mt-0 mb-0 pb-0 pt-0">
                        <v-chip class="ma-2" outlined color="headerColor">
                          Sevkiyat Adresleri
                          <v-icon right>mdi-map-marker</v-icon>
                        </v-chip>
                      </v-card-title>
                      <v-tabs v-model="tab" background-color="headerColor" dark>
                        <v-tab v-for="n in 3" :key="n">Adres {{ n }}</v-tab>
                        <v-tab @click="yaz()">
                          <v-icon>mdi-map-marker-plus</v-icon>
                        </v-tab>
                      </v-tabs>
                      <v-card-text class="text-center">
                        <v-tabs-items v-model="tab">
                          <v-tab-item v-for="i in 3" :key="i">
                            <v-card flat>
                              <v-card-text>{{ i }}.</v-card-text>
                            </v-card>
                          </v-tab-item>
                        </v-tabs-items>
                      </v-card-text>
                    </v-card>
                    <!-- ######################################### SEVKİYAT ADRESLERİ SONU ######################################### -->
                  </v-col>
                </v-row>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
              <v-expansion-panel-header class="pt-0 pb-0">
                <template v-slot:default="{ open }">
                  <v-fab-transition>
                    <v-row v-if="!open" justify="center" align="center" class="mt-0 mb-0">
                      <v-col cols="1" class="mt-0 mb-0">
                        <v-row justify="center" class="mt-0 mb-0">
                          <v-row justify="center" class="mt-0 mb-0">
                            <v-img
                              class="mt-0 mb-0"
                              aspect-ratio="4/3"
                              height="64px"
                              src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
                            />
                          </v-row>
                        </v-row>
                      </v-col>
                      <v-col cols="5">
                        <v-row justify="center">
                          <v-label>Örnek Ürün</v-label>
                        </v-row>
                      </v-col>
                      <v-col cols="6">
                        <v-row justify="center">
                          <v-chip outlined>Örnek Ürün</v-chip>
                        </v-row>
                      </v-col>
                    </v-row>
                    <v-row v-else class="text-center">
                      <v-col cols="2">
                        <v-chip pill outlined color="thirdBg">Örnek Ürün</v-chip>
                      </v-col>
                    </v-row>
                  </v-fab-transition>
                </template>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-row>
                  <v-col cols="12" xl="6" lg="6" md="6">
                    <v-row
                      justify="center"
                      align="center"
                      align-lg="start"
                      align-xl="start"
                      align-md="start"
                    >
                      <v-col cols="8" xl="4" lg="4" md="4" sm="6">
                        <v-row>
                          <v-img src="https://cdn.vuetifyjs.com/images/parallax/material.jpg" />
                        </v-row>
                      </v-col>
                      <v-col cols="12" xl="8" lg="8" md="8" class="pt-0 mt-0">
                        <v-row>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Firma Adı"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Firma Tel No"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Vergi Dairesi"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                            <v-text-field
                              outlined
                              readonly
                              label="Vergi No"
                              type="email"
                              required
                              dense
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-col>
                    </v-row>
                  </v-col>
                  <v-col cols="12" xl="6" lg="6" md="6">
                    <v-textarea label="Firma Adres*" counter="250" outlined></v-textarea>
                    <!-- ######################################### SEVKİYAT ADRESLERİ BAŞI ######################################### -->
                    <v-card elevation="3">
                      <v-card-title class="mt-0 mb-0 pb-0 pt-0">
                        <v-chip class="ma-2" outlined color="headerColor">
                          Sevkiyat Adresleri
                          <v-icon right>mdi-map-marker</v-icon>
                        </v-chip>
                      </v-card-title>
                      <v-tabs v-model="tab" background-color="headerColor" dark>
                        <v-tab v-for="n in 3" :key="n">Adres {{ n }}</v-tab>
                        <v-tab @click="yaz()">
                          <v-icon>mdi-map-marker-plus</v-icon>
                        </v-tab>
                      </v-tabs>
                      <v-card-text class="text-center">
                        <v-tabs-items v-model="tab">
                          <v-tab-item v-for="i in 3" :key="i">
                            <v-card flat>
                              <v-card-text>{{ i }}.</v-card-text>
                            </v-card>
                          </v-tab-item>
                        </v-tabs-items>
                      </v-card-text>
                    </v-card>
                    <!-- ######################################### SEVKİYAT ADRESLERİ SONU ######################################### -->
                  </v-col>
                </v-row>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-card-text>
      </v-card>
    </v-row>

    <!-- ######################################### DİALOG BAŞLANGICI ######################################### -->
    <v-row>
      <v-col>
        <v-dialog v-model="newStock" persistent scrollable width="70vw">
          <v-form ref="dialogCard">
            <v-card style="border-radius:12px;" height="90vh">
              <v-card-title class="banner">
                <v-row align="center" justify="space-between" class="px-2">
                  <v-chip class="ma-2" color="white" outlined pill>
                    Yeni Stock Kayıt
                    <v-icon right>mdi-folder-outline</v-icon>
                  </v-chip>

                  <v-btn color="banner" dark class="white--text" @click="closeDialog()">
                    <v-icon>mdi-close</v-icon>Kapat
                  </v-btn>
                </v-row>
              </v-card-title>
              <v-card-text>
                <Stock />
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
  </v-container>
</template>

<script>
import Stock from "@/components/stock/Stock";
export default {
  name: "StockList",
  components: {
    Stock,
  },
  data() {
    return {
      tab: 0,
      newStock: false,
      dialog: false,
      waitSave: false,
      search: "",
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
  methods: {
    closeDialog() {
      this.newStock = false;
    },
    yaz() {
      alert("yaraaaak");
      setTimeout(() => {
        this.tab = 0;
      }, 100);
    },
  },
  watch: {
    length(val) {
      this.tab = val - 1;
    },
  },
};
</script>

<style>
</style>