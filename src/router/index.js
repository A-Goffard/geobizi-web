import { createRouter, createWebHistory } from 'vue-router';
import InicioView from '../views/InicioView.vue';
import FilosofiaView from '../views/FilosofiaView.vue';
import ServiciosView from '../views/ServiciosView.vue';
import CalendarioView from '../views/CalendarioView.vue';
import ReservasView from '../views/ReservasView.vue';
import GeotiendaView from '../views/GeotiendaView.vue';
import BlogView from '../views/BlogView.vue';
import ContactoView from '../views/ContactoView.vue';


const routes = [
    {
        path: '/',
        name: 'inicio',
        component: InicioView,
    },
    {
        path: '/filosofia',
        name: 'filosofia',
        component: FilosofiaView,
    },    
    {
        path: '/servicios',
        name: 'servicios',
        component: ServiciosView,
    },
    {
        path: '/calendario',
        name: 'calendario',
        component: CalendarioView,
    },
    {
        path: '/reservas',
        name: 'reservas',
        component: ReservasView,
    },
    {
        path: '/geotienda',
        name: 'geotienda',
        component: GeotiendaView,
    },
    {
        path: '/blog',
        name: 'blog',
        component: BlogView,
    },
    {
        path: '/contacto',
        name: 'contacto',
        component: ContactoView,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
  });

export default router;