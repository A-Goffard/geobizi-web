import { createRouter, createWebHistory } from "vue-router";

// --- VISTAS PRINCIPALES ---
import InicioView from "../views/InicioView.vue";
import ServiciosView from "../views/ServiciosView.vue";
import CalendarioView from "../views/CalendarioView.vue";
import ProyectosView from '../views/ProyectosView.vue';
import BlogView from "../views/BlogView.vue";
import ContactoView from "../views/ContactoView.vue";
import OtrosView from "@/views/OtrosView.vue";
import ReservasView from "@/views/ReservasView.vue";

// --- VISTAS DE PROYECTOS ---
import DetalleFlyschView from "@/views/proyectos/DetalleFlyschView.vue";
import DetalleZallaNaturaView from "@/views/proyectos/DetalleZallaNaturaView.vue";
import DetalleSemanaCienciaView from '@/views/proyectos/DetalleSemanaCienciaView.vue';
import DetalleAsteBerdeaView from '@/views/proyectos/DetalleAsteBerdeaView.vue';
import DetalleSopelaKostaFestView from '@/views/proyectos/DetalleSopelaKostaFestView.vue';
import DetalleDiaArbolView from '@/views/proyectos/DetalleDiaArbolView.vue';

// --- VISTAS DEL BLOG ---
import NummulitesView from "@/views/blog/NummulitesView.vue";
import FlyschBizkaiaView from "@/views/blog/FlyschBizkaiaView.vue";
import PatrimonioEuropeoView from "@/views/blog/PatrimonioEuropeoView.vue";
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
import EstramonioView from "@/views/blog/EstramonioView.vue";

// --- LEGAL Y OTROS ---
import PoliticadecancelacionesView from "../views/PoliticadecancelacionesView.vue";
import AvisolegalView from "../views/AvisolegalView.vue";
import PoliticadeprivacidadView from "../views/PoliticadeprivacidadView.vue";

// --- COMPONENTES DE SERVICIOS (Detalles) ---
import DetalleRutas from "../components/servicios/DetalleRutas.vue";
import DetalleActividades from "../components/servicios/DetalleActividades.vue";
import DetalleSensibilizacion from "../components/servicios/DetalleSensibilizacion.vue";
import DetalleDigitalySostenible from "../components/servicios/DetalleDigitalySostenible.vue";
import DetalleFormacion from "../components/servicios/DetalleFormacion.vue";
import DetalleDescargas from "../components/servicios/DetalleDescargas.vue";
import FitxasEtnobotanicasEnkarterri from "../components/contenido-creado/FitxasEtnobotanicasEnkarterri.vue";

// --- OTROS ---
import Calendario from "@/components/calendario/CalendarioActividades2025.vue";

const routes = [
    { path: "/", name: "inicio", component: InicioView },
    { path: "/servicios", name: "servicios", component: ServiciosView },
    { path: "/calendario", name: "calendario", component: CalendarioView },
    { path: '/reservas', name: 'reservas', component: ReservasView },
    { path: '/reservas/:id', name: 'reservaActividad', component: ReservasView },
    { path: "/proyectos", name: "proyectos", component: ProyectosView },

    // --- REDIRECCIONES SEO (De URLs antiguas a nuevas) ---
    { path: '/detalle-rutas', redirect: '/servicios/rutas' },
    { path: '/detalle-actividades', redirect: '/servicios/actividades' },
    { path: '/detalle-sensibilizacion', redirect: '/servicios/sensibilizacion' },
    { path: '/detalle-digital', redirect: '/servicios/digital-sostenible' },
    { path: '/detalle-formacion', redirect: '/servicios/formacion' },
    { path: '/detalle-descargas', redirect: '/servicios/descargas' },
    { path: '/detalle-semana-verde', redirect: '/servicios/actividades' },
    { path: '/detalle-dia-de-arbol', redirect: '/servicios/sensibilizacion' },
    { path: '/detalle-aste-berdea', redirect: '/servicios/actividades' },

    // --- NUEVAS RUTAS JERÁRQUICAS ---
    { path: "/servicios/rutas", name: "DetalleRutas", component: DetalleRutas },
    { path: "/servicios/actividades", name: "DetalleActividades", component: DetalleActividades },
    { path: "/servicios/sensibilizacion", name: "DetalleSensibilizacion", component: DetalleSensibilizacion },
    { path: "/servicios/digital-sostenible", name: "DetalleDigitalySostenible", component: DetalleDigitalySostenible },
    { path: "/servicios/formacion", name: "DetalleFormacion", component: DetalleFormacion },
    { path: "/servicios/descargas", name: "DetalleDescargas", component: DetalleDescargas },

    // --- PROYECTOS ---
    { path: "/detalle-flysch", name: "detalle-flysch", component: DetalleFlyschView },
    { path: "/detalle-zalla-natura", name: "detalle-zalla-natura", component: DetalleZallaNaturaView },
    { path: "/detalle-semana-ciencia", name: "detalle-semana-ciencia", component: DetalleSemanaCienciaView },
    { path: "/detalle-aste-berdea", name: "detalle-aste-berdea", component: DetalleAsteBerdeaView },
    { path: "/detalle-sopela-kosta-fest", name: "detalle-sopela-kosta-fest", component: DetalleSopelaKostaFestView },
    { path: "/detalle-dia-arbol", name: "detalle-dia-arbol", component: DetalleDiaArbolView },

    // --- BLOG ---
    { path: "/blog", name: "blog", component: BlogView },
    { path: "/blog/nummulites-flysch", name: "nummulites-flysch", component: NummulitesView },
    { path: "/blog/flysch-bizkaia", name: "flysch-bizkaia", component: FlyschBizkaiaView },
    { path: "/blog/patrimonio-europeo", name: "patrimonio-europeo", component: PatrimonioEuropeoView },
    { path: "/blog/free-tours", name: "free-tours", component: FreeToursView },
    { path: "/blog/valeriana-roja", name: "valeriana-roja", component: ValerianaRojaView },
    { path: "/blog/estuarios", name: "estuarios", component: EstuariosView },
    { path: "/blog/mariquitas", name: "mariquitas", component: MariquitasView },
    { path: "/blog/biodiversidad", name: "biodiversidad", component: BiodiversidadView },
    { path: "/blog/sapito-corredor", name: "sapito-corredor", component: SapitoView },
    { path: "/blog/carpobrotus", name: "carpobrotus", component: CarpobrotusView },
    { path: "/blog/estramonio", name: "estramonio", component: EstramonioView },
    { path: "/blog/flora-autoctona", name: "flora-autoctona", component: FloraAutoctonaView },
    { path: "/blog/fosiles", name: "fosiles", component: FosilesView },
    { path: "/blog/dia-tierra", name: "dia-tierra", component: DiaTierraView },

    // --- OTROS ---
    { path: "/otros", name: "otros", component: OtrosView },
    { path: "/contacto", name: "contacto", component: ContactoView },
    { path: "/politicadecancelaciones", name: "cancelaciones", component: PoliticadecancelacionesView },
    { path: "/avisolegal", name: "aviso", component: AvisolegalView },
    { path: "/politicadeprivacidad", name: "privacidad", component: PoliticadeprivacidadView },
    { path: "/fitxas-etnobotanicas-enkarterri", name: "fitxas-etnobotanicas-enkarterri", component: FitxasEtnobotanicasEnkarterri },
    { path: "/calendario", name: "Calendario", component: Calendario },

    {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component: () => import('@/views/NotFoundView.vue'),
        beforeEnter: (to, from, next) => {
            // Si la ruta contiene fragmentos de URLs antiguas, redirige automáticamente
            if (to.fullPath.includes('/geotienda/') || to.fullPath.includes('/investigacion/')) {
                next({ path: '/servicios', replace: true });
            } else {
                next(); // Si no, muestra la página 404
            }
        }
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior() { return { top: 0 }; },
});

export default router;