import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import login from '../views/login.vue'
import makeRoom from '../components/makeRoom.vue'
import lobby from '../views/lobby.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: login
  },
  {
    path: '/makeRoom',
    name: 'makeRoom',
    component: makeRoom
  },
  {
    path: '/lobby',
    name: 'lobby',
    component: lobby
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router