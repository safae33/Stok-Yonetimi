import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    apiUrl: "192.168.2.133:5000",
    isAuth: true,
    errMessage: "",
    applyArr: [

    ],
    isAdmin: true,
    user: { isAdmin: false , id:0},
    allUsers: [],
    dataHere: true,


    ////////////////////////////////////////////// ürünler
    allProducts: {
      1: {
        'code': "ali",
        'name': "Patates",
        'cat': ['Sebze', 'Yeraltı'],
        'mainUrl': "https://image.shutterstock.com/z/stock-photo-fresh-and-organic-potato-on-the-grass-field-mock-up-or-example-of-potato-products-in-fresh-market-1608883555.jpg",
        'otherUrls': ["https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg", "https://cdn.vuetifyjs.com/images/carousel/sky.jpg", "https://cdn.vuetifyjs.com/images/carousel/bird.jpg", "https://cdn.vuetifyjs.com/images/carousel/planet.jpg"],
        'specs': [
          {
            'specName': 'Renk',
            'specUnit': '-',
            'specValue': 'Açık Kahverengi'
          },
          {
            'specName': 'Uzunluk',
            'specUnit': 'cm',
            'specValue': '13'
          },
          {
            'specName': 'Genişlik',
            'specUnit': 'cm',
            'specValue': '5'
          },
        ]
      },
      2: {
        'code': "veli",
        'name': "Domates",
        'cat': ['Sebze', 'Dalda Yetişen'],
        'mainUrl': "https://image.shutterstock.com/z/stock-photo-three-tomatoes-are-lying-on-a-protective-medical-mask-on-a-white-background-agricultural-crisis-1698227782.jpg",
        'otherUrls': ["https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg", "https://cdn.vuetifyjs.com/images/carousel/sky.jpg", "https://cdn.vuetifyjs.com/images/carousel/bird.jpg", "https://cdn.vuetifyjs.com/images/carousel/planet.jpg"],
        'specs': [
          {
            'specName': 'Renk',
            'specUnit': '-',
            'specValue': 'Açık Kahverengi'
          },
          {
            'specName': 'Uzunluk',
            'specUnit': 'cm',
            'specValue': '13'
          },
          {
            'specName': 'Genişlik',
            'specUnit': 'cm',
            'specValue': '5'
          },
        ]
      },
      3: {
        'code': "123",
        'name': "Havuç ",
        'cat': ['Sebze', 'Yeraltı'],
        'mainUrl': "https://image.shutterstock.com/z/stock-photo-organic-carrot-growing-business-card-mock-up-with-harvested-root-vegetable-on-garden-soil-1426377680.jpg",
        'otherUrls': ["https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg", "https://cdn.vuetifyjs.com/images/carousel/sky.jpg", "https://cdn.vuetifyjs.com/images/carousel/bird.jpg", "https://cdn.vuetifyjs.com/images/carousel/planet.jpg"],
        'specs': [
          {
            'specName': 'Renk',
            'specUnit': '-',
            'specValue': 'Açık Kahverengi'
          },
          {
            'specName': 'Uzunluk',
            'specUnit': 'cm',
            'specValue': '13'
          },
          {
            'specName': 'Genişlik',
            'specUnit': 'cm',
            'specValue': '5'
          },
        ]
      },
    },
    prodDialog: false,
    activeProdId: null,
  },
  getters: {
    getApiUrl(state) {
      return state.apiUrl;
    },
    getIsAuth(state) {
      return state.isAuth;
    },
    getApplyArr(state) {
      return state.applyArr;
    },
    getIsAdmin(state) {
      return state.user.isAdmin;
    },
    getUsers(state) {
      return state.user.isAdmin;
    },
    getDataHere(state) {
      return state.dataHere;
    },
    getErrMessage(state) {
      return state.errMessage;
    },
    getAllUsers(state) {
      return state.allUsers;
    },
    getAllProducts(state) {
      return state.allProducts;
    },
    getProdDialog(state) {
      return state.prodDialog;
    },
    getActiveProdId(state) {
      return state.activeProdId;
    },
  },
  mutations: {

    setIsAuth(state, isAuth) {
      state.isAuth = isAuth;
    },
    setApplyArr(state, data) {
      state.applyArr = data;
    },
    setUser(state, data) {
      state.user = data;
    },
    setDataHere(state, data) {
      state.dataHere = data;
    },
    setErrMessage(state, data) {
      state.errMessage = data;
    },
    setAllUsers(state, data) {
      state.allUsers = data;
    },
    setAllProducts(state, data) {
      state.allProducts = data;
    },
    setActiveProdId(state, data) {
      state.activeProdId = data;
    },
    setProdDialog(state, data) {
      state.prodDialog = data;
    },
  },
  actions: {
    getProductById({ commit, state }) {
      //burada axios get i olacak. istenen iddeki ürünün detay bilgisi istendiği zaman çekilecek. activeProdId prodDialog
    },







    setProdDialog({ commit, state }, status) {
      commit('setProdDialog', status);
    },
    setActiveProdId({ commit, state }, index) {
      commit('setActiveProdId', index);
    },
    /////////////////////////////////////////////////////////////////
    setIsAuthAct({ commit }, isAuth) {
      commit('setIsAuth', isAuth);
    },
    async setApplyListApi({ commit, state }) {
      await axios
        .post("http://" + state.apiUrl + "/api/getAllApplies", { "isAdmin": state.user.isAdmin, "id": state.user.id })
        .then(response => {
          commit('setDataHere', false);
          commit('setApplyArr', response.data["result"]);
          console.log(state.applyArr)

        })
        .catch(error => {
          console.log(error);
        });
    },
    async check_user({ commit, state }, [mail, passwd]) {
      await axios
        .post("http://" + state.apiUrl + "/api/checkUser", { mail: mail, passwd: passwd })
        .then(response => {

          if (response.data["result"] == "0") {
            commit('setIsAuth', true);
            commit('setUser', response.data["data"]);
          }
          else {
            commit('setErrMessage', response.data["data"])
          }
        })
        .catch(error => {
          commit('setErrMessage', "Sunucu İle Bağlantı Kurulamadı.")
          console.log(error);
        });
    },

    async get_users({ commit, state }) {
      await axios
        .get("http://" + state.apiUrl + "/api/getUsers")
        .then(response => {
          commit('setAllUsers', response.data["result"]);
        })
        .catch(error => {
          console.log(error);
        });
    },
    async save_user({ state }, user) {
      await axios
        .post("http://" + state.apiUrl + "/api/addUser", { user: user })
        .then(response => {
          return response.data["result"];
        })
        .catch(error => console.log(error));
    },
    async delete_user({ state }, id) {
      await axios
        .post("http://" + state.apiUrl + "/api/delUser", { id: id })
        .then(response => {
          return response.data["result"];
        })
        .catch(error => console.log(error));
    },
  },
  modules: {
  }
})
