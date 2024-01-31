import Vue from 'vue'
import VueRouter from 'vue-router'

import IndexPage from "@/views/IndexPage";
import CustomerPage from "@/views/CustomerPage";
import SupplierPage from "@/views/SupplierPage";

import CONF from "@/conf";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: IndexPage,
    meta: {
      title: 'Главная',
      layout: 'IndexLayout'
    }
  },
  {
    path: '/customer',
    name: 'customer',
    component: CustomerPage,
    meta: {
      title: 'Заказчику',
      layout: 'DefaultLayout'
    }
  },
  {
    path: '/supplier',
    name: 'supplier',
    component: SupplierPage,
    meta: {
      title: 'Поставщику',
      layout: 'DefaultLayout'
    }
  }
]

const router = new VueRouter({
  routes
})

const DEFAULT_TITLE = CONF.TITLE
const TITLE_SEPARATOR = ' — '

router.afterEach((to) => {
  Vue.nextTick(() => {
    document.title = to.meta.title + TITLE_SEPARATOR + DEFAULT_TITLE || DEFAULT_TITLE;
  });
});

export default router
