import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Maintenance',
    meta: {layout: 'empty'},
    component: () => import('@/views/Maintenance.vue')
  },
  {
    path: '/catalog',
    name: 'Catalog',
    component: () => import( '@/views/Catalog/Catalog.vue')
  },
  {
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
