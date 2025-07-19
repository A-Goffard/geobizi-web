<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <h2>Editar Reserva</h2>
      <form @submit.prevent="guardarCambios">
        <div class="form-group">
          <label for="edit-personas">Número de Personas:</label>
          <input type="number" id="edit-personas" v-model.number="form.numero_personas" required>
        </div>
        <div class="form-group checkbox-group">
          <input type="checkbox" id="edit-aprobada" v-model="form.aprobada">
          <label for="edit-aprobada">Aprobada</label>
        </div>
        <div class="form-group checkbox-group">
          <input type="checkbox" id="edit-confirmacion" v-model="form.confirmacion_enviada">
          <label for="edit-confirmacion">Confirmación Enviada</label>
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
  reserva: { type: Object, required: true }
})
const emit = defineEmits(['close', 'update'])

const form = ref({})

watch(() => props.reserva, (newVal) => {
  if (newVal) {
    form.value = { ...newVal }
  }
}, { immediate: true })

const guardarCambios = () => {
  emit('update', { id: props.reserva.id_reserva, data: form.value })
}
</script>


