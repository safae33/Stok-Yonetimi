import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import tr from 'vuetify/src/locale/tr';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    options: {
      customProperties: true,
    },
    themes: {
      light: {
        primary: '#4398d5',
        secondary: '#424242',
        accent: '#82B1FF',
        error: '#FF5252',
        info: '#2196F3',
        success: '#4CAF50',
        warning: '#FFC107',
        myColor: '#363062',
        headerColor: '#4398d5', 
        listColor: '#283992',
        second: '#2479b5',
        third: '#717171',
        fourth: '#B3E5FC',
        fifth: '#363636',
        navColor: '#363636',
      },
    },
  },
  lang: {
    locales: { tr },
    current: 'tr',
  },
});
