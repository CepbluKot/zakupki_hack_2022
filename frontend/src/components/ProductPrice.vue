<template>
  <div>
    <div>
      <v-tooltip bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-icon v-if="analyze == 'lower'" color="red" v-bind="attrs" v-on="on">
            mdi-arrow-top-right
          </v-icon>
        </template>
        <span>Цена выше рыночной</span>
      </v-tooltip>

      <v-tooltip bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-icon v-if="analyze == 'higher'" color="green" v-bind="attrs" v-on="on">
            mdi-arrow-bottom-left
          </v-icon>
        </template>
        <span>Цена ниже рыночной</span>
      </v-tooltip>

      <span
          label
          class="text-h6 ml-2 font-weight-bold"
      >
        {{ price | currency() }}
      </span>

      <span class="text-body-2 ml-2 text--secondary">
        <span
            v-if="!tax.toLowerCase().includes('ндс')"
        >
          НДС:
        </span>
        {{ tax }}
      </span>
    </div>
    <div class="text-body-2 text--secondary mt-1">
      {{ packaging }}
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductPrice",
  props: [
    "analyze",
    "price",
    "tax",
    "packaging"
  ]
}
</script>

<style scoped>

</style>