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
import { useHead } from '@vueuse/head' // añadido

const pageUrl = 'https://www.geobizi.com/detalle-instituciones'
const ogImage = 'https://www.geobizi.com/imagenes/servicios/detalle/jepplaya.avif'

useHead({
  title: 'Servicios para Instituciones | GeoBizi',
  meta: [
    { name: 'description', content: 'Formaciones, rutas y proyectos colaborativos para ayuntamientos e instituciones: sensibilización, biorregeneración y talleres especializados.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'GeoBizi' },
    { name: 'keywords', content: 'instituciones, formación medioambiental, biorregeneración, talleres, GeoBizi' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Servicios para Instituciones | GeoBizi' },
    { property: 'og:description', content: 'Formaciones, rutas y proyectos colaborativos para ayuntamientos e instituciones: sensibilización y biorregeneración.' },
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
        "@context":"https://schema.org",
        "@type":"WebPage",
        "url": pageUrl,
        "name": "Servicios para Instituciones | GeoBizi",
        "description": "Formaciones, rutas y proyectos colaborativos para ayuntamientos e instituciones: sensibilización y biorregeneración.",
        "inLanguage": "es",
        "image": ogImage
      })
    }
  ]
})
</script>

<style scoped></style>