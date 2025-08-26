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
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/servicios/asociaciones'
const ogImage = 'https://www.geobizi.com/imagenes/servicios/asociaciones.avif'

useHead({
  title: 'Servicios para Asociaciones | GeoBizi',
  meta: [
    { name: 'description', content: 'Servicios y colaboraciones con asociaciones: talleres, proyectos participativos y formaciones a medida.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' }
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
            "serviceType":"Servicios y colaboraciones para asociaciones",
            "provider": { "@type":"Organization","@id":"https://www.geobizi.com/#organization" },
            "name":"Servicios para Asociaciones | GeoBizi",
            "description":"Talleres, formaciones y proyectos participativos para asociaciones y colectivos.",
            "url": pageUrl,
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