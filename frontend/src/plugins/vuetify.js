import Vue from 'vue'
import 'vuetify/dist/vuetify.min.css'
import Vuetify from 'vuetify';
import '@mdi/font/css/materialdesignicons.css'
import '../assets/main.scss'
import '../assets/transitions.css'

Vue.use(Vuetify)

const opts = {
    icons: {
        iconfont: 'mdi', // default - only for display purposes
    },
}

export default new Vuetify(opts)