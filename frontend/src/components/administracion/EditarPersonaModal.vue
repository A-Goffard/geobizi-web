<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <h2>Editar Persona</h2>
      <form @submit.prevent="guardarCambios" class="form-grid">
        <!-- Fila 1: Nombre y Apellido -->
        <div class="form-group">
          <label for="edit-nombre">Nombre:</label>
          <input type="text" id="edit-nombre" v-model="form.nombre" required minlength="2" maxlength="50">
        </div>
        <div class="form-group">
          <label for="edit-apellido">Apellido:</label>
          <input type="text" id="edit-apellido" v-model="form.apellido" required minlength="2" maxlength="50">
        </div>

        <!-- Fila 2: Email y Teléfono -->
        <div class="form-group">
          <label for="edit-email">Email:</label>
          <input type="email" id="edit-email" v-model="form.email" required>
        </div>
        <div class="form-group">
          <label for="edit-telefono">Teléfono:</label>
          <input type="tel" id="edit-telefono" v-model="form.telefono" required pattern="^\+?(\d\s?){9,15}$" title="Introduce un número de teléfono válido.">
        </div>

        <!-- Fila 3: DNI y Fecha Nacimiento -->
        <div class="form-group">
          <label for="edit-dni">DNI:</label>
          <input type="text" id="edit-dni" v-model="form.dni" @input="form.dni = $event.target.value.toUpperCase()" pattern="^(\d{8}[A-Z]{1})|([XYZ]{1}\d{7}[A-Z]{1})$" title="Formato de DNI/NIE inválido.">
        </div>
        <div class="form-group">
          <label for="edit-fecha_nacimiento">Fecha de Nacimiento:</label>
          <input type="date" id="edit-fecha_nacimiento" :value="formatDate(form.fecha_nacimiento)" @input="form.fecha_nacimiento = $event.target.value">
        </div>

        <!-- Fila 4: Dirección -->
        <div class="form-group full-width">
          <label for="edit-direccion">Dirección:</label>
          <input type="text" id="edit-direccion" v-model="form.direccion">
        </div>

        <!-- Fila 5: CP, Población y País -->
        <div class="form-group">
          <label for="edit-cp">Código Postal:</label>
          <input type="text" id="edit-cp" v-model="form.cp" pattern="\d{5}" title="El código postal debe tener 5 dígitos.">
        </div>
        <div class="form-group">
          <label for="edit-poblacion">Población:</label>
          <input type="text" id="edit-poblacion" v-model="form.poblacion">
        </div>
        <div class="form-group">
          <label for="edit-pais">País:</label>
          <input type="text" id="edit-pais" v-model="form.pais">
        </div>

        <!-- Fila 6: Género -->
        <div class="form-group">
          <label for="edit-genero">Género:</label>
          <select id="edit-genero" v-model="form.genero">
            <option value="Masculino">Masculino</option>
            <option value="Femenino">Femenino</option>
            <option value="Otro">Otro</option>
            <option value="No especificado">No especificado</option>
          </select>
        </div>

        <!-- Fila 7: Observaciones -->
        <div class="form-group full-width">
          <label for="edit-observaciones">Observaciones:</label>
          <textarea id="edit-observaciones" v-model="form.observaciones"></textarea>
        </div>

        <div class="modal-actions full-width">
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
  persona: { type: Object, required: true }
})
const emit = defineEmits(['close', 'update'])

const form = ref({})

const formatDate = (dateString) => {
  if (!dateString) return ''
  // Asegurarse de que la fecha se interpreta correctamente sin problemas de zona horaria
  const date = new Date(dateString)
  const year = date.getUTCFullYear()
  const month = String(date.getUTCMonth() + 1).padStart(2, '0')
  const day = String(date.getUTCDate()).padStart(2, '0')
  return `${year}-${month}-${day}`
}

watch(() => props.persona, (newVal) => {
  if (newVal) {
    form.value = { ...newVal }
  }
}, { immediate: true })

const guardarCambios = () => {
  emit('update', { id: props.persona.id_persona, data: { ...form.value } })
}
</script>
