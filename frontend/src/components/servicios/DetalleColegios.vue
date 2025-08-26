<template>
  <div class="contenedor-principal">
    <h1>Para colegios y centros de enseñanza</h1>
    <p>
      Rutas geológicas, medioambientales, talleres, actividades mixtas,
      proyectos medioambientales para colegios...
    </p>

    <h2>Actividades medioambientales</h2>
    <p>
      Aquí tenemos algunas de las actividades que tenemos disponibles para
      colegios. ¿Quieres que tus alumnos disfruten y aprendan sobre el mundo que
      les rodea? ¿Una actividad original y diferente?
    </p>
    <p>
      Adaptamos las actividades a las edades de los alumnos y al currículo
      escolar. Primaria, secundaria, bachillerato, ciclos formativos y
      universidades. Podemos realizar las actividades en euskera y/o castellano.
      Si tienes algún interés especial, diseñamos una actividad a tu medida.
    </p>

    <div class="horizontal">

      <div class="card-servicios">
        <div class="imagen-servicios">
          <img class="img" src="/imagenes/servicios/detalle/talleres.avif" alt="Talleres medioambientales para colegios" title="Talleres medioambientales para colegios" loading="lazy"/>
        </div>
        <div class="lista-servicios">
          <h3>Talleres</h3>
          <ul>
            <li>Talleres científicos</li>
            <li>Reciclaje</li>
            <li>Plantas medicinales</li>
            <li>Herbario</li>
            <li>Huertos</li>
            <li>Bombas de semillas</li>
            <li>Biorregeneración</li>
          </ul>
        </div>
      </div>


      <div class="card-servicios">
        <div class="imagen-servicios">
          <img class="img" src="/imagenes/servicios/detalle/rutas.avif" alt="Rutas guiadas educativas para colegios (Flysch, árboles, Azkorri)" title="Rutas guiadas educativas para colegios" loading="lazy"/>
        </div>
        <div class="lista-servicios">
          <h3>Rutas guiadas</h3>
        <ul>
          <li>Ruta geológica por el Flysch de Sopela</li>
          <li>Ruta geomedioambiental por el Flysch de Getxo</li>
          <li>Identificación de árboles</li>
          <li>Ruta medioambiental en Azkorri</li>
          <li>Ruta por el Arboretum de la UPV-EHU</li>
          <li>En busca de plantas medicinales</li>
        </ul>
        </div>
      </div>

      <div class="card-servicios">
        <div class="imagen-servicios">
          <img class="img" src="/imagenes/servicios/detalle/experiencias.avif" alt="Experiencias educativas y de inmersión en la naturaleza para centros educativos" title="Experiencias educativas en la naturaleza" loading="lazy"/>
        </div>
        <div class="lista-servicios">
          <h3>Experiencias</h3>
        <ul>
          <li>Inmersiones en la naturaleza</li>
          <li>Actividades mixtas</li>
          <li>Limpieza de entornos naturales</li>
          <li>Actividades experimentales</li>
        </ul>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head' // añadido

const pageUrl = 'https://www.geobizi.com/detalle-colegios'
const ogImage = 'https://www.geobizi.com/imagenes/servicios/detalle/talleres.avif'

useHead({
  title: 'Servicios para colegios y centros de enseñanza | GeoBizi',
  meta: [
    { name: 'description', content: 'Actividades educativas para colegios: rutas geológicas, talleres prácticos y proyectos medioambientales adaptados al currículo y a distintas edades.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'GeoBizi' },
    { name: 'keywords', content: 'actividades colegios, talleres educativos, rutas escolares, GeoBizi, educación ambiental' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Servicios para colegios y centros de enseñanza | GeoBizi' },
    { property: 'og:description', content: 'Rutas, talleres y proyectos medioambientales para colegios. Actividades adaptadas por edad y currículo.' },
    { property: 'og:type', content: 'website' },
    { property: 'og:url', content: pageUrl },
    { property: 'og:image', content: ogImage },
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:image', content: ogImage }
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
        "name": "Servicios para colegios y centros de enseñanza | GeoBizi",
        "description": "Rutas, talleres y proyectos medioambientales para colegios. Actividades adaptadas por edad y currículo.",
        "inLanguage": "es",
        "image": ogImage
      })
    }
  ]
})
</script>

<style scoped></style>
