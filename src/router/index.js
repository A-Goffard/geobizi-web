import { createRouter, createWebHistory } from 'vue-router';
import InicioView from '../views/InicioView.vue';
/* import FilosofiaView from '../views/FilosofiaView.vue'; */
import ServiciosView from '../views/ServiciosView.vue';
import CalendarioView from '../views/CalendarioView.vue';
import ReservasView from '../views/ReservasView.vue';
import GeotiendaView from '../views/GeotiendaView.vue';
import BlogView from '../views/BlogView.vue';
import ContactoView from '../views/ContactoView.vue';
import PoliticadecancelacionesView from '../views/PoliticadecancelacionesView.vue';
import AvisolegalView from '../views/AvisolegalView.vue';
import PoliticadeprivacidadView from '../views/PoliticadeprivacidadView.vue';


const routes = [
    {
        path: '/',
        name: 'inicio',
        component: InicioView,
    },
/*     {
        path: '/filosofia',
        name: 'filosofia',
        component: FilosofiaView,
    },    */ 
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
    {
        path: '/politicadecancelaciones',
        name: 'cancelaciones',
        component: PoliticadecancelacionesView,
    },
    {
        path: '/avisolegal',
        name: 'aviso',
        component: AvisolegalView,
    },
    {
        path: '/politicadeprivacidad',
        name: 'privacidad',
        component: PoliticadeprivacidadView,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
  });

export default router;