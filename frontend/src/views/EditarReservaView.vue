<template>
  <div class="container" style="padding: 4rem 1rem; max-width: 600px; margin: 0 auto;">
    <div class="card" style="background: #fff; padding: 2rem; border-radius: 8px; border: 1px solid #ddd;">
      <h2 style="color: #2c5e3b; margin-top: 0;">✏️ Modificar Reserva</h2>

      <div v-if="cargando">
        <p>Cargando datos de tu reserva...</p>
      </div>

      <div v-else-if="errorToken">
        <p style="color: red; font-weight: bold;">{{ errorToken }}</p>
        <button @click="router.push('/calendario')" class="btn-reserva" style="margin-top: 1rem;">Volver al inicio</button>
      </div>

      <form v-else @submit.prevent="actualizarReserva">
        <p><strong>Actividad:</strong> {{ actividad.titulo }}</p>
        
        <h3>Datos de contacto</h3>
        <div class="form-group">
          <label>Nombre:</label>
          <input type="text" v-model="reserva.nombre_contacto" required class="form-control">
        </div>
        <div class="form-group">
          <label>Apellidos:</label>
          <input type="text" v-model="reserva.apellidos_contacto" required class="form-control">
        </div>
        <div class="form-group">
          <label>Correo Electrónico:</label>
          <input type="email" v-model="reserva.email" required class="form-control">
        </div>
        <div class="form-group">
          <label>Teléfono:</label>
          <input type="tel" v-model="reserva.phone" required class="form-control">
        </div>
        <div class="form-group">
          <label>Observaciones:</label>
          <textarea v-model="reserva.observaciones" class="form-control"></textarea>
        </div>

        <div style="display: flex; gap: 1rem; margin-top: 2rem;">
          <button type="submit" class="btn-reserva">Guardar Cambios</button>
          <button type="button" @click="router.push('/calendario')" class="volver-btn" style="background: #ccc; color: #333;">Cancelar</button>
        </div>

        <p v-if="mensajeExito" style="color: #2c5e3b; font-weight: bold; margin-top: 1rem;">{{ mensajeExito }}</p>
        <p v-if="mensajeError" style="color: red; font-weight: bold; margin-top: 1rem;">{{ mensajeError }}</p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();
const token = route.query.token;

const cargando = ref(true);
const errorToken = ref('');
const reserva = ref({});
const actividad = ref({});
const mensajeExito = ref('');
const mensajeError = ref('');

onMounted(async () => {
  if (!token) {
    errorToken.value = 'Enlace de modificación no válido.';
    cargando.value = false;
    return;
  }

  try {
    const response = await fetch(`http://localhost:5000/api/token/${token}`);
    const data = await response.json();
    if (response.ok) {
      reserva.value = data.reserva;
      actividad.value = data.actividad;
    } else {
      throw new Error(data.detail || 'No se pudo cargar la reserva.');
    }
  } catch (err) {
    errorToken.value = err.message;
  } finally {
    cargando.value = false;
  }
});

const actualizarReserva = async () => {
  mensajeExito.value = '';
  mensajeError.value = '';

  try {
    const response = await fetch(`http://localhost:5000/api/token/${token}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(reserva.value)
    });
    const data = await response.json();
    if (response.ok) {
      mensajeExito.value = '¡Datos actualizados con éxito!';
    } else {
      throw new Error(data.detail || 'Error al actualizar.');
    }
  } catch (err) {
    mensajeError.value = err.message;
  }
};
</script>