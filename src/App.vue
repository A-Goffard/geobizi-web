<template>
  <div>
    <Nav />
    <router-view></router-view>
    <Footer />
  </div>
</template>
<script setup>
import Nav from './components/NavBar.vue';
import Footer from './components/FooterComponent.vue';

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
background-color: white;
}
:root {
  --black: #000000;
  --white: #ffffff;

  --lightgrey: #dddddd;
  --darkgrey: #333333;

  --lightgreen: #26B12C;
  --green: #498536;
  --darkgreen: #2c770f;

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
.margen {
margin: 2rem;
}

.contenedor-principal {
  padding-top: 7rem;
  background-color: rgb(255, 255, 255);
  padding-bottom: 2rem;
}


@media (min-width: 950px) {
  .contenedor-principal {
    max-width: 950px;
    margin: 0 auto; /* Centra el contenido */
  }
}
</style>
