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
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/servicios/colegios'
const ogImage = 'https://www.geobizi.com/imagenes/servicios/colegios.avif'

useHead({
  title: 'Servicios para Colegios | GeoBizi',
  meta: [
    { name: 'description', content: 'Actividades educativas para colegios: rutas, talleres y programas adaptados al curriculum.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Servicios para Colegios | GeoBizi' },
    { property: 'og:description', content: 'Actividades educativas para colegios: rutas, talleres y programas adaptados al curriculum.' },
    { property: 'og:type', content: 'website' },
    { property: 'og:url', content: pageUrl },
    { property: 'og:image', content: ogImage }
  ],
  link: [
    { rel: 'canonical', href: pageUrl },
    { rel: 'image_src', href: ogImage },
    { rel: 'apple-touch-icon', href: '/apple-touch-icon.png', sizes: '180x180' }
  ],
  script: [
    {
      type: 'application/ld+json',
      children: JSON.stringify({
        "@context":"https://schema.org",
        "@graph":[
          {
            "@type":"Organization",
            "@id":"https://www.geobizi.com/#organization",
            "name":"GeoBizi",
            "url":"https://www.geobizi.com",
            "logo": { "@type":"ImageObject","url":"https://www.geobizi.com/imagenes/GeobiziLogo.7ae1d6ce.png","width":1417,"height":313 },
            "sameAs":[
              "https://www.facebook.com/geobizirik/",
              "https://www.instagram.com/geotxiki/",
              "https://www.youtube.com/channel/UCw-C_J0y-jKHp7Zx92lsKfg"
            ]
          },
          {
            "@type":"Service",
            "serviceType":"Actividades educativas para colegios",
            "provider": { "@type":"Organization", "@id":"https://www.geobizi.com/#organization" },
            "name":"Servicios para Colegios | GeoBizi",
            "description":"Actividades educativas para colegios: rutas, talleres y programas adaptados al curriculum.",
            "url": pageUrl,
            "areaServed": "Bizkaia, Euskadi, España",
            "inLanguage":"es",
            "image": { "@type":"ImageObject","url":ogImage,"width":1080,"height":1080 }
          }
        ]
      })
    }
  ]
})
</script>

<style scoped></style>
