<template>
  <div class="text--secondary text-caption">
    Поставщик: {{ inn }}
  </div>
</template>

<script>
export default {
  name: "ProductInn",
  props: [
    "inn"
  ]
}
</script>

<style scoped>

</style>