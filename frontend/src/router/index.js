import { createRouter, createWebHistory } from "vue-router";

import InicioView from "../views/InicioView.vue";
import ServiciosView from "../views/ServiciosView.vue";
import CalendarioView from "../views/CalendarioView.vue";
// import ReservasView from "@/views/ReservasView.vue";
// import TiendaView from "../views/TiendaView.vue";

import ProjectosView from '../views/ProjectosView.vue';

import DetalleFlyschView from "@/views/proyectos/DetalleFlyschView.vue";
import DetalleZallaNaturaView from "@/views/proyectos/DetalleZallaNaturaView.vue";
import DetalleSemanaCienciaView from '@/views/proyectos/DetalleSemanaCienciaView.vue'
import DetalleAsteBerdeaView from '@/views/proyectos/DetalleAsteBerdeaView.vue'
import DetalleSopelaKostaFestView from '@/views/proyectos/DetalleSopelaKostaFestView.vue'
import DetalleDiaArbolView from '@/views/proyectos/DetalleDiaArbolView.vue'


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
import EstramonioView from "@/views/blog/EstramonioView.vue"; // <-- nueva importación

import ContactoView from "../views/ContactoView.vue";

import PoliticadecancelacionesView from "../views/PoliticadecancelacionesView.vue";
import AvisolegalView from "../views/AvisolegalView.vue";
import PoliticadeprivacidadView from "../views/PoliticadeprivacidadView.vue";

import DetalleRutas from "../components/servicios/DetalleRutas.vue";
import DetalleActividades from "../components/servicios/DetalleActividades.vue";
import DetalleSensibilizacion from "../components/servicios/DetalleSensibilizacion.vue";
import DetalleDigitalySostenible from "../components/servicios/DetalleDigitalySostenible.vue";
import DetalleFormacion from "../components/servicios/DetalleFormacion.vue";
import DetalleDescargas from "../components/servicios/DetalleDescargas.vue";


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
    // {
    //     path: "/tienda",
    //     name: "tienda",
    //     component: TiendaView,
    // },
    
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
        path: "/detalle-semana-ciencia",
        name: "detalle-semana-ciencia",
        component: DetalleSemanaCienciaView,
    },
    {
        path: "/detalle-aste-berdea",
        name: "detalle-aste-berdea",
        component: DetalleAsteBerdeaView,
    },
    {
        path: "/detalle-sopela-kosta-fest",
        name: "detalle-sopela-kosta-fest",
        component: DetalleSopelaKostaFestView,
    },
    {
        path: "/detalle-dia-arbol",
        name: "detalle-dia-arbol",
        component: DetalleDiaArbolView,
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
        path: "/blog/detalle-estramonio",
        name: "estramonio",
        component: EstramonioView,
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
        path: "/detalle-rutas",
        name: "DetalleRutas",
        component: DetalleRutas,
    },
    {
        path: "/detalle-actividades",
        name: "DetalleActividades",
        component: DetalleActividades,
    },
    {
        path: "/detalle-sensibilizacion",
        name: "DetalleSensibilizacion",
        component: DetalleSensibilizacion,
    },
    {
        path: "/detalle-digital",
        name: "DetalleDigitalySostenible",
        component: DetalleDigitalySostenible,
    },
    {
        path: "/detalle-formacion",
        name: "DetalleFormacion",
        component: DetalleFormacion,
    },
    {
        path: "/detalle-descargas",
        name: "DetalleDescargas",
        component: DetalleDescargas,
    },
    {
        path: "/calendario",
        name: "Calendario",
        component: Calendario,
    },

    // Redirige cualquier ruta no existente a una página de error personalizada
    {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component: () => import('@/views/NotFoundView.vue')
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
