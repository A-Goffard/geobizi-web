<template>
  <div class="container-cancelar">
    <div class="card-cancelacion">
      <h2 class="titulo-cancelacion">Cancelación de Reserva</h2>

      <!-- Estado: Procesando la petición -->
      <div v-if="cargando" class="estado-caja">
        <p class="texto-cargando">Procesando la cancelación y liberando plazas...</p>
      </div>

      <!-- Estado: Mensaje de resultado (Éxito o Error) -->
      <div v-else-if="mensajeEstado" class="estado-caja">
        <p :class="['mensaje-estado', error ? 'mensaje-error' : 'mensaje-exito']">
          {{ mensajeEstado }}
        </p>
        <button @click="router.push('/calendario')" class="btn-accion">
          Volver a actividades
        </button>
      </div>

      <!-- Estado inicial: Confirmación previa -->
      <div v-else class="contenido-cancelar">
        <p class="texto-descripcion">
          Has solicitado cancelar tu inscripción para esta actividad. Si continúas, tus plazas se liberarán de inmediato y se ofrecerán a la lista de espera u otras personas interesadas.
        </p>

        <div class="acciones-botones">
          <!-- Este botón abre el modal defensivo de confirmación -->
          <button @click="abrirConfirmacion" class="btn-alerta">
            Quiero cancelar mi reserva
          </button>
          <button @click="router.push('/calendario')" class="btn-secundario">
            No, mantener mi plaza
          </button>
        </div>
      </div>
    </div>

    <!-- Modal de confirmación defensiva / acción irreversible -->
    <div v-if="mostrarModal" class="modal-overlay" @click.self="cerrarConfirmacion">
      <div class="modal-tarjeta">
        <div class="modal-icono">⚠️</div>
        <h3 class="modal-titulo">¿Confirmas la cancelación definitiva?</h3>

        <div class="modal-alerta-box">
          <p class="modal-alerta-texto">
            <strong>Atención: Esta acción es totalmente irreversible.</strong>
          </p>
          <p class="modal-subtexto">
            Una vez confirmada, tu reserva quedará anulada y perderás tus plazas de forma inmediata sin posibilidad de recuperarlas.
          </p>
        </div>

        <div class="modal-acciones">
          <button @click="ejecutarCancelacion" class="btn-destructivo">
            Sí, cancelar definitivamente
          </button>
          <button @click="cerrarConfirmacion" class="btn-secundario">
            Volver atrás
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const cargando = ref(false);
const mostrarModal = ref(false);
const mensajeEstado = ref('');
const error = ref(false);
const token = route.query.token;

const abrirConfirmacion = () => {
  mostrarModal.value = true;
};

const cerrarConfirmacion = () => {
  mostrarModal.value = false;
};

const ejecutarCancelacion = async () => {
  cerrarConfirmacion();

  if (!token) {
    mensajeEstado.value = 'El enlace o token de cancelación no es válido.';
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
      error.value = false;
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

<style scoped>
.container-cancelar {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 12rem);
  padding: 4rem 1.5rem;
  background-color: var(--white);
  box-sizing: border-box;
}

.card-cancelacion {
  width: 100%;
  max-width: 520px;
  background-color: var(--white);
  border: 1px solid var(--supershoftbrownred);
  border-radius: 12px;
  padding: 2.5rem 2rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  text-align: center;
}

.titulo-cancelacion {
  color: var(--brownred);
  margin-top: 0;
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
}

.texto-descripcion,
.texto-cargando {
  color: var(--darkgrey);
  line-height: 1.6;
  margin: 0 0 2rem 0;
  font-size: 1rem;
}
</style>