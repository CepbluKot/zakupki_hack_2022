<template>
  <div class="d-flex justify-center">
    <div class="text-h5 ma-6 font-weight-medium">
      {{ title }}
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchHeader",
  props: [
    'title'
  ]
}
</script>

<style scoped>

</style>