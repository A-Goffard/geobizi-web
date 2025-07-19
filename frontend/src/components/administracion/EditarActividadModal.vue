<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <h2>Editar Actividad</h2>
      <form @submit.prevent="guardarCambios" class="form-grid">
        <!-- Fila 1 -->
        <div class="form-group">
          <label for="edit-nombre">Nombre:</label>
          <input type="text" id="edit-nombre" v-model="form.nombre" required>
        </div>
        <div class="form-group">
          <label for="edit-tipo">Tipo:</label>
          <input type="text" id="edit-tipo" v-model="form.tipo">
        </div>
        <!-- Fila 2 -->
        <div class="form-group">
          <label for="edit-lugar">Lugar:</label>
          <input type="text" id="edit-lugar" v-model="form.lugar">
        </div>
        <div class="form-group">
          <label for="edit-responsable">Responsable:</label>
          <input type="text" id="edit-responsable" v-model="form.responsable">
        </div>
        <!-- Fila 3 -->
        <div class="form-group">
          <label for="edit-fecha">Fecha:</label>
          <input type="date" id="edit-fecha" :value="formatDate(form.fecha)" @input="form.fecha = $event.target.value">
        </div>
        <div class="form-group">
          <label for="edit-hora">Hora:</label>
          <input type="time" id="edit-hora" v-model="form.hora">
        </div>
        <!-- Fila 4 -->
        <div class="form-group">
          <label for="edit-estado">Estado:</label>
          <select id="edit-estado" v-model="form.estado">
            <option value="pendiente">Pendiente</option>
            <option value="confirmada">Confirmada</option>
            <option value="realizada">Realizada</option>
            <option value="cancelada">Cancelada</option>
          </select>
        </div>
        <div class="form-group">
          <label for="edit-categoria">Categoría:</label>
          <select id="edit-categoria" v-model="form.categoria">
            <option value="digital">Digital</option>
            <option value="bioregeneracion">Proyecto de Bioregeneración</option>
            <option value="educativa">Educativa</option>
            <option value="turistica">Turística</option>
          </select>
        </div>
        <!-- Fila 5 -->
        <div class="form-group full-width">
          <label for="edit-descripcion">Descripción:</label>
          <textarea id="edit-descripcion" v-model="form.descripcion"></textarea>
        </div>
        <!-- Fila 6 -->
        <div class="form-group">
          <label for="edit-precio">Precio por persona (€):</label>
          <input type="number" step="0.01" id="edit-precio" v-model.number="form.precio">
        </div>
        <div class="form-group">
          <label for="edit-coste_economico">Coste total (€):</label>
          <input type="number" step="0.01" id="edit-coste_economico" v-model.number="form.coste_economico">
        </div>
        <div class="form-group">
          <label for="edit-num_participantes">Nº Participantes:</label>
          <input type="number" id="edit-num_participantes" v-model.number="form.num_participantes">
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
  actividad: { type: Object, required: true }
})
const emit = defineEmits(['close', 'update'])

const form = ref({})

// Función para formatear la fecha para el input type="date"
const formatDate = (dateString) => {
  if (!dateString) return ''
  return new Date(dateString).toISOString().split('T')[0]
}

watch(() => props.actividad, (newVal) => {
  if (newVal) {
    form.value = { ...newVal }
  }
}, { immediate: true })

const guardarCambios = () => {
  emit('update', { id: props.actividad.id_actividad, data: form.value })
}
</script>
