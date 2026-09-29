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

        <!-- Lista dinámica de asistentes -->
        <div class="participantes-lista">
          <div v-for="(p, index) in participantes" :key="index" class="participante-card">
            <div class="participante-header">
              <h4 class="participante-titulo">Asistente {{ index + 1 }}</h4>

              <!-- Solo se muestra si hay más de 1 persona en la reserva -->
              <button 
                v-if="participantes.length > 1" 
                type="button" 
                @click="solicitarEliminarAsistente(index)"
                class="btn-quitar" 
                title="Quitar a este asistente"
              >
                ✕ Quitar
              </button>
            </div>

            <div class="participante-grid">
              <div class="form-subgroup">
                <label :for="'p-nombre-' + index">Nombre:</label>
                <input type="text" :id="'p-nombre-' + index" v-model="p.nombre" required class="form-input" />
              </div>

              <div class="form-subgroup">
                <label :for="'p-apellidos-' + index">Apellidos:</label>
                <input type="text" :id="'p-apellidos-' + index" v-model="p.apellidos" required class="form-input" />
              </div>

              <div class="form-subgroup grupo-edad">
                <label :for="'p-edad-' + index">Edad:</label>
                <input 
                  type="number" 
                  :id="'p-edad-' + index" 
                  v-model.number="p.edad" 
                  min="0" 
                  max="120" 
                  required
                  class="form-input" 
                />
              </div>
            </div>
          </div>
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

    <!-- MODAL DE DOBLE VERIFICACIÓN PARA QUITAR ASISTENTE -->
    <div v-if="mostrarModalQuitar" class="modal-overlay">
      <div class="modal-tarjeta">
        <div class="modal-icono">⚠️</div>
        <h3 class="modal-titulo">¿Quitar a este asistente?</h3>

        <div class="modal-alerta-box">
          <p class="modal-alerta-texto">
            <strong>Atención: Esta plaza se liberará.</strong>
          </p>
          <p class="modal-subtexto">
            Estás a punto de quitar a
            <strong>{{ asistenteSeleccionadoInfo }}</strong>. Al guardar los cambios, esta plaza quedará disponible para
            otras personas y <strong>podrías no recuperarla</strong> si la actividad se llena.
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

    <!-- MODAL DE ÉXITO TRAS MODIFICAR LA RESERVA -->
    <div v-if="mostrarModalExito" class="modal-overlay">
      <div class="modal-tarjeta">
        <div class="modal-icono">🌿</div>
        <h3 class="modal-titulo-exito">¡Reserva modificada con éxito!</h3>

        <p class="modal-subtexto">
          Los cambios se han guardado correctamente en el sistema. Te hemos enviado un correo con el resumen actualizado
          de tu inscripción.
        </p>

        <div class="modal-acciones">
          <button @click="irACalendario" class="btn-accion">
            Aceptar y volver
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

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
  display: flex;
  justify-content: center;
  align-items: flex-start;
  min-height: calc(100vh - 12rem);
  padding: 7rem 1.5rem 3rem 1.5rem;
  background-color: var(--white);
  box-sizing: border-box;
}

.card-editar {
  width: 100%;
  max-width: 680px;
  background-color: var(--white);
  border: 1px solid var(--shoftgreen);
  border-radius: 0.5rem;
  padding: 2.5rem 2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.titulo-editar {
  color: var(--darkgreen);
  margin-top: 0;
  margin-bottom: 1.5rem;
  text-align: center;
}

.texto-cargando {
  color: var(--darkgrey);
  line-height: 1.6;
  font-size: 1rem;
}

/* Tarjeta resumen de la actividad */
.actividad-resumen {
  background-color: var(--megashoftgreen);
  border-left: 4px solid var(--green);
  border-radius: 4px;
  padding: 1rem 1.25rem;
  margin-bottom: 2rem;
}

.actividad-titulo {
  font-weight: bold;
  color: var(--darkgreen);
  margin: 0 0 0.3rem 0;
  font-size: 1.05rem;
}

.actividad-detalles {
  color: var(--darkgrey);
  font-size: 0.9rem;
  margin: 0;
}

.seccion-titulo {
  color: var(--green);
  border-bottom: 2px solid var(--supershoftgreen);
  padding-bottom: 0.4rem;
  margin: 2rem 0 1.25rem 0;
}

/* Caja de información y disponibilidad de plazas */
.caja-disponibilidad {
  background-color: var(--megashoftgreen);
  border: 1px solid var(--supershoftgreen);
  border-radius: 6px;
  padding: 1rem 1.25rem;
  margin-bottom: 1.5rem;
}

.plazas-conteo {
  color: var(--darkgreen);
  font-size: 1rem;
  margin-bottom: 0.4rem;
}

.aviso-disponibles {
  color: var(--darkgrey);
  font-size: 0.9rem;
  line-height: 1.4;
}

.aviso-disponibles strong {
  color: var(--green);
}

.aviso-completo {
  background-color: var(--yellow);
  color: var(--darkyellow);
  border-left: 3px solid var(--orange);
  padding: 0.5rem 0.75rem;
  border-radius: 4px;
  font-size: 0.85rem;
  line-height: 1.4;
  margin-top: 0.4rem;
}

/* Estructura del formulario */
.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  margin-bottom: 1.25rem;
}

.form-group label,
.form-subgroup label {
  font-weight: bold;
  font-size: 0.9rem;
  color: var(--darkgrey);
}

.form-input,
.form-textarea {
  width: 100%;
  padding: 0.65rem 0.8rem;
  border: 1px solid var(--lightgrey);
  border-radius: 4px;
  font-size: 0.95rem;
  color: var(--darkgrey);
  background-color: var(--white);
  box-sizing: border-box;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.form-input:focus,
.form-textarea:focus {
  outline: none;
  border-color: var(--green);
  box-shadow: 0 0 0 3px var(--supershoftgreen);
}

.form-textarea {
  min-height: 90px;
  resize: vertical;
}

/* Fichas de asistentes y controles específicos */
.participantes-lista {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1.5rem;
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

/* Adaptación responsive */
@media (max-width: 650px) {
  .participante-grid {
    grid-template-columns: 1fr;
  }
}
</style>