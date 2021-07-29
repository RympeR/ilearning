import { createRouter, createWebHistory } from 'vue-router'
//import i18n from '../i18n'

const routes = [
  /*{
    path: '/:locale',
    component: {
      template: "<router-view></router-view>"
    },
    beforeEnter: (to, from, next) => {
      const locale = to.params.locale
      const supported_locales = process.env.VUE_APP_I18N_SUPPORTED_LOCALE.split(',')

      if(!supported_locales.includes(locale)) return next('en')

      //console.log(i18n.locale + ' ' + locale)
      if(i18n.locale !== locale) {
        i18n.locale = locale
      }
      //console.log(i18n.locale + ' ' + locale)

      return next()
    },
    children: [{
      path: 'catalog',
      name: 'Catalog',
      component: () => import('@/views/Catalog/Catalog.vue')
    }]
  },*/
  {
    path: '/',
    name: 'Maintenance',
    meta: {layout: 'empty'},
    component: () => import('@/views/Maintenance.vue')
  },
  {
    // path: '/:locale/catalog',
    path: '/catalog',
    name: 'Catalog',
    component: () => import( '@/views/Catalog/Catalog.vue')
  },
  {
    // path: '/:locale/catalog/item/:id',
    path: '/catalog/item/:id',
    name: 'CatalogItem',
    component: () => import( '@/views/Catalog/Item.vue')
  },
  {
    path: '/my',
    name: 'profile',
    component: () => import( '@/views/Cabinet/Profile.vue')
  },
  {
    path: '/my/collections',
    name: 'collections',
    component: () => import( '@/views/Cabinet/Collections.vue')
  },
  {
    path: '/my/purchases',
    name: 'purchases',
    component: () => import( '@/views/Cabinet/Purchases.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
