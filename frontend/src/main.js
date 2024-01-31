import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from "@/plugins/vuetify";
import Vue2Filters from "vue2-filters";

Vue.config.productionTip = false

let Vue2FiltersConfig = {
  capitalize: {
    onlyFirstLetter: false
  },
  number: {
    format: '0',
    thousandsSeparator: ',',
    decimalSeparator: ' '
  },
  bytes: {
    decimalDigits: 2
  },
  percent: {
    decimalDigits: 2,
    multiplier: 100,
    decimalSeparator: '.'
  },
  currency: {
    symbol: '₽',
    decimalDigits: 2,
    thousandsSeparator: ' ',
    decimalSeparator: ',',
    symbolOnLeft: false,
    spaceBetweenAmountAndSymbol: true,
    showPlusSign: false
  },
  pluralize: {
    includeNumber: false
  },
  ordinal: {
    includeNumber: false
  }
}

Vue.use(Vue2Filters, Vue2FiltersConfig)

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
