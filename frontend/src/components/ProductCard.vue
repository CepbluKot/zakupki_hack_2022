<template>
  <v-card class="shadow mt-4 mb-4">
    <v-row no-gutters>

      <v-col cols="12" md="1" lg="1" xl="1" class="pa-6">
        <ProductAvatar/>
      </v-col>

      <v-col cols="12" md="9" lg="9" xl="9" class="pr-6">
        <v-card-title style="word-break: normal">
          {{ title }}
        </v-card-title>

        <v-card-text>
          <ProductOKPD2Props
              v-if="opkd2_code != null && opkd2_name != null"
              :code="opkd2_code"
              :name="opkd2_name"
          />
        </v-card-text>

        <v-card-text class="text--secondary">
          <ProductDescription
              :description="description"
          />
        </v-card-text>
      </v-col>

      <v-col cols="12" md="2" lg="2" xl="2" class="pa-4">
        <ProductPrice
            :analyze="price_analyze.status"
            :price="price"
            :tax="tax"
            :packaging="packaging"
        />
        <ProductCountry
            class="mt-2"
            :country-code="country"
        />
        <ProductInn
            class="mt-4"
            :inn="inn"
        />
      </v-col>

    </v-row>
  </v-card>
</template>

<script>
import ProductAvatar from "@/components/ProductAvatar";
import ProductPrice from "@/components/ProductPrice";
import ProductDescription from "@/components/ProductDescription";
import ProductOKPD2Props from "@/components/ProductOKPD2Props";
import ProductCountry from "@/components/ProductCountry";
import ProductInn from "@/components/ProductInn";

export default {
  name: "ProductCard",
  props: [
    "title",
    "description",
    "price",
    "country",
    "tax",
    "packaging",
    "inn",
    "opkd2_code",
    "opkd2_name",
    "price_analyze"
  ],
  components: {
    ProductAvatar: ProductAvatar,
    ProductPrice: ProductPrice,
    ProductDescription: ProductDescription,
    ProductOKPD2Props: ProductOKPD2Props,
    ProductCountry: ProductCountry,
    ProductInn: ProductInn
  }
}
</script>

<style scoped>

</style>