<template>
  <div class="contenedor-principal">
    <h1>Gestión de Reservas</h1>
    
    <form @submit.prevent="crearReserva">
      <div class="form-group">
        <label for="id_persona">ID Persona:</label>
        <input type="number" id="id_persona" v-model.number="form.id_persona" required>
      </div>
      <div class="form-group">
        <label for="id_actividad">ID Actividad:</label>
        <input type="number" id="id_actividad" v-model.number="form.id_actividad" required>
      </div>
      <div class="form-group">
        <label for="numero_personas">Nº Personas:</label>
        <input type="number" id="numero_personas" v-model.number="form.numero_personas" required>
      </div>
      <button type="submit">Crear Reserva</button>
    </form>
    <p v-if="error" class="error-message">{{ error }}</p>
    
    <hr>
    <h2>Reservas</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Cliente</th>
          <th>Actividad</th>
          <th>Pers</th>
          <th>A&nbsp;pagar</th>
          <th>Estado</th>
          <th>Confirmación</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="reserva in reservas" :key="reserva.id_reserva">
          <td>{{ reserva.id_reserva }}</td>
          <td>
            <div>{{ reserva.persona ? `${reserva.persona.nombre} ${reserva.persona.apellido}` : 'N/A' }}</div>
            <div><small>{{ reserva.persona ? reserva.persona.email : '' }}</small></div>
            <div><small>{{ reserva.persona ? reserva.persona.telefono : '' }}</small></div>
          </td>
          <td>
            <div>{{ reserva.actividad ? reserva.actividad.nombre : 'N/A' }}</div>
            <div><small>{{ reserva.actividad ? formatearFecha(reserva.actividad.fecha) : '' }}</small></div>
            <div><small>{{ reserva.actividad ? reserva.actividad.hora : '' }}</small></div>
          </td>
          <td>{{ reserva.numero_personas }}</td>
          <td>{{ calcularTotal(reserva) }} €</td>

          <!-- COLUMNA ESTADO -->
          <td class="estado-column">
            <div class="estado-container">
              <div class="estado-icon-text">
                <img 
                  :src="reserva.aprobada ? okIcon : noIcon" 
                  :alt="reserva.aprobada ? 'Aprobada' : 'Pendiente'"
                  class="estado-icon"
                />
                <span :class="getEstadoClass(reserva)">
                  {{ getEstadoTexto(reserva) }}
                </span>
              </div>
              <div class="estado-buttons">
                <button 
                  v-if="!reserva.aprobada" 
                  class="btn-mini btn-aprobar" 
                  @click="aprobarReserva(reserva.id_reserva)"
                  title="Aprobar reserva"
                >
                  Aprobar
                </button>
                <button 
                  v-if="reserva.aprobada" 
                  class="btn-mini btn-rechazar" 
                  @click="rechazarReserva(reserva.id_reserva)"
                  title="Rechazar reserva"
                >
                  Rechazar
                </button>
              </div>
            </div>
          </td>

          <!-- COLUMNA CONFIRMACIÓN -->
          <td class="confirmacion-column">
            <div class="confirmacion-container">
              <div class="confirmacion-icon-text">
                <img 
                  :src="reserva.confirmacion_enviada ? okIcon : noIcon" 
                  :alt="reserva.confirmacion_enviada ? 'Enviada' : 'Pendiente'"
                  class="confirmacion-icon"
                />
                <span :class="reserva.confirmacion_enviada ? 'estado-enviado' : 'estado-pendiente'">
                  {{ reserva.confirmacion_enviada ? 'Enviada' : 'Pendiente' }}
                </span>
              </div>
              <div class="confirmacion-buttons">
                <button 
                  v-if="reserva.aprobada && !reserva.confirmacion_enviada"
                  class="btn-mini btn-confirmar" 
                  @click="enviarConfirmacion(reserva.id_reserva)"
                  title="Enviar confirmación por email"
                >
                  Enviar Confirmación
                </button>
                <span v-else-if="!reserva.aprobada && !reserva.confirmacion_enviada" class="texto-nota">
                  (Requiere aprobación)
                </span>
              </div>
            </div>
          </td>

          <!-- COLUMNA ACCIONES -->
          <td class="acciones">
            <button class="btn-mini btn-editar" @click="abrirModalEditar(reserva)" title="Editar reserva">
              Editar
            </button>
            <button class="btn-mini btn-eliminar" @click="eliminarReserva(reserva.id_reserva)" title="Eliminar reserva">
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Modal de Edición -->
    <EditarReservaModal
      v-if="isEditModalVisible"
      :reserva="reservaAEditar"
      @close="cerrarModalEditar"
      @update="actualizarReserva"
    />
  </div>
    <!-- Botón para volver al panel de administración -->
    <div class="contenedor-principal"><button class="btn-editar" @click="volverAlPanel">Volver al panel</button></div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import EditarReservaModal from '@/components/administracion/EditarReservaModal.vue'
import '@/assets/styles/admin.css'
import okIcon from '@/assets/icons/ok.png'
import noIcon from '@/assets/icons/no.png'

const form = ref({ id_persona: null, id_actividad: null, numero_personas: 1 })
const reservas = ref([])
const error = ref(null)
const isEditModalVisible = ref(false)
const reservaAEditar = ref(null)

const fetchReservas = async () => {
  try {
    const res = await fetch('/api/admin/reservas')
    if (!res.ok) throw new Error('Error al cargar reservas')
    reservas.value = await res.json()
  } catch (e) {
    error.value = e.message
  }
}

const crearReserva = async () => {
  error.value = null
  try {
    const res = await fetch('/api/admin/reservas', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form.value)
    })
    if (!res.ok) {
      const errData = await res.json()
      throw new Error(errData.detail || 'Error al crear reserva')
    }
    form.value = { id_persona: null, id_actividad: null, numero_personas: 1 }
    fetchReservas()
  } catch (e) {
    error.value = e.message
  }
}

const eliminarReserva = async (id) => {
  await fetch(`/api/admin/reservas/${id}`, { method: 'DELETE' })
  fetchReservas()
}

const abrirModalEditar = (reserva) => {
  reservaAEditar.value = { ...reserva }
  isEditModalVisible.value = true
}

const cerrarModalEditar = () => {
  isEditModalVisible.value = false
  reservaAEditar.value = null
}

const actualizarReserva = async ({ id, data }) => {
  await fetch(`/api/admin/reservas/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  cerrarModalEditar()
  fetchReservas()
}

const volverAlPanel = () => {
  // Redirige al panel de administración
  window.location.href = '/admin/panel';
}

const aprobarReserva = async (id) => {
  try {
    const res = await fetch(`/api/admin/reservas/${id}/aprobar`, { method: 'PUT' })
    if (!res.ok) throw new Error('Error al aprobar reserva')
    fetchReservas()
  } catch (e) {
    error.value = e.message
  }
}

const rechazarReserva = async (id) => {
  try {
    const res = await fetch(`/api/admin/reservas/${id}/rechazar`, { method: 'PUT' })
    if (!res.ok) throw new Error('Error al rechazar reserva')
    fetchReservas()
  } catch (e) {
    error.value = e.message
  }
}

const enviarConfirmacion = async (id) => {
  try {
    const res = await fetch(`/api/admin/reservas/${id}/enviar-confirmacion`, { method: 'POST' })
    if (!res.ok) throw new Error('Error al enviar confirmación')
    fetchReservas()
  } catch (e) {
    error.value = e.message
  }
}

const getEstadoTexto = (reserva) => {
  if (reserva.aprobada) return 'Aprobada'
  return 'Pendiente'
}

const getEstadoClass = (reserva) => {
  if (reserva.aprobada) return 'estado-aprobado'
  return 'estado-pendiente'
}

function calcularTotal(reserva) {
  if (reserva.actividad && reserva.actividad.precio && reserva.numero_personas) {
    return (reserva.actividad.precio * reserva.numero_personas).toFixed(2)
  }
  return 'N/A'
}

function formatearFecha(fechaStr) {
  if (!fechaStr) return ''
  const fecha = new Date(fechaStr)
  return fecha.toISOString().slice(0, 10) // yyyy-mm-dd
}

onMounted(fetchReservas)
</script>

<style scoped>
/* ...existing code... */

/* Estilos para las columnas de estado y confirmación */
.estado-column,
.confirmacion-column {
  min-width: 5rem;
  vertical-align: top;
}

.estado-container,
.confirmacion-container {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  align-items: flex-start;
}

.estado-icon-text,
.confirmacion-icon-text {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.estado-icon,
.confirmacion-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.estado-buttons,
.confirmacion-buttons {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  width: 100%;
}

/* Botones mini */
.btn-mini {
  padding: 0.25rem 0.5rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.75rem;
  font-weight: 500;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.btn-aprobar {
  background-color: #28a745;
  color: white;
}

.btn-aprobar:hover {
  background-color: #218838;
  transform: translateY(-1px);
}

.btn-rechazar {
  background-color: #df9019;
  color: white;
}

.btn-rechazar:hover {
  background-color: #c47f17;
  transform: translateY(-1px);
}

.btn-confirmar {
  background-color: #007bff;
  color: white;
}

.btn-confirmar:hover {
  background-color: #0069d9;
  transform: translateY(-1px);
}

/* Estilos para textos de estado */
.estado-aprobado {
  color: #28a745;
  font-weight: 600;
  font-size: 0.85rem;
}

.estado-pendiente {
  color: #c29e26;
  font-weight: 600;
  font-size: 0.85rem;
}

.estado-enviado {
  color: #28a745;
  font-weight: 600;
  font-size: 0.85rem;
}

.texto-nota {
  font-size: 0.7rem;
  color: #6c757d;
  font-style: italic;
}

/* Acciones generales */
.acciones {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  min-width: 100px;
}

/* Responsive */
@media (max-width: 768px) {
  table {
    font-size: 0.8rem;
  }
  
  .estado-column,
  .confirmacion-column {
    min-width: 140px;
  }
  
  .btn-mini {
    padding: 0.2rem 0.4rem;
    font-size: 0.7rem;
  }
  
  .estado-icon,
  .confirmacion-icon {
    width: 16px;
    height: 16px;
  }
}


</style>

