import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from "@/views/Home.vue";
import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";
import AboutUs from "@/views/AboutUs.vue";
import Articles from "@/views/Articles.vue";
import Blog from "@/views/Blog.vue";


const routes: Array<RouteRecordRaw> = [
    {path: '/', component: Home},
    {path: '/auth/sign-in', component: Login, meta: {title: "Login - Women's Diary"}},
    {path: '/auth/sign-up', component: Register, meta: {title: "Register - Women's Diary"}},
    {path: '/about-us', component: AboutUs, meta: {title: "About us - Women's Diary"}},
    {path: '/articles', component: Articles, meta: {title: "Articles - Women's Diary"}},
    {path: '/blog', component: Blog, meta: {title: "Blog - Women's Diary"}}
]

const router = createRouter({
    history: createWebHistory(process.env.VITE_BASE_URL),
    routes
})

export default router