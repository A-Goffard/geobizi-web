<template>
  <div class="container">
    <div v-if="!actividadSeleccionada" class="general-container">
      <h1>Actividades disponibles</h1>
      <div class="container">
        <div 
          v-for="actividad in actividadesFiltradas" 
          :key="actividad.id" 
          class="card" 
          @click="seleccionarActividad(actividad)"
        >

          <h2>{{ actividad.titulo }}</h2>
          <div class="img-hover-container">
            <img
              :src="actividad.imagen1"
              alt="Imagen de la actividad"
              class="img-base"
            />
            <img
              :src="actividad.imagen2"
              alt="Imagen secundaria de la actividad"
              class="img-hover"
            />
          </div>
          <p>{{ actividad.descripcion1 }}</p>
          <p><strong>Fecha:</strong> {{ actividad.fecha }}</p>
          <p><strong>Hora:</strong> {{ actividad.hora }}</p>
          <p><strong>Precio:</strong> {{ actividad.precio }} € por persona</p>
        </div>
      </div>
    </div>

    <div v-else class="contact-container">
      <h1>Reserva de {{ actividadSeleccionada.titulo }}</h1>
      <p class="fecha-reserva">
        <strong>Fecha:</strong> {{ actividadSeleccionada.fecha }} &nbsp; <strong>Hora:</strong> {{ actividadSeleccionada.hora }}
      </p>
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
        <div class="form-group">
          <label for="numPersonas">Número de personas:</label>
          <input type="number" id="numPersonas" v-model="formData.numPersonas" min="1" required>
        </div>
        <div class="form-group">
          <label for="message">Mensaje:</label>
          <textarea id="message" v-model="formData.message" required></textarea>
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
            Es una petición de reserva, no una reserva confirmada. Nos pondremos en contacto contigo para confirmar la disponibilidad.
          </label>
        </div>
        <div class="center">
          <button type="submit">Pedir reserva</button>
        </div>
        <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </form>
      <div class="center">
        <button @click="volverALista" class="volver-btn">Volver a la lista de actividades</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import actividades from '@/assets/json/actividades.json';

const route = useRoute();
const router = useRouter();

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
  numPersonas: 1
});
const successMessage = ref('');
const errorMessage = ref('');

// Filtrar actividades futuras con reservas habilitadas
const actividadesFiltradas = computed(() => {
  const hoy = new Date();
  return actividades.filter(
    actividad => new Date(actividad.fecha) >= hoy && actividad.reservas
  );
});

// Selección por URL
watch(
  () => route.params.id,
  (id) => {
    if (id) {
      actividadSeleccionada.value = actividadesFiltradas.value.find(a => String(a.id) === String(id));
      if (actividadSeleccionada.value) {
        formData.value.actividad = `${actividadSeleccionada.value.fecha} - ${actividadSeleccionada.value.hora}`;
      }
    } else {
      actividadSeleccionada.value = null;
    }
  },
  { immediate: true }
);

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
        successMessage.value = 'Reserva enviada correctamente.';
        formData.value = {
          nombre: '',
          apellidos: '',
          email: '',
          phone: '',
          actividad: '',
          message: '',
          privacyAccepted: false,
          privacyAcceptedAviso: false,
          numPersonas: 1
        };
      } else {
        throw new Error('Error al enviar la reserva.');
      }
    })
    .catch(error => {
      errorMessage.value = 'Hubo un error al enviar la reserva. Por favor, inténtalo de nuevo.';
      console.error('Error:', error);
    });
};
</script>

<style scoped>
  .container {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    justify-content: center;
  }
.general-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  padding-top: 7rem;
  padding-left: 2rem;
  padding-right: 2rem;
  padding-bottom: 2rem;
}
.contact-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 2rem;
  border: 1px solid var(--shoftgreen);
  border-radius: 8px;
  box-shadow: 0px 0px 10px rgba(49, 49, 49, 0.7);
  padding-bottom: 2rem;
  margin-top: 7rem;
  margin-bottom: 3rem;
}
.card {
  width: 300px;
  padding: 20px;
  background-color: var(--megashoftgreen);
  border: 1px solid var(--shoftgreen);
  border-radius: 0.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
  cursor: pointer;
}
.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}
.card h2 {
  margin-top: 0;
}
.card p {
  color: var(--darkgrey);
}
img {
  width: 100%;
  border-radius: 0.5rem;
}
.horizontalC { 
  margin: 1rem;
  display: flex;
  flex-direction: row;
  gap: 1rem;
}
.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  font-weight: bold;
}

input[type="text"],
input[type="email"],
input[type="tel"],
input[type="number"],
select,
textarea {
  width: 100%;
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid var(--shoftgreen);
  background-color: var(--megashoftgreen);
  border-radius: 4px;
}

button {
  padding: 0.75rem 1rem;
  background-color: var(--green);
  color: var(--white);
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: var(--lightgreen);
}

a{
  color: var(--green);
}

.center {
  display: flex;
  justify-content: center;
  margin-top: 1rem;
}

.volver-btn {
  margin-top: 1rem;
  padding: 0.75rem 1rem;
  background-color: var(--green);
  color: var(--white);
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s ease;
}

.volver-btn:hover {
  background-color: var(--lightgreen);
}

@media (max-width: 613px) {
  .contact-container {
    padding: 1rem;
    margin: 0.5rem;
    margin-top: 5rem; /* Ajuste adicional para evitar que quede debajo del menú en móvil */
  }
  .general-container {
    padding: 1rem;
    margin: 0.5rem;
    margin-top: 2rem;
  }
}

.success-message {
  color: var(--green);
  text-align: center;
  margin-top: 1rem;
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 1rem;
}

.fecha-reserva {
    font-size: 1.1rem;
    margin-bottom: 1.5rem;
    color: var(--darkgrey);
    text-align: center;
  }

.img-hover-container {
  position: relative;
  width: 100%;
  aspect-ratio: 4/3;
  overflow: hidden;
  border-radius: 0.5rem;
}

.img-hover-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 0.5rem;
  transition: opacity 0.5s ease;
  position: absolute;
  top: 0;
  left: 0;
}

.img-hover-container .img-base {
  z-index: 1;
  opacity: 1;
  position: relative;
}

.img-hover-container .img-hover {
  z-index: 2;
  opacity: 0;
}

.card:hover .img-hover-container .img-hover {
  opacity: 1;
}

.card:hover .img-hover-container .img-base {
  opacity: 0;
}
</style>
