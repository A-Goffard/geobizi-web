<template>
  <div class="contenedor-principal">
    <h1>Recursos y descargas</h1>
    <p>Aquí encontrarás una selección de materiales educativos y recursos para descargar.</p>
    <p>Si los usas y crees que están bien y merecen la pena, acuérdate de nosotros.</p>
    <p>También podemos personalizar y diseñar materiales didácticos a medida.</p>

    <h2>Material disponible</h2>

    <h4>Próximamente</h4>

    <h2>Se realizan para</h2>
    <p>Podemos diseñar materiales a medida según las necesidades de cada cliente.</p>
    <p>Pueden ser en formatos diferentes como láminas, folletos o recursos digitales interactivos por ejemplo.</p>
    <p>Los materiales están pensados para colegios, asociaciones, entidades locales y público general.</p>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'
const pageUrl = 'https://www.geobizi.com/servicios/descargas'
useHead({
  title: 'Recursos y descargas | GeoBizi',
  meta: [{ name: 'description', content: 'Fichas didácticas, guías de campo y materiales descargables para apoyar rutas, talleres y proyectos educativos.' }],
  link: [{ rel: 'canonical', href: pageUrl }]
})
</script>

<style scoped></style>