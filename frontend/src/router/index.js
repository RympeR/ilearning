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
    component: () => import( '../views/Catalog.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
