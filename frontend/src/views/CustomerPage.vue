<template>
  <div>
    <SearchHeader
      title="Поиск у поставщиков"
    />
    <v-text-field
        solo
        v-model="searchWord"
        append-icon="mdi-magnify"
        @keydown.enter="getProducts(searchWord)"
        @click:append="getProducts(searchWord)"
        label="Товар или услуга"
        placeholder=""
        @input="slugifyInput"
    />

    <div v-if="links != null" class="mb-6">
      <span v-for="link in links" :key="link" >
        <v-chip color="primary" class="shadow mr-1 mt-1 mb-1" @click="addToSearch(link)">
          <v-icon dark small class="mr-1">mdi-plus</v-icon>
          {{link}}
        </v-chip>
      </span>
    </div>

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
      <ProductAnalytics
          v-if="products.length != 0"
          :search_word="searchedWord"
          :average_price="analyze.average_price"
          :lower_price="analyze.lower_price"
          :upper_price="analyze.higher_price"
      />
      <div v-for="product in products" :key="product">
        <ProductCard
          :title="product.product_name"
          :description="product.product_characteristics"
          :opkd2_code="product.okpd2_code"
          :opkd2_name="product.okpd2_name"
          :price="product.price"
          :country="product.country_code"
          :tax="product.product_vat_rate"
          :packaging="product.product_msr"
          :inn="product.inn"
          :price_analyze="product.alnalize"
        />
      </div>
    </div>
  </div>
</template>

<script>
import SearchHeader from "@/components/SearchHeader";
import ProductCard from "@/components/ProductCard";
import MessageAlert from "@/components/MessageAlert";
import EmptyData from "@/components/EmptyData";
import ProductAnalytics from "@/components/ProductAnalytics";

import API from "@/api";
import axios from 'axios'

export default {
  name: "CustomerPage",
  components: {
    SearchHeader: SearchHeader,
    ProductCard: ProductCard,
    MessageAlert: MessageAlert,
    EmptyData: EmptyData,
    ProductAnalytics: ProductAnalytics
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
      searchedWord: '',
      response: null,
      products: [],
      analyze: [],
      links: []
    }
  },
  methods: {
    slugifyInput() {
      let punctuation = /[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g
      this.searchWord = this.searchWord.replace(punctuation, " ")
    },
    addToSearch(append_word) {
      this.searchWord += ' ' + append_word.toLowerCase()

      this.getProducts(this.searchWord)
    },
    getProducts(searchWord) {
      this.response = null
      this.products = []
      this.analyze = []
      this.links = []
      this.apiError.is = false
      this.apiSearching = true
      this.apiNotFound = false

          axios.get(this.apiConf.ENDPOINT + this.apiConf.CUSTOMER + searchWord.toLowerCase())
          .then((response) => {
            // handle success
            console.log(response.data)
            if (response.data.length == 0) {
              this.apiNotFound = true
            }
            else {
              this.response = response.data
              this.analyze = response.data.analyse
              this.links = response.data.name_groups
              this.products = response.data.products.products
              this.searchedWord = this.searchWord
            }
          })
          .catch((error) => {
            if (error.response.status == 404) {
              this.apiNotFound = true
            }
            else {
              this.apiError.is = true
              this.apiError.text = error
              console.log(error)
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