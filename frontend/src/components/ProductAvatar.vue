<template>
  <div class="d-flex justify-center align-start">
    <v-avatar rounded :color="randomVuetifyColor()">
      <v-icon
          x-large dark
      >
        mdi-package-variant
      </v-icon>
    </v-avatar>
  </div>
</template>

<script>
export default {
  name: "ProductAvatar",
  methods: {
    randomVuetifyColor() {
      let colors = ['red', 'pink', 'purple', 'deep-purple', 'indigo', 'blue', 'light-blue', 'cyan', 'teal', 'green', 'light-green', 'lime', 'amber', 'orange', 'deep-orange']

      return colors[Math.floor(Math.random() * colors.length)] + ' lighten-3';
    }
  }
}
</script>

<style scoped>

</style>