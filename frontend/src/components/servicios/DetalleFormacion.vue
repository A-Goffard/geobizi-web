<template>
  <div class="contenedor-principal">
    <h1>Formación y asesoramiento</h1>
    <p>Ofrecemos formaciones y asesoramiento en diversas áreas relacionadas con el medio ambiente, la sostenibilidad y otros ámbitos transversales.</p>
    <p>Tanto para empresas como para instituciones, adaptamos nuestros programas a las necesidades específicas de cada cliente.</p>
    <p>También ofrecemos formaciones para centros formativos.</p>

    <h2>Áreas de formación</h2>

    <p>Sensibilización medioambiental y participación ciudadana.</p>
    <p>Sostenibilidad.</p>
    <p>Comunicación efectiva.</p>
    <p>Divulgación.</p>
    <p>Diseño de actividades.</p>
    <p>Ecoturismo.</p>
    <p>Técnicas de ocio y tiempo libre.</p>
    <p>Gestión de equipos.</p>
    <p>Diseño de espacios verdes.</p>
    <p>Regeneración y seguimiento de proyectos.</p>
    <p>Formación para docentes y monitores.</p>
    <p>Técnicas de educación ambiental.</p>
    <p>Metodologías activas de enseñanza.</p>
    <p>Proyectos educativos.</p>
    <p>Uso de la IA en la educación.</p>
    <p>Herramientas digitales en la educación.</p>
    <p>Gamificación.</p>
    <p>Otras áreas relacionadas con el medio ambiente, la sostenibilidad y la educación.</p>

    <h2>Se realizan para</h2>
    <p>Ofrecemos formación para administraciones, colegios, asociaciones, empresas y centros de formación.</p>
        <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/servicios/formacion/formacion1.avif"
          alt="Ruta Flysch en Sopela — personas observando formaciones geológicas"
          title="Ruta Flysch en Sopela — imagen 1"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/servicios/formacion/formacion2.avif"
          alt="Personas identificando anfibios en un entorno natural"
          title="Ruta medioambiental en Azkorri — imagen 2"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/servicios/formacion/formacion3.avif"
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
const pageUrl = 'https://www.geobizi.com/servicios/formacion'
useHead({
  title: 'Formación | GeoBizi',
  meta: [{ name: 'description', content: 'Formación en sensibilización ambiental, regeneración, gestión de espacios y formación para docentes y técnicos.' }],
  link: [{ rel: 'canonical', href: pageUrl }]
})
</script>

<style scoped></style>