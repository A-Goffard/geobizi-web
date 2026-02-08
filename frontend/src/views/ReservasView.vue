<template>
  <div class="container">
    
    <div v-if="!actividadSeleccionada" class="general-container">
      <h1>Actividades disponibles</h1>
      
      <div class="container-grid">
        <div 
          v-for="actividad in actividadesFiltradas" 
          :key="actividad.id" 
          class="card" 
          @click="seleccionarActividad(actividad)"
        >

          <h2>{{ actividad.titulo }}</h2>
          
          <div class="img-hover-container">
            <img :src="actividad.imagen1" :alt="actividad.titulo" class="img-base" loading="lazy" />
            <img :src="actividad.imagen2" :alt="actividad.titulo" class="img-hover" loading="lazy" />
          </div>

          <p class="descripcion">{{ actividad.descripcion1 }}</p>

          <div class="info-rapida">
            <p><strong>📅 {{ formatearFecha(actividad.fecha) }}</strong></p>
            <p>⏰ {{ actividad.hora }}</p>
            <p v-if="actividad.ubicacion">📍 {{ actividad.ubicacion }}</p>
            <p class="precio-tag">💶 {{ actividad.precio === 0 ? 'Gratis' : actividad.precio + '€' }}</p>
            
            <span class="badge" :class="actividad.proyecto || 'general'">
            {{ formatProyecto(actividad.proyecto) }}
            </span>
        </div>
        </div>
      </div>
    </div>

    <div v-else class="contact-container">
      <div class="header-reserva">
        <span class="badge-large" :class="actividadSeleccionada.proyecto || 'general'">
          {{ formatProyecto(actividadSeleccionada.proyecto) }}
        </span>
        <h1>Reserva: {{ actividadSeleccionada.titulo }}</h1>
      </div>

      <div class="info-reserva-detalle">
        <p><strong>Fecha:</strong> {{ formatearFecha(actividadSeleccionada.fecha) }}</p>
        <p><strong>Hora:</strong> {{ actividadSeleccionada.hora }}</p>
        <p v-if="actividadSeleccionada.ubicacion"><strong>Ubicación:</strong> {{ actividadSeleccionada.ubicacion }}</p>
      </div>

      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" v-model="formData.nombre" required>
        </div>
        <div class="form-group">
          <label for="apellidos">Apellidos:</label>
          <input type="text" id="apellidos" v-model="formData.apellidos" required>
        </div>
        <div class="form-group">
          <label for="email">Correo Electrónico:</label>
          <input type="email" id="email" v-model="formData.email" required>
        </div>
        <div class="form-group">
          <label for="phone">Teléfono:</label>
          <input type="tel" id="phone" v-model="formData.phone" required>
        </div>

        <!-- <div v-if="actividadSeleccionada.proyecto === 'zalla'" class="form-group highlight-group">
          <label for="dni">DNI (Requisito municipal):</label>
          <input type="text" id="dni" v-model="formData.dni" required placeholder="12345678X">
        </div> -->

        <div v-if="actividadSeleccionada.descripcion2.toLowerCase().includes('familia')" class="form-group highlight-group">
          <label for="edadNinos">Edad de los niños (si asisten):</label>
          <input type="text" id="edadNinos" v-model="formData.edadNinos" placeholder="Ej: 5 y 8 años">
        </div>

        <div class="form-group">
          <label for="numPersonas">Número de personas:</label>
          <input type="number" id="numPersonas" v-model="formData.numPersonas" min="1" required>
        </div>

        <div class="form-group">
          <label for="message">Mensaje / Observaciones:</label>
          <textarea id="message" v-model="formData.message"></textarea>
        </div>

        <div class="horizontalC">
          <input type="checkbox" id="privacy" v-model="formData.privacyAccepted" required>
          <label for="privacy">
            He leído y acepto la 
            <a href="/politica-de-privacidad" target="_blank">política de privacidad</a>.
          </label>
        </div>
        <div class="horizontalC">
          <input type="checkbox" id="privacyAviso" v-model="formData.privacyAcceptedAviso" required>
          <label for="privacyAviso">
            Entiendo que esto es una solicitud de reserva pendiente de confirmación.
          </label>
        </div>
        <div v-if="['zalla', 'flysch', 'naturgaua'].includes(actividadSeleccionada.proyecto)" class="caja-fotos">
          <div class="horizontalC">
            <input type="checkbox" id="imageRights" v-model="formData.imageRightsAccepted">
            <label for="imageRights">
              <strong>¡Queremos un recuerdo!</strong><br>
              Autorizo a Geobizi a tomar imágenes durante la actividad para enviárnoslas después y para usarlas en sus redes sociales/web como muestra de su trabajo.
              <br>
              <span class="nota-fotos">
                *Siempre seleccionamos imágenes respetuosas, priorizando planos generales, de espaldas o detalles (manos trabajando, lupas...) sobre los primeros planos de los menores.
              </span>
            </label>
          </div>
        </div>

        <div class="center">
          <button type="submit" class="btn-submit">Enviar Solicitud</button>
        </div>
        
        <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </form>

      <div class="center">
        <button @click="volverALista" class="volver-btn">← Volver a actividades</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import actividades from '@/assets/json/actividades.json';
import { useHead } from '@vueuse/head';

const route = useRoute();
const router = useRouter();

// SEO CONFIG
const pageUrl = 'https://www.geobizi.com/reservas';
const ogImage = 'https://www.geobizi.com/imagenes/proyectos/zallanatura/zallanatura2.avif';

useHead({
  title: 'Reservas y Actividades | Geobizi',
  meta: [
    { name: 'description', content: 'Reserva actividades y rutas de Geobizi. Consulta fechas, precios y plazas disponibles.' },
    { name: 'theme-color', content: '#0b8a4c' },
    { property: 'og:title', content: 'Reservas y Actividades | Geobizi' },
    { property: 'og:image', content: ogImage },
    { property: 'og:url', content: pageUrl } // <--- AQUÍ SE USA AHORA (Arregla el error)
  ],
  link: [
    { rel: 'canonical', href: pageUrl } // <--- AQUÍ TAMBIÉN
  ]
});

// STATE
const actividadSeleccionada = ref(null);
const formData = ref({
  nombre: '',
  apellidos: '',
  email: '',
  phone: '',
  actividad: '',
  message: '',
  privacyAccepted: false,
  privacyAcceptedAviso: false,
  numPersonas: 1,
  dni: '',
  edadNinos: ''
});
const successMessage = ref('');
const errorMessage = ref('');

// LOGIC
// 1. Filtrar por fecha futura y ordenar
const actividadesFiltradas = computed(() => {
  const hoy = new Date();
  hoy.setHours(0,0,0,0); 
  
  return actividades
    .filter(actividad => {
      const fechaActividad = new Date(actividad.fecha);
      return fechaActividad >= hoy && actividad.reservas && actividad.publicar;
    })
    .sort((a, b) => {
      const dateA = new Date(`${a.fecha}T${a.hora}`);
      const dateB = new Date(`${b.fecha}T${b.hora}`);
      return dateA - dateB;
    });
});

// 2. Mapeo de nombres para las Badges (Incluyendo Ferias)
const formatProyecto = (slug) => {
  const map = {
    'zalla': 'Zalla Natura',
    'flysch': 'Flysch en Familia',
    'naturgaua': 'Naturgaua',
    'ferias': 'Feria / Mercado', // <--- AÑADIDO
    'general': 'Actividad'
  };
  return map[slug] || 'Actividad';
};

// 3. Formato de fecha legible
const formatearFecha = (fechaStr) => {
  if(!fechaStr) return '';
  const opciones = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  const fecha = new Date(fechaStr);
  return fecha.toLocaleDateString('es-ES', opciones);
};

// 4. Watcher para URL (Deep linking)
watch(
  () => route.params.id,
  (id) => {
    if (id) {
      actividadSeleccionada.value = actividadesFiltradas.value.find(a => String(a.id) === String(id));
      if (actividadSeleccionada.value) {
        formData.value.actividad = `Reserva ID ${id}: ${actividadSeleccionada.value.titulo} (${actividadSeleccionada.value.fecha})`;
        formData.value.dni = '';
        formData.value.edadNinos = '';
      }
    } else {
      actividadSeleccionada.value = null;
    }
  },
  { immediate: true }
);

// ACTIONS
const seleccionarActividad = (actividad) => {
  router.push({ name: 'reservaActividad', params: { id: actividad.id } });
};

const volverALista = () => {
  router.push('/reservas');
};

const submitForm = () => {
  successMessage.value = '';
  errorMessage.value = '';

  fetch('https://formspree.io/f/xanedzed', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(formData.value)
  })
    .then(response => {
      if (response.ok) {
        successMessage.value = 'Solicitud enviada correctamente. Nos pondremos en contacto contigo.';
        // Reset form simple
        formData.value.message = '';
        formData.value.privacyAccepted = false;
        formData.value.privacyAcceptedAviso = false;
      } else {
        throw new Error('Error en el envío');
      }
    })
    .catch(error => {
      errorMessage.value = 'Hubo un error al enviar. Inténtalo de nuevo o contáctanos por email.';
      console.error(error);
    });
};
</script>

<style scoped>
/* ESTRUCTURA GENERAL */
.general-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  padding: 7rem 2rem 2rem 2rem;
}

.container-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
}

/* TARJETAS (CARDS) */
.card {
  width: 320px; /* Un poco más anchas para que quepa la info */
  padding: 20px;
  background-color: var(--megashoftgreen);
  border: 1px solid var(--shoftgreen);
  border-radius: 0.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
  cursor: pointer;
  position: relative; /* Para el badge absoluto */
  display: flex;
  flex-direction: column;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.card h2 {
  margin-top: 1.5rem; /* Espacio para el badge */
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
  line-height: 1.3;
}

.descripcion {
  color: var(--darkgrey);
  font-size: 0.9rem;
  margin-bottom: 1rem;
  flex-grow: 1; /* Para alinear botones al final si hubiese */
}

/* BADGES (Etiquetas de color) - AQUÍ ESTÁN LOS COLORES */
/* BADGES (Etiquetas de color) */
.badge {
  display: block;         
  width: fit-content;     
  margin: 1rem auto 0 auto;
  padding: 4px 12px;     
  border-radius: 20px;   
  font-size: 0.75rem;
  font-weight: bold;
  color: white;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  text-align: center;
}

/* Colores alineados con la leyenda del calendario */
.badge.flysch { background-color: orange; }
.badge.naturgaua { background-color: purple; }
.badge.zalla { background-color: blue; }
.badge.general { background-color: green; }
.badge.ferias { background-color: plum; }

/* INFO RÁPIDA EN TARJETA */
.info-rapida {
  background: rgba(255,255,255,0.5);
  padding: 0.8rem;
  border-radius: 0.5rem;
  font-size: 0.9rem;
}
.info-rapida p {
  margin: 4px 0;
  color: #333;
}

/* IMÁGENES */
.img-hover-container {
  position: relative;
  width: 100%;
  aspect-ratio: 16/9;
  overflow: hidden;
  border-radius: 0.5rem;
  margin-bottom: 1rem;
}
.img-hover-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: opacity 0.5s ease;
  position: absolute;
  top: 0; left: 0;
}
.img-base { opacity: 1; z-index: 1; }
.img-hover { opacity: 0; z-index: 2; }
.card:hover .img-hover { opacity: 1; }
.card:hover .img-base { opacity: 0; }

/* FORMULARIO Y DETALLE */
.contact-container {
  max-width: 650px;
  margin: 7rem auto 3rem auto;
  padding: 2rem;
  border: 1px solid var(--shoftgreen);
  border-radius: 8px;
  box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
  background: white;
}

.header-reserva {
  margin-bottom: 1.5rem;
  border-bottom: 1px solid #eee;
  padding-bottom: 1rem;
}

.badge-large {
  display: inline-block;
  padding: 5px 15px;
  border-radius: 15px;
  color: white;
  font-weight: bold;
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
}
/* Reutilizamos los mismos colores */
.badge-large.flysch { background-color: orange; }
.badge-large.naturgaua { background-color: purple; }
.badge-large.zalla { background-color: blue; }
.badge-large.general { background-color: green; }
.badge-large.ferias { background-color: plum; }

.info-reserva-detalle {
  margin-bottom: 2rem;
  background: var(--megashoftgreen);
  padding: 1rem;
  border-radius: 0.5rem;
}
.info-reserva-detalle p {
  margin: 0.5rem 0;
}

/* INPUTS */
.form-group { margin-bottom: 1.2rem; }
label { display: block; font-weight: bold; margin-bottom: 0.3rem; font-size: 0.95rem; }
input, select, textarea {
  width: 100%;
  padding: 0.7rem;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box; /* Importante para que no se salgan */
}
input:focus, textarea:focus {
  outline: none;
  border-color: var(--shoftgreen);
  box-shadow: 0 0 0 2px var(--megashoftgreen);
}

.highlight-group {
  background-color: #f0fdf4; /* Verde muy suave */
  padding: 15px;
  border-radius: 6px;
  border: 1px dashed var(--shoftgreen);
}

.horizontalC {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  margin-bottom: 1rem;
}
.horizontalC input { width: auto; margin-top: 5px; }
.horizontalC label { font-weight: normal; font-size: 0.9rem; }

/* BOTONES */
.btn-submit {
  width: 100%;
  padding: 1rem;
  background-color: var(--green);
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1.1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s;
}
.btn-submit:hover { background-color: var(--lightgreen); }

.volver-btn {
  background: none;
  border: none;
  color: #666;
  text-decoration: underline;
  cursor: pointer;
  margin-top: 1rem;
}

/* RESPONSIVE */
@media (max-width: 613px) {
  .general-container, .contact-container { padding: 1rem; margin-top: 5rem; }
  .card { width: 100%; }
}

.success-message { color: var(--green); text-align: center; margin-top: 1rem; font-weight: bold; }
.error-message { color: red; text-align: center; margin-top: 1rem; }
</style>