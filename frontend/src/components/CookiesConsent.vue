<template>
  <div v-if="mostrar" class="cookies-consent">
    <p>Este sitio utiliza cookies para mejorar la experiencia del usuario. Al continuar navegando, aceptas su uso.</p>
    <button @click="aceptarCookies">Aceptar</button>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const mostrar = ref(!localStorage.getItem('cookiesAceptadas'));

const aceptarCookies = () => {
  localStorage.setItem('cookiesAceptadas', 'true');
  mostrar.value = false;
};
</script>

<style scoped>
.cookies-consent {
  position: fixed;
  bottom: 0;
  width: 100%;
  background-color: var(--supershoftgreen);
  color: var(--black);
  padding: 1rem;
  text-align: center;
  box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
}

.cookies-consent p {
  margin-bottom: 0.5rem;
}

.cookies-consent button {
  background-color: var(--shoftgreen);
  color: var(--black);
  border: none;
  border-radius: 4px;
  padding: 0.5rem 1rem;
  cursor: pointer;
}
</style>
