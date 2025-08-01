<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <h2>Editar Empresa</h2>
      <form @submit.prevent="guardarCambios" class="form-grid">
        <div class="form-group">
          <label for="edit-nombre">Nombre de la empresa:</label>
          <input type="text" id="edit-nombre" v-model="form.nombre" required minlength="2" maxlength="100">
        </div>
        <div class="form-group">
          <label for="edit-nif">NIF:</label>
          <input type="text" id="edit-nif" v-model="form.nif" @input="form.nif = $event.target.value.toUpperCase()" pattern="^([A-Z]{1}\d{7}[A-Z0-9]{1})|(\d{8}[A-Z]{1})|([XYZ]{1}\d{7}[A-Z]{1})$" title="Formato de NIF, DNI o NIE inválido.">
        </div>
        <div class="form-group full-width">
          <label for="edit-razon_social">Razón Social:</label>
          <input type="text" id="edit-razon_social" v-model="form.razon_social" required minlength="2" maxlength="100">
        </div>
        <div class="form-group full-width">
          <label for="edit-direccion">Dirección:</label>
          <input type="text" id="edit-direccion" v-model="form.direccion" required minlength="5" maxlength="150">
        </div>
        <div class="form-group">
          <label for="edit-provincia">Provincia:</label>
          <input type="text" id="edit-provincia" v-model="form.provincia" required maxlength="50">
        </div>
        <div class="form-group">
          <label for="edit-cp">Código Postal:</label>
          <input type="text" id="edit-cp" v-model="form.cp" required pattern="\d{5}" title="El código postal debe tener 5 dígitos.">
        </div>
        <div class="form-group">
          <label for="nombre_contacto">Nombre de contacto:</label>
          <input type="text" id="nombre_contacto" v-model="form.nombre_contacto">
        </div>
        <div class="form-group">
          <label for="email_contacto">Email de contacto:</label>
          <input type="email" id="email_contacto" v-model="form.email_contacto">
        </div>
        <div class="form-group">
          <label for="edit-telefono_empresa">Teléfono:</label>
          <input type="tel" id="edit-telefono_empresa" v-model="form.telefono_empresa">
        </div>
        <div class="form-group">
          <label for="edit-email_empresa">Email de empresa:</label>
          <input type="email" id="edit-email_empresa" v-model="form.email_empresa">
        </div>
        <div class="form-group">
          <label for="edit-sector">Sector:</label>
          <input type="text" id="edit-sector" v-model="form.sector" maxlength="50">
        </div>
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
  emit('update', { id: props.empresa.id_empresa, data: { ...form.value } })
}
</script>



