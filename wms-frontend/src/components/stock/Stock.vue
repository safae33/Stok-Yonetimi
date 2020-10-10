<template>
  <v-container>
    <v-row>
      <v-col cols="12" xl="6" lg="6" md="6">
        <v-row justify="center" align="center" align-lg="start" align-xl="start" align-md="start">
          <v-col cols="8" xl="4" lg="4" md="4" sm="6">
            <v-row>
              <v-img src="https://cdn.vuetifyjs.com/images/parallax/material.jpg" />
            </v-row>
          </v-col>
          <v-col cols="12" xl="8" lg="8" md="8" class="pt-0 mt-0">
            <v-row>
              <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                <v-text-field outlined readonly label="Firma Adı" type="email" required dense></v-text-field>
              </v-col>
              <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                <v-text-field outlined readonly label="Firma Tel No" type="email" required dense></v-text-field>
              </v-col>
              <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                <v-text-field outlined readonly label="Vergi Dairesi" type="email" required dense></v-text-field>
              </v-col>
              <v-col cols="12" class="pt-0 mt-0 pb-0 mb-0">
                <v-text-field outlined readonly label="Vergi No" type="email" required dense></v-text-field>
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
                  <v-card-text> {{ i }}.</v-card-text>
                </v-card>
              </v-tab-item>
            </v-tabs-items>
          </v-card-text>
        </v-card>
        <!-- ######################################### SEVKİYAT ADRESLERİ SONU ######################################### -->
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
export default {
  name: "StockList",
};
</script>

<style>
</style>