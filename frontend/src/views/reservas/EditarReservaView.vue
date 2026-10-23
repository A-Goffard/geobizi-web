<template>
  <div class="container-editar">
    <div class="card-editar">
      <h2 class="titulo-editar">✏️ Modificar Reserva</h2>

      <!-- Estado: Cargando datos -->
      <div v-if="cargando" class="estado-caja">
        <p class="texto-cargando">Cargando datos de tu reserva...</p>
      </div>

      <!-- Estado: Error con el token -->
      <div v-else-if="errorToken" class="estado-caja">
        <p class="mensaje-error">{{ errorToken }}</p>
        <button @click="router.push('/calendario')" class="btn-secundario">
          Volver a actividades
        </button>
      </div>

      <!-- Formulario principal de edición -->
      <form v-else @submit.prevent="actualizarReserva" class="formulario-editar">
        <!-- Resumen de la actividad -->
        <div class="actividad-resumen">
          <p class="actividad-titulo">{{ actividad.titulo }}</p>
          <p class="actividad-detalles">
            📅 {{ actividad.fecha }} &nbsp;|&nbsp; ⏰ {{ actividad.hora }} &nbsp;|&nbsp; 📍 {{ actividad.ubicacion }}
          </p>
        </div>

        <h3 class="seccion-titulo">Datos de la persona de contacto</h3>

        <div class="form-group">
          <label for="contacto-nombre">Nombre:</label>
          <input type="text" id="contacto-nombre" v-model="reserva.nombre_contacto" required class="form-input" />
        </div>

        <div class="form-group">
          <label for="contacto-apellidos">Apellidos:</label>
          <input type="text" id="contacto-apellidos" v-model="reserva.apellidos_contacto" required class="form-input" />
        </div>

        <div class="form-group">
          <label for="contacto-email">Correo Electrónico:</label>
          <input type="email" id="contacto-email" v-model="reserva.email" required class="form-input" />
        </div>

        <div class="form-group">
          <label for="contacto-phone">Teléfono:</label>
          <input type="tel" id="contacto-phone" v-model="reserva.phone" required class="form-input" />
        </div>

        <h3 class="seccion-titulo">Plazas y Asistentes</h3>

        <!-- Caja informativa de plazas y disponibilidad -->
        <div class="caja-disponibilidad">
          <div class="plazas-conteo">
            Plazas reservadas actualmente: <strong>{{ participantes.length }}</strong>
          </div>

          <div v-if="plazasLibresAdicionales > 0" class="aviso-disponibles">
            ℹ️ Quedan <strong>{{ plazasLibresAdicionales }}</strong> {{ plazasLibresAdicionales === 1 ? 'plaza libre adicional' : 'plazas libres adicionales' }} por si deseas añadir a más personas.
          </div>

          <div v-else class="aviso-completo">
            ⚠️ Aforo completo: no quedan más plazas libres para añadir más asistentes a esta actividad.
          </div>
        </div>

        <!-- Lista dinámica de asistentes mediante ParticipanteCard reutilizable -->
        <div class="participantes-lista">
          <ParticipanteCard
            v-for="(p, index) in participantes"
            :key="index"
            v-model="participantes[index]"
            :index="index"
            :can-remove="participantes.length > 1"
            @remove="solicitarEliminarAsistente(index)"
          />
        </div>

        <!-- Botón para añadir asistentes cómodamente -->
        <button 
          v-if="plazasLibresAdicionales > 0" 
          type="button" 
          @click="agregarAsistente" 
          class="btn-anadir-asistente"
        >
          ➕ Añadir otro asistente
        </button>

        <div class="form-group">
          <label for="reserva-observaciones">Observaciones:</label>
          <textarea id="reserva-observaciones" v-model="reserva.observaciones" class="form-textarea"></textarea>
        </div>

        <!-- Botones de acción -->
        <div class="acciones-botones">
          <button type="submit" class="btn-guardar" :disabled="guardando">
            {{ guardando ? 'Guardando cambios...' : 'Guardar Cambios' }}
          </button>
          <button type="button" @click="router.push('/calendario')" class="btn-cancelar">
            Volver
          </button>
        </div>

        <p v-if="mensajeError" class="mensaje-error">{{ mensajeError }}</p>
      </form>
    </div>

    <!-- Modal de confirmación defensivo al quitar asistente -->
    <div v-if="mostrarModalQuitar" class="modal-overlay" @click.self="cancelarEliminarAsistente">
      <div class="modal-tarjeta">
        <div class="modal-icono">⚠️</div>
        <h3 class="modal-titulo">¿Quitar a este asistente?</h3>

        <div class="modal-alerta-box">
          <p class="modal-alerta-texto">
            <strong>Atención: Esta plaza se liberará.</strong>
          </p>
          <p class="modal-subtexto">
            Estás a punto de quitar a <strong>{{ asistenteSeleccionadoInfo }}</strong>. Al guardar los cambios, esta plaza quedará disponible para la lista de espera u otras personas y <strong>podrías no recuperarla</strong> si la actividad se llena.
          </p>
        </div>

        <div class="modal-acciones">
          <button @click="confirmarEliminarAsistente" class="btn-destructivo">
            Sí, quitar asistente
          </button>
          <button @click="cancelarEliminarAsistente" class="btn-secundario">
            Cancelar
          </button>
        </div>
      </div>
    </div>

    <!-- Modal de éxito reutilizable tras guardar cambios -->
    <ModalExito
      :visible="mostrarModalExito"
      :es-lista-espera="false"
      titulo="¡Reserva modificada con éxito!"
      mensaje="Los cambios se han guardado correctamente en el sistema. Te hemos enviado un correo con el resumen actualizado de tu inscripción."
      @cerrar="irACalendario"
    />
  </div>
</template>

<script setup>
/* eslint-disable */
import { ref, computed, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import ParticipanteCard from '@/components/reservas/ParticipanteCard.vue';
import ModalExito from '@/components/reservas/ModalExito.vue';

const route = useRoute();
const router = useRouter();
const token = route.query.token;

const cargando = ref(true);
const guardando = ref(false);
const errorToken = ref('');
const reserva = ref({});
const actividad = ref({});
const participantes = ref([]);
const plazasIniciales = ref(0);
const mensajeError = ref('');

// Modales reactivos
const mostrarModalQuitar = ref(false);
const indiceAEliminar = ref(null);
const mostrarModalExito = ref(false);

onMounted(async () => {
  if (!token) {
    errorToken.value = 'El enlace de modificación no es válido o ha expirado.';
    cargando.value = false;
    return;
  }

  try {
    const response = await fetch(`http://localhost:5000/api/token/${token}`);
    const data = await response.json();

    if (response.ok) {
      reserva.value = data.reserva;
      actividad.value = data.actividad;
      participantes.value = data.participantes || [];
      plazasIniciales.value = Number(data.reserva.num_personas) || 1;
    } else {
      throw new Error(data.detail || 'No se pudo cargar la información de la reserva.');
    }
  } catch (err) {
    errorToken.value = err.message;
  } finally {
    cargando.value = false;
  }
});

const plazasLibresAdicionales = computed(() => {
  if (!actividad.value.plazas_totales) return 0;
  
  const libresEnActividad = actividad.value.plazas_totales - actividad.value.plazas_ocupadas;
  const maximoPosible = libresEnActividad + plazasIniciales.value;
  const restantes = maximoPosible - participantes.value.length;
  
  return Math.max(0, restantes);
});

const asistenteSeleccionadoInfo = computed(() => {
  if (indiceAEliminar.value === null) return '';
  const p = participantes.value[indiceAEliminar.value];
  if (!p) return '';
  const nombreCompleto = `${p.nombre || ''} ${p.apellidos || ''}`.trim();
  return nombreCompleto ? `${nombreCompleto} (Asistente ${indiceAEliminar.value + 1})` : `Asistente ${indiceAEliminar.value + 1}`;
});

const agregarAsistente = () => {
  if (plazasLibresAdicionales.value <= 0) return;
  participantes.value.push({ nombre: '', apellidos: '', edad: '' });
  reserva.value.num_personas = participantes.value.length;
};

const solicitarEliminarAsistente = (index) => {
  if (participantes.value.length <= 1) return;
  const p = participantes.value[index];

  // Si la tarjeta está completamente vacía, se retira directamente sin confirmación
  if (!p.nombre?.trim() && !p.apellidos?.trim()) {
    participantes.value.splice(index, 1);
    reserva.value.num_personas = participantes.value.length;
    return;
  }

  indiceAEliminar.value = index;
  mostrarModalQuitar.value = true;
};

const confirmarEliminarAsistente = () => {
  if (indiceAEliminar.value !== null) {
    participantes.value.splice(indiceAEliminar.value, 1);
    reserva.value.num_personas = participantes.value.length;
  }
  cancelarEliminarAsistente();
};

const cancelarEliminarAsistente = () => {
  mostrarModalQuitar.value = false;
  indiceAEliminar.value = null;
};

const actualizarReserva = async () => {
  mensajeError.value = '';
  guardando.value = true;

  const payload = {
    ...reserva.value,
    num_personas: participantes.value.length,
    participantes: participantes.value.map(p => ({
      nombre: p.nombre,
      apellidos: p.apellidos,
      edad: Number(p.edad)
    }))
  };

  try {
    const response = await fetch(`http://localhost:5000/api/token/${token}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = await response.json();

    if (response.ok) {
      plazasIniciales.value = payload.num_personas;
      mostrarModalExito.value = true;
    } else {
      throw new Error(data.detail || 'Error al actualizar la reserva.');
    }
  } catch (err) {
    mensajeError.value = err.message;
  } finally {
    guardando.value = false;
  }
};

const irACalendario = () => {
  mostrarModalExito.value = false;
  router.push('/calendario');
};
</script>

<style scoped>
.container-editar {
  max-width: 680px;
  margin: 2.5rem auto;
  padding: 0 1rem;
}

.card-editar {
  background: var(--white);
  border: 1px solid var(--supershoftgreen);
  border-radius: 12px;
  padding: 2.2rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

.titulo-editar {
  color: var(--darkgreen);
  font-size: 1.6rem;
  margin-bottom: 1.5rem;
  text-align: center;
}

.actividad-resumen {
  background: var(--megashoftgreen);
  border-left: 4px solid var(--green);
  border-radius: 6px;
  padding: 1rem 1.2rem;
  margin-bottom: 1.5rem;
}

.actividad-titulo {
  color: var(--darkgreen);
  font-weight: 700;
  font-size: 1.1rem;
  margin: 0 0 0.35rem 0;
}

.actividad-detalles {
  color: var(--darkgrey);
  font-size: 0.9rem;
  margin: 0;
}

.seccion-titulo {
  color: var(--darkgreen);
  font-size: 1.15rem;
  margin: 1.5rem 0 0.75rem 0;
  padding-bottom: 0.35rem;
  border-bottom: 2px solid var(--supershoftgreen);
}

.form-group {
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
}

.form-group label {
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--darkgrey);
  margin-bottom: 0.3rem;
}

.form-input,
.form-textarea {
  padding: 0.6rem 0.75rem;
  border: 1px solid var(--lightgrey);
  border-radius: 6px;
  font-size: 0.95rem;
  color: var(--darkgrey);
  background: var(--white);
  outline: none;
  transition: border-color 0.2s;
}

.form-input:focus,
.form-textarea:focus {
  border-color: var(--green);
}

.form-textarea {
  min-height: 80px;
  resize: vertical;
}

.caja-disponibilidad {
  background: var(--white);
  border: 1px solid var(--lightgrey);
  border-radius: 6px;
  padding: 0.9rem 1rem;
  margin-bottom: 1rem;
}

.plazas-conteo {
  color: var(--darkgrey);
  font-size: 0.95rem;
  margin-bottom: 0.35rem;
}

.aviso-disponibles {
  color: var(--darkgreen);
  font-size: 0.85rem;
}

.aviso-completo {
  color: var(--darkyellow);
  background: var(--yellow);
  border-radius: 4px;
  padding: 0.4rem 0.6rem;
  font-size: 0.85rem;
}

.btn-anadir-asistente {
  background: var(--megashoftgreen);
  color: var(--darkgreen);
  border: 1px dashed var(--green);
  width: 100%;
  padding: 0.75rem;
  border-radius: 6px;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  margin: 0.5rem 0 1.25rem 0;
  transition: all 0.2s;
}

.btn-anadir-asistente:hover {
  background: var(--supershoftgreen);
}

.acciones-botones {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
}

.btn-guardar {
  flex: 2;
  background: var(--green);
  color: var(--white);
  border: none;
  padding: 0.85rem;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s;
}

.btn-guardar:hover:not(:disabled) {
  background: var(--darkgreen);
}

.btn-guardar:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-cancelar,
.btn-secundario {
  flex: 1;
  background: var(--lightgrey);
  color: var(--darkgrey);
  border: none;
  padding: 0.85rem;
  border-radius: 6px;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  text-align: center;
  transition: background 0.2s;
}

.btn-cancelar:hover,
.btn-secundario:hover {
  background: #cacaca;
}

.mensaje-error {
  color: var(--brownred);
  background: var(--supershoftbrownred);
  border: 1px solid var(--lightbrownred);
  border-radius: 6px;
  padding: 0.75rem;
  font-size: 0.9rem;
  margin-top: 1rem;
  text-align: center;
}

/* Modal de confirmación defensiva al eliminar asistente */
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
}

.modal-icono {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.modal-titulo {
  color: var(--darkgrey);
  font-size: 1.25rem;
  margin: 0 0 0.75rem 0;
}

.modal-alerta-box {
  background: var(--supershoftbrownred);
  border: 1px solid var(--lightbrownred);
  border-radius: 6px;
  padding: 0.9rem;
  margin-bottom: 1.25rem;
  text-align: left;
}

.modal-alerta-texto {
  color: var(--brownred);
  font-size: 0.85rem;
  margin: 0 0 0.35rem 0;
}

.modal-subtexto {
  color: var(--darkgrey);
  font-size: 0.85rem;
  line-height: 1.4;
  margin: 0;
}

.modal-acciones {
  display: flex;
  gap: 0.75rem;
}

.btn-destructivo {
  flex: 1;
  background: var(--brownred);
  color: var(--white);
  border: none;
  padding: 0.75rem;
  border-radius: 6px;
  font-size: 0.9rem;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s;
}

.btn-destructivo:hover {
  background: #9f4935;
}
</style>