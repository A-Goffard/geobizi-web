<template>
  <div class="container">

    <!-- VISTA 1: LISTADO DE ACTIVIDADES DISPONIBLES (GRID) -->
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

          <div class="acciones-card">
            <a 
              v-if="actividad.linkReserva" 
              :href="actividad.linkReserva" 
              target="_blank"
              class="btn-reserva btn-externo"
              @click.stop
            >
              Inscribirse (web externa)
            </a>

            <button 
              v-else-if="actividad.plazas_totales && actividad.plazas_ocupadas >= actividad.plazas_totales" 
              @click.stop="seleccionarActividad(actividad)" 
              class="btn-reserva btn-espera"
            >
              ⚠️ Plazas agotadas · Lista de espera
            </button>

            <button 
              v-else 
              @click.stop="seleccionarActividad(actividad)" 
              class="btn-reserva"
            >
              Inscribirse / Reservar
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- VISTA 2: FORMULARIO DINÁMICO (RESERVA O LISTA DE ESPERA) -->
    <div v-else class="contact-container">
      <div class="header-reserva">
        <span class="badge-large" :class="actividadSeleccionada.proyecto || 'general'">
          {{ formatProyecto(actividadSeleccionada.proyecto) }}
        </span>
        <h1>{{ esModoListaEspera ? 'Lista de espera:' : 'Reserva:' }} {{ actividadSeleccionada.titulo }}</h1>
      </div>

      <div class="info-reserva-detalle">
        <p><strong>Fecha:</strong> {{ formatearFecha(actividadSeleccionada.fecha) }}</p>
        <p><strong>Hora:</strong> {{ actividadSeleccionada.hora }}</p>
        <p v-if="actividadSeleccionada.ubicacion"><strong>Ubicación:</strong> {{ actividadSeleccionada.ubicacion }}</p>
        <p v-if="actividadSeleccionada.precio"><strong>Precio:</strong> {{ actividadSeleccionada.precio }} € por persona</p>
        <p v-if="actividadSeleccionada.descripcion"><strong>Descripción:</strong> {{ actividadSeleccionada.descripcion }}</p>
        <p v-if="actividadSeleccionada.detalles"><strong>Detalles:</strong> {{ actividadSeleccionada.detalles }}</p>
        <p v-if="actividadSeleccionada.oharrak"><strong>Notas:</strong> {{ actividadSeleccionada.oharrak }}</p>
      </div>

      <!-- CASO 1: Aforo 100% agotado de antemano -->
      <div v-if="actividadTotalmenteAgotada" class="caja-aviso-espera">
        <h3 class="titulo-espera">⚠️ Aforo completo</h3>
        <p>
          No quedan plazas libres para esta actividad. Rellena los datos de tu grupo para entrar en la 
          <strong>lista de espera</strong>. Si se liberan plazas suficientes para todos vosotros, os avisaremos por riguroso orden de registro.
        </p>
      </div>

      <!-- CASO 2: Quedan plazas libres, pero se han añadido más asistentes de los disponibles -->
      <div v-else-if="plazasInsuficientes" class="caja-aviso-espera">
        <h3 class="titulo-espera">⚠️ No quedan suficientes plazas para todo tu grupo</h3>
        <p>
          Actualmente solo {{ plazasDisponibles === 1 ? 'queda' : 'quedan' }} 
          <strong>{{ plazasDisponibles }} {{ plazasDisponibles === 1 ? 'plaza libre' : 'plazas libres' }}</strong>, pero has añadido fichas para <strong>{{ totalAsistentes }} asistentes</strong>.
        </p>
        <p style="margin-top: 0.5rem;">
          Para no separar al grupo, podéis continuar y <strong>quedaréis anotados en la lista de espera juntos</strong>. Si preferís reservar ahora mismo solo las plazas que quedan libres:
        </p>
        <button 
          type="button" 
          @click="ajustarAPlazasDisponibles" 
          class="btn-ajustar-plazas"
        >
          Ajustar a {{ plazasDisponibles }} {{ plazasDisponibles === 1 ? 'asistente' : 'asistentes' }} y reservar ahora
        </button>
      </div>

      <!-- CASO 3: Hay plazas libres suficientes -->
      <div v-else class="aviso-plazas" :class="{ 'casi-lleno': plazasDisponibles <= 3 }">
        <p>
          Plazas libres disponibles: <strong>{{ plazasDisponibles }}</strong> &nbsp;|&nbsp; 
          Asistentes a inscribir: <strong>{{ totalAsistentes }}</strong>
        </p>
      </div>

      <!-- FORMULARIO ÚNICO -->
      <form @submit.prevent="enviarFormulario">
        <h3 class="seccion-titulo">Datos de la persona responsable / contacto</h3>

        <div class="form-group">
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" v-model="formData.nombre" required />
        </div>

        <div class="form-group">
          <label for="apellidos">Apellidos:</label>
          <input type="text" id="apellidos" v-model="formData.apellidos" required />
        </div>

        <div class="form-group">
          <label for="email">Correo Electrónico:</label>
          <input type="email" id="email" v-model="formData.email" required />
        </div>

        <div class="form-group">
          <label for="phone">Teléfono de contacto:</label>
          <input type="tel" id="phone" v-model="formData.phone" required />
        </div>

        <!-- LISTADO DINÁMICO DE ASISTENTES (FICHA POR PERSONA) -->
        <h3 class="seccion-titulo">
          Asistentes ({{ totalAsistentes }} {{ totalAsistentes === 1 ? 'plaza' : 'plazas' }})
        </h3>
        <p class="texto-ayuda">
          Indica los datos de cada persona participante (incluyéndote a ti si vas a asistir a la actividad).
        </p>

<div class="participantes-lista">
  <ParticipanteCard
    v-for="(p, index) in formData.participantes"
    :key="index"
    v-model="formData.participantes[index]"
    :index="index"
    :can-remove="formData.participantes.length > 1"
    @remove="eliminarAsistente(index)"
  />
</div>

        <!-- Botón para sumar acompañantes (se deshabilita al alcanzar el aforo total) -->
        <button 
          type="button" 
          @click="agregarAsistente" 
          class="btn-anadir-asistente"
          :disabled="totalAsistentes >= topeMaximo"
        >
          ➕ Añadir otro asistente
        </button>

        <div class="form-group">
          <label for="message">Mensaje / Observaciones:</label>
          <textarea id="message" v-model="formData.message"></textarea>
        </div>

        <!-- Permisos de imagen -->
        <div 
          v-if="!esModoListaEspera && ['zalla', 'flysch', 'naturgaua', 'eventos', 'general'].includes(actividadSeleccionada.proyecto)" 
          class="caja-fotos"
        >
          <p class="titulo-fotos">📸 Permisos de imagen</p>
          <div class="horizontalC">
            <input type="checkbox" id="imageRights" v-model="formData.imageRightsAccepted" />
            <label for="imageRights">
              Autorizo a Geobizi a tomar imágenes durante la actividad para enviárnoslas de recuerdo y/o usarlas en sus redes sociales/web con fines divulgativos.
              <br />
              <span class="nota-fotos">
                *Priorizamos siempre planos generales o de espaldas, respetando la privacidad de los menores.
              </span>
            </label>
          </div>
        </div>

        <div class="horizontalC">
          <input type="checkbox" id="privacy" v-model="formData.privacyAccepted" required />
          <label for="privacy">
            He leído y acepto la <a href="/politicadeprivacidad" target="_blank">política de privacidad</a>.
          </label>
        </div>

        <div class="horizontalC">
          <input type="checkbox" id="privacyAviso" v-model="formData.privacyAcceptedAviso" required />
          <label for="privacyAviso">
            Entiendo las condiciones de participación. <b>Revisa tu carpeta de spam</b> si no ves el correo de confirmación.
          </label>
        </div>

        <div class="center">
          <button 
            type="submit" 
            class="btn-submit" 
            :class="{ 'btn-espera': esModoListaEspera }"
            :disabled="enviando"
          >
            {{ enviando ? 'Enviando...' : textoBotonEnvio }}
          </button>
        </div>

        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </form>

      <div class="center">
        <button @click="volverALista" class="volver-btn">← Volver a actividades</button>
      </div>
    </div>

    <!-- MODAL DE ÉXITO BLOQUEANTE -->
<!-- Reemplaza el div manual .modal-overlay por esto: -->
<ModalExito
  :visible="mostrarModalExito"
  :es-lista-espera="esListaEsperaModal"
  :mensaje="successMessage"
  @cerrar="cerrarModalYVolver"
/>

  </div>
</template>

<script setup>
import ParticipanteCard from '@/components/reservas/ParticipanteCard.vue';
import ModalExito from '@/components/reservas/ModalExito.vue';
import { ref, computed, watch, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useHead } from '@vueuse/head';
// Importamos los endpoints
import { ENDPOINTS } from '@/config/api';

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
const esListaEsperaModal = ref(false);
const enviando = ref(false);
const successMessage = ref('');
const errorMessage = ref('');

const formData = ref({
  nombre: '',
  apellidos: '',
  email: '',
  phone: '',
  message: '',
  privacyAccepted: false,
  privacyAcceptedAviso: false,
  imageRightsAccepted: false,
  participantes: [{ nombre: '', apellidos: '', edad: '' }]
});

const cargarActividades = async () => {
  try {
    // Cambia la URL fija por ENDPOINTS.ACTIVIDADES:
const response = await fetch(ENDPOINTS.ACTIVIDADES);
    if (response.ok) {
      actividades.value = await response.json();
      verificarSeleccionActividad();
    }
  } catch (error) {
    console.error("Error al conectar con la API de actividades:", error);
  }
};

const verificarSeleccionActividad = () => {
  const id = route.params.id;
  if (id) {
    const actividadActualizada = actividades.value.find(a => String(a.id) === String(id));
    if (actividadActualizada) {
      actividadSeleccionada.value = actividadActualizada;
    }
  } else {
    actividadSeleccionada.value = null;
  }
};

onMounted(() => {
  cargarActividades();
});

watch(() => route.params.id, () => {
  verificarSeleccionActividad();
});

// Control dinámico de asistentes
const totalAsistentes = computed(() => {
  return formData.value.participantes.length;
});

// El tope máximo ahora es reactivo y toma las plazas totales de la actividad (o 20 por defecto)
const topeMaximo = computed(() => {
  return actividadSeleccionada.value?.plazas_totales || 20;
});

const agregarAsistente = () => {
  if (formData.value.participantes.length >= topeMaximo.value) {
    alert(`No puedes añadir más de ${topeMaximo.value} personas (aforo máximo de la actividad).`);
    return;
  }
  formData.value.participantes.push({ nombre: '', apellidos: '', edad: '' });
};

const eliminarAsistente = (index) => {
  if (formData.value.participantes.length > 1) {
    formData.value.participantes.splice(index, 1);
  }
};

const ajustarAPlazasDisponibles = () => {
  const disponibles = plazasDisponibles.value;
  if (disponibles > 0 && formData.value.participantes.length > disponibles) {
    formData.value.participantes = formData.value.participantes.slice(0, disponibles);
  }
};

const actividadesFiltradas = computed(() => {
  const hoy = new Date();
  hoy.setHours(0, 0, 0, 0);

  return actividades.value
    .filter(actividad => {
      const fechaActividad = new Date(actividad.fecha + 'T00:00:00');
      return fechaActividad >= hoy && Number(actividad.reservas) === 1 && Number(actividad.publicar) === 1;
    })
    .sort((a, b) => new Date(`${a.fecha}T${a.hora}`) - new Date(`${b.fecha}T${b.hora}`));
});

// Plazas y estados
const plazasDisponibles = computed(() => {
  if (!actividadSeleccionada.value || actividadSeleccionada.value.plazas_totales === undefined) return 0;
  return Math.max(0, actividadSeleccionada.value.plazas_totales - actividadSeleccionada.value.plazas_ocupadas);
});

const actividadTotalmenteAgotada = computed(() => {
  return plazasDisponibles.value <= 0;
});

const plazasInsuficientes = computed(() => {
  return plazasDisponibles.value > 0 && totalAsistentes.value > plazasDisponibles.value;
});

const esModoListaEspera = computed(() => {
  return actividadTotalmenteAgotada.value || plazasInsuficientes.value;
});

const textoBotonEnvio = computed(() => {
  const total = totalAsistentes.value;
  if (esModoListaEspera.value) {
    return `Unir al grupo a la lista de espera (${total} ${total === 1 ? 'plaza' : 'plazas'})`;
  }
  return `Confirmar Reserva (${total} ${total === 1 ? 'plaza' : 'plazas'})`;
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

const seleccionarActividad = (actividad) => {
  router.push({ name: 'reservaActividad', params: { id: actividad.id } });
};

const volverALista = () => {
  router.push('/calendario');
};

const cerrarModalYVolver = () => {
  mostrarModalExito.value = false;
  router.push('/calendario');
};

const enviarFormulario = async () => {
  errorMessage.value = '';
  enviando.value = true;

  if (esModoListaEspera.value) {
    await ejecutarListaEspera();
  } else {
    await ejecutarReserva();
  }

  enviando.value = false;
};

const ejecutarReserva = async () => {
  const payload = {
    actividad_id: Number(actividadSeleccionada.value.id),
    nombre_contacto: formData.value.nombre,
    apellidos_contacto: formData.value.apellidos,
    email: formData.value.email,
    phone: formData.value.phone,
    num_personas: totalAsistentes.value,
    permiso_fotos: Boolean(formData.value.imageRightsAccepted),
    observaciones: formData.value.message || "",
    participantes: formData.value.participantes.map(p => ({
      nombre: p.nombre,
      apellidos: p.apellidos,
      edad: Number(p.edad)
    }))
  };

  try {
    const res = await fetch(ENDPOINTS.RESERVAS, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = await res.json();

    if (res.ok) {
      esListaEsperaModal.value = false;
      successMessage.value = '¡Reserva realizada con éxito! Las plazas han quedado asignadas.';
      mostrarModalExito.value = true;
    } else {
      // 1. Extraer el mensaje del backend
      const errorMsg = Array.isArray(data.detail)
        ? data.detail.map(e => `${e.loc.join('.')}: ${e.msg}`).join(', ')
        : (data.detail || 'Error al procesar la reserva.');

      // 2. Si el fallo es por falta de plazas (alguien reservó antes)
      if (res.status === 400 && (errorMsg.includes('plazas') || errorMsg.includes('libres'))) {
        // Refrescamos los datos reales desde el servidor
        await cargarActividades();
        
        // Mensaje pedagógico informando de la transición a lista de espera
        errorMessage.value = '⚠️ Las últimas plazas acaban de reservarse hace un instante. Hemos actualizado el formulario para que puedas apuntar a tu grupo a la lista de espera directamente.';
        return;
      }

      throw new Error(errorMsg);
    }
  } catch (err) {
    errorMessage.value = err.message;
  }
};

const ejecutarListaEspera = async () => {
  const payload = {
    actividad_id: Number(actividadSeleccionada.value.id),
    nombre_contacto: formData.value.nombre,
    apellidos_contacto: formData.value.apellidos,
    email: formData.value.email,
    phone: formData.value.phone,
    num_personas: totalAsistentes.value,
    permiso_fotos: Boolean(formData.value.imageRightsAccepted),
    observaciones: formData.value.message || "",
    participantes: formData.value.participantes.map(p => ({
      nombre: p.nombre,
      apellidos: p.apellidos,
      edad: Number(p.edad)
    }))
  };

  try {
    const res = await fetch(ENDPOINTS.LISTA_ESPERA, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = await res.json();
    if (res.ok) {
      esListaEsperaModal.value = true;
      successMessage.value = data.message || 'Tu grupo ha quedado registrado en la lista de espera. Si se liberan plazas suficientes, os avisaremos por correo.';
      mostrarModalExito.value = true;
    } else {
      const errorMsg = Array.isArray(data.detail)
        ? data.detail.map(e => `${e.loc.join('.')}: ${e.msg}`).join(', ')
        : (data.detail || 'Error al registrarse en la lista de espera.');
      throw new Error(errorMsg);
    }
  } catch (err) {
    errorMessage.value = err.message;
  }
};
</script>

<style scoped>
.container {
  margin-top: 5rem;
}

.general-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  padding: 2rem;
}

.container-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
}

/* Tarjetas */
.card {
  width: 320px;
  padding: 20px;
  background-color: var(--megashoftgreen);
  border: 1px solid var(--shoftgreen);
  border-radius: 0.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
  cursor: pointer;
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

.acciones-card {
  margin-top: 1rem;
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
}

.btn-externo {
  display: block;
  text-decoration: none;
  background-color: var(--lightblue);
  color: var(--white);
}

.btn-externo:hover {
  background-color: var(--blue);
}

/* Imágenes con efecto hover */
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

.info-rapida {
  background: rgba(255, 255, 255, 0.5);
  padding: 0.8rem;
  border-radius: 0.5rem;
  font-size: 0.9rem;
}

.info-rapida p {
  margin: 4px 0;
  color: var(--darkgrey);
}

/* Contenedor del Formulario */
.contact-container {
  max-width: 680px;
  margin: 1rem auto 3rem auto;
  padding: 2rem;
  border: 1px solid var(--shoftgreen);
  border-radius: 8px;
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.08);
  background: var(--white);
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

.seccion-titulo {
  color: var(--green);
  border-bottom: 2px solid var(--supershoftgreen);
  padding-bottom: 0.4rem;
  margin: 2rem 0 1rem 0;
}

.texto-ayuda {
  color: var(--grey);
  font-size: 0.85rem;
  margin: -0.5rem 0 1.25rem 0;
}

/* Cajas de aviso */
.caja-aviso-espera {
  background-color: var(--yellow);
  border-left: 4px solid var(--orange);
  padding: 1rem 1.25rem;
  border-radius: 4px;
  margin-bottom: 1.5rem;
}

.titulo-espera {
  color: var(--darkyellow);
  margin-top: 0;
  margin-bottom: 0.5rem;
}

.caja-aviso-espera p {
  color: var(--darkgrey);
  font-size: 0.95rem;
  line-height: 1.5;
  margin: 0;
}

.btn-ajustar-plazas {
  margin-top: 0.8rem;
  background-color: var(--white);
  color: var(--darkgreen);
  border: 1px solid var(--green);
  border-radius: 4px;
  padding: 0.45rem 0.9rem;
  font-size: 0.85rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.2s ease, color 0.2s ease;
}

.btn-ajustar-plazas:hover {
  background-color: var(--green);
  color: var(--white);
}

.aviso-plazas {
  padding: 0.6rem 0.8rem;
  border-radius: 4px;
  margin-bottom: 1rem;
  background-color: var(--megashoftgreen);
  color: var(--darkgreen);
  font-size: 0.95rem;
}

.aviso-plazas.casi-lleno {
  background-color: var(--yellow);
  color: var(--darkyellow);
}

/* Formulario */
.form-group {
  margin-bottom: 1.2rem;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 0.3rem;
  font-size: 0.95rem;
  color: var(--darkgrey);
}

input, select, textarea {
  width: 100%;
  padding: 0.7rem;
  font-size: 1rem;
  border: 1px solid var(--lightgrey);
  border-radius: 4px;
  box-sizing: border-box;
}

input:focus, textarea:focus {
  outline: none;
  border-color: var(--green);
  box-shadow: 0 0 0 3px var(--supershoftgreen);
}

/* Fichas dinámicas de asistentes */
.participantes-lista {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1.2rem;
}

.participante-card {
  background-color: var(--megashoftgreen);
  border: 1px solid var(--supershoftgreen);
  border-radius: 6px;
  padding: 1.2rem;
}

.participante-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.participante-titulo {
  color: var(--darkgreen);
  margin: 0;
  font-size: 0.95rem;
}

.btn-quitar {
  background-color: var(--supershoftbrownred);
  border: 1px solid var(--lightbrownred);
  color: var(--brownred);
  border-radius: 4px;
  padding: 0.3rem 0.65rem;
  font-size: 0.8rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.btn-quitar:hover {
  background-color: var(--brownred);
  color: var(--white);
}

.btn-anadir-asistente {
  background-color: var(--megashoftgreen);
  border: 1px dashed var(--green);
  color: var(--darkgreen);
  border-radius: 6px;
  padding: 0.65rem 1rem;
  font-size: 0.9rem;
  font-weight: bold;
  cursor: pointer;
  width: 100%;
  margin-bottom: 1.5rem;
  transition: background-color 0.2s ease, border-color 0.2s ease;
}

.btn-anadir-asistente:hover {
  background-color: var(--supershoftgreen);
  border-color: var(--darkgreen);
}

.participante-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 90px;
  gap: 0.75rem;
}

.form-subgroup {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
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
  color: var(--green);
  margin-top: 0;
  margin-bottom: 10px;
}

.nota-fotos {
  display: block;
  margin-top: 5px;
  font-size: 0.85rem;
  color: var(--grey);
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
  margin-top: 3px;
}

.horizontalC label {
  font-weight: normal;
  font-size: 0.9rem;
}

.center {
  text-align: center;
}

/* Responsive */
@media (max-width: 650px) {
  .participante-grid {
    grid-template-columns: 1fr;
  }
}
</style>