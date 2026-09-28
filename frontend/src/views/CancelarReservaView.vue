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

      <!-- Estado inicial: Pregunta básica -->
      <div v-else class="contenido-cancelar">
        <p class="texto-descripcion">
          Has solicitado cancelar tu inscripción para esta actividad. Si continúas, tus plazas se pondrán a disposición de otras personas interesadas.
        </p>

        <div class="acciones-botones">
          <!-- Este botón abre el modal de seguridad, no borra aún -->
          <button @click="abrirConfirmacion" class="btn-alerta">
            Quiero cancelar mi reserva
          </button>
          <button @click="router.push('/calendario')" class="btn-secundario">
            No, mantener mi plaza
          </button>
        </div>
      </div>
    </div>

    <!-- MODAL DE DOBLE VERIFICACIÓN / ACCIÓN IRREVERSIBLE -->
    <div v-if="mostrarModal" class="modal-overlay">
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
  padding: 7rem 1.5rem 3rem 1.5rem;
  background-color: var(--white);
  box-sizing: border-box;
}

.card-cancelacion {
  width: 100%;
  max-width: 520px;
  background-color: var(--white);
  border: 1px solid var(--lightgrey);
  border-radius: 0.5rem;
  padding: 2.5rem 2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
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

.estado-caja {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
}

.mensaje-estado {
  font-weight: bold;
  font-size: 1.05rem;
  line-height: 1.5;
  margin: 0;
}

.mensaje-exito {
  color: var(--darkgreen);
}

.mensaje-error {
  color: var(--brownred);
}

.acciones-botones {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* Botón inicial de intención de cancelación */
.btn-alerta {
  background-color: var(--brownred);
  color: var(--white);
  border: none;
  border-radius: 4px;
  padding: 0.75rem 1.4rem;
  font-size: 0.95rem;
  font-weight: bold;
  cursor: pointer;
  transition: opacity 0.3s ease, transform 0.2s ease;
}

.btn-alerta:hover {
  opacity: 0.9;
  transform: translateY(-2px);
}

/* Botón secundario para abortar acción */
.btn-secundario {
  background-color: var(--lightgrey);
  color: var(--darkgrey);
  border: none;
  border-radius: 4px;
  padding: 0.75rem 1.4rem;
  font-size: 0.95rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.btn-secundario:hover {
  background-color: #cacaca;
  transform: translateY(-2px);
}

/* Botón para volver a actividades tras finalizar */
.btn-accion {
  display: inline-block;
  background-color: var(--green);
  color: var(--white);
  border: none;
  border-radius: 4px;
  padding: 0.75rem 1.5rem;
  font-size: 0.95rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.btn-accion:hover {
  background-color: var(--darkgreen);
  transform: translateY(-2px);
}

/* ==========================================
   ESTILOS DEL MODAL DE ADVERTENCIA
   ========================================== */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 1rem;
  box-sizing: border-box;
}

.modal-tarjeta {
  background-color: var(--white);
  border-radius: 0.5rem;
  max-width: 460px;
  width: 100%;
  padding: 2rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
  text-align: center;
  animation: fadeIn 0.2s ease-out;
}

.modal-icono {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.modal-titulo {
  color: var(--brownred);
  margin: 0 0 1rem 0;
  font-size: 1.3rem;
}

.modal-alerta-box {
  background-color: var(--yellow);
  border-left: 4px solid var(--orange);
  padding: 0.8rem 1rem;
  border-radius: 4px;
  margin-bottom: 1.5rem;
  text-align: left;
}

.modal-alerta-texto {
  color: #7a5200;
  margin: 0 0 0.4rem 0;
  font-size: 0.95rem;
}

.modal-subtexto {
  color: var(--darkgrey);
  font-size: 0.85rem;
  line-height: 1.4;
  margin: 0;
}

.modal-acciones {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* Botón de confirmación destructiva final */
.btn-destructivo {
  background-color: var(--brownred);
  color: var(--white);
  border: none;
  border-radius: 4px;
  padding: 0.75rem 1.4rem;
  font-size: 0.95rem;
  font-weight: bold;
  cursor: pointer;
  transition: opacity 0.3s ease;
}

.btn-destructivo:hover {
  opacity: 0.9;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 600px) {
  .acciones-botones,
  .modal-acciones {
    flex-direction: column;
    width: 100%;
  }

  .btn-alerta,
  .btn-secundario,
  .btn-accion,
  .btn-destructivo {
    width: 100%;
  }
}
</style>