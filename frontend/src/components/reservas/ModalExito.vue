<template>
  <div v-if="visible" class="modal-overlay" @click.self="$emit('cerrar')">
    <div class="modal-tarjeta">
      <div class="modal-icono">{{ iconoModal }}</div>
      <h3 
        class="modal-titulo-exito" 
        :class="{ 'titulo-espera': esListaEspera }"
      >
        {{ tituloModal }}
      </h3>
      <p class="modal-subtexto">{{ mensaje }}</p>
      <div class="modal-acciones">
        <button 
          @click="$emit('cerrar')" 
          class="btn-accion"
          :class="{ 'btn-espera': esListaEspera }"
        >
          {{ textoBoton }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
/* eslint-disable */
import { computed } from 'vue';

const props = defineProps({
  visible: {
    type: Boolean,
    default: false
  },
  esListaEspera: {
    type: Boolean,
    default: false
  },
  titulo: {
    type: String,
    default: ''
  },
  mensaje: {
    type: String,
    required: true
  },
  textoBoton: {
    type: String,
    default: 'Aceptar y volver'
  }
});

defineEmits(['cerrar']);

const iconoModal = computed(() => {
  return props.esListaEspera ? '📋' : '🌿';
});

const tituloModal = computed(() => {
  if (props.titulo) return props.titulo;
  return props.esListaEspera 
    ? '¡Anotados en la lista de espera!' 
    : '¡Reserva Confirmada!';
});
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.65);
  backdrop-filter: blur(2px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
  padding: 1rem;
}

.modal-tarjeta {
  background: var(--white);
  border-radius: 12px;
  max-width: 440px;
  width: 100%;
  padding: 2rem;
  text-align: center;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
  animation: popIn 0.25s ease-out;
}

@keyframes popIn {
  from {
    transform: scale(0.92);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}

.modal-icono {
  font-size: 2.8rem;
  margin-bottom: 0.75rem;
}

.modal-titulo-exito {
  color: var(--darkgreen);
  font-size: 1.35rem;
  margin: 0 0 0.75rem 0;
}

.modal-titulo-exito.titulo-espera {
  color: var(--amber);
}

.modal-subtexto {
  color: var(--darkgrey);
  font-size: 0.95rem;
  line-height: 1.5;
  margin: 0 0 1.5rem 0;
}

.modal-acciones {
  display: flex;
  justify-content: center;
}

.btn-accion {
  background-color: var(--green);
  color: var(--white);
  border: none;
  padding: 0.7rem 1.6rem;
  border-radius: 6px;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.btn-accion:hover {
  background-color: var(--darkgreen);
}

.btn-accion.btn-espera {
  background-color: var(--amber);
}

.btn-accion.btn-espera:hover {
  background-color: var(--darkamber);
}
</style>