<template>

  <div class="contenedor-principal">
    <h1>Semana de la Ciencia</h1>
    <h2>Zientzia Astea</h2>

    <h3>Descubrir, experimentar y aprender con la ciencia</h3>

    <p>La <strong>Semana de la Ciencia</strong> es una oportunidad única para acercar la ciencia a todas las edades a través de actividades dinámicas, creativas y participativas.</p>

    <h3>Aprendizaje vivencial y divulgativo</h3>

    <p>A lo largo de diferentes ediciones, Geobizi ha participado en la <strong>Zientzia Astea</strong> con propuestas diseñadas para centros escolares y público general. Las actividades se adaptan a cada espacio y nivel educativo, fomentando la curiosidad, la observación y la experimentación.</p>

    <p>Charlas, talleres de micromundo, experiencias medioambientales, rutas divulgativas, talleres de cianotipia, juegos de colores, identificación de árboles o recogida de muestras… Cada actividad es una puerta abierta al conocimiento y la exploración del entorno.</p>

    <p>Una propuesta para disfrutar de la ciencia de forma amena, participativa y cercana a la naturaleza.</p>

    <h3>¿Por qué elegir la Semana de la Ciencia?</h3>

    <p>
      <img src="/imagenes/iconos/color/libro.png" alt="Icono educativo" title="Educativo" class="icono" loading="lazy" />
      <strong>Educativo</strong> – Promueve el pensamiento científico y la curiosidad desde la práctica.
    </p>
    <p>
      <img src="/imagenes/iconos/color/familia.png" alt="Icono inclusivo" title="Para todos los públicos" class="icono" loading="lazy" />
      <strong>Para todos los públicos</strong> – Actividades adaptadas para escolares, familias y grupos.
    </p>
    <p>
      <img src="/imagenes/iconos/color/naturaleza.png" alt="Icono medioambiental" title="Conciencia ambiental" class="icono" loading="lazy" />
      <strong>Conciencia ambiental</strong> – Pone en valor la relación entre ciencia y naturaleza.
    </p>
    <p>
      <img src="/imagenes/iconos/color/aventura.png" alt="Icono de talleres prácticos" title="Talleres prácticos" class="icono" loading="lazy" />
      <strong>Práctico y participativo</strong> – Aprendizaje activo a través de la experimentación directa.
    </p>

    <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/zientziaastea/semanaciencia1.avif"
          alt="Talleres y actividades en la Semana de la Ciencia"
          title="Semana de la Ciencia — imagen 1"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/zientziaastea/semanaciencia2.avif"
          alt="Niños y niñas experimentando en talleres de ciencia"
          title="Semana de la Ciencia — imagen 2"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/zientziaastea/semanaciencia3.avif"
          alt="Exploración del entorno natural durante la Zientzia Astea"
          title="Semana de la Ciencia — imagen 3"
          loading="lazy"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/detalle-semana-ciencia'
const ogImage = 'https://www.geobizi.com/imagenes/proyectos/semanaciencia1.avif'

useHead({
  title: 'Semana de la Ciencia — Zientzia Astea | Geobizi',
  meta: [
    { name: 'description', content: 'Semana de la Ciencia (Zientzia Astea): talleres, rutas y actividades educativas para acercar la ciencia y el medio ambiente a todos los públicos.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Semana de la Ciencia — Zientzia Astea | Geobizi' },
    { property: 'og:description', content: 'Semana de la Ciencia (Zientzia Astea): talleres, rutas y actividades educativas para acercar la ciencia y el medio ambiente a todos los públicos.' },
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
            "name": "Semana de la Ciencia — Zientzia Astea | Geobizi",
            "description": "Semana de la Ciencia (Zientzia Astea): talleres, rutas y actividades educativas para acercar la ciencia y el medio ambiente a todos los públicos.",
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
