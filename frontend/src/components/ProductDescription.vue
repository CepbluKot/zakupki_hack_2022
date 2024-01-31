<template>
  <v-simple-table dense class="text--secondary description-table">
    <template v-slot:default>
      <tbody>
      <tr
          v-for="[key, value] of Object.entries(description)"
          :key="key"
      >
        <!--<td>{{ item.key }}</td>
        <td>{{ item.value }}</td>-->
        <td>{{ key }}</td>
        <td>{{ value }}</td>
      </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
export default {
  name: "ProductDescription",
  props: [
    "description"
  ],
  computed: {
    /*
    desc_items: function () {
      let desc = this.description

      let desc_array = desc.split(" || ")
      let desc_table_data = []

      for (const element of desc_array) {
        // desc_table_data.push(element.split(/:(.*)/s))

        const value = element.slice(element.indexOf(': ') + 1);
        const key = element.slice(0, element.indexOf(': '));

        desc_table_data.push({key, value})
      }

      return desc_table_data
    }
     */
  }
}
</script>

<style scoped>

</style>