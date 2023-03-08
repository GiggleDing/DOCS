import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/home/Index.vue'

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: '/',
			name: 'home',
			component: HomeView
		},
		{
			path: '/user/:username',
			name: 'user',
			component: () => import('../views/user/Index.vue'),
			children: [
				{
					path: 'home',
					component: () => import('../views/user/Home.vue')
				}
			]
		},
		{
			path: '/login',
			name: 'login',
			component: () => import('../views/user/Login.vue')
		},
		{
			path: '/register',
			name: 'register',
			component: () => import('../views/user/Register.vue')
		},
		{
			path: '/:patchMatch(.*)*',
			name: 'NotFound',
			component: () => import('../views/other/NotFound.vue')
		}
	]
})

export default router
