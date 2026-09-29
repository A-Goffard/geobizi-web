<template>
  <div class="contenedor-principal contenedor-calendario">
    <Calendario />

    <div class="leyendaContenedor">
      <h1>Actividades Programadas</h1>

      <h3>Filtrar por tipo:</h3>
      <div class="leyenda">
        <button 
          v-for="(info, key) in infoProyectos" 
          :key="key" 
          @click="filtroSeleccionado = key"
          class="leyenda-item btn-filtro" 
          :class="{ activo: filtroSeleccionado === key }"
        >
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
            <!-- CASO 1: Enlace externo -->
            <a 
              v-if="actividad.reservas && actividad.linkReserva" 
              :href="actividad.linkReserva" 
              target="_blank"
              class="btn-reserva btn-externo"
            >
              Inscribirse (web externa)
            </a>

            <!-- CASO 2A: Reservas de Geobizi - Plazas agotadas (Lista de espera) -->
            <button 
              v-else-if="actividad.reservas && estaAgotada(actividad)" 
              class="btn-reserva btn-espera"
              @click="irAReserva(actividad.id)"
            >
              ⚠️ Plazas agotadas · Lista de espera
            </button>

            <!-- CASO 2B: Reservas de Geobizi - Plazas disponibles -->
            <button 
              v-else-if="actividad.reservas" 
              class="btn-reserva"
              @click="irAReserva(actividad.id)"
            >
              Inscribirse / Reservar
            </button>

            <!-- CASO 3: Inscripción pendiente o por determinar -->
            <span v-else-if="actividad.estadoReserva === 'pendiente'" class="aviso-pendiente">
              ⏳ Inscripción por determinar
            </span>

            <!-- CASO 4: Entrada libre -->
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
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router';
import actividadesJson from '@/assets/json/actividades.json';

const router = useRouter();
const filtroSeleccionado = ref('todos');

// Estado reactivo inicializado con el JSON
const listaActividades = ref(actividadesJson);

// Sincroniza en tiempo real las plazas ocupadas desde el backend SQLite
onMounted(async () => {
  try {
    const res = await fetch('http://localhost:5000/api/actividades');
    if (res.ok) {
      const actividadesBd = await res.json();
      listaActividades.value = listaActividades.value.map(act => {
        const bd = actividadesBd.find(b => b.id === act.id);
        if (bd) {
          return {
            ...act,
            plazas_totales: bd.plazas_totales,
            plazas_ocupadas: bd.plazas_ocupadas
          };
        }
        return act;
      });
    }
  } catch (err) {
    // Si la API no responde en local, continúa con los datos del JSON
    console.warn('Aviso: Cargando aforo base desde JSON local.', err);
  }
});

const infoProyectos = {
  flysch: { nombre: 'FlyschBizkaia en Familia', color: 'orange', descripcion: 'Ruta geológica y medioambiental por la Costa de Getxo...' },
  naturgaua: { nombre: 'Naturgaua', color: 'purple', descripcion: 'Exploración nocturna y observación de fauna...' },
  zalla: { nombre: 'Actividad de Zalla Natura', color: 'blue', descripcion: 'Talleres y rutas en el entorno de Zalla...' },
  eventos: { nombre: 'Ferias y Eventos', color: 'plum', descripcion: 'Encuéntranos en los stands de divulgación...' },
  general: { nombre: 'Otras actividades', color: 'green', descripcion: 'Talleres variados y eventos especiales...' }
};

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

// Comprueba si una actividad ya no tiene hueco libre
const estaAgotada = (actividad) => {
  if (actividad.plazas_totales && actividad.plazas_ocupadas >= actividad.plazas_totales) {
    return true;
  }
  return false;
};

const irAReserva = (id) => {
  router.push({ name: 'reservaActividad', params: { id } });
};

const actividadesFiltradas = computed(() => {
  const hoy = new Date();
  hoy.setHours(0, 0, 0, 0);

  return listaActividades.value.filter(a => {
    const fechaActividad = new Date(a.fecha);
    const esFutura = fechaActividad >= hoy;
    const coincideFiltro = filtroSeleccionado.value === 'todos' || a.proyecto === filtroSeleccionado.value;
    return a.publicar && esFutura && coincideFiltro;
  }).sort((a, b) => new Date(a.fecha) - new Date(b.fecha));
});

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
});
</script>

<style scoped>
/* =========================================
   1. ESTRUCTURA Y CONTENEDOR ESPECÍFICO
   ========================================= */
.contenedor-calendario {
  max-width: 1200px;
  margin: 0 auto;
  min-height: 100vh;
  padding-bottom: 4rem;
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
  background: var(--white);
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

.card h2 {
  margin-top: 0.5rem;
  font-size: 1.2rem;
  margin-bottom: 0.8rem;
  line-height: 1.3;
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
  margin-bottom: 0;
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
  background: rgba(255, 255, 255, 0.7);
  padding: 0.8rem;
  border-radius: 0.5rem;
  font-size: 0.9rem;
}

.info-rapida p {
  margin: 4px 0;
  color: var(--darkgrey);
}

.precio-tag {
  font-weight: bold;
  color: var(--green);
}

/* Badges temáticos */
.badge-container {
  margin-top: 10px;
  display: flex;
  justify-content: center;
}

.badge {
  display: block;
  width: fit-content;
  padding: 4px 12px;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: bold;
  color: var(--white);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  text-align: center;
}

/* =========================================
   4. ESTADO DE RESERVAS Y BOTONES
   ========================================= */
.reserva-status {
  margin-top: 1.2rem;
  padding-top: 1rem;
  border-top: 1px dashed var(--shoftgreen);
  text-align: center;
}

.btn-reserva {
  width: 100%;
  background-color: var(--green);
  color: var(--white);
  border: none;
  padding: 10px;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.btn-reserva:hover {
  background-color: var(--lightgreen);
  transform: translateY(-2px);
}

/* Botón específico para lista de espera cuando está agotado */
.btn-espera {
  background-color: #d97706; /* Ámbar cálido visible */
  color: var(--white);
}

.btn-espera:hover {
  background-color: #b45309;
}

/* Botón especial para reservas externas */
.btn-externo {
  display: block;
  text-align: center;
  background-color: var(--lightblue);
  color: var(--white);
  padding: 10px;
  border-radius: 4px;
  font-weight: bold;
  box-sizing: border-box;
}

.btn-externo:hover {
  background-color: var(--blue);
  color: var(--white);
}

.aviso-no-reserva {
  display: block;
  text-align: center;
  font-size: 0.85rem;
  color: var(--grey);
  font-style: italic;
}

.aviso-pendiente {
  display: block;
  text-align: center;
  font-size: 0.85rem;
  color: var(--darkyellow);
  font-weight: bold;
  background-color: var(--yellow);
  padding: 8px;
  border-radius: 4px;
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

  .contenedor-calendario {
    padding-top: 5.5rem;
  }
}
</style>