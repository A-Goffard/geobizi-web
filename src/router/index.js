import { createRouter, createWebHistory } from 'vue-router';
import InicioView from '../views/InicioView.vue';
import ServiciosView from '../views/ServiciosView.vue';
import CalendarioView from '../views/CalendarioView.vue';
import ReservasView from '../views/ReservasView.vue';
import GeotiendaView from '../views/GeotiendaView.vue';
import BlogView from '../views/BlogView.vue';
import ContactoView from '../views/ContactoView.vue';
import PoliticadecancelacionesView from '../views/PoliticadecancelacionesView.vue';
import AvisolegalView from '../views/AvisolegalView.vue';
import PoliticadeprivacidadView from '../views/PoliticadeprivacidadView.vue';
import PatrimonioEuropeo2023View from '../views/blog/PatrimonioEuropeo2023View.vue';
import FreeToursView from '@/views/blog/FreeToursView.vue';
import ValerianaRojaView from '@/views/blog/ValerianaRojaView.vue';
import EstuariosView from '@/views/blog/EstuariosView.vue';
import MariquitasView from '@/views/blog/MariquitasView.vue';
import BiodiversidadView from '@/views/blog/BiodiversidadView.vue';
import SapitoView from '@/views/blog/SapitoView.vue';
import CarpobrotusView from '@/views/blog/CarpobrotusView.vue';
import FloraAutoctonaView from '@/views/blog/FloraAutoctonaView.vue';
import FosilesView from '@/views/blog/FosilesView.vue';
import DiaTierraView from '@/views/blog/DiaTierraView.vue';
import MariquitasView from '@/views/blog/MariquitasView.vue';

const routes = [
    {
        path: '/',
        name: 'inicio',
        component: InicioView,
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
        path: '/blog/detalle-patrimonio',
        name: 'detalle-patrimonio',
        component: PatrimonioEuropeo2023View,
    },
    {
        path: '/blog/detalle-free-tours',
        name: 'free-tour',
        component: FreeToursView,
    },
    {
        path: '/blog/detalle-valeriana-roja',
        name: 'valerianaroja',
        component: ValerianaRojaView,
    },
    {
        path: '/blog/detalle-estuarios',
        name: 'estuarios',
        component: EstuariosView,
    },
    {
        path: '/blog/detalle-mariquitas',
        name: 'mariquitas',
        component: MariquitasView,
    },
    {
        path: '/blog/detalle-biodiversidad',
        name: 'biodiversidad',
        component: BiodiversidadView,
    },
    {
        path: '/blog/detalle-sapito',
        name: 'sapito',
        component: SapitoView,
    },
    {
        path: '/blog/detalle-carpobrotus',
        name: 'carpobrotus',
        component: CarpobrotusView,
    },
    {
        path: '/blog/detalle-flora-autoctona',
        name: 'flora-autoctona',
        component: FloraAutoctonaView,
    },
    {
        path: '/blog/detalle-fosiles',
        name: 'fosiles',
        component: FosilesView,
    },
    {
        path: '/blog/detalle-dia-tierra',
        name: 'dia-tierra',
        component: DiaTierraView,
    },


    {
        path: '/blog/detalle-mariquitas',
        name: 'mariquitas',
        component: MariquitasView,
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