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

        <div v-if="['zalla', 'flysch', 'naturgaua', 'ferias'].includes(actividadSeleccionada.proyecto)" class="caja-fotos">
          <p class="titulo-fotos">📸 Recuerdo de la actividad</p>
          <div class="horizontalC">
            <input type="checkbox" id="imageRights" v-model="formData.imageRightsAccepted">
            <label for="imageRights">
              Autorizo a Geobizi a tomar imágenes durante la actividad para enviárnoslas de recuerdo y usarlas en sus redes sociales/web con fines divulgativos.
              <br>
              <span class="nota-fotos">
                *Priorizamos siempre planos generales o de espaldas, respetando la privacidad de los menores.
              </span>
            </label>
          </div>
        </div>

        <div class="horizontalC">
          <input type="checkbox" id="privacy" v-model="formData.privacyAccepted" required>
          <label for="privacy">
            He leído y acepto la <a href="/politica-de-privacidad" target="_blank">política de privacidad</a>.
          </label>
        </div>
        <div class="horizontalC">
          <input type="checkbox" id="privacyAviso" v-model="formData.privacyAcceptedAviso" required>
          <label for="privacyAviso">
            Entiendo que esto es una solicitud de reserva pendiente de confirmación.
          </label>
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

const pageUrl = 'https://www.geobizi.com/reservas';
const ogImage = 'https://www.geobizi.com/imagenes/proyectos/zallanatura/zallanatura2.avif';

useHead({
  title: 'Reservas y Actividades | Geobizi',
  meta: [
    { name: 'description', content: 'Reserva actividades y rutas de Geobizi.' },
    { name: 'theme-color', content: '#0b8a4c' },
    { property: 'og:title', content: 'Reservas y Actividades | Geobizi' },
    { property: 'og:image', content: ogImage },
    { property: 'og:url', content: pageUrl }
  ],
  link: [{ rel: 'canonical', href: pageUrl }]
});

const actividadSeleccionada = ref(null);

// AQUÍ ESTÁ LA CLAVE: Inicializamos imageRightsAccepted a false
const formData = ref({
  nombre: '',
  apellidos: '',
  email: '',
  phone: '',
  actividad: '',
  message: '',
  privacyAccepted: false,
  privacyAcceptedAviso: false,
  imageRightsAccepted: false, // <--- IMPORTANTE: Debe estar aquí
  numPersonas: 1,
  dni: '',
  edadNinos: ''
});

const successMessage = ref('');
const errorMessage = ref('');

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

const formatProyecto = (slug) => {
  const map = {
    'zalla': 'Zalla Natura',
    'flysch': 'Flysch en Familia',
    'naturgaua': 'Naturgaua',
    'ferias': 'Feria / Mercado',
    'general': 'Actividad'
  };
  return map[slug] || 'Actividad';
};

const formatearFecha = (fechaStr) => {
  if(!fechaStr) return '';
  const opciones = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(fechaStr).toLocaleDateString('es-ES', opciones);
};

watch(() => route.params.id, (id) => {
  if (id) {
    actividadSeleccionada.value = actividadesFiltradas.value.find(a => String(a.id) === String(id));
    if (actividadSeleccionada.value) {
      formData.value.actividad = `Reserva ID ${id}: ${actividadSeleccionada.value.titulo} (${actividadSeleccionada.value.fecha})`;
      // Reseteamos campos específicos
      formData.value.dni = '';
      formData.value.edadNinos = '';
      formData.value.imageRightsAccepted = false;
    }
  } else {
    actividadSeleccionada.value = null;
  }
}, { immediate: true });

const seleccionarActividad = (actividad) => {
  router.push({ name: 'reservaActividad', params: { id: actividad.id } });
};

const volverALista = () => {
  router.push('/reservas');
};

const submitForm = () => {
  successMessage.value = '';
  errorMessage.value = '';

  // PREPARAMOS LOS DATOS PARA EL EMAIL (TRUCO PARA QUE SE LEA BIEN)
  const datosParaEnviar = {
    ...formData.value,
    // Convertimos los booleanos a texto para que en el email se vea claro
    'Acepta Política Privacidad': formData.value.privacyAccepted ? 'SÍ' : 'NO',
    'Entiende que es solicitud': formData.value.privacyAcceptedAviso ? 'SÍ' : 'NO',
    'Autoriza Fotos (Derechos Imagen)': formData.value.imageRightsAccepted ? 'SÍ, AUTORIZA' : 'NO AUTORIZA'
  };

  fetch('https://formspree.io/f/xanedzed', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(datosParaEnviar) // Enviamos los datos procesados
  })
    .then(response => {
      if (response.ok) {
        successMessage.value = 'Solicitud enviada correctamente. Nos pondremos en contacto contigo.';
        // Limpiar formulario
        formData.value.message = '';
        formData.value.privacyAccepted = false;
        formData.value.privacyAcceptedAviso = false;
        formData.value.imageRightsAccepted = false;
      } else {
        throw new Error('Error en el envío');
      }
    })
    .catch(error => {
      errorMessage.value = 'Hubo un error al enviar. Inténtalo de nuevo.';
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
  width: 320px;
  padding: 20px;
  background-color: var(--megashoftgreen);
  border: 1px solid var(--shoftgreen);
  border-radius: 0.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
  cursor: pointer;
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
  margin-bottom: 0.5rem;
  line-height: 1.3;
}

.descripcion {
  color: var(--darkgrey);
  font-size: 0.9rem;
  margin-bottom: 1rem;
  flex-grow: 1;
}

/* BADGES */
.badge {
  display: block;
  width: fit-content;
  margin: 1rem auto 0 auto; /* Centrado abajo */
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: bold;
  color: white;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  text-align: center;
}

/* COLORES DE BADGES */
.badge.flysch { background-color: orange; }
.badge.naturgaua { background-color: purple; }
.badge.zalla { background-color: blue; }
.badge.ferias { background-color: plum; }
.badge.general { background-color: green; }

.badge-large {
  display: inline-block;
  padding: 5px 15px;
  border-radius: 15px;
  color: white;
  font-weight: bold;
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
}
.badge-large.flysch { background-color: orange; }
.badge-large.naturgaua { background-color: purple; }
.badge-large.zalla { background-color: blue; }
.badge-large.ferias { background-color: plum; }
.badge-large.general { background-color: green; }

/* INFO RÁPIDA */
.info-rapida {
  background: rgba(255,255,255,0.5);
  padding: 0.8rem;
  border-radius: 0.5rem;
  font-size: 0.9rem;
}
.info-rapida p { margin: 4px 0; color: #333; }

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
  width: 100%; height: 100%; object-fit: cover;
  transition: opacity 0.5s ease; position: absolute; top: 0; left: 0;
}
.img-base { opacity: 1; z-index: 1; }
.img-hover { opacity: 0; z-index: 2; }
.card:hover .img-hover { opacity: 1; }
.card:hover .img-base { opacity: 0; }

/* FORMULARIO */
.contact-container {
  max-width: 650px;
  margin: 7rem auto 3rem auto;
  padding: 2rem;
  border: 1px solid var(--shoftgreen);
  border-radius: 8px;
  box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
  background: white;
}

.header-reserva { margin-bottom: 1.5rem; border-bottom: 1px solid #eee; padding-bottom: 1rem; }
.info-reserva-detalle { margin-bottom: 2rem; background: var(--megashoftgreen); padding: 1rem; border-radius: 0.5rem; }
.info-reserva-detalle p { margin: 0.5rem 0; }

.form-group { margin-bottom: 1.2rem; }
label { display: block; font-weight: bold; margin-bottom: 0.3rem; font-size: 0.95rem; }
input, select, textarea {
  width: 100%; padding: 0.7rem; font-size: 1rem;
  border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box;
}
input:focus, textarea:focus {
  outline: none; border-color: var(--shoftgreen);
  box-shadow: 0 0 0 2px var(--megashoftgreen);
}

.highlight-group {
  background-color: #f0fdf4; padding: 15px;
  border-radius: 6px; border: 1px dashed var(--shoftgreen);
}

/* CAJA DE FOTOS */
.caja-fotos {
  background-color: #f9f9f9;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 20px;
}
.titulo-fotos {
  font-weight: bold; color: var(--shoftgreen);
  margin-top: 0; margin-bottom: 10px;
}
.nota-fotos {
  display: block; margin-top: 5px; font-size: 0.85rem; color: #666; font-style: italic;
}

.horizontalC { display: flex; align-items: flex-start; gap: 10px; margin-bottom: 1rem; }
.horizontalC input { width: auto; margin-top: 5px; }
.horizontalC label { font-weight: normal; font-size: 0.9rem; }

.btn-submit {
  width: 100%; padding: 1rem; background-color: var(--green);
  color: white; border: none; border-radius: 4px;
  font-size: 1.1rem; font-weight: bold; cursor: pointer; transition: background 0.3s;
}
.btn-submit:hover { background-color: var(--lightgreen); }

.volver-btn {
  background: none; border: none; color: #666;
  text-decoration: underline; cursor: pointer; margin-top: 1rem;
}

@media (max-width: 613px) {
  .general-container, .contact-container { padding: 1rem; margin-top: 5rem; }
  .card { width: 100%; }
}

.success-message { color: var(--green); text-align: center; margin-top: 1rem; font-weight: bold; }
.error-message { color: red; text-align: center; margin-top: 1rem; }
</style>