<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <h2>Editar Empresa</h2>
      <form @submit.prevent="guardarCambios" class="form-grid">
        <div class="form-group">
          <label for="edit-nombre">Nombre:</label>
          <input type="text" id="edit-nombre" v-model="form.nombre" required>
        </div>
        <div class="form-group">
          <label for="edit-nif">NIF:</label>
          <input type="text" id="edit-nif" v-model="form.nif">
        </div>
        <div class="form-group full-width">
          <label for="edit-razon_social">Razón Social:</label>
          <input type="text" id="edit-razon_social" v-model="form.razon_social" required>
        </div>
        <div class="form-group full-width">
          <label for="edit-direccion">Dirección:</label>
          <input type="text" id="edit-direccion" v-model="form.direccion" required>
        </div>
        <div class="form-group">
          <label for="edit-provincia">Provincia:</label>
          <input type="text" id="edit-provincia" v-model="form.provincia" required>
        </div>
        <div class="form-group">
          <label for="edit-cp">Código Postal:</label>
          <input type="text" id="edit-cp" v-model="form.cp" required>
        </div>
        <div class="form-group">
          <label for="edit-sector">Sector:</label>
          <input type="text" id="edit-sector" v-model="form.sector">
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
  empresa: { type: Object, required: true }
})
const emit = defineEmits(['close', 'update'])

const form = ref({})

watch(() => props.empresa, (newVal) => {
  if (newVal) {
    form.value = { ...newVal }
  }
}, { immediate: true })

const guardarCambios = () => {
  emit('update', { id: props.empresa.id_empresa, data: form.value })
}
</script>

