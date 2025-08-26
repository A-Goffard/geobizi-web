<template>
  <div class="contenedor-principal">
    <h1>Para instituciones</h1>
    <p>
      Ofrecemos actividades y formaciones para ayuntamientos y otras instituciones. Pon en valor el medio natural de tu entorno y forma a tus ciudadanos y empresas en temas medioambientales.
    </p>

    <h2>Actividades para instituciones</h2>
    <p>
      Aquí tienes algunas de las actividades que ofrecemos. Todas nuestras actividades pueden realizarse en euskera y/o castellano.
      Si tienes algún interés especial, diseñamos una actividad a tu medida.
    </p>

    <div class="horizontal">

      <div class="card-servicios">
        <div class="imagen-servicios">
          <img class="img" src="/imagenes/servicios/detalle/jepazkorri.avif" alt="Formación medioambiental para instituciones" title="Formación medioambiental para instituciones" loading="lazy"/>
        </div>
        <div class="lista-servicios">
          <h3>Formación para las empresas y el pueblo</h3>
          <ul>
            <li>Sensibilización medioambiental</li>
            <li>Mejora de la sostenibilidad empresarial</li>
            <li>Sinergias sostenibles</li>
          </ul>
        </div>
      </div>

      <div class="card-servicios">
        <div class="imagen-servicios">
          <img class="img" src="/imagenes/servicios/detalle/eguzkilores.avif" alt="Rutas guiadas y talleres para instituciones" title="Rutas guiadas y talleres para instituciones" loading="lazy"/>
        </div>
        <div class="lista-servicios">
          <h3>Rutas Guiadas y talleres</h3>
          <ul>
            <li>Rutas geológicas</li>
            <li>Rutas medioambientales</li>
            <li>Identificación de árboles</li>
            <li>Talleres temáticos para eventos</li>
            <li>Talleres temáticos para grupos sociales</li>
          </ul>
        </div>
      </div>

      <div class="card-servicios">
        <div class="imagen-servicios">
          <img class="img" src="/imagenes/servicios/detalle/jepplaya.avif" alt="Proyectos colaborativos de biorregeneración" title="Proyectos de biorregeneración colaborativa" loading="lazy"/>
        </div>
        <div class="lista-servicios">
          <h3>Proyectos de Bio-regeneración colaborativos</h3>
          <ul>
            <li>Diagnóstico inicial</li>
            <li>Diseño y desarrollo del proyecto</li>
            <li>Implementación con la colaboración de la ciudadanía</li>
            <li>Evaluación y medición del impacto</li>
          </ul>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/servicios/instituciones'
const ogImage = 'https://www.geobizi.com/imagenes/servicios/instituciones.avif'

useHead({
  title: 'Servicios para Instituciones | GeoBizi',
  meta: [
    { name: 'description', content: 'Programas y proyectos para instituciones: educación ambiental, diagnósticos y colaboraciones técnicas.' },
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
            "serviceType":"Proyectos y programas para instituciones",
            "provider": { "@type":"Organization","@id":"https://www.geobizi.com/#organization" },
            "name":"Servicios para Instituciones | GeoBizi",
            "description":"Formaciones, proyectos de restauración y asesoramiento técnico para instituciones públicas y privadas.",
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