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
          <th>Persona</th>
          <th>Actividad</th>
          <th>Aprobada</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="reserva in reservas" :key="reserva.id_reserva">
          <td>{{ reserva.id_reserva }}</td>
          <td>{{ reserva.persona ? reserva.persona.nombre : 'N/A' }}</td>
          <td>{{ reserva.actividad ? reserva.actividad.nombre : 'N/A' }}</td>
          <td>{{ reserva.aprobada ? 'Sí' : 'No' }}</td>
          <td>
            <button class="btn-eliminar" @click="eliminarReserva(reserva.id_reserva)">Eliminar</button>
            <button class="btn-editar" @click="abrirModalEditar(reserva)">Editar</button>
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
</template>

<script setup>
import { ref, onMounted } from 'vue'
import EditarReservaModal from '@/components/administracion/EditarReservaModal.vue'
import '@/assets/styles/admin.css'

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

onMounted(fetchReservas)
</script>
