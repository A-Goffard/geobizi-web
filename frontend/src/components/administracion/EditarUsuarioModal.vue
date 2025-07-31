<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <h2>Editar Usuario</h2>
      <form @submit.prevent="guardarCambios">
        <div class="form-group">
          <label for="edit-email">Correo Electrónico:</label>
          <input type="email" id="edit-email" v-model="form.email" required>
        </div>
        <div class="form-group">
          <label for="edit-password">Nueva Contraseña (dejar en blanco para no cambiar):</label>
          <input type="password" id="edit-password" v-model="form.password">
        </div>
        <div class="form-group">
          <label for="edit-id_rol">Rol:</label>
          <select id="edit-id_rol" v-model="form.id_rol">
            <option :value="null">
              (Mantener: {{ getRolNombre(props.usuario.id_rol) }})
            </option>
            <option v-for="rol in roles" :key="rol.id" :value="rol.id">
              {{ rol.nombre }}
            </option>
          </select>
        </div>
        <div class="form-group">
          <label for="edit-id_persona">ID Persona:</label>
          <input type="number" id="edit-id_persona" v-model="form.id_persona" min="1">
        </div>
        <div class="form-group">
          <label for="edit-superuser">¿Superusuario?</label>
          <select id="edit-superuser" v-model="form.is_superuser">
            <option :value="false">No</option>
            <option :value="true">Sí</option>
          </select>
        </div>
        <div class="modal-actions">
          <button type="submit">Guardar Cambios</button>
          <button type="button" class="btn-cancelar" @click="$emit('close')">Cancelar</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  usuario: Object,
  roles: Array
})

const emit = defineEmits(['close', 'update'])

const form = ref({
  email: '',
  password: '',
  id_rol: null,
  id_persona: null,
  is_superuser: false // Por defecto siempre "No"
})

function getRolNombre(id) {
  const rol = props.roles.find(r => r.id === id)
  return rol ? rol.nombre : 'Sin rol'
}

// Actualiza el formulario cuando cambia el usuario
watch(() => props.usuario, (newVal) => {
  if (newVal) {
    form.value.email = newVal.email
    form.value.id_rol = newVal.id_rol
    form.value.id_persona = newVal.id_persona
    form.value.is_superuser = newVal.is_superuser ?? false
    form.value.password = '' // La contraseña siempre empieza vacía por seguridad
  }
}, { immediate: true })

const guardarCambios = () => {
  let payload = { ...form.value }
  if (payload.id_rol === null) {
    // No enviar id_rol si no se selecciona nada
    delete payload.id_rol
  }
  emit('update', { id: props.usuario.id_usuario, data: payload })
}
</script>



