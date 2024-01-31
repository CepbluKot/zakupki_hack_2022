<template>
  <div>
    <div class="mb-6">
      Найдено <strong>{{ count_seller }}</strong> поставщиков и <strong>{{ count_sale }}</strong> предложений по запросу
      <strong>{{ search_word }}</strong>
    </div>
    <div class="d-flex mt-2 mb-8 text-body-2 text--secondary">
      <div class="mr-4">
        Средняя цена:
        <v-chip color="white" class="shadow text--primary ma-1" label>{{ average_price | currency() }}</v-chip>
      </div>
      <div class="mr-4">
        Медианная цена:
        <v-chip color="white" class="shadow text--primary ma-1" label>{{ median_price | currency() }}</v-chip>
      </div>
      <div class="mr-4">
        Диапазон цен: от
        <v-chip color="white" class="shadow text--primary ma-1" label>{{ lower_price | currency() }}</v-chip>
        до
        <v-chip color="white" class="shadow text--primary ma-1" label>{{ upper_price | currency() }}</v-chip>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductAnalytics",
  props: [
    "search_word",
    "average_price",
    "count_sale",
    "count_seller",
    "lower_price",
    "median_price",
    "sellers_info",
    "upper_price"
  ]
}
</script>

<style scoped>

</style>