<template>
  <div class="contenedor-principal">
    <h1>Proyectos digitales y sostenibilidad</h1>
    <p>Diseñamos y desarrollamos proyectos digitales orientados al medio ambiente: yincanas digitales, rutas interactivas, juegos educativos y recursos online combinados con acciones de sostenibilidad práctica.</p>
    <p>Todos los proyectos digitales tienen la huella de carbono compensada.</p>
    <p>Yincanas y rutas interactivas para espacios naturales (móvil + pruebas).</p>
    <p>Recursos digitales para docentes: fichas, guías y actividades descargables.</p>
    <p>Páginas web con compensación de carbono.</p>

    <h2>Ejemplos</h2>

    <p><a href="https://www.geobizi.com/detalle-flysch">Flysch Digital</a></p>
    <p>Nuestra página web</p>

    <h2>Se realizan para</h2>
    <p>Estos proyectos son transversales: se diseñan para colegios, asociaciones, empresas y administraciones, ajustando contenidos, idiomas y accesibilidad.</p>
      <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/servicios/digital/digital1.avif"
          alt="Ruta Flysch en Sopela — personas observando formaciones geológicas"
          title="Ruta Flysch en Sopela — imagen 1"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/servicios/digital/digital2.avif"
          alt="Personas identificando anfibios en un entorno natural"
          title="Ruta medioambiental en Azkorri — imagen 2"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/servicios/digital/digital3.avif"
          alt="Ruta escolar por Azkorri"
          title="Ruta escolar por Azkorri — imagen 3"
          loading="lazy"
        />
      </div>
    </div>
  
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'
const pageUrl = 'https://www.geobizi.com/servicios/digital-sostenible'
useHead({
  title: 'Proyectos digitales y sostenibilidad | Geobizi',
  meta: [{ name: 'description', content: 'Yincanas digitales, rutas interactivas y recursos digitales para educación ambiental y campañas sostenibles.' }],
  link: [{ rel: 'canonical', href: pageUrl }]
})
</script>

<style scoped></style>