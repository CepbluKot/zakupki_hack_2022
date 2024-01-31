<template>
  <v-card class="shadow mt-4 mb-4">
    <v-row no-gutters>

      <v-col cols="12" md="1" lg="1" xl="1" class="pa-6">
        <SupplierAvatar/>
      </v-col>

      <v-col cols="12" md="9" lg="9" xl="9" class="pr-6">
        <v-card-title>
          <span class="text--secondary font-weight-regular">ИНН:</span> &nbsp; {{ inn }}
        </v-card-title>
      </v-col>

      <v-col cols="12" md="2" lg="2" xl="2" class="pa-4">
        <span class="text--secondary text-body-2">продано</span> {{ sold }} шт.
      </v-col>

    </v-row>
  </v-card>
</template>

<script>
import SupplierAvatar from "@/components/SupplierAvatar";

export default {
  name: "SupplierCard",
  props: [
    "inn",
    "sold"
  ],
  components: {
    SupplierAvatar: SupplierAvatar
  }
}
</script>

<style scoped>

</style>