<template>
  <div class="contenedor-principal">
    <h1>Gestión de Reservas</h1>

    <!-- Formulario de Reserva Rápida -->
    <form @submit.prevent="crearReservaRapida" class="form-grid">
      <div class="form-group">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" v-model="formRapida.nombre" required>
      </div>
      <div class="form-group">
        <label for="apellido">Apellido:</label>
        <input type="text" id="apellido" v-model="formRapida.apellido" required>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="formRapida.email" required>
      </div>
      <div class="form-group">
        <label for="telefono">Teléfono:</label>
        <input type="tel" id="telefono" v-model="formRapida.telefono" required>
      </div>
      <div class="form-group">
        <label for="actividad">Actividad:</label>
        <select id="actividad" v-model="formRapida.id_actividad" required>
          <option value="">Selecciona una actividad</option>
          <option v-for="actividad in actividadesDisponibles" :key="actividad.id_actividad" :value="actividad.id_actividad">
            {{ actividad.nombre }} - {{ formatearFecha(actividad.fecha) }} {{ actividad.hora }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="numPersonas">Número de personas:</label>
        <input type="number" id="numPersonas" v-model.number="formRapida.numero_personas" min="1" required>
      </div>
      <div class="form-group full-width">
        <button type="submit" class="btn-crear-rapida">Crear Reserva Rápida</button>
      </div>
      <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
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
            <div>
              <template v-if="reserva.persona && typeof reserva.persona.nombre !== 'undefined'">
                {{ reserva.persona.nombre }} {{ reserva.persona.apellido || '' }}
              </template>
              <template v-else>
                N/A
              </template>
            </div>
            <div><small>{{ reserva.persona && reserva.persona.email ? reserva.persona.email : '' }}</small></div>
            <div><small>{{ reserva.persona && reserva.persona.telefono ? reserva.persona.telefono : '' }}</small></div>
          </td>
          <td>
            <div>{{ reserva.actividad?.nombre || 'N/A' }}</div>
            <div><small>{{ reserva.actividad?.fecha ? formatearFecha(reserva.actividad.fecha) : '' }}</small></div>
            <div><small>{{ reserva.actividad?.hora || '' }}</small></div>
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

const formRapida = ref({
  nombre: '',
  apellido: '',
  email: '',
  telefono: '',
  id_actividad: '',
  numero_personas: 1
})
const actividadesDisponibles = ref([])
const reservas = ref([])
const error = ref(null)
const errorMessage = ref('')
const successMessage = ref('')
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

const fetchActividades = async () => {
  try {
    const res = await fetch('/api/admin/actividades')
    if (!res.ok) throw new Error('Error al cargar actividades')
    const actividades = await res.json()
    const hoy = new Date()
    actividadesDisponibles.value = actividades.filter(act => 
      act.activo === 1 && new Date(act.fecha) >= hoy
    )
  } catch (e) {
    error.value = 'Error cargando actividades'
  }
}

function formatearFecha(fechaStr) {
  if (!fechaStr) return ''
  const fecha = new Date(fechaStr)
  return fecha.toISOString().slice(0, 10) // yyyy-mm-dd
}

const crearReservaRapida = async () => {
  errorMessage.value = ''
  successMessage.value = ''
  // Validación básica
  if (!formRapida.value.nombre || !formRapida.value.apellido || !formRapida.value.email || !formRapida.value.telefono || !formRapida.value.id_actividad || !formRapida.value.numero_personas) {
    errorMessage.value = 'Rellena todos los campos obligatorios'
    return
  }
  try {
    // 1. Buscar persona por teléfono
    let personaRes = await fetch(`/api/admin/personas?telefono=${encodeURIComponent(formRapida.value.telefono)}`)
    let persona = null
    if (personaRes.ok) {
      const personasEncontradas = await personaRes.json()
      if (personasEncontradas.length > 0) {
        persona = personasEncontradas[0]
        // Actualiza todos los datos si son diferentes
        await fetch(`/api/admin/personas/${persona.id_persona}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            nombre: formRapida.value.nombre,
            apellido: formRapida.value.apellido || persona.apellido,
            email: formRapida.value.email || persona.email,
            telefono: formRapida.value.telefono,
            // ...otros campos si los tienes en el formulario...
          })
        })
      }
    }
    // 2. Si no existe, crear persona
    if (!persona) {
      const nuevaPersona = {
        nombre: formRapida.value.nombre,
        apellido: formRapida.value.apellido,
        email: formRapida.value.email,
        telefono: formRapida.value.telefono
      }
      const crearRes = await fetch('/api/admin/personas', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(nuevaPersona)
      })
      if (!crearRes.ok) {
        const errData = await crearRes.json()
        throw new Error(errData.detail || 'Error al crear persona')
      }
      persona = await crearRes.json()
    }
    // 3. Crear reserva
    const reservaData = {
      id_persona: persona.id_persona,
      id_actividad: formRapida.value.id_actividad,
      numero_personas: formRapida.value.numero_personas
    }
    const res = await fetch('/api/admin/reservas', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(reservaData)
    })
    if (!res.ok) {
      const errData = await res.json()
      throw new Error(errData.detail || 'Error al crear reserva')
    }
    successMessage.value = 'Reserva rápida creada correctamente'
    formRapida.value = { nombre: '', apellido: '', email: '', telefono: '', id_actividad: '', numero_personas: 1 }
    fetchReservas()
  } catch (e) {
    errorMessage.value = e.message
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

onMounted(() => {
  fetchReservas()
  fetchActividades()
})
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

/* Formulario de Reserva Rápida */
.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.btn-crear-rapida {
  background-color: #007bff;
  color: white;
  padding: 0.5rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
  transition: background-color 0.2s ease;
}

.btn-crear-rapida:hover {
  background-color: #0069d9;
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
  
  .form-grid {
    grid-template-columns: 1fr;
  }
}

</style>
