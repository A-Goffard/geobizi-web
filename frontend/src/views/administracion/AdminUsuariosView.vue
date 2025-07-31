<template>
  <div class="contenedor-principal">
    <h1>Gestión de Usuarios</h1>
    <form @submit.prevent="crearUsuario">
      <div class="form-group">
        <label for="email">Correo Electrónico:</label>
        <input type="email" id="email" v-model="form.email" required maxlength="100">
      </div>
      <div class="form-group">
        <label for="password">Contraseña:</label>
        <input type="password" id="password" v-model="form.password" required minlength="8" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Debe contener al menos un número, una mayúscula, una minúscula y 8 o más caracteres.">
      </div>
      <div class="form-group">
        <label for="id_rol">Rol:</label>
        <select id="id_rol" v-model="form.id_rol">
          <option v-for="rol in roles" :key="rol.id" :value="rol.id">{{ rol.nombre }}</option>
        </select>
      </div>
      <button type="submit">Crear usuario</button>
    </form>
    <!-- Mensaje de error -->
    <p v-if="error" class="error-message">{{ error }}</p>
    <hr>
    <h2>Usuarios activos</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Email</th>
          <th>Rol</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="usuario in usuarios" :key="usuario.id_usuario">
          <td>{{ usuario.id_usuario }}</td>
          <td>{{ usuario.email }}</td>
          <td>{{ usuario.rol ? usuario.rol.nombre : 'Sin rol' }}</td>
          <td>
            <button class="btn-eliminar" @click="desactivarUsuario(usuario.id_usuario)">Eliminar</button>
            <button class="btn-editar" @click="abrirModalEditar(usuario)">Editar</button>
            <button class="btn-detalles" @click="verDetalles(usuario)">Ver Detalles</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Nueva sección para usuarios inactivos -->
    <template v-if="usuariosInactivos.length > 0">
      <hr>
      <h2>Usuarios inactivos</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Email</th>
            <th>Rol</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="usuario in usuariosInactivos" :key="usuario.id_usuario">
            <td>{{ usuario.id_usuario }}</td>
            <td>{{ usuario.email }}</td>
            <td>{{ usuario.rol ? usuario.rol.nombre : 'Sin rol' }}</td>
            <td>
              <button class="btn-reactivar" @click="reactivarUsuario(usuario.id_usuario)">Reactivar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </template>

    <!-- Tarjeta de Detalles del Usuario -->
    <div v-if="usuarioSeleccionado" class="detalles-card">
      <h3>Detalles de {{ usuarioSeleccionado.email }}</h3>
      <ul>
        <li><strong>ID Usuario:</strong> {{ usuarioSeleccionado.id_usuario }}</li>
        <li><strong>ID Persona:</strong> {{ usuarioSeleccionado.id_persona || 'No asignado' }}</li>
        <li><strong>Rol:</strong> {{ usuarioSeleccionado.rol ? usuarioSeleccionado.rol.nombre : 'Sin rol' }} (ID: {{ usuarioSeleccionado.rol ? usuarioSeleccionado.rol.id_rol : 'N/A' }})</li>
        <li><strong>Es Superusuario:</strong> {{ usuarioSeleccionado.is_superuser ? 'Sí' : 'No' }}</li>
        <li><strong>Activo:</strong> {{ usuarioSeleccionado.activo ? 'Sí' : 'No' }}</li>
      </ul>
      <button @click="cerrarDetalles">Cerrar</button>
    </div>

    <!-- Modal de Edición -->
    <EditarUsuarioModal
      v-if="isEditModalVisible"
      :usuario="usuarioAEditar"
      :roles="roles"
      @close="cerrarModalEditar"
      @update="actualizarUsuario"
    />
  </div>
    <!-- Botón para volver al panel de administración -->
    <div class="contenedor-principal"><button class="btn-editar" @click="volverAlPanel">Volver al panel</button></div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import EditarUsuarioModal from '@/components/administracion/EditarUsuarioModal.vue'
import '@/assets/styles/admin.css'

// Define los roles reales (deben coincidir con los de la BD)
const roles = [
  { id: 1, nombre: 'Administrador' },
  { id: 2, nombre: 'Gestor' },
  { id: 3, nombre: 'Cliente' },
  { id: 4, nombre: 'Empresa' }
]

const form = ref({
  email: '',
  password: '',
  id_rol: 3, // Cliente por defecto
  id_persona: null
})

const usuarios = ref([])
const usuariosInactivos = ref([]) // Nuevo estado para usuarios inactivos
const isEditModalVisible = ref(false)
const usuarioAEditar = ref(null)
const usuarioSeleccionado = ref(null)
const error = ref(null) // Nuevo estado para el mensaje de error

const fetchUsuarios = async () => {
  try {
    const resActivos = await fetch('/api/admin/usuarios')
    usuarios.value = await resActivos.json()

    const resInactivos = await fetch('/api/admin/usuarios/inactivos')
    usuariosInactivos.value = await resInactivos.json()
  } catch (e) {
    console.error('No se pudo conectar con el backend. ¿Está corriendo en el puerto 5000?')
  }
}

const crearUsuario = async () => {
  error.value = null // Limpiamos el error anterior
  try {
    const response = await fetch('/api/admin/usuarios', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form.value)
    })

    if (!response.ok) {
      const errorData = await response.json()
      throw new Error(errorData.detail || 'Error desconocido al crear el usuario.')
    }

    form.value = { email: '', password: '', id_rol: 3, id_persona: null }
    fetchUsuarios()
  } catch (e) {
    error.value = e.message
    console.error(e)
  }
}

const desactivarUsuario = async (id) => {
    usuarioSeleccionado.value = null // Cierra la tarjeta de detalles si está abierta

  // Añadimos /api al principio de la ruta
  await fetch(`/api/admin/usuarios/${id}`, { method: 'DELETE' })
  fetchUsuarios()
}

const reactivarUsuario = async (id) => {
  await fetch(`/api/admin/usuarios/${id}/reactivar`, { method: 'PUT' })
  fetchUsuarios()
}

const abrirModalEditar = (usuario) => {
  usuarioSeleccionado.value = null // Cierra la tarjeta de detalles si está abierta
  usuarioAEditar.value = { ...usuario } // Copiamos el objeto para evitar mutaciones directas
  isEditModalVisible.value = true
}

const cerrarModalEditar = () => {
  isEditModalVisible.value = false
  usuarioAEditar.value = null
}

const actualizarUsuario = async ({ id, data }) => {
  const payload = { ...data }
  if (!payload.password) {
    delete payload.password
  }

  try {
    const response = await fetch(`/api/admin/usuarios/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    if (!response.ok) {
      const errorData = await response.json()
      error.value = errorData.detail || 'Error al actualizar usuario'
      return
    }
    cerrarModalEditar()
    fetchUsuarios()
  } catch (e) {
    error.value = e.message
  }
}

const verDetalles = (usuario) => {
  usuarioSeleccionado.value = usuario
}

const cerrarDetalles = () => {
  usuarioSeleccionado.value = null
}

const volverAlPanel = () => {
  // Redirige al panel de administración
  window.location.href = '/admin/panel';
}

onMounted(fetchUsuarios)
</script>

