<template>
  <div>
    <!-- ASİDE MENÜ BAŞI -->
    <v-navigation-drawer v-model="drawer" app color="navColor" :expand-on-hover="this.isMobile">
      <v-list class="pt-0 pb-2">
        <v-list-item dark three-line to="/">
          <v-row justify="center" align="center">
            <v-list-item-avatar class="pr-2" height="auto" width="100%">
              <img src="@/assets/logof.png" />
            </v-list-item-avatar>
          </v-row>
        </v-list-item>

        <v-divider></v-divider>
        <!-- Anasayfa linki ayrı olduğu için menüye böyle ekledim. -->
        <v-list-item active-class="activeGroup" exact dark class="btnText elevation-6 textW" to="/">
          <v-list-item-action>
            <v-icon medium color="white">mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Ana Sayfa</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <!-- sonu -->
        <v-list-group
          v-for="group in this.menu"
          :key="group.id"
          :value="group.value"
          :prepend-icon="group.icon"
          class="elevation-6"
        >
          <template v-slot:activator>
            <v-list-item-title class="btnText">{{ group.title }}</v-list-item-title>
          </template>
          <v-list-item-group class="mr-2 ml-3" dark>
            <v-list-item
              v-for="item in group.submenu"
              :key="item.id"
              dense
              class="white--text btnText submenuBg pl-2 rounded-r-pill"
              active-class="activeGroup"
              :to="item.to"
            >
              <v-list-item-action>
                <v-icon color="white">{{item.icon}}</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>{{item.title}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
          <v-divider></v-divider>
        </v-list-group>
      </v-list>
    </v-navigation-drawer>
    <!-- ASİDE MENÜ SONU -->

    <!-- TOPBAR MENÜ BAŞI -->
    <v-app-bar elevate-on-scroll app dark color="#717171">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <span class="routeName">{{this.currentRouteName}}</span>

      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn @click="logout" rounded elevation="24" dark color="#910330">
          <v-icon large class="pr-1">mdi-exit-to-app</v-icon>Çıkış
        </v-btn>
      </v-toolbar-items>
    </v-app-bar>
    <!-- TOPBAR MENÜ BAŞI -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import router from "../router";
import json from "../config/menu.json";

export default {
  name: "Aside",
  data() {
    return {
      menu: json.items,
      menü1: true,
      drawer: null,
      items: [
        {
          icon: "mdi-bluetooth",
          text: "Bluetooth",
        },
        {
          icon: "mdi-chart-donut",
          text: "Data Usage",
        },
      ],
      model: 1,
    };
  },
  computed: {
    ...mapGetters(["getIsAdmin", "getTitle"]),
    currentRouteName() {
      return this.$route.name;
    },
    isMobile() {
      if (this.$vuetify.breakpoint.lgAndUp) return true;
      else return false;
    },
  },
  mounted() {},
  methods: {
    logout() {
      this.setIsAuthAct(false);
      router.push("/auth");
    },
    ...mapActions(["setIsAuthAct"]),
  },
};
</script>

<style scoped>
.routeName {
  font-size: 1.5rem;
  color: white;
  font-family: "Poppins", sans-serif;
}
i.v-icon {
  color: white;
}

.activeGroup {
  background-color: teal;
  color: white;
}

.listBg {
  background-color: #b2dfdb;
  color: black;
}
</style>