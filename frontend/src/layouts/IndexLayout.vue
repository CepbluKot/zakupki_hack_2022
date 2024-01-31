<template>
  <v-main>
    <v-container>
      <div class="d-flex justify-center align-center text-center">

        <div class="mt-12">
          <v-avatar color="primary lighten-3" class="mb-6">
            <v-icon dark>mdi-magnify</v-icon>
          </v-avatar>

          <div class="text-h4 font-weight-bold ">
            <span style="color: #1976D2">Интеллектуальный</span> поиск
          </div>

          <div class="mt-12">
            <v-btn to="/customer" color="primary" text large>
              Я заказчик
            </v-btn>
            <span class="ma-2"> / </span>
            <v-btn to="/supplier" color="primary" text large>
              Я поставщик
            </v-btn>
          </div>
        </div>

      </div>
    </v-container>
  </v-main>
</template>

<style>

</style>
