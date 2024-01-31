<template>
  <div>
    <span class="text--secondary mr-2">
      ОПКД2:
    </span>

    <v-chip small outlined label color="primary" class="mr-1 font-weight-medium">
      {{ code }}
    </v-chip>

    {{ name }}
  </div>
</template>

<script>
export default {
  name: "ProductOKPD2Props",
  props: [
    'code',
    'name'
  ]
}
</script>

<style scoped>

</style>