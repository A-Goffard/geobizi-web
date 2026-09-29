<template>
  <div id="app">
    <header>
      <Nav />
    </header>
    <main>
      <router-view></router-view>
    </main>
    <footer>
      <Footer />
      <CookiesConsent />
    </footer>
  </div>
</template>
<script setup>
import Nav from './components/NavBar.vue';
import Footer from './components/FooterComponent.vue';
import CookiesConsent from './components/CookiesConsent.vue';

</script>

<style>
/* ==========================================================================
   1. RESET Y CONFIGURACIÓN GENERAL
   ========================================================================== */
* {
  margin: 0;
  padding: 0;
  text-decoration: none;
  list-style: none;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-decoration: none;
  box-sizing: border-box;
}
:root {
  /* Escala monocromática */
  --black: #000000;
  --white: #ffffff;
  --lightgrey: #dddddd;
  --darkgrey: #333333;
  --grey: #666666;

  /* Alertas, avisos y lista de espera */
  --yellow: #fff3cd;
  --darkyellow: #7a5200;           /* Texto oscuro legible sobre amarillos */
  --orange: #ffc107;              /* Bordes de aviso */
  --amber: #d97706;               /* Botón lista de espera */
  --darkamber: #b45309;           /* Hover botón lista de espera */
  --brownred: #b85d46;            /* Cancelaciones y destructivos */
  --lightbrownred: #f8c3b7;
  --supershoftbrownred: #fff0ec;

  /* Paleta corporativa verde Geobizi */
  --megashoftgreen: #efffec;
  --supershoftgreen: #d2f8cd;
  --shoftgreen: #9bee9f;
  --lightgreen: #26b12c;
  --green: #50963b;
  --darkgreen: #2c770f;

  /* Colores temáticos y proyectos */
  --lightblue: #7ed4e9;
  --blue: #418ed6;
  --purple: #8b5cf6;
  --plum: #c084fc;
}

/* ==========================================================================
   2. ESTRUCTURA BASE Y LAYOUT GLOBAL
   ========================================================================== */
html,
body {
  height: 100%;
  margin: 0;
  display: flex;
  flex-direction: column;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  flex: 1;
}

footer {
  margin-top: auto;
}

.contenedor-principal {
  padding-top: 7rem;
  background-color: var(--white);
  padding-bottom: 2rem;
}

/* ==========================================================================
   3. TIPOGRAFÍA Y ENLACES
   ========================================================================== */
h1 {
  color: var(--darkgreen);
  margin: 1rem;
}

h2 {
  color: var(--green);
  margin: 1rem;
}

h3 {
  color: var(--lightgreen);
  margin: 1rem;
}

h4 {
  color: var(--green);
  margin: 1rem;
}

p {
  margin: 1rem;
  line-height: 1.6;
  color: var(--darkgrey);
  margin-bottom: 0.8rem;
}

ul {
  margin: 1rem;
  list-style: disc;
}

li {
  margin: 0.5rem 0;
  margin-left: 1rem;
  color: var(--darkgrey);
}

a {
  font-weight: bold;
  font-style: oblique;
  color: var(--lightgreen);
  text-decoration: none;
  transition: color 0.3s ease;
}

a:hover {
  color: var(--shoftgreen);
}

/* ==========================================================================
   4. CLASES DE UTILIDAD Y COMPONENTES COMPARTIDOS
   ========================================================================== */
.margen {
  margin: 2rem;
}

.mleft {
  margin-left: 1rem;
}

.img {
  border-radius: 0.5rem;
  width: 100%;
}

.horizontal {
  margin: 1rem;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  gap: 1rem;
}

.card-servicios {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.imagen-servicios {
  width: 100%;
  display: flex;
  justify-content: center;
}

.lista-servicios {
  padding: 1rem;
}

.imagen-trio {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.imagen-trio div {
  flex: 1;
}

/* Badges globales (para fichas y cabeceras) */
.badge,
.badge-large {
  display: inline-block;
  color: var(--white);
  font-weight: bold;
  text-align: center;
}

.badge {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.badge-large {
  padding: 5px 15px;
  border-radius: 15px;
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}

.badge.flysch, .badge-large.flysch { background-color: var(--amber); }
.badge.naturgaua, .badge-large.naturgaua { background-color: var(--purple); }
.badge.zalla, .badge-large.zalla { background-color: var(--blue); }
.badge.eventos, .badge-large.eventos { background-color: var(--plum); }
.badge.general, .badge-large.general { background-color: var(--green); }

/* ==========================================================================
   5. SISTEMA GLOBAL DE BOTONES
   ========================================================================== */
.acciones-botones {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* Botón principal / guardar / confirmar */
.btn-guardar,
.btn-submit {
  background-color: var(--green);
  color: var(--white);
  border: none;
  border-radius: 4px;
  padding: 0.85rem 1.6rem;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.btn-guardar:hover:not(:disabled),
.btn-submit:hover:not(:disabled) {
  background-color: var(--darkgreen);
  transform: translateY(-2px);
}

.btn-guardar:disabled,
.btn-submit:disabled {
  background-color: var(--lightgrey);
  cursor: not-allowed;
}

/* Botón lista de espera */
.btn-espera {
  background-color: var(--amber) !important;
  color: var(--white) !important;
}

.btn-espera:hover:not(:disabled) {
  background-color: var(--darkamber) !important;
}

/* Botón de acción genérica positiva */
.btn-accion {
  display: inline-block;
  background-color: var(--green);
  color: var(--white);
  border: none;
  border-radius: 4px;
  padding: 0.75rem 1.5rem;
  font-size: 0.95rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  text-decoration: none;
}

.btn-accion:hover {
  background-color: var(--darkgreen);
  transform: translateY(-2px);
  color: var(--white);
}

/* Botones secundarios */
.btn-secundario,
.btn-cancelar {
  background-color: var(--lightgrey);
  color: var(--darkgrey);
  border: none;
  border-radius: 4px;
  padding: 0.75rem 1.4rem;
  font-size: 0.95rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.2s ease, transform 0.2s ease;
}

.btn-secundario:hover,
.btn-cancelar:hover {
  background-color: #cacaca;
  transform: translateY(-2px);
}

/* Botones de alerta y destructivos */
.btn-alerta {
  background-color: var(--brownred);
  color: var(--white);
  border: none;
  border-radius: 4px;
  padding: 0.75rem 1.4rem;
  font-size: 0.95rem;
  font-weight: bold;
  cursor: pointer;
  transition: opacity 0.3s ease, transform 0.2s ease;
}

.btn-alerta:hover {
  opacity: 0.9;
  transform: translateY(-2px);
}

.btn-destructivo {
  background-color: var(--brownred);
  color: var(--white);
  border: none;
  border-radius: 4px;
  padding: 0.75rem 1.4rem;
  font-size: 0.95rem;
  font-weight: bold;
  cursor: pointer;
  transition: opacity 0.3s ease;
}

.btn-destructivo:hover {
  opacity: 0.9;
}

.volver-btn {
  background: none;
  border: none;
  color: var(--grey);
  text-decoration: underline;
  cursor: pointer;
  margin-top: 1.5rem;
  font-size: 0.9rem;
}

.btn-servicio {
  display: inline-block;
  padding: 0.5rem 1rem;
  background-color: var(--shoftgreen);
  color: var(--black);
  border-radius: 4px;
  text-decoration: none;
  font-weight: bold;
  font-size: 0.9rem;
  transition: background-color 0.3s;
}

.btn-servicio:hover {
  background-color: var(--green);
  color: var(--white);
}

/* ==========================================================================
   6. MENSAJES Y CAJAS DE ESTADO
   ========================================================================== */
.estado-caja {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  text-align: center;
  padding: 2rem 0;
}

.mensaje-estado {
  font-weight: bold;
  font-size: 1.05rem;
  line-height: 1.5;
  margin: 0;
}

.mensaje-exito {
  color: var(--darkgreen);
  font-weight: bold;
  margin-top: 1rem;
}

.mensaje-error {
  color: var(--brownred);
  font-weight: bold;
  margin-top: 1rem;
}

/* ==========================================================================
   7. SISTEMA GLOBAL DE MODALES
   ========================================================================== */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 1rem;
}

.modal-tarjeta {
  background-color: var(--white);
  border-radius: 0.5rem;
  max-width: 480px;
  width: 100%;
  padding: 2rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
  text-align: center;
  animation: fadeIn 0.2s ease-out;
}

.modal-icono {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.modal-titulo {
  color: var(--brownred);
  margin: 0 0 1rem 0;
  font-size: 1.3rem;
}

.modal-titulo-exito {
  color: var(--darkgreen);
  margin: 0 0 1rem 0;
  font-size: 1.3rem;
}

.modal-alerta-box {
  background-color: var(--yellow);
  border-left: 4px solid var(--orange);
  padding: 0.85rem 1rem;
  border-radius: 4px;
  margin-bottom: 1.5rem;
  text-align: left;
}

.modal-alerta-texto {
  color: var(--darkyellow);
  margin: 0 0 0.4rem 0;
  font-size: 0.95rem;
}

.modal-subtexto {
  color: var(--darkgrey);
  font-size: 0.9rem;
  line-height: 1.5;
  margin: 0 0 1.5rem 0;
}

.modal-acciones {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* ==========================================================================
   8. MEDIA QUERIES / RESPONSIVE
   ========================================================================== */
@media (min-width: 950px) {
  .contenedor-principal {
    max-width: 950px;
    margin: 0 auto;
  }
}

@media (max-width: 750px) {
  .imagen-trio {
    flex-direction: column;
    gap: 1rem;
  }

  .horizontal {
    flex-direction: column;
    gap: 1rem;
  }
}

@media (max-width: 600px) {
  .acciones-botones,
  .modal-acciones {
    flex-direction: column;
    width: 100%;
  }

  .btn-guardar,
  .btn-submit,
  .btn-secundario,
  .btn-cancelar,
  .btn-alerta,
  .btn-destructivo,
  .btn-accion,
  .btn-espera {
    width: 100%;
  }
}
</style>