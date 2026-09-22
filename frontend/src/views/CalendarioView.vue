<template>
  <div class="contenedor-principal">
    <Calendario />

    <div class="leyendaContenedor">
      <h1>Actividades Programadas</h1>

      <h3>Filtrar por tipo:</h3>
      <div class="leyenda">
        <button v-for="(info, key) in infoProyectos" :key="key" @click="filtroSeleccionado = key"
          class="leyenda-item btn-filtro" :class="{ activo: filtroSeleccionado === key }">
          <span class="punto leyenda-punto" :style="{ backgroundColor: info.color }"></span>
          <span>{{ info.nombre }}</span>
        </button>
        <button @click="filtroSeleccionado = 'todos'" class="leyenda-item btn-filtro">
          <span>Mostrar todas</span>
        </button>
      </div>

      <div v-if="filtroSeleccionado !== 'todos'" class="info-detalle-proyecto">
        <h2>{{ infoProyectos[filtroSeleccionado].nombre }}</h2>
        <p>{{ infoProyectos[filtroSeleccionado].descripcion }}</p>
      </div>
    </div>

    <div class="fichas-container">
      <div class="container-grid">
        <div v-for="actividad in actividadesFiltradas" :key="actividad.id" class="card">
          <h2>{{ actividad.titulo }}</h2>

          <div class="img-hover-container">
            <img :src="actividad.imagen1" :alt="actividad.titulo" class="img-base" loading="lazy" />
            <img :src="actividad.imagen2" :alt="actividad.titulo" class="img-hover" loading="lazy" />
          </div>

          <!-- DESCRIPCIÓN Y PÚBLICO EN LA FICHA -->
          <p class="descripcion">{{ actividad.descripcion }}</p>
          

          <div class="info-rapida">
            <p><strong>📅 {{ actividad.fecha }}</strong></p>
            <p>⏰ {{ actividad.hora }}</p>
            <p v-if="actividad.ubicacion">📍 {{ actividad.ubicacion }}</p>
            <p v-if="actividad.detalles" class="publico-tag"><strong>👥 Público:</strong> {{ actividad.detalles }}</p>
            <p class="precio-tag">💶 {{ actividad.precio === 0 ? 'Gratis' : actividad.precio + ' € por persona' }}</p>

            <div class="badge-container">
              <span class="badge" :class="actividad.proyecto || 'general'">
                {{ formatProyecto(actividad.proyecto) }}
              </span>
            </div>
          </div>

          <div class="reserva-status">
            <!-- CASO 1: Reservas externas (linkReserva tiene valor) -->
            <a v-if="actividad.reservas && actividad.linkReserva" :href="actividad.linkReserva" target="_blank"
              class="btn-reserva btn-externo">
              Inscribirse (web externa)
            </a>

            <!-- CASO 2: Reservas internas (típicas de Geobizi) -->
            <button v-else-if="actividad.reservas" class="btn-reserva"
              @click="router.push({ name: 'reservaActividad', params: { id: actividad.id } })">
              Inscribirse / Reservar
            </button>

            <!-- CASO 4: Pendiente / Por determinar -->
            <span v-else-if="actividad.estadoReserva === 'pendiente'" class="aviso-pendiente">
              ⏳ Inscripción por determinar
            </span>

            <!-- CASO 3: Sin reserva / Entrada libre -->
            <span v-else class="aviso-no-reserva">
              Entrada libre / Sin reserva
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import Calendario from '@/components/calendario/CalendarioActividades2025.vue'
import { useHead } from '@vueuse/head'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router';
import actividades from '@/assets/json/actividades.json';

const router = useRouter();
const filtroSeleccionado = ref('todos')

const infoProyectos = {
  flysch: { nombre: 'FlyschBizkaia en Familia', color: 'orange', descripcion: 'Ruta geológica y medioambiental por la Costa de Getxo...' },
  naturgaua: { nombre: 'Naturgaua', color: 'purple', descripcion: 'Exploración nocturna y observación de fauna...' },
  zalla: { nombre: 'Actividad de Zalla Natura', color: 'blue', descripcion: 'Talleres y rutas en el entorno de Zalla...' },
  eventos: { nombre: 'Ferias y Eventos', color: 'plum', descripcion: 'Encuéntranos en los stands de divulgación...' },
  general: { nombre: 'Otras actividades', color: 'green', descripcion: 'Talleres variados y eventos especiales...' }
}

const formatProyecto = (slug) => {
  const map = {
    'zalla': 'Zalla Natura',
    'flysch': 'Flysch en Familia',
    'naturgaua': 'Naturgaua',
    'eventos': 'Feria / Evento',
    'general': 'Actividad',
  };
  return map[slug] || 'Actividad';
};

const actividadesFiltradas = computed(() => {
  const hoy = new Date();
  hoy.setHours(0, 0, 0, 0);

  return actividades.filter(a => {
    const fechaActividad = new Date(a.fecha);
    const esFutura = fechaActividad >= hoy;
    const coincideFiltro = filtroSeleccionado.value === 'todos' || a.proyecto === filtroSeleccionado.value;
    return a.publicar && esFutura && coincideFiltro;
  }).sort((a, b) => {
    return new Date(a.fecha) - new Date(b.fecha);
  });
})

const pageUrl = 'https://www.geobizi.com/calendario'
const ogImage = 'https://www.geobizi.com/imagenes/proyectos/zallanatura/zallanatura2.avif'

useHead({
  title: 'Calendario de Actividades | Geobizi',
  meta: [
    { name: 'description', content: 'Consulta el calendario de Geobizi: rutas, talleres y actividades familiares y educativas. Reserva plazas y revisa fechas, horarios y ubicaciones.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'publisher', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Calendario de Actividades | Geobizi' },
    { property: 'og:description', content: 'Consulta el calendario de Geobizi: rutas, talleres y actividades familiares y educativas. Reserva plazas y revisa fechas, horarios y ubicaciones.' },
    { property: 'og:type', content: 'website' },
    { property: 'og:url', content: pageUrl },
    { property: 'og:image', content: ogImage }
  ],
  link: [{ rel: 'canonical', href: pageUrl }]
})
</script>

<style scoped>
/* =========================================
   1. ESTRUCTURA Y CONTENEDORES GENERALES
   ========================================= */
.contenedor-principal {
  padding-top: 7rem;
  background-color: #fff;
  padding-bottom: 4rem;
  min-height: 100vh;
}

@media (min-width: 950px) {
  .contenedor-principal {
    max-width: 1200px;
    margin: 0 auto;
  }
}

.leyendaContenedor {
  padding: 0 3rem;
  margin-bottom: 2rem;
}

/* =========================================
   2. FILTROS (BOTONES DE LEYENDA)
   ========================================= */
.leyenda {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin: 1.5rem 0;
}

.btn-filtro {
  display: flex;
  align-items: center;
  gap: 10px;
  border: 1px solid #eee;
  background: white;
  padding: 10px 18px;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: inherit;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.btn-filtro:hover {
  background-color: #f9f9f9;
  border-color: var(--shoftgreen);
  transform: translateY(-2px);
}

.btn-filtro.activo {
  background-color: var(--megashoftgreen);
  border-color: var(--shoftgreen);
  font-weight: bold;
}

.punto {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  display: inline-block;
  flex-shrink: 0;
}

/* Info del proyecto al filtrar */
.info-detalle-proyecto {
  background-color: #f9fdfb;
  border-left: 4px solid var(--shoftgreen);
  padding: 1.5rem;
  margin: 1rem 0 2rem 0;
  border-radius: 0 8px 8px 0;
}

.info-detalle-proyecto h2 {
  margin-top: 0;
  font-size: 1.4rem;
  color: var(--green);
}

/* =========================================
   3. GRID DE ACTIVIDADES (FICHAS)
   ========================================= */
.fichas-container {
  padding: 0 3rem;
}

.container-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
}

.card {
  width: 320px;
  padding: 20px;
  background-color: var(--megashoftgreen);
  border: 1px solid var(--shoftgreen);
  border-radius: 0.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
  position: relative;
  display: flex;
  flex-direction: column;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

/* Badges (Etiquetas de tipo de actividad) */
.badge {
  display: block;
  width: fit-content;
  padding: 4px 12px;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: bold;
  color: white;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  text-align: center;
}

.acciones-card {
  margin-top: 12px;
  border-top: 1px solid #eee;
  padding-top: 10px;
}

.btn-reserva {
  width: 100%;
  background-color: var(--green);
  color: white;
  border: none;
  padding: 8px;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  transform: ease all 0.3s;
}

.btn-reserva:hover {
  background-color: var(--lightgreen);
}

/* Botón especial para reservas externas */
.btn-externo {
  display: block;
  text-align: center;
  background-color: var(--lightblue);
  text-decoration: none;
  padding: 8px;
  border-radius: 4px;
  color: white;
  font-weight: bold;
}

.btn-externo:hover {
  background-color: var(--blue);
  opacity: 0.9;
}

a {
  font-style: normal;
  font-size: 0.9rem;
}

.aviso-no-reserva {
  display: block;
  text-align: center;
  font-size: 0.85rem;
  color: #888;
  font-style: italic;
}

.aviso-pendiente {
  display: block;
  text-align: center;
  font-size: 0.85rem;
  color: #b7791f; /* Un tono anaranjado/marrón elegante que indica estado pendiente */
  font-weight: bold;
  background-color: #fef3c7; /* Fondo sutil clarito */
  padding: 6px;
  border-radius: 4px;
}

.badge-container {
  margin-top: 10px;
  display: flex;
  justify-content: center;
}

.badge.flysch {
  background-color: orange;
}

.badge.naturgaua {
  background-color: purple;
}

.badge.zalla {
  background-color: blue;
}

.badge.eventos {
  background-color: plum;
}

.badge.general {
  background-color: green;
}

.card h2 {
  margin-top: 0.5rem;
  font-size: 1.2rem;
  margin-bottom: 0.8rem;
  line-height: 1.3;
  padding-right: 0;
  /* Para no solapar con la badge */
}

.descripcion {
  color: var(--darkgrey);
  font-size: 0.9rem;
  margin-bottom: 1rem;
  flex-grow: 1;
}

/* Imágenes con efecto hover */
.img-hover-container {
  position: relative;
  width: 100%;
  aspect-ratio: 1/1;
  overflow: hidden;
  border-radius: 0.5rem;
  margin-bottom: 0rem;
}

.img-hover-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: opacity 0.5s ease;
  position: absolute;
  top: 0;
  left: 0;
}

.img-base {
  opacity: 1;
  z-index: 1;
}

.img-hover {
  opacity: 0;
  z-index: 2;
}

.card:hover .img-hover {
  opacity: 1;
}

.card:hover .img-base {
  opacity: 0;
}

.info-rapida {
  background: rgba(255, 255, 255, 0.6);
  padding: 0.8rem;
  border-radius: 0.5rem;
  font-size: 0.9rem;
}

.info-rapida p {
  margin: 4px 0;
  color: #333;
}

.precio-tag {
  font-weight: bold;
  color: var(--green);
}

/* SECCIÓN NUEVA: Estado de Reserva en ficha */
.reserva-status {
  margin-top: 1.2rem;
  padding-top: 1rem;
  border-top: 1px dashed var(--shoftgreen);
  text-align: center;
}

.msg-abierto {
  color: var(--green);
  font-weight: bold;
  font-size: 0.85rem;
  margin-bottom: 0.6rem;
}

.msg-cerrado {
  color: #888;
  font-size: 0.8rem;
  font-style: italic;
  margin: 10px 0;
}



/* =========================================
   4. FORMULARIO DE RESERVA (CONTACT-CONTAINER)
   ========================================= */
.contact-container {
  max-width: 650px;
  margin: 2rem auto 4rem auto;
  padding: 2rem;
  border: 1px solid var(--shoftgreen);
  border-radius: 12px;
  background: white;
  box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.08);
}

.header-reserva {
  margin-bottom: 1.5rem;
  border-bottom: 1px solid #eee;
  padding-bottom: 1rem;
}

.badge-large {
  display: inline-block;
  padding: 5px 15px;
  border-radius: 0.5rem;
  color: white;
  font-weight: bold;
  margin-bottom: 0.5rem;
  font-size: 0.8rem;
}

.info-reserva-detalle {
  margin-bottom: 2rem;
  background: var(--megashoftgreen);
  padding: 1.2rem;
  border-radius: 0.5rem;
}

.form-group {
  margin-bottom: 1.2rem;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 0.4rem;
  font-size: 0.9rem;
}

input,
textarea {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  box-sizing: border-box;
}

input:focus,
textarea:focus {
  outline: none;
  border-color: var(--shoftgreen);
  box-shadow: 0 0 0 3px var(--megashoftgreen);
}

.highlight-group {
  background-color: #f0fdf4;
  padding: 15px;
  border-radius: 8px;
  border: 1px dashed var(--shoftgreen);
  margin-bottom: 1.5rem;
}

.caja-fotos {
  background-color: #f9f9f9;
  border: 1px solid #eee;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 1.5rem;
}

.titulo-fotos {
  font-weight: bold;
  color: var(--shoftgreen);
  margin-bottom: 8px;
  display: block;
}

.nota-fotos {
  font-size: 0.8rem;
  color: #777;
  font-style: italic;
}

.horizontalC {
  display: flex;
  gap: 12px;
  margin-bottom: 1rem;
  align-items: flex-start;
}

.horizontalC input {
  width: auto;
  margin-top: 4px;
}

.horizontalC label {
  font-weight: normal;
  font-size: 0.85rem;
  line-height: 1.4;
}

.btn-submit {
  width: 100%;
  padding: 1.2rem;
  background-color: var(--green);
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1.1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s;
}

.btn-submit:hover {
  background-color: var(--lightgreen);
}

.volver-btn {
  background: none;
  border: none;
  color: #888;
  text-decoration: underline;
  cursor: pointer;
  margin-top: 1.5rem;
  font-size: 0.9rem;
}

.center {
  text-align: center;
}

/* Mensajes de feedback */
.success-message {
  color: var(--green);
  text-align: center;
  margin-top: 1rem;
  font-weight: bold;
}

.error-message {
  color: #d32f2f;
  text-align: center;
  margin-top: 1rem;
}

/* =========================================
   5. RESPONSIVE
   ========================================= */
@media (max-width: 768px) {

  .leyendaContenedor,
  .fichas-container {
    padding: 0 1.5rem;
  }

  .leyenda {
    justify-content: center;
  }

  .card {
    width: 100%;
  }

  .contact-container {
    margin: 1rem;
    padding: 1.5rem;
  }

  .contenedor-principal {
    padding-top: 5.5rem;
  }
}
</style>