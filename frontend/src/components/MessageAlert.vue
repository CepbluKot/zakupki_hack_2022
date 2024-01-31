<template>
  <v-alert
      border="left"
      colored-border
      :type="type"
      elevation="3"
  >
    <span v-if="type == 'error'">Ошибка: </span>
    <code>{{ text }}</code>
  </v-alert>
</template>

<script>
export default {
  name: "MessageAlert",
  props: [
    'type',
    'text'
  ]
}
</script>

<style scoped>

</style>