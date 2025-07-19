<template>
  <div class="contenedor-principal">
    <h1>Panel de Administración</h1>
    <div class="container">
      <router-link to="/" class="admin-btn">Ir a la página principal</router-link>
      <router-link to="/admin/usuarios" class="admin-btn">Gestionar usuarios</router-link>
      <router-link to="/admin/actividades" class="admin-btn">Gestionar actividades</router-link>
      <router-link to="/admin/empresas" class="admin-btn">Gestionar empresas</router-link>
      <router-link to="/admin/reservas" class="admin-btn">Gestionar reservas</router-link>
      <router-link to="/admin/personas" class="admin-btn">Gestionar personas</router-link>
    </div>
  </div>
</template>

<script setup>
// Puedes añadir lógica de autenticación aquí si lo necesitas
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  align-items: center;
  margin: 2rem 0;
}

.admin-btn {
  min-width: 220px;
  max-width: 250px;
  padding: 0.7rem 1.2rem;
  background: var(--lightgreen);
  color: #fff;
  border-radius: 5px;
  text-decoration: none;
  transition: background 0.2s;
  font-size: 1.05rem;
  font-weight: 500;
  text-align: center;
  border: none;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
  margin: 0 auto;
  display: block;
}

.admin-btn:hover {
  background: var(--green);
}
</style>
