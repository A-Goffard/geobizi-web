import { createRouter, createWebHistory } from "vue-router";

import InicioView from "../views/InicioView.vue";
import ServiciosView from "../views/ServiciosView.vue";
import CalendarioView from "../views/CalendarioView.vue";
// import ReservasView from "@/views/ReservasView.vue";
import TiendaView from "../views/TiendaView.vue";

import ProjectosView from '../views/ProjectosView.vue';

import DetalleFlyschView from "@/views/proyectos/DetalleFlyschView.vue";
import DetalleZallaNaturaView from "@/views/proyectos/DetalleZallaNaturaView.vue";

import BlogView from "../views/BlogView.vue";

import PatrimonioEuropeo2023View from "../views/blog/PatrimonioEuropeo2023View.vue";
import FreeToursView from "@/views/blog/FreeToursView.vue";
import ValerianaRojaView from "@/views/blog/ValerianaRojaView.vue";
import EstuariosView from "@/views/blog/EstuariosView.vue";
import MariquitasView from "@/views/blog/MariquitasView.vue";
import BiodiversidadView from "@/views/blog/BiodiversidadView.vue";
import SapitoView from "@/views/blog/SapitoView.vue";
import CarpobrotusView from "@/views/blog/CarpobrotusView.vue";
import FloraAutoctonaView from "@/views/blog/FloraAutoctonaView.vue";
import FosilesView from "@/views/blog/FosilesView.vue";
import DiaTierraView from "@/views/blog/DiaTierraView.vue";

import ContactoView from "../views/ContactoView.vue";

import PoliticadecancelacionesView from "../views/PoliticadecancelacionesView.vue";
import AvisolegalView from "../views/AvisolegalView.vue";
import PoliticadeprivacidadView from "../views/PoliticadeprivacidadView.vue";



import DetalleColegios from "../components/servicios/DetalleColegios.vue";
import DetalleAsociaciones from "../components/servicios/DetalleAsociaciones.vue";
import DetalleInstituciones from "../components/servicios/DetalleInstituciones.vue";
import DetalleDigital from "../components/servicios/DetalleDigital.vue";
import DetalleProyectos from "../components/servicios/DetalleProyectos.vue";
import DetalleGeneral from "../components/servicios/DetalleGeneral.vue";
import Calendario from "@/components/calendario/CalendarioActividades2025.vue";


const routes = [
    {
        path: "/",
        name: "inicio",
        component: InicioView,
    },
    {
        path: "/servicios",
        name: "servicios",
        component: ServiciosView,
    },
    {
        path: "/calendario",
        name: "calendario",
        component: CalendarioView,
    },
    {
    path: '/reservas',
    name: 'reservas',
    component: () => import('@/views/ReservasView.vue')
    },
    {
    path: '/reservas/:id',
    name: 'reservaActividad',
    component: () => import('@/views/ReservasView.vue')
    },
    {
        path: "/tienda",
        name: "tienda",
        component: TiendaView,
    },
    
    {
        path: "/projectos",
        name: "projectos",
        component: ProjectosView,
    },
    {
        path: "/detalle-flysch",
        name: "detalle-flysch",
        component: DetalleFlyschView,
    },
    {
        path: "/detalle-zalla-natura",
        name: "detalle-zalla-natura",
        component: DetalleZallaNaturaView,
    },

    {
        path: "/blog",
        name: "blog",
        component: BlogView,
    },
    {
        path: "/blog/detalle-patrimonio",
        name: "detalle-patrimonio",
        component: PatrimonioEuropeo2023View,
    },
    {
        path: "/blog/detalle-free-tours",
        name: "free-tour",
        component: FreeToursView,
    },
    {
        path: "/blog/detalle-valeriana-roja",
        name: "valerianaroja",
        component: ValerianaRojaView,
    },
    {
        path: "/blog/detalle-estuarios",
        name: "estuarios",
        component: EstuariosView,
    },
    {
        path: "/blog/detalle-mariquitas",
        name: "mariquitas",
        component: MariquitasView,
    },
    {
        path: "/blog/detalle-biodiversidad",
        name: "biodiversidad",
        component: BiodiversidadView,
    },
    {
        path: "/blog/detalle-sapito",
        name: "sapito",
        component: SapitoView,
    },
    {
        path: "/blog/detalle-carpobrotus",
        name: "carpobrotus",
        component: CarpobrotusView,
    },
    {
        path: "/blog/detalle-flora-autoctona",
        name: "flora-autoctona",
        component: FloraAutoctonaView,
    },
    {
        path: "/blog/detalle-fosiles",
        name: "fosiles",
        component: FosilesView,
    },
    {
        path: "/blog/detalle-dia-tierra",
        name: "dia-tierra",
        component: DiaTierraView,
    },
    {
        path: "/contacto",
        name: "contacto",
        component: ContactoView,
    },


    {
        path: "/politicadecancelaciones",
        name: "cancelaciones",
        component: PoliticadecancelacionesView,
    },
    {
        path: "/avisolegal",
        name: "aviso",
        component: AvisolegalView,
    },
    {
        path: "/politicadeprivacidad",
        name: "privacidad",
        component: PoliticadeprivacidadView,
    },


    {
        path: "/detalle-colegios",
        name: "DetalleColegios",
        component: DetalleColegios,
    },
    {
        path: "/detalle-asociaciones",
        name: "DetalleAsociaciones",
        component: DetalleAsociaciones,
    },
    {
        path: "/detalle-instituciones",
        name: "DetalleInstituciones",
        component: DetalleInstituciones,
    },
    {
        path: "/detalle-digital",
        name: "DetalleDigital",
        component: DetalleDigital,
    },
    {
        path: "/detalle-proyectos",
        name: "DetalleProyectos",
        component: DetalleProyectos,
    },
    {
        path: "/detalle-general",
        name: "DetalleGeneral",
        component: DetalleGeneral,
    },
    {
        path: "/calendario",
        name: "Calendario",
        component: Calendario,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior() {
        // Siempre desplaza hacia la parte superior
        return { top: 0 };
    },
});

export default router;
