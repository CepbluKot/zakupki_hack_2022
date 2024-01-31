<template>
  <div>
    <SearchHeader
        title="Поиск по заказам"
    />

    <v-text-field
        solo
        v-model="searchWord"
        append-icon="mdi-magnify"
        @keydown.enter="getProducts(searchWord)"
        @click:append="getProducts(searchWord)"
        label="Заказ или предложение"
        placeholder=""
    />

    <v-progress-linear
        v-if="apiSearching"
        indeterminate rounded
        color="primary"
    ></v-progress-linear>

    <MessageAlert
        v-if="apiError.is"
        :text="apiError.text"
        type="error"
    />

    <EmptyData
        v-if="apiNotFound"
        class="mt-6"
    />

    <div v-else>
      <SupplierAnalytics
          v-if="suppliers.length != 0"
          :sellers_info="suppliers.sellers_info"
          :search_word="searchWord"
          :average_price="suppliers.average_price"
          :median_price="suppliers.mediana_price"
          :lower_price="suppliers.lower_price"
          :upper_price="suppliers.upper_price"
          :count_seller="suppliers.count_seller"
          :count_sale="suppliers.count_sale"
      />

      <div v-for="supplier in suppliers.sellers_info" :key="supplier">
        <SupplierCard
          :inn="supplier.inn"
          :sold="supplier.count_sale"
        />
      </div>
    </div>
  </div>
</template>

<script>
import SearchHeader from "@/components/SearchHeader";
import SupplierCard from "@/components/SupplierCard";
import MessageAlert from "@/components/MessageAlert";
import EmptyData from "@/components/EmptyData";
import SupplierAnalytics from "@/components/SupplierAnalytics";

import API from "@/api";
import axios from 'axios'

export default {
  name: "SupplierPage",
  components: {
    SearchHeader: SearchHeader,
    SupplierCard: SupplierCard,
    MessageAlert: MessageAlert,
    EmptyData: EmptyData,
    SupplierAnalytics: SupplierAnalytics
  },
  data() {
    return {
      apiConf: API,
      apiSearching: false,
      apiNotFound: false,
      apiError: {
        is: false,
        text: null
      },
      searchWord: '',
      response: null,
      suppliers: []
    }
  },
  methods: {
    slugifyInput() {
      let punctuation = /[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g
      this.searchWord = this.searchWord.replace(punctuation, " ")
    },
    getProducts(searchWord) {
      this.response = []
      this.suppliers = []
      this.apiError.is = false
      this.apiSearching = true
      this.apiNotFound = false

      axios.get(this.apiConf.ENDPOINT + this.apiConf.SUPPLIER + searchWord)
          .then((response) => {
            // handle success
            console.log(response.data)
            if (response.data.length === 0) {
              this.apiNotFound = true
            }
            else {
              this.response = response
              this.suppliers = response.data
            }
          })
          .catch((error) => {
            if (error.response.status == 404) {
              this.apiNotFound = true
            }
            else {
              this.apiError.is = true
              this.apiError.text = error
              console.log(error);
            }
          })
          .finally(() => {
            this.apiSearching = false
          });
    }
  }
}
</script>

<style scoped>

</style>