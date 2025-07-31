<template>
  <div class="contenedor-principal">
    <h1>Gestión de Actividades</h1>
    
    <!-- Formulario de Creación -->
    <form @submit.prevent="crearActividad" class="creation-form">
      <div class="form-grid">
        <div class="form-group">
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre" v-model="form.nombre" required maxlength="100">
        </div>
        <div class="form-group">
          <label for="tipo">Tipo:</label>
          <input type="text" id="tipo" v-model="form.tipo" maxlength="50">
        </div>
        <div class="form-group">
          <label for="lugar">Lugar:</label>
          <input type="text" id="lugar" v-model="form.lugar" maxlength="100">
        </div>
        <div class="form-group">
          <label for="fecha">Fecha:</label>
          <input type="date" id="fecha" v-model="form.fecha">
        </div>
        <div class="form-group">
          <label for="hora">Hora:</label>
          <input type="time" id="hora" v-model="form.hora">
        </div>
        <div class="form-group">
          <label for="categoria">Categoría:</label>
          <select id="categoria" v-model="form.categoria">
            <option value="digital">Digital</option>
            <option value="bioregeneracion">Proyecto de Bioregeneración</option>
            <option value="educativa">Educativa</option>
            <option value="turistica">Turística</option>
          </select>
        </div>
        <div class="form-group">
          <label for="precio">Precio por persona (€):</label>
          <input type="number" step="0.01" id="precio" v-model.number="form.precio" min="0">
        </div>
        <div class="form-group full-width">
          <label for="descripcion">Descripción:</label>
          <textarea id="descripcion" v-model="form.descripcion" maxlength="500"></textarea>
        </div>
      </div>
      <button type="submit">Crear Actividad</button>
    </form>
    <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
    <p v-if="error" class="error-message">{{ error }}</p>
    
    <hr>
    <h2>Actividades Activas</h2>
    <table>
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Fecha</th>
          <th>Lugar</th>
          <th>Precio</th>
          <th>Estado</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="actividad in actividades" :key="actividad.id_actividad">
          <td>{{ actividad.nombre }}</td>
          <td>
            <div>{{ formatDate(actividad.fecha) }}</div>
            <div>{{ actividad.hora }}</div>
          </td>
          <td>{{ actividad.lugar }}</td>
          <td>{{ actividad.precio }} €</td>
          <td>{{ actividad.estado }}</td>
          <td>
            <button class="btn-eliminar" @click="desactivarActividad(actividad.id_actividad)">Eliminar</button>
            <button class="btn-editar" @click="abrirModalEditar(actividad)">Editar</button>
            <button class="btn-detalles" @click="verDetalles(actividad)">Ver Detalles</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Nueva sección para actividades inactivas -->
    <template v-if="actividadesInactivas.length > 0">
      <hr>
      <h2>Actividades inactivas</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Tipo</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="actividad in actividadesInactivas" :key="actividad.id_actividad">
            <td>{{ actividad.id_actividad }}</td>
            <td>{{ actividad.nombre }}</td>
            <td>{{ actividad.tipo }}</td>
            <td>
              <button class="btn-reactivar" @click="reactivarActividad(actividad.id_actividad)">Reactivar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </template>

    <!-- Tarjeta de Detalles de la Actividad -->
    <div v-if="actividadSeleccionada" class="detalles-card">
      <h3>Detalles de {{ actividadSeleccionada.nombre }}</h3>
      <ul>
        <li><strong>ID:</strong> {{ actividadSeleccionada.id_actividad }}</li>
        <li><strong>Tipo:</strong> {{ actividadSeleccionada.tipo }}</li>
        <li><strong>Lugar:</strong> {{ actividadSeleccionada.lugar }}</li>
        <li><strong>Fecha:</strong> {{ formatDate(actividadSeleccionada.fecha) }}</li>
        <li><strong>Hora:</strong> {{ actividadSeleccionada.hora }}</li>
        <li><strong>Categoría:</strong> {{ actividadSeleccionada.categoria }}</li>
        <li><strong>Estado:</strong> {{ actividadSeleccionada.estado }}</li>
        <li><strong>Precio por persona:</strong> {{ actividadSeleccionada.precio }} €</li>
        <li><strong>Coste para la empresa:</strong> {{ actividadSeleccionada.coste_economico }} €</li>
        <li><strong>Descripción:</strong> {{ actividadSeleccionada.descripcion }}</li>
      </ul>
      <button @click="cerrarDetalles">Cerrar</button>
    </div>

    <!-- Modal de Edición -->
    <EditarActividadModal
      v-if="isEditModalVisible"
      :actividad="actividadAEditar"
      @close="cerrarModalEditar"
      @update="actualizarActividad"
    />
    <!-- Botón para volver al panel de administración -->
    <div class="contenedor-principal"><button class="btn-editar" @click="volverAlPanel">Volver al panel</button></div>
  </div>

</template>

<script setup>
import { ref, onMounted } from 'vue'
import EditarActividadModal from '@/components/administracion/EditarActividadModal.vue'
import '@/assets/styles/admin.css'

const form = ref({
  nombre: '',
  tipo: '',
  lugar: '',
  fecha: null,
  hora: '',
  descripcion: '',
  estado: 'pendiente',
  categoria: 'educativa',
  precio: 0,
  coste_economico: 0 // Campo añadido
})
const actividades = ref([])
const actividadesInactivas = ref([])
const error = ref(null)
const successMessage = ref('')
const isEditModalVisible = ref(false)
const actividadAEditar = ref(null)
const actividadSeleccionada = ref(null)

const formatDate = (dateString) => {
  if (!dateString) return 'N/A'
  const date = new Date(dateString)
  return date.toLocaleDateString('es-ES')
}

const fetchActividades = async () => {
  try {
    const res = await fetch('/api/admin/actividades')
    if (!res.ok) throw new Error('Error al cargar actividades')
    actividades.value = await res.json()

    const resInactivas = await fetch('/api/admin/actividades/inactivas')
    if (!resInactivas.ok) throw new Error('Error al cargar actividades inactivas')
    actividadesInactivas.value = await resInactivas.json()
  } catch (e) {
    error.value = e.message
  }
}

const crearActividad = async () => {
  error.value = null
  successMessage.value = ''
  try {
    // Combina fecha y hora solo para el envío
    let actividadPayload = { ...form.value }
    if (form.value.fecha && form.value.hora) {
      actividadPayload.fecha = new Date(form.value.fecha + 'T' + form.value.hora).toISOString()
    }
    // Elimina campos que puedan ser null o vacíos si no son obligatorios
    Object.keys(actividadPayload).forEach(key => {
      if (actividadPayload[key] === null || actividadPayload[key] === '') {
        delete actividadPayload[key]
      }
    })
    const res = await fetch('/api/admin/actividades', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(actividadPayload)
    })
    if (!res.ok) {
      let errMsg = 'Error al crear actividad'
      let errorBody = null
      try {
        errorBody = await res.clone().json()
        errMsg = errorBody.detail || errMsg
      } catch {
        errMsg = await res.text()
      }
      throw new Error(errMsg)
    }
    const result = await res.json()
    successMessage.value = result.msg || 'Actividad creada correctamente.'
    form.value = { nombre: '', tipo: '', lugar: '', fecha: '', hora: '', descripcion: '', estado: 'pendiente', categoria: 'educativa', precio: 0, coste_economico: 0 }
    fetchActividades()
  } catch (e) {
    error.value = e.message
  }
}

const desactivarActividad = async (id) => {
  actividadSeleccionada.value = null
  await fetch(`/api/admin/actividades/${id}`, { method: 'DELETE' })
  fetchActividades()
}

const reactivarActividad = async (id) => {
  await fetch(`/api/admin/actividades/${id}/reactivar`, { method: 'PUT' })
  fetchActividades()
}

const abrirModalEditar = (actividad) => {
  actividadSeleccionada.value = null
  actividadAEditar.value = { ...actividad }
  isEditModalVisible.value = true
}

const cerrarModalEditar = () => {
  isEditModalVisible.value = false
  actividadAEditar.value = null
}

const actualizarActividad = async ({ id, data }) => {
  await fetch(`/api/admin/actividades/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  cerrarModalEditar()
  fetchActividades()
}

const verDetalles = (actividad) => {
  actividadSeleccionada.value = actividad
}

const cerrarDetalles = () => {
  actividadSeleccionada.value = null
}

const volverAlPanel = () => {
  // Redirige al panel de administración
  window.location.href = '/admin/panel';
}

onMounted(fetchActividades)
</script>

