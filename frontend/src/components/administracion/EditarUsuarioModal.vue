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
            <option :value="1">Superusuario</option>
            <option :value="2">Empleado</option>
            <option :value="3">Visitante</option>
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
  usuario: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['close', 'update'])

const form = ref({
  email: '',
  password: '',
  id_rol: 3,
  id_persona: null
})

// Cuando el prop 'usuario' cambia, actualizamos el formulario con sus datos
watch(() => props.usuario, (newVal) => {
  if (newVal) {
    form.value.email = newVal.email
    form.value.id_rol = newVal.id_rol
    form.value.id_persona = newVal.id_persona
    form.value.password = '' // La contraseña siempre empieza vacía por seguridad
  }
}, { immediate: true })

const guardarCambios = () => {
  emit('update', { id: props.usuario.id_usuario, data: form.value })
}
</script>


