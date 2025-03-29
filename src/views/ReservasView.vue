<template>
  <div class="contenedor-principal">
    <div class="contact-container">
      <h1>Reserva de actividades</h1>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="titulo">Título de la actividad:</label>
          <select id="titulo" v-model="tituloSeleccionado" @change="actualizarFechas" required>
            <option value="" disabled>Selecciona una actividad</option>
            <option v-for="titulo in titulosUnicos" :key="titulo" :value="titulo">
              {{ titulo }}
            </option>
          </select>
        </div>
        <div class="form-group" v-if="fechasDisponibles.length > 0">
          <label for="fecha">Fecha y hora:</label>
          <select id="fecha" v-model="formData.actividad" required>
            <option value="" disabled>Selecciona una fecha y hora</option>
            <option v-for="fecha in fechasDisponibles" :key="fecha.id" :value="`${fecha.fecha} - ${fecha.hora}`">
              {{ fecha.fecha }} - {{ fecha.hora }}
            </option>
          </select>
        </div>
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
          <input type="checkbox" id="privacy" v-model="formData.privacyAccepted" required>
          <label for="privacy">
            Es una petición de reserva, no una reserva confirmada. Nos pondremos en contacto contigo para confirmar la disponibilidad.
          </label>
        </div>
        <div class="center">
          <button type="submit">Pedir reserva</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import actividades from '@/assets/json/actividades.json'

const formData = ref({
  nombre: '',
  apellidos: '',
  email: '',
  phone: '',
  actividad: '',
  message: '',
  privacyAccepted: false,
  numPersonas: 1 // Nuevo campo para el número de personas
})

const tituloSeleccionado = ref('')
const fechasDisponibles = ref([])

// Obtener títulos únicos
const titulosUnicos = computed(() => {
  const hoy = new Date()
  const actividadesFiltradas = actividades.filter(actividad => new Date(actividad.fecha) >= hoy)
  return [...new Set(actividadesFiltradas.map(actividad => actividad.titulo))]
})

// Actualizar las fechas disponibles según el título seleccionado
const actualizarFechas = () => {
  const hoy = new Date()
  fechasDisponibles.value = actividades.filter(
    actividad => actividad.titulo === tituloSeleccionado.value && new Date(actividad.fecha) >= hoy
  )
}

const submitForm = () => {
  if (!formData.value.privacyAccepted) {
    alert('Debes aceptar la política de privacidad para enviar el mensaje.')
    return
  }

  // Crear el mensaje de reserva
  const messageData = {
    nombre: formData.value.nombre,
    apellidos: formData.value.apellidos,
    email: formData.value.email,
    phone: formData.value.phone,
    actividad: formData.value.actividad,
    numPersonas: formData.value.numPersonas, // Incluir el número de personas
    message: formData.value.message
  }

  const emailRecipient = 'geobizi@hotmail.com'
  const emailBody = `
    Nombre: ${messageData.nombre}\n
    Apellidos: ${messageData.apellidos}\n
    Correo Electrónico: ${messageData.email}\n
    Teléfono: ${messageData.phone}\n
    Actividad: ${messageData.actividad}\n
    Número de personas: ${messageData.numPersonas}\n
    Mensaje: ${messageData.message}
  `
  console.log('Enviando correo electrónico a', emailRecipient, 'con el siguiente contenido:')
  console.log(emailBody)

  // Reiniciar el formulario después de enviar
  formData.value.nombre = ''
  formData.value.apellidos = ''
  formData.value.email = ''
  formData.value.phone = ''
  formData.value.actividad = ''
  formData.value.message = ''
  formData.value.privacyAccepted = false
  formData.value.numPersonas = 1

  alert('Mensaje enviado correctamente.')
}
</script>

<style scoped>
.contenedor-principal {
  padding-top: 7rem;
  background-color: rgb(255, 255, 255);
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

}

@media (max-width: 613px) {
  .contact-container {
    padding: 1rem;
    margin: 0.5rem;
  }
}
</style>
