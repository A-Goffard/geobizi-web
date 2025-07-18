<template>
  <div class="notfound-container">
    <h1>Página no encontrada</h1>
    <p>La ruta que has solicitado no existe en Geobizi.</p>
    <router-link to="/" class="volver-link">Volver a la página principal</router-link>
  </div>
</template>

<script setup>
// No es necesario código adicional
</script>

<style scoped>
.notfound-container {
  max-width: 500px;
  margin: 80px auto;
  padding: 2rem;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.08);
  text-align: center;
}
.notfound-container h1 {
  margin-bottom: 1rem;
}
.notfound-container p {
  color: #333;
  margin-bottom: 2rem;
}
.volver-link {
  display: inline-block;
  padding: 0.5rem 1.2rem;
  background: var(--lightgreen);
  color: #fff;
  border-radius: 5px;
  text-decoration: none;
  transition: background 0.2s;
}
.volver-link:hover {
  background: var(--green);
}
</style>
