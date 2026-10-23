<template>
  <div class="participante-card">
    <div class="participante-header">
      <h4 class="participante-titulo">Asistente {{ index + 1 }}</h4>
      <button 
        v-if="canRemove" 
        type="button" 
        @click="$emit('remove')" 
        class="btn-quitar"
        title="Quitar asistente"
      >
        ✕ Quitar
      </button>
    </div>

    <div class="participante-grid">
      <div class="form-subgroup">
        <label :for="'p-nombre-' + index">Nombre:</label>
        <input 
          type="text" 
          :id="'p-nombre-' + index" 
          :value="modelValue.nombre" 
          @input="actualizarCampo('nombre', $event.target.value)"
          required 
          placeholder="Nombre" 
        />
      </div>

      <div class="form-subgroup">
        <label :for="'p-apellidos-' + index">Apellidos:</label>
        <input 
          type="text" 
          :id="'p-apellidos-' + index" 
          :value="modelValue.apellidos" 
          @input="actualizarCampo('apellidos', $event.target.value)"
          required 
          placeholder="Apellidos" 
        />
      </div>

      <div class="form-subgroup grupo-edad">
        <label :for="'p-edad-' + index">Edad:</label>
        <input 
          type="number" 
          :id="'p-edad-' + index" 
          :value="modelValue.edad" 
          @input="actualizarCampo('edad', $event.target.value === '' ? '' : Number($event.target.value))"
          min="0" 
          max="120" 
          required 
          placeholder="Ej: 8" 
        />
      </div>
    </div>
  </div>
</template>

<script setup>
/* eslint-disable */
const props = defineProps({
  modelValue: {
    type: Object,
    required: true
  },
  index: {
    type: Number,
    required: true
  },
  canRemove: {
    type: Boolean,
    default: true
  }
});

const emit = defineEmits(['update:modelValue', 'remove']);

const actualizarCampo = (campo, valor) => {
  emit('update:modelValue', {
    ...props.modelValue,
    [campo]: valor
  });
};
</script>

<style scoped>
.participante-card {
  background: var(--white);
  border: 1px solid var(--supershoftgreen);
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 0.85rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}

.participante-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
  padding-bottom: 0.4rem;
  border-bottom: 1px dashed var(--supershoftgreen);
}

.participante-titulo {
  margin: 0;
  font-size: 0.95rem;
  color: var(--darkgreen);
  font-weight: 700;
}

.btn-quitar {
  background: transparent;
  border: 1px solid var(--lightbrownred);
  color: var(--brownred);
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  font-size: 0.8rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-quitar:hover {
  background: var(--supershoftbrownred);
  border-color: var(--brownred);
}

.participante-grid {
  display: grid;
  grid-template-columns: 1.2fr 1.5fr 0.8fr;
  gap: 0.75rem;
}

@media (max-width: 600px) {
  .participante-grid {
    grid-template-columns: 1fr;
    gap: 0.5rem;
  }
}

.form-subgroup {
  display: flex;
  flex-direction: column;
}

.form-subgroup label {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--darkgrey);
  margin-bottom: 0.25rem;
}

.form-subgroup input {
  padding: 0.5rem;
  border: 1px solid var(--lightgrey);
  border-radius: 4px;
  font-size: 0.9rem;
  color: var(--darkgrey);
}

.form-subgroup input:focus {
  outline: none;
  border-color: var(--green);
}
</style>