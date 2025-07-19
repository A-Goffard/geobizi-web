<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <h2>Editar Persona</h2>
      <form @submit.prevent="guardarCambios">
        <div class="form-group">
          <label for="edit-nombre">Nombre:</label>
          <input type="text" id="edit-nombre" v-model="form.nombre" required>
        </div>
        <div class="form-group">
          <label for="edit-apellido">Apellido:</label>
          <input type="text" id="edit-apellido" v-model="form.apellido">
        </div>
        <div class="form-group">
          <label for="edit-email">Email:</label>
          <input type="email" id="edit-email" v-model="form.email" required>
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
  persona: { type: Object, required: true }
})
const emit = defineEmits(['close', 'update'])

const form = ref({})

watch(() => props.persona, (newVal) => {
  if (newVal) {
    form.value = { ...newVal }
  }
}, { immediate: true })

const guardarCambios = () => {
  emit('update', { id: props.persona.id_persona, data: form.value })
}
</script>


