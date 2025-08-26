<template>
  <div class="contenedor-principal">
    <h1>Para público general</h1>
    <p>
      Ofrecemos rutas y talleres para la población general. Cuéntanos lo que necesitas y diseñamos una actividad a tu medida.
    </p>

    <h2>Actividades para público general</h2>
    <p>
      Aquí tienes algunas de las actividades que ofrecemos. Todas nuestras actividades pueden realizarse en euskera y/o castellano.
      Si tienes algún interés especial, diseñamos una actividad a tu medida.
    </p>
    <p>Si te gusta hacer cosas en familia, no te pierdas las actividades que tenemos programadas. También puedes juntarte con otras familias y pedir una actividad para todos.</p>
    <p>
      ¿Que si hacemos actividades para los más experimentados de la vida? Por supuesto que sí. Un taller, una ruta, un día de actividades. ¿Qué te apetece más?
    </p>
    <div class="horizontal">

      <div class="card-servicios">
        <div class="imagen-servicios">
          <img class="img" src="/imagenes/servicios/detalle/bombas.avif" alt="Talleres medioambientales para público general — bombas de semillas y huertos" title="Talleres medioambientales para público general" loading="lazy"/>
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
          <img class="img" src="/imagenes/servicios/detalle/sopela.avif" alt="Ruta geológica en Sopela — actividad para público general" title="Ruta geológica en Sopela" loading="lazy"/>
        </div>
        <div class="lista-servicios">
          <h3>Rutas Guiadas</h3>
          <ul>
            <li>Ruta geológica por el Flysch de Sopela</li>
            <li>Ruta geomedioambiental por el Flysch de Getxo</li>
            <li>Identificación de árboles</li>
          </ul>
        </div>
      </div>

      <div class="card-servicios">
        <div class="imagen-servicios">
          <img class="img" src="/imagenes/servicios/detalle/micro.avif" alt="Experiencias de inmersión en la naturaleza para público general" title="Experiencias de inmersión en la naturaleza" loading="lazy"/>
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

const pageUrl = 'https://www.geobizi.com/detalle-general'
const ogImage = 'https://www.geobizi.com/imagenes/servicios/detalle/bombas.avif'

useHead({
  title: 'Actividades para público general | GeoBizi',
  meta: [
    { name: 'description', content: 'Rutas, talleres y experiencias medioambientales para público general: actividades familiares, talleres y proyectos para disfrutar y aprender en la naturaleza.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'GeoBizi' },
    { name: 'keywords', content: 'actividades público general, talleres familiares, rutas naturales, GeoBizi' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Actividades para público general | GeoBizi' },
    { property: 'og:description', content: 'Rutas, talleres y experiencias medioambientales para público general: actividades familiares y proyectos para conectar con la naturaleza.' },
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
        "name": "Actividades para público general | GeoBizi",
        "description": "Rutas, talleres y experiencias medioambientales para público general: actividades familiares y proyectos para disfrutar y aprender en la naturaleza.",
        "inLanguage": "es",
        "image": ogImage
      })
    }
  ]
})

const pageUrlGen = 'https://www.geobizi.com/servicios'
const ogImageGen = 'https://www.geobizi.com/imagenes/servicios/servicios-hero.avif'

useHead({
  title: 'Servicios GeoBizi',
  meta: [
    { name: 'description', content: 'Servicios de GeoBizi: rutas, talleres, formaciones y proyectos medioambientales para todo tipo de colectivos.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Servicios GeoBizi' },
    { property: 'og:description', content: 'Rutas, talleres, formaciones y proyectos medioambientales para colegios, empresas e instituciones.' },
    { property: 'og:type', content: 'website' },
    { property: 'og:url', content: pageUrlGen },
    { property: 'og:image', content: ogImageGen }
  ],
  link: [
    { rel: 'canonical', href: pageUrlGen },
    { rel: 'image_src', href: ogImageGen },
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
            "serviceType":"Servicios medioambientales y educativos",
            "provider": { "@type":"Organization","@id":"https://www.geobizi.com/#organization" },
            "name":"Servicios GeoBizi",
            "description":"Rutas, talleres, formaciones y proyectos medioambientales para colegios, empresas e instituciones.",
            "url": pageUrlGen,
            "inLanguage":"es",
            "image": { "@type":"ImageObject","url":ogImageGen,"width":1080,"height":1080 }
          }
        ]
      })
    }
  ]
})
</script>

<style scoped>
</style>