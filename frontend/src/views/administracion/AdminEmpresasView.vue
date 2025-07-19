<template>
  <div class="contenedor-principal">
    <h1>Gestión de Empresas</h1>
    
    <form @submit.prevent="crearEmpresa" class="creation-form">
      <div class="form-grid">
        <div class="form-group">
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" v-model="form.nombre" required>
        </div>
        <div class="form-group">
          <label for="nif">NIF:</label>
          <input type="text" id="nif" v-model="form.nif">
        </div>
        <div class="form-group">
          <label for="razon_social">Razón Social:</label>
          <input type="text" id="razon_social" v-model="form.razon_social" required>
        </div>
        <div class="form-group">
          <label for="direccion">Dirección:</label>
          <input type="text" id="direccion" v-model="form.direccion" required>
        </div>
        <div class="form-group">
          <label for="provincia">Provincia:</label>
          <input type="text" id="provincia" v-model="form.provincia" required>
        </div>
        <div class="form-group">
          <label for="cp">Código Postal:</label>
          <input type="text" id="cp" v-model="form.cp" required>
        </div>
      </div>
      <button type="submit">Crear Empresa</button>
    </form>
    <p v-if="error" class="error-message">{{ error }}</p>
    
    <hr>
    <h2>Empresas Activas</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre</th>
          <th>NIF</th>
          <th>Contacto</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="empresa in empresas" :key="empresa.id_empresa">
          <td>{{ empresa.id_empresa }}</td>
          <td>{{ empresa.nombre }}</td>
          <td>{{ empresa.nif }}</td>
          <td>{{ empresa.persona ? empresa.persona.nombre : 'N/A' }}</td>
          <td>
            <button class="btn-eliminar" @click="desactivarEmpresa(empresa.id_empresa)">Eliminar</button>
            <button class="btn-editar" @click="abrirModalEditar(empresa)">Editar</button>
            <button class="btn-detalles" @click="verDetalles(empresa)">Ver Detalles</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Tarjeta de Detalles -->
    <div v-if="empresaSeleccionada" class="detalles-card">
      <h3>Detalles de {{ empresaSeleccionada.nombre }}</h3>
      <ul>
        <li><strong>ID:</strong> {{ empresaSeleccionada.id_empresa }}</li>
        <li><strong>NIF:</strong> {{ empresaSeleccionada.nif }}</li>
        <li><strong>Contacto:</strong> {{ empresaSeleccionada.persona ? `${empresaSeleccionada.persona.nombre} (${empresaSeleccionada.persona.email})` : 'No asignado' }}</li>
        <li><strong>Dirección:</strong> {{ empresaSeleccionada.direccion }}</li>
        <li><strong>Provincia:</strong> {{ empresaSeleccionada.provincia }}</li>
        <li><strong>CP:</strong> {{ empresaSeleccionada.cp }}</li>
        <li><strong>Sector:</strong> {{ empresaSeleccionada.sector }}</li>
      </ul>
      <button @click="cerrarDetalles">Cerrar</button>
    </div>

    <!-- Modal de Edición -->
    <EditarEmpresaModal
      v-if="isEditModalVisible"
      :empresa="empresaAEditar"
      @close="cerrarModalEditar"
      @update="actualizarEmpresa"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import EditarEmpresaModal from '@/components/administracion/EditarEmpresaModal.vue'
import '@/assets/styles/admin.css'

const form = ref({ nombre: '', nif: '', razon_social: '', direccion: '', provincia: '', cp: '' })
const empresas = ref([])
const error = ref(null)
const isEditModalVisible = ref(false)
const empresaAEditar = ref(null)
const empresaSeleccionada = ref(null)

const fetchEmpresas = async () => {
  try {
    const res = await fetch('/api/admin/empresas')
    if (!res.ok) throw new Error('Error al cargar empresas')
    empresas.value = await res.json()
  } catch (e) {
    error.value = e.message
  }
}

const crearEmpresa = async () => {
  error.value = null
  try {
    const res = await fetch('/api/admin/empresas', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form.value)
    })
    if (!res.ok) {
      const errData = await res.json()
      throw new Error(errData.detail || 'Error al crear empresa')
    }
    form.value = { nombre: '', nif: '', razon_social: '', direccion: '', provincia: '', cp: '' }
    fetchEmpresas()
  } catch (e) {
    error.value = e.message
  }
}

const desactivarEmpresa = async (id) => {
  empresaSeleccionada.value = null
  await fetch(`/api/admin/empresas/${id}`, { method: 'DELETE' })
  fetchEmpresas()
}

const abrirModalEditar = (empresa) => {
  empresaSeleccionada.value = null
  empresaAEditar.value = { ...empresa }
  isEditModalVisible.value = true
}

const cerrarModalEditar = () => {
  isEditModalVisible.value = false
  empresaAEditar.value = null
}

const actualizarEmpresa = async ({ id, data }) => {
  await fetch(`/api/admin/empresas/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  cerrarModalEditar()
  fetchEmpresas()
}

const verDetalles = (empresa) => {
  empresaSeleccionada.value = empresa
}

const cerrarDetalles = () => {
  empresaSeleccionada.value = null
}

onMounted(fetchEmpresas)
</script>

