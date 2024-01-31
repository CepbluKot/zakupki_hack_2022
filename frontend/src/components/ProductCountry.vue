<template>
  <div class="text-body-2 text--secondary">
    <div
        v-if="countryProps != null"
        class="d-flex align-center justify-start"
    >
      <div class="mr-2">
        <country-flag
            :country="countryProps.ALFA2"
            size="medium"
        />
      </div>

      <div>
        {{ countryProps.FULLNAME }}
      </div>
    </div>

    <div v-else>
      Страна-производитель неизвестна
    </div>
  </div>
</template>

<script>
import countriesCodesJson from "../data/iso_countries.json"
import CountryFlag from 'vue-country-flag'

export default {
  name: "ProductCountry",
  data() {
    return {
      countriesCodes: countriesCodesJson
    }
  },
  components: {
    CountryFlag
  },
  props: [
    'countryCode'
  ],
  computed: {
    countryProps: function () {
      for (const country of this.countriesCodes) {
        if (Number(country.CODE) == Number(this.countryCode)) {
          return country
        }
      }
      console.log("Error: no country with iso code", this.countryCode)
      return null
    }
  }
}
</script>

<style scoped>

</style>