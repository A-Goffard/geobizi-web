<template>
  <div class="contenedor-principal">
    <h1>Para asociaciones y empresas</h1>
    <p>
      Diseñamos y realizamos actividades medioambientales y geológicas a medida para asociaciones y empresas.
      ¿Quieres fortalecer el trabajo en equipo, mejorar la sostenibilidad de tu empresa o simplemente disfrutar de experiencias únicas en la naturaleza?
    </p>

    <h2>Actividades para asociaciones y empresas</h2>
    <p>
      Aquí tienes algunas de las actividades que ofrecemos. Todas nuestras actividades pueden realizarse en euskera y/o castellano.
      Si tienes algún interés especial, diseñamos una actividad a tu medida.
    </p>

    <div class="horizontal">

      <div class="card-servicios">
        <div class="imagen-servicios">
          <img class="img" src="/imagenes/servicios/detalle/actividades.avif" alt="Talleres medioambientales para empresas" title="Talleres medioambientales para empresas" loading="lazy"/>
        </div>
        <div class="lista-servicios">
          <h3>Talleres</h3>
          <ul>
            <li>Talleres científicos</li>
            <li>Reciclaje</li>
            <li>Plantas medicinales</li>
            <li>Aromaterapia</li>
            <li>Arteterapia</li>
          </ul>
        </div>
      </div>

      <div class="card-servicios">
        <div class="imagen-servicios">
          <img class="img" src="/imagenes/servicios/detalle/rutas2.avif" alt="Rutas guiadas para empresas — Flysch y geología" title="Rutas guiadas para empresas — Flysch y geología" loading="lazy"/>
        </div>
        <div class="lista-servicios">
          <h3>Rutas guiadas</h3>
          <ul>
            <li>Ruta geológica por el Flysch de Sopela</li>
            <li>Ruta geomedioambiental por el Flysch de Getxo</li>
            <li>Identificación de árboles</li>
          </ul>
        </div>
      </div>

      <div class="card-servicios">
        <div class="imagen-servicios">
          <img class="img" src="/imagenes/servicios/detalle/experiencias2.avif" alt="Experiencias y team building en la naturaleza" title="Team building y experiencias en la naturaleza" loading="lazy"/>
        </div>
        <div class="lista-servicios">
          <h3>Experiencias</h3>
          <ul>
            <li>Team Building</li>
            <li>Ruta en barco por el Flysch de Bizkaia</li>
            <li>Inmersiones en la naturaleza</li>
            <li>Actividades mixtas</li>
            <li>Limpieza de entornos naturales</li>
          </ul>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head' // añadido

const pageUrl = 'https://www.geobizi.com/detalle-asociaciones'
const ogImage = 'https://www.geobizi.com/imagenes/servicios/detalle/actividades.avif'

useHead({
  title: 'Servicios para Asociaciones y Empresas | GeoBizi',
  meta: [
    { name: 'description', content: 'Actividades y talleres a medida para asociaciones y empresas: team building, rutas geológicas y experiencias medioambientales con enfoque didáctico.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'GeoBizi' },
    { name: 'keywords', content: 'servicios empresas, team building, talleres medioambientales, rutas guiadas, GeoBizi' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Servicios para Asociaciones y Empresas | GeoBizi' },
    { property: 'og:description', content: 'Team building, talleres y rutas educativas para asociaciones y empresas. Actividades personalizadas y sostenibles.' },
    { property: 'og:type', content: 'website' },
    { property: 'og:url', content: pageUrl },
    { property: 'og:image', content: ogImage },
    { name: 'twitter:card', content: 'summary_large_image' }
  ],
  link: [
    { rel: 'canonical', href: pageUrl },
    { rel: 'image_src', href: ogImage }
  ],
  script: [
    {
      type: 'application/ld+json',
      children: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "WebPage",
        "url": pageUrl,
        "name": "Servicios para Asociaciones y Empresas | GeoBizi",
        "description": "Team building, talleres y rutas educativas para asociaciones y empresas. Actividades personalizadas y sostenibles.",
        "inLanguage": "es",
        "image": ogImage
      })
    }
  ]
})
</script>

<style scoped></style>