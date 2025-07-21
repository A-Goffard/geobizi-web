<template>
  <div class="contenedor-principal">
    <h1>Gestión de Personas</h1>
    
    <form @submit.prevent="crearPersona" class="creation-form">
      <div class="form-grid">
        <div class="form-group">
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" v-model="form.nombre" required minlength="2" maxlength="50">
        </div>
        <div class="form-group">
          <label for="apellido">Apellido:</label>
          <input type="text" id="apellido" v-model="form.apellido" required minlength="2" maxlength="50">
        </div>
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="form.email" required>
        </div>
        <div class="form-group">
          <label for="telefono">Teléfono:</label>
          <input type="tel" id="telefono" v-model="form.telefono" required pattern="^\+?(\d\s?){9,15}$" title="Introduce un número de teléfono válido.">
        </div>
      </div>
      <button type="submit">Crear Persona</button>
    </form>
    <p v-if="error" class="error-message">{{ error }}</p>
    
    <hr>
    <h2>Personas Activas</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre Completo</th>
          <th>Email</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="persona in personas" :key="persona.id_persona">
          <td>{{ persona.id_persona }}</td>
          <td>{{ persona.nombre }} {{ persona.apellido }}</td>
          <td>{{ persona.email }}</td>
          <td>
            <button class="btn-eliminar" @click="desactivarPersona(persona.id_persona)">Desactivar</button>
            <button class="btn-editar" @click="abrirModalEditar(persona)">Editar</button>
            <button class="btn-detalles" @click="verDetalles(persona)">Ver Detalles</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Personas Inactivas -->
    <template v-if="personasInactivas.length > 0">
      <hr>
      <h2>Personas Inactivas</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre Completo</th>
            <th>Email</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="persona in personasInactivas" :key="persona.id_persona">
            <td>{{ persona.id_persona }}</td>
            <td>{{ persona.nombre }} {{ persona.apellido }}</td>
            <td>{{ persona.email }}</td>
            <td>
              <button class="btn-reactivar" @click="reactivarPersona(persona.id_persona)">Reactivar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </template>

    <!-- Tarjeta de Detalles -->
    <div v-if="personaSeleccionada" class="detalles-card">
      <h3>Detalles de {{ personaSeleccionada.nombre }} {{ personaSeleccionada.apellido }}</h3>
      <ul>
        <li><strong>ID:</strong> {{ personaSeleccionada.id_persona }}</li>
        <li><strong>Email:</strong> {{ personaSeleccionada.email }}</li>
        <li><strong>Teléfono:</strong> {{ personaSeleccionada.telefono }}</li>
        <li><strong>DNI:</strong> {{ personaSeleccionada.dni || 'N/A' }}</li>
        <li><strong>Dirección:</strong> {{ personaSeleccionada.direccion || 'N/A' }}</li>
        <li><strong>Código Postal:</strong> {{ personaSeleccionada.cp || 'N/A' }}</li>
        <li><strong>Población:</strong> {{ personaSeleccionada.poblacion || 'N/A' }}</li>
        <li><strong>País:</strong> {{ personaSeleccionada.pais || 'N/A' }}</li>
        <li><strong>Fecha de Nacimiento:</strong> {{ personaSeleccionada.fecha_nacimiento ? new Date(personaSeleccionada.fecha_nacimiento).toLocaleDateString() : 'N/A' }}</li>
        <li><strong>Género:</strong> {{ personaSeleccionada.genero || 'N/A' }}</li>
        <li><strong>Observaciones:</strong> {{ personaSeleccionada.observaciones || 'N/A' }}</li>
      </ul>
      <button @click="cerrarDetalles">Cerrar</button>
    </div>

    <!-- Modal de Edición -->
    <EditarPersonaModal
      v-if="isEditModalVisible"
      :persona="personaAEditar"
      @close="cerrarModalEditar"
      @update="actualizarPersona"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import EditarPersonaModal from '@/components/administracion/EditarPersonaModal.vue'
import '@/assets/styles/admin.css'

const form = ref({ nombre: '', apellido: '', email: '', telefono: '' })
const personas = ref([])
const personasInactivas = ref([])
const error = ref(null)
const isEditModalVisible = ref(false)
const personaAEditar = ref(null)
const personaSeleccionada = ref(null)

const fetchPersonas = async () => {
  try {
    const res = await fetch('/api/admin/personas')
    if (!res.ok) throw new Error('Error al cargar personas')
    personas.value = await res.json()

    const resInactivas = await fetch('/api/admin/personas/inactivas')
    if (!resInactivas.ok) throw new Error('Error al cargar personas inactivas')
    personasInactivas.value = await resInactivas.json()
  } catch (e) {
    error.value = e.message
  }
}

const crearPersona = async () => {
  error.value = null
  try {
    const res = await fetch('/api/admin/personas', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form.value)
    })
    if (!res.ok) {
      const errData = await res.json()
      throw new Error(errData.detail || 'Error al crear persona')
    }
    form.value = { nombre: '', apellido: '', email: '', telefono: '' }
    fetchPersonas()
  } catch (e) {
    error.value = e.message
  }
}

const desactivarPersona = async (id) => {
  personaSeleccionada.value = null
  await fetch(`/api/admin/personas/${id}`, { method: 'DELETE' })
  fetchPersonas()
}

const reactivarPersona = async (id) => {
  await fetch(`/api/admin/personas/${id}/reactivar`, { method: 'PUT' })
  fetchPersonas()
}

const abrirModalEditar = (persona) => {
  personaSeleccionada.value = null
  personaAEditar.value = { ...persona }
  isEditModalVisible.value = true
}

const cerrarModalEditar = () => {
  isEditModalVisible.value = false
  personaAEditar.value = null
}

const actualizarPersona = async ({ id, data }) => {
  await fetch(`/api/admin/personas/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  cerrarModalEditar()
  fetchPersonas()
}

const verDetalles = (persona) => {
  personaSeleccionada.value = persona
}

const cerrarDetalles = () => {
  personaSeleccionada.value = null
}

onMounted(fetchPersonas)
</script>

