<template>
  <v-app id="app">
    <v-navigation-drawer
        v-model="mobileDrawer"
        absolute
        temporary
    >
      <v-list-item>
        <!--<v-list-item-avatar>
          <v-icon></v-icon>
        </v-list-item-avatar>-->

        <v-list-item-content>
          <v-list-item-title>{{ conf.TITLE }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item
            v-for="link in links"
            :key="link"
            :to="link.to"
            link
        >
          <!--<v-list-item-icon>
            <v-icon>{{  }}</v-icon>
          </v-list-item-icon>-->

          <v-list-item-content>
            <v-list-item-title> {{ link.name }} </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      app
      color="white"
      flat
    >
        <v-app-bar-nav-icon
            @click.stop="mobileDrawer = !mobileDrawer"
            class="hidden-md-and-up mr-2"
        />

        <v-avatar
            class="mr-2 mr-sm-10 mr-lg-10 mr-xl-10"
            color="primary"
            size="32"
        >
          <v-icon dark>mdi-cube-scan</v-icon>
        </v-avatar>

        <v-tabs
            class="hidden-sm-and-down"
            show-arrows
        >
          <v-tabs-slider></v-tabs-slider>
          <v-tab
              v-for="link in links"
              :key="link"
              :to="link.to"
          >
            {{ link.name }}
          </v-tab>
        </v-tabs>

        <v-spacer />

        <v-avatar size="32" class="ml-2">
          <v-icon
            color="primary"
          >mdi-account</v-icon>
        </v-avatar>
    </v-app-bar>

    <vue-extend-layouts/>

    <v-footer>
      <v-col
          class="mt-8 mb-4 text-center text--secondary text-body-2"
          cols="12"
      >
        {{conf.TITLE}} <br />
        {{conf.HACK}}, {{conf.YEAR}}
      </v-col>
    </v-footer>

  </v-app>
</template>

<script>
import VueExtendLayouts from 'vue-extend-layout'
import CONF from "@/conf";

export default {
  name: 'App',
  components: {VueExtendLayouts},
  data() {
    return {
      mobileDrawer: false,
      conf: CONF,
      links: [
        {
          name: 'Главная',
          to: '/'
        },
        {
          name: 'Заказчику',
          to: 'customer'
        },
        {
          name: 'Поставщику',
          to: 'supplier'
        }
      ]
    }
  }
}
</script>
