<template>
  <div class="contenedor-principal">
    <h1>Gestión de Empresas</h1>
    
    <form @submit.prevent="crearEmpresa" class="creation-form">
      <div class="form-grid">
        <div class="form-group">
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" v-model="form.nombre" required minlength="2" maxlength="100">
        </div>
        <div class="form-group">
          <label for="nif">NIF:</label>
          <input type="text" id="nif" v-model="form.nif" @input="form.nif = $event.target.value.toUpperCase()" pattern="^([A-Z]{1}\d{7}[A-Z0-9]{1})|(\d{8}[A-Z]{1})|([XYZ]{1}\d{7}[A-Z]{1})$" title="Formato de NIF, DNI o NIE inválido.">
        </div>
        <div class="form-group">
          <label for="razon_social">Razón Social:</label>
          <input type="text" id="razon_social" v-model="form.razon_social" required minlength="2" maxlength="100">
        </div>
        <div class="form-group">
          <label for="direccion">Dirección:</label>
          <input type="text" id="direccion" v-model="form.direccion" required minlength="5" maxlength="150">
        </div>
        <div class="form-group">
          <label for="provincia">Provincia:</label>
          <input type="text" id="provincia" v-model="form.provincia" required maxlength="50">
        </div>
        <div class="form-group">
          <label for="cp">Código Postal:</label>
          <input type="text" id="cp" v-model="form.cp" required pattern="\d{5}" title="El código postal debe tener 5 dígitos.">
        </div>
        <div class="form-group">
          <label for="nombre_contacto">Nombre de Contacto:</label>
          <input type="text" id="nombre_contacto" v-model="form.nombre_contacto">
        </div>
        <div class="form-group">
          <label for="telefono_empresa">Teléfono:</label>
          <input type="tel" id="telefono_empresa" v-model="form.telefono_empresa">
        </div>
        <div class="form-group">
          <label for="email_empresa">Email:</label>
          <input type="email" id="email_empresa" v-model="form.email_empresa">
        </div>
        <div class="form-group full-width">
          <label for="observaciones">Observaciones:</label>
          <textarea id="observaciones" v-model="form.observaciones"></textarea>
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
            <button class="btn-eliminar" @click="desactivarEmpresa(empresa.id_empresa)">Desactivar</button>
            <button class="btn-editar" @click="abrirModalEditar(empresa)">Editar</button>
            <button class="btn-detalles" @click="verDetalles(empresa)">Ver Detalles</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Nueva sección para empresas inactivas -->
    <template v-if="empresasInactivas.length > 0">
      <hr>
      <h2>Empresas Inactivas</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>NIF</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="empresa in empresasInactivas" :key="empresa.id_empresa">
            <td>{{ empresa.id_empresa }}</td>
            <td>{{ empresa.nombre }}</td>
            <td>{{ empresa.nif }}</td>
            <td>
              <button class="btn-reactivar" @click="reactivarEmpresa(empresa.id_empresa)">Reactivar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </template>

    <!-- Tarjeta de Detalles -->
    <div v-if="empresaSeleccionada" class="detalles-card">
      <h3>Detalles de {{ empresaSeleccionada.nombre }}</h3>
      <ul>
        <li><strong>ID:</strong> {{ empresaSeleccionada.id_empresa }}</li>
        <li><strong>NIF:</strong> {{ empresaSeleccionada.nif }}</li>
        <li><strong>Contacto Principal:</strong> {{ empresaSeleccionada.persona ? `${empresaSeleccionada.persona.nombre} (${empresaSeleccionada.persona.email})` : 'No asignado' }}</li>
        <li><strong>Dirección:</strong> {{ empresaSeleccionada.direccion }}, {{ empresaSeleccionada.cp }}, {{ empresaSeleccionada.provincia }}</li>
        <hr>
        <li><strong>Contacto Empresa:</strong> {{ empresaSeleccionada.nombre_contacto }}</li>
        <li><strong>Teléfono Empresa:</strong> {{ empresaSeleccionada.telefono_empresa }}</li>
        <li><strong>Email Empresa:</strong> {{ empresaSeleccionada.email_empresa }}</li>
        <hr>
        <li><strong>Sector:</strong> {{ empresaSeleccionada.sector }}</li>
        <li><strong>Observaciones:</strong> {{ empresaSeleccionada.observaciones }}</li>
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

const form = ref({ nombre: '', nif: '', razon_social: '', direccion: '', provincia: '', cp: '', nombre_contacto: '', telefono_empresa: '', email_empresa: '', observaciones: '' })
const empresas = ref([])
const empresasInactivas = ref([])
const error = ref(null)
const isEditModalVisible = ref(false)
const empresaAEditar = ref(null)
const empresaSeleccionada = ref(null)

const fetchEmpresas = async () => {
  try {
    const res = await fetch('/api/admin/empresas')
    if (!res.ok) throw new Error('Error al cargar empresas')
    empresas.value = await res.json()

    const resInactivas = await fetch('/api/admin/empresas/inactivas')
    if (!resInactivas.ok) throw new Error('Error al cargar empresas inactivas')
    empresasInactivas.value = await resInactivas.json()

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
    form.value = { nombre: '', nif: '', razon_social: '', direccion: '', provincia: '', cp: '', nombre_contacto: '', telefono_empresa: '', email_empresa: '', observaciones: '' }
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

const reactivarEmpresa = async (id) => {
  await fetch(`/api/admin/empresas/${id}/reactivar`, { method: 'PUT' })
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

<style>
hr {
    border: none;
    border-top: 1px solid var(--shoftgreen);
    margin: 1rem 0;
}
</style>