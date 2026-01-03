<template>

  <div class="contenedor-principal">
    <h1>Día del Árbol</h1>
    <h2>Sembrando vida y conciencia ambiental</h2>

    <h3>Una jornada para reconectar con la naturaleza</h3>

    <p>
      El <strong>Día del Árbol</strong> es una celebración dedicada a la naturaleza y al cuidado del entorno. 
      Geobizi participa cada año con actividades educativas y participativas para todas las edades, 
      fomentando el respeto y la acción directa por los ecosistemas.
    </p>

    <h3>Actividades que inspiran y regeneran</h3>

    <p>
      En las diferentes ediciones del Día del Árbol se han desarrollado <strong>talleres de bombas de semillas</strong>,
      actividades de <strong>identificación de árboles</strong> y jornadas de <strong>limpieza del entorno</strong>, 
      promoviendo una relación activa y respetuosa con el medio natural.
    </p>

    <p>
      También se han realizado <strong>talleres de micromundo</strong>, explorando la vida invisible del suelo y 
      comprendiendo su papel esencial en los bosques y ecosistemas.
    </p>

    <p>
      Una experiencia de aprendizaje, acción y conexión que invita a sembrar futuro.
    </p>

    <h3>¿Por qué participar en el Día del Árbol?</h3>

    <p>
      <img src="/imagenes/iconos/color/naturaleza.png" alt="Icono naturaleza" title="Naturaleza" class="icono" loading="lazy" />
      <strong>Compromiso con la naturaleza</strong> – Actividades que fomentan el respeto, la observación y la restauración del entorno natural.
    </p>
    <p>
      <img src="/imagenes/iconos/color/familia.png" alt="Icono comunidad" title="Comunidad y participación" class="icono" loading="lazy" />
      <strong>Comunidad y cooperación</strong> – Experiencias colectivas para aprender y actuar en grupo, en familia o con amistades.
    </p>
    <p>
      <img src="/imagenes/iconos/color/libro.png" alt="Icono aprendizaje" title="Aprendizaje ambiental" class="icono" loading="lazy" />
      <strong>Aprendizaje ambiental</strong> – Actividades didácticas para comprender los ecosistemas y su importancia.
    </p>
    <p>
      <img src="/imagenes/iconos/color/hojas.png" alt="Icono acción" title="Acción ecológica" class="icono" loading="lazy" />
      <strong>Acción ecológica</strong> – Pequeños gestos que generan grandes cambios: sembrar, limpiar, cuidar.
    </p>

    <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/diadelarbol/diadelarbol1.avif"
          alt="Taller de bombas de semillas en el Día del Árbol"
          title="Día del Árbol — imagen 1"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/diadelarbol/diadelarbol2.avif"
          alt="Personas identificando árboles y especies autóctonas"
          title="Día del Árbol — imagen 2"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/diadelarbol/diadelarbol3.avif"
          alt="Actividad educativa sobre el micromundo del suelo"
          title="Día del Árbol — imagen 3"
          loading="lazy"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/detalle-dia-del-arbol'
const ogImage = 'https://www.geobizi.com/imagenes/proyectos/diadelarbol1.avif'

useHead({
  title: 'Día del Árbol — Educación y acción ambiental | Geobizi',
  meta: [
    { name: 'description', content: 'Día del Árbol: talleres, rutas y actividades participativas de Geobizi para cuidar, conocer y celebrar la naturaleza.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Día del Árbol — Educación y acción ambiental | Geobizi' },
    { property: 'og:description', content: 'Día del Árbol: talleres, rutas y actividades participativas de Geobizi para cuidar, conocer y celebrar la naturaleza.' },
    { property: 'og:type', content: 'article' },
    { property: 'og:url', content: pageUrl },
    { property: 'og:image', content: ogImage },
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:image', content: ogImage }
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
        "@context": "https://schema.org",
        "@graph": [
          {
            "@type": "Organization",
            "@id": "https://www.geobizi.com/#organization",
            "name": "Geobizi",
            "url": "https://www.geobizi.com",
            "logo": {
              "@type": "ImageObject",
              "url": "https://www.geobizi.com/imagenes/GeobiziLogo.7ae1d6ce.png",
              "width": 1417,
              "height": 313
            },
            "sameAs": [
              "https://www.facebook.com/geobizirik/",
              "https://www.instagram.com/geotxiki/",
              "https://www.youtube.com/channel/UCw-C_J0y-jKHp7Zx92lsKfg"
            ]
          },
          {
            "@type": "WebPage",
            "url": pageUrl,
            "name": "Día del Árbol — Educación y acción ambiental | Geobizi",
            "description": "Día del Árbol: talleres, rutas y actividades participativas de Geobizi para cuidar, conocer y celebrar la naturaleza.",
            "inLanguage": "es",
            "isPartOf": { "@id": "https://www.geobizi.com/#organization" },
            "image": { "@type": "ImageObject", "url": ogImage, "width": 1080, "height": 1080 }
          }
        ]
      })
    }
  ]
})
</script>

<style scoped>
.contenedor-principal {
  padding-top: 7rem;
  background-color: rgb(255, 255, 255);
  padding-bottom: 2rem;
}
.icono {
  width: 20px;
  height: 20px;
  margin-right: 8px;
  vertical-align: middle;
}
</style>
