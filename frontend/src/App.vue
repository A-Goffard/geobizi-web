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

* {
margin: 0;
padding: 0;
text-decoration: none;
list-style: none;
font-family: Avenir, Helvetica, Arial, sans-serif;
text-decoration: none;
box-sizing: border-box;
/* background-color: white; */
}
:root {
  --black: #000000;
  --white: #ffffff;

  --lightgrey: #dddddd;
  --darkgrey: #333333;

  --megashoftgreen: #efffec;
  --supershoftgreen: #d2f8cd;
  --shoftgreen: #9bee9f;
  --lightgreen: #26B12C;
  --green: #498536;
  --darkgreen: #2c770f;

}

html, body {
  height: 100%;
  margin: 0;
  display: flex;
  flex-direction: column;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* Asegura que el contenedor ocupe toda la altura de la ventana */
}

main {
  flex: 1; /* Permite que el contenido principal ocupe el espacio restante */
}

footer {
  margin-top: auto; /* Empuja el footer hacia la parte inferior */
}

h1 {
  color: var(--darkgreen);
  margin: 1rem;
}
h2,
h3 {
  color: var(--lightgreen);
  margin: 1rem;
}
p {
  margin: 1rem;
}
ul{
    margin: 1rem;
}
.margen {
margin: 2rem;
}

.contenedor-principal {
  padding-top: 7rem;
  background-color: white;
  padding-bottom: 2rem;
}

.img {
  border-radius: 0.5rem;
  width: 100%;/* Ensure the image maintains its aspect ratio */
}

.horizontal { 
  margin: 1rem;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  gap: 1rem;
}

.card-servicios {
  flex: 1; /* Ensure all cards take an equal amount of space */
  display: flex;
  flex-direction: column; /* Stack the image and list vertically */
  align-items: center; /* Center align contents */
}

.imagen-servicios {
  width: 100%;
  display: flex;
  justify-content: center; /* Center the image horizontally */
}

.lista-servicios {
  padding: 1rem;
}
.imagen-trio{
  display: flex;
  gap: 1rem;
}

.imagen-trio div {
  flex: 1; /* Distribuye el espacio de manera equitativa */
}

@media (min-width: 950px) {
  .contenedor-principal {
    max-width: 950px;
    margin: 0 auto; /* Centra el contenido */
  }
}

@media (max-width: 750px) {
  .imagen-trio{
  display: flex;
  flex-direction: column;
  gap: 1rem;

  }

  .horizontal { 
  margin: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  gap: 1rem;
}

}


</style>
