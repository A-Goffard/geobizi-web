<template>
  <div class="container center" style="padding: 4rem 1rem;">
    <div class="card-cancelacion" style="max-width: 500px; margin: 0 auto; background: #fff; padding: 2rem; border-radius: 8px; border: 1px solid #ddd;">
      <h2 style="color: #b85d46; margin-top: 0;">⚠️ Cancelación de Reserva</h2>
      
      <div v-if="cargando">
        <p>Procesando la solicitud...</p>
      </div>

      <div v-else-if="mensajeEstado">
        <p :style="{ color: error ? 'red' : '#2c5e3b', fontWeight: 'bold' }">{{ mensajeEstado }}</p>
        <button @click="router.push('/calendario')" class="btn-reserva" style="margin-top: 1rem;">Volver al inicio</button>
      </div>

      <div v-else>
        <p>¿Estás totalmente seguro/a de que deseas cancelar tu reserva? Esta acción no se puede deshacer y tus plazas quedarán liberadas inmediatamente.</p>
        
        <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 2rem;">
          <button @click="ejecutarCancelacion" class="btn-reserva" style="background-color: #b85d46;">Sí, cancelar reserva</button>
          <button @click="router.push('/calendario')" class="volver-btn" style="background-color: #ccc; color: #333;">Mantener reserva</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'; // <-- Quitamos onMounted de aquí
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const cargando = ref(false);
const mensajeEstado = ref('');
const error = ref(false);
const token = route.query.token;

const ejecutarCancelacion = async () => {
  if (!token) {
    mensajeEstado.value = 'Token de cancelación no válido.';
    error.value = true;
    return;
  }

  cargando.value = true;
  try {
    const response = await fetch(`http://localhost:5000/api/token/${token}`, {
      method: 'DELETE'
    });
    
    const data = await response.json();
    if (response.ok) {
      mensajeEstado.value = 'Tu reserva ha sido cancelada con éxito. Las plazas han quedado liberadas.';
    } else {
      throw new Error(data.detail || 'No se pudo cancelar la reserva.');
    }
  } catch (err) {
    mensajeEstado.value = err.message;
    error.value = true;
  } finally {
    cargando.value = false;
  }
};
</script>