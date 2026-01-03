<template>

  <div class="contenedor-principal">
    <h1>Semana Verde</h1>
    <h2>Aste Berdea</h2>

    <h3>Acción, naturaleza y conciencia ambiental</h3>

    <p>La <strong>Semana Verde</strong> es un evento que celebra el compromiso con el medio ambiente y la sostenibilidad a través de actividades participativas, educativas y al aire libre.</p>

    <h3>Actividades para conectar con la naturaleza</h3>

    <p>Durante diferentes ediciones de la <strong>Aste Berdea de Getxo</strong>, Geobizi ha desarrollado una amplia variedad de talleres y rutas diseñadas para sensibilizar y disfrutar del entorno natural de una forma práctica y divertida.</p>

    <p>Entre las actividades destacan los talleres de micromundo, los talleres medioambientales, rutas divulgativas y geológicas, la creación e instalación de hoteles de insectos, o las limpiezas colaborativas de playas.</p>

    <p>Cada edición invita a la acción y al aprendizaje colectivo, fomentando la participación ciudadana y el respeto por la naturaleza.</p>

    <h3>¿Por qué participar en la Semana Verde?</h3>

    <p>
      <img src="/imagenes/iconos/color/naturaleza.png" alt="Icono naturaleza" title="Compromiso ambiental" class="icono" loading="lazy" />
      <strong>Compromiso ambiental</strong> – Actividades centradas en la sostenibilidad y el cuidado del entorno.
    </p>
    <p>
      <img src="/imagenes/iconos/color/familia.png" alt="Icono participativo" title="Participativo" class="icono" loading="lazy" />
      <strong>Participativo</strong> – Impulsa la implicación ciudadana en la mejora ambiental.
    </p>
    <p>
      <img src="/imagenes/iconos/color/libro.png" alt="Icono educativo" title="Educativo" class="icono" loading="lazy" />
      <strong>Educativo</strong> – Promueve valores de respeto, sostenibilidad y ciencia ciudadana.
    </p>
    <p>
      <img src="/imagenes/iconos/color/comunidad.png" alt="Icono comunidad" title="Comunidad" class="icono" loading="lazy" />
      <strong>Comunitario</strong> – Fortalece la colaboración entre vecinos, asociaciones y familias.
    </p>

    <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/asteberdea/semanaverde1.avif"
          alt="Participantes en talleres medioambientales durante la Semana Verde"
          title="Semana Verde — imagen 1"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/asteberdea/semanaverde2.avif"
          alt="Instalación de hoteles de insectos en la Aste Berdea"
          title="Semana Verde — imagen 2"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/asteberdea/semanaverde3.avif"
          alt="Limpieza colaborativa de playas en Getxo"
          title="Semana Verde — imagen 3"
          loading="lazy"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/detalle-semana-verde'
const ogImage = 'https://www.geobizi.com/imagenes/proyectos/semanaverde1.avif'

useHead({
  title: 'Semana Verde — Aste Berdea | Geobizi',
  meta: [
    { name: 'description', content: 'Semana Verde (Aste Berdea): talleres medioambientales, rutas divulgativas y actividades de sostenibilidad en Getxo. Una experiencia participativa y educativa.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Semana Verde — Aste Berdea | Geobizi' },
    { property: 'og:description', content: 'Semana Verde (Aste Berdea): talleres medioambientales, rutas divulgativas y actividades de sostenibilidad en Getxo. Una experiencia participativa y educativa.' },
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
            "name": "Semana Verde — Aste Berdea | Geobizi",
            "description": "Semana Verde (Aste Berdea): talleres medioambientales, rutas divulgativas y actividades de sostenibilidad en Getxo. Una experiencia participativa y educativa.",
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
