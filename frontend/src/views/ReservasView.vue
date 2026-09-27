<template>
  <div class="container">

    <div v-if="!actividadSeleccionada" class="general-container">
      <h1>Actividades disponibles</h1>
      <div class="container-grid">
        <div v-for="actividad in actividadesFiltradas" :key="actividad.id" class="card"
          @click="seleccionarActividad(actividad)">
          <h2>{{ actividad.titulo }}</h2>

          <div class="img-hover-container">
            <img :src="actividad.imagen1" :alt="actividad.titulo" class="img-base" loading="lazy" />
            <img :src="actividad.imagen2" :alt="actividad.titulo" class="img-hover" loading="lazy" />
          </div>

          <p class="descripcion">{{ actividad.descripcion }}</p>

          <div class="info-rapida">
            <p><strong>📅 {{ formatearFecha(actividad.fecha) }}</strong></p>
            <p>⏰ {{ actividad.hora }}</p>
            <p v-if="actividad.ubicacion">📍 {{ actividad.ubicacion }}</p>
            <p v-if="actividad.detalles" class="publico-tag"><strong>👥 Público:</strong> {{ actividad.detalles }}</p>
            <p class="precio-tag">💶 {{ actividad.precio === 0 ? 'Gratis' : actividad.precio + '€' }}</p>

            <span class="badge" :class="actividad.proyecto || 'general'">
              {{ formatProyecto(actividad.proyecto) }}
            </span>
          </div>
          <div style="margin-top: 1rem; text-align: center;">
            <a v-if="actividad.linkReserva" :href="actividad.linkReserva" target="_blank"
              class="btn-reserva btn-externo" style="display: block; text-decoration: none;">
              Inscribirse (web externa)
            </a>
            <button v-else @click="seleccionarActividad(actividad)" class="btn-reserva">
              Inscribirse / Reservar
            </button>
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
        <p v-if="actividadSeleccionada.precio"><strong>Precio:</strong> {{ actividadSeleccionada.precio }} € por persona
        </p>
        <p v-if="actividadSeleccionada.descripcion"><strong>Descripción:</strong> {{ actividadSeleccionada.descripcion
        }}</p>
        <p v-if="actividadSeleccionada.detalles"><strong>Detalles:</strong> {{ actividadSeleccionada.detalles }}</p>
        <p v-if="actividadSeleccionada.oharrak"><strong>Notas:</strong> {{ actividadSeleccionada.oharrak }}</p>
      </div>

      <div v-if="actividadSeleccionada" class="contact-container">
        <form @submit.prevent="submitForm">

          <!-- DATOS DE CONTACTO (RESPONSABLE) -->
          <h3>Datos de la persona responsable / contacto</h3>
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
          <div class="aviso-plazas" :class="{ 'casi-lleno': plazasDisponibles <= 3 }">
            <p v-if="plazasDisponibles > 0">
              Plazas libres disponibles: <strong>{{ plazasDisponibles }}</strong>
            </p>
            <p v-else class="completo">
              ¡Lo sentimos! Esta actividad ya está completa.
            </p>
          </div>
          <div class="form-group">
            <label for="numPersonas">Número de plazas totales a reservar:</label>
            <input type="number" id="numPersonas" v-model.number="formData.num_personas" min="1"
              :max="plazasDisponibles" required />
          </div>

          <!-- ASISTENTES DINÁMICOS -->
          <div class="participantes-container" v-if="formData.participantes.length > 0">
            <h3 class="subtitulo-participantes">Datos de los asistentes (incluyéndote a tí si vas a participar) ({{
              formData.participantes.length }} personas)</h3>

            <div v-for="(p, index) in formData.participantes" :key="index" class="participante-card">
              <h4>Asistente {{ index + 1 }}</h4>
              <div class="form-group">
                <label :for="'p-nombre-' + index">Nombre:</label>
                <input type="text" :id="'p-nombre-' + index" v-model="p.nombre" required>
              </div>
              <div class="form-group">
                <label :for="'p-apellidos-' + index">Apellidos:</label>
                <input type="text" :id="'p-apellidos-' + index" v-model="p.apellidos" required>
              </div>
              <div class="form-group">
                <label :for="'p-edad-' + index">Edad:</label>
                <input type="number" :id="'p-edad-' + index" v-model.number="p.edad" min="0" max="120" required
                  placeholder="Ej: 8">
              </div>
            </div>
          </div>

          <div class="form-group">
            <label for="message">Mensaje / Observaciones:</label>
            <textarea id="message" v-model="formData.message"></textarea>
          </div>

          <div v-if="['zalla', 'flysch', 'naturgaua', 'eventos', 'general'].includes(actividadSeleccionada.proyecto)"
            class="caja-fotos">
            <p class="titulo-fotos">📸 Permisos de imagen</p>
            <div class="horizontalC">
              <input type="checkbox" id="imageRights" v-model="formData.imageRightsAccepted">
              <label for="imageRights">
                Autorizo a Geobizi a tomar imágenes durante la actividad para enviárnoslas de recuerdo y/o usarlas en
                sus redes sociales/web con fines divulgativos.
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
              He leído y acepto la <a href="/politicadeprivacidad" target="_blank">política de privacidad</a>.
            </label>
          </div>

          <div class="horizontalC">
            <input type="checkbox" id="privacyAviso" v-model="formData.privacyAcceptedAviso" required>
            <label for="privacyAviso">
              Entiendo que es una actividad con límite de aforo. <b>Mira en tu carpeta de spam</b> si no recibes el
              correo de confirmación.
            </label>
          </div>

          <div class="center">
            <button type="submit" class="btn-submit">Confirmar Reserva</button>
          </div>

          <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
          <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
        </form>
      </div>
      <div class="center">
        <button @click="volverALista" class="volver-btn">← Volver a actividades</button>
      </div>
    </div>
    <!-- MODAL DE ÉXITO BLOQUEANTE -->
    <div v-if="mostrarModalExito" class="modal-overlay"
      style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); display: flex; align-items: center; justify-content: center; z-index: 1000;">
      <div class="modal-content"
        style="background: white; padding: 2.5rem; border-radius: 8px; text-align: center; max-width: 400px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
        <h3 style="color: #2c5e3b; margin-top: 0;">🌿 ¡Reserva Confirmada!</h3>
        <p style="color: #333; margin: 1.5rem 0;">{{ successMessage }}</p>
        <p style="font-size: 13px; color: #666; margin-bottom: 1.5rem;">Te hemos enviado un correo electrónico con los
          detalles y las recomendaciones.</p>
        <button @click="mostrarModalExito = false; router.push('/calendario')" class="btn-reserva"
          style="padding: 10px 20px; cursor: pointer;">
          Aceptar y volver
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
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

const actividades = ref([]);
const actividadSeleccionada = ref(null);
const mostrarModalExito = ref(false);

// Función centralizada para cargar las actividades desde la API
const cargarActividades = async () => {
  try {
    const response = await fetch('http://localhost:5000/api/actividades');
    if (response.ok) {
      const data = await response.json();
      actividades.value = data;
      verificarSeleccionActividad();
    } else {
      console.error("Error en la respuesta de la API:", response.status);
    }
  } catch (error) {
    console.error("Error al conectar con la API de actividades:", error);
  }
};

// Comprueba la URL actual y selecciona la actividad correspondiente
const verificarSeleccionActividad = () => {
  const id = route.params.id;
  if (id) {
    actividadSeleccionada.value = actividades.value.find(a => String(a.id) === String(id));
    if (actividadSeleccionada.value) {
      formData.value.imageRightsAccepted = false;
    }
  } else {
    actividadSeleccionada.value = null;
  }
};

// Al montar el componente, cargamos los datos
onMounted(() => {
  cargarActividades();
});

// Si cambia la ruta (por ejemplo, al volver atrás o cambiar de tarjeta), re-verificamos
watch(() => route.params.id, () => {
  verificarSeleccionActividad();
});

const formData = ref({
  nombre: '',
  apellidos: '',
  email: '',
  phone: '',
  message: '',
  privacyAccepted: false,
  privacyAcceptedAviso: false,
  imageRightsAccepted: false,
  num_personas: 1,
  participantes: [{ nombre: '', apellidos: '', edad: '' }]
});

const successMessage = ref('');
const errorMessage = ref('');

// Sincronizar dinámicamente el número de formularios de participantes con numPersonas
// Vigila correctamente a num_personas
watch(() => formData.value.num_personas, (newVal) => {
  const count = parseInt(newVal) || 1;
  if (formData.value.participantes.length < count) {
    while (formData.value.participantes.length < count) {
      formData.value.participantes.push({ nombre: '', apellidos: '', edad: '' });
    }
  } else if (formData.value.participantes.length > count) {
    formData.value.participantes = formData.value.participantes.slice(0, count);
  }
});

// const actividadesFiltradas = computed(() => {
//   const hoy = new Date();
//   hoy.setHours(0, 0, 0, 0);
//   return actividades.value
//     .filter(actividad => {
//       const fechaActividad = new Date(actividad.fecha);
//       return fechaActividad >= hoy && actividad.reservas && actividad.publicar;
//     })
//     .sort((a, b) => {
//       const dateA = new Date(`${a.fecha}T${a.hora}`);
//       const dateB = new Date(`${b.fecha}T${b.hora}`);
//       return dateA - dateB;
//     });
// });

const actividadesFiltradas = computed(() => {
  const hoy = new Date();
  hoy.setHours(0, 0, 0, 0);

  return actividades.value
    .filter(actividad => {
      // Forzamos hora local añadiendo T00:00:00 para evitar errores de zona horaria
      const fechaActividad = new Date(actividad.fecha + 'T00:00:00');

      // Comprobamos fecha y aseguramos que reservas y publicar sean verdaderos (1 o true)
      return fechaActividad >= hoy && Number(actividad.reservas) === 1 && Number(actividad.publicar) === 1;
    })
    .sort((a, b) => {
      const dateA = new Date(`${a.fecha}T${a.hora}`);
      const dateB = new Date(`${b.fecha}T${b.hora}`);
      return dateA - dateB;
    });
});
const plazasDisponibles = computed(() => {
  if (!actividadSeleccionada.value) return 0;
  return actividadSeleccionada.value.plazas_totales - actividadSeleccionada.value.plazas_ocupadas;
});
const formatProyecto = (slug) => {
  const map = {
    'zalla': 'Zalla Natura',
    'flysch': 'Flysch en Familia',
    'naturgaua': 'Naturgaua',
    'eventos': 'Feria / Mercado',
    'general': 'Actividad',
  };
  return map[slug] || 'Actividad';
};

const formatearFecha = (fechaStr) => {
  if (!fechaStr) return '';
  const opciones = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(fechaStr).toLocaleDateString('es-ES', opciones);
};

// Modificamos el watch del ID para que busque o espere correctamente
watch(() => route.params.id, async (id) => {
  if (id) {
    // Si la lista aún está vacía (por la asincronía del fetch), podemos buscarla o asegurar que cargue
    if (actividades.value.length === 0) {
      try {
        const response = await fetch('http://localhost:5000/api/actividades');
        if (response.ok) {
          actividades.value = await response.json();
        }
      } catch (error) {
        console.error("Error al cargar la actividad seleccionada:", error);
      }
    }

    actividadSeleccionada.value = actividades.value.find(a => String(a.id) === String(id));
    if (actividadSeleccionada.value) {
      formData.value.imageRightsAccepted = false;
    }
  } else {
    actividadSeleccionada.value = null;
  }
}, { immediate: true });

const seleccionarActividad = (actividad) => {
  if (typeof window.gtag === 'function') {
    window.gtag('event', 'intento_reserva', {
      'event_category': 'Reservas',
      'event_label': actividad.titulo
    });
  }
  router.push({ name: 'reservaActividad', params: { id: actividad.id } });
};

const volverALista = () => {
  router.push('/calendario');
};

const submitForm = async () => {
  successMessage.value = '';
  errorMessage.value = '';

  const payload = {
    actividad_id: Number(actividadSeleccionada.value.id),
    nombre_contacto: formData.value.nombre,        // <-- Debe coincidir con schemas.py
    apellidos_contacto: formData.value.apellidos,  // <-- Debe coincidir con schemas.py
    email: formData.value.email,
    phone: formData.value.phone,
    num_personas: Number(formData.value.num_personas),
    permiso_fotos: Boolean(formData.value.imageRightsAccepted),
    observaciones: formData.value.message || "",   // <-- Mapeado a observaciones
    participantes: formData.value.participantes.map(p => ({
      nombre: p.nombre,
      apellidos: p.apellidos,
      edad: Number(p.edad)
    }))
  };

  try {
    const response = await fetch('http://localhost:5000/api/reservas', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = await response.json();

    if (response.ok) {
      mostrarModalExito.value = true; // <-- Asegúrate de que esté en true limpio
      successMessage.value = '¡Reserva realizada con éxito! Las plazas han quedado asignadas.';

      // Limpiamos el formulario por completo
      formData.value = {
        nombre: '',
        apellidos: '',
        email: '',
        phone: '',
        message: '',
        privacyAccepted: false,
        privacyAcceptedAviso: false,
        imageRightsAccepted: false,
        num_personas: 1,
        participantes: [{ nombre: '', apellidos: '', edad: '' }]
      };

      // ... limpiar formulario ...
    } else {
      // Si FastAPI devuelve un error de validación (array o string), lo capturamos bien
      const errorMsg = Array.isArray(data.detail)
        ? data.detail.map(err => `${err.loc.join('.')}: ${err.msg}`).join(', ')
        : (data.detail || 'Error al procesar la reserva.');
      throw new Error(errorMsg);
    }
  } catch (error) {
    errorMessage.value = error.message; // <-- Evitamos que salga [object Object]
    console.error(error);
  }
};
</script>

<style scoped>
/* ESTRUCTURA GENERAL */
.container {
  margin-top: 5rem;
}

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

/* PARTICIPANTES DINÁMICOS */
.participantes-container {
  background: #fdfdfd;
  border: 1px solid #e2e8f0;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 1.5rem;
}

.subtitulo-participantes {
  margin-top: 0;
  color: var(--shoftgreen);
  font-size: 1.1rem;
  border-bottom: 1px solid #edf2f7;
  padding-bottom: 8px;
  margin-bottom: 15px;
}

.participante-card {
  background: #f7fafc;
  border: 1px dashed #cbd5e0;
  padding: 12px;
  border-radius: 6px;
  margin-bottom: 12px;
}

.participante-card h4 {
  margin: 0 0 10px 0;
  font-size: 0.95rem;
  color: #4a5568;
}

/* BADGES */
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

.badge-large {
  display: inline-block;
  padding: 5px 15px;
  border-radius: 15px;
  color: white;
  font-weight: bold;
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
}

.badge-large.flysch {
  background-color: orange;
}

.badge-large.naturgaua {
  background-color: purple;
}

.badge-large.zalla {
  background-color: blue;
}

.badge-large.eventos {
  background-color: plum;
}

.badge-large.general {
  background-color: green;
}

/* INFO RÁPIDA */
.info-rapida {
  background: rgba(255, 255, 255, 0.5);
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

/* FORMULARIO */
.contact-container {
  max-width: 650px;
  margin: 1rem auto 1rem auto;
  padding: 2rem;
  border: 1px solid var(--shoftgreen);
  border-radius: 8px;
  box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
  background: white;
}

.header-reserva {
  margin-bottom: 1.5rem;
  border-bottom: 1px solid #eee;
  padding-bottom: 1rem;
}

.info-reserva-detalle {
  margin-bottom: 2rem;
  background: var(--megashoftgreen);
  padding: 1rem;
  border-radius: 0.5rem;
}

.info-reserva-detalle p {
  margin: 0.5rem 0;
}

.form-group {
  margin-bottom: 1.2rem;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 0.3rem;
  font-size: 0.95rem;
}

input,
select,
textarea {
  width: 100%;
  padding: 0.7rem;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

input:focus,
textarea:focus {
  outline: none;
  border-color: var(--shoftgreen);
  box-shadow: 0 0 0 2px var(--megashoftgreen);
}

.caja-fotos {
  background-color: #f9f9f9;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 20px;
}

.titulo-fotos {
  font-weight: bold;
  color: var(--shoftgreen);
  margin-top: 0;
  margin-bottom: 10px;
}

.nota-fotos {
  display: block;
  margin-top: 5px;
  font-size: 0.85rem;
  color: #666;
  font-style: italic;
}

.horizontalC {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  margin-bottom: 1rem;
}

.horizontalC input {
  width: auto;
}

.horizontalC label {
  font-weight: normal;
  font-size: 0.9rem;
}

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

.btn-submit:hover {
  background-color: var(--lightgreen);
}

.volver-btn {
  background: none;
  border: none;
  color: #666;
  text-decoration: underline;
  cursor: pointer;
  margin-top: 1rem;
}

.success-message {
  color: var(--green);
  text-align: center;
  margin-top: 1rem;
  font-weight: bold;
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 1rem;
}
</style>