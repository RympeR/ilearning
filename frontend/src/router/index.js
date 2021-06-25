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
    component: () => import( '@/views/Catalog.vue')
  },
  {
    path: '/my',
    name: 'profile',
    component: () => import( '@/views/Profile.vue')
  },
  {
    path: '/my/collections',
    name: 'collections',
    component: () => import( '@/views/Collections.vue')
  },
  {
    path: '/my/purchases',
    name: 'purchases',
    component: () => import( '@/views/Purchases.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
