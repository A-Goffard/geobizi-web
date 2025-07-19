<template>
  <div class="contenedor-principal">
    <h1>Gestión de Personas</h1>
    
    <form @submit.prevent="crearPersona">
      <div class="form-group">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" v-model="form.nombre" required>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="form.email" required>
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
          <th>Nombre</th>
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
            <button class="btn-eliminar" @click="desactivarPersona(persona.id_persona)">Eliminar</button>
            <button class="btn-editar" @click="abrirModalEditar(persona)">Editar</button>
          </td>
        </tr>
      </tbody>
    </table>

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

const form = ref({ nombre: '', email: '' })
const personas = ref([])
const error = ref(null)
const isEditModalVisible = ref(false)
const personaAEditar = ref(null)

const fetchPersonas = async () => {
  try {
    const res = await fetch('/api/admin/personas')
    if (!res.ok) throw new Error('Error al cargar personas')
    personas.value = await res.json()
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
    form.value = { nombre: '', email: '' }
    fetchPersonas()
  } catch (e) {
    error.value = e.message
  }
}

const desactivarPersona = async (id) => {
  await fetch(`/api/admin/personas/${id}`, { method: 'DELETE' })
  fetchPersonas()
}

const abrirModalEditar = (persona) => {
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

onMounted(fetchPersonas)
</script>

