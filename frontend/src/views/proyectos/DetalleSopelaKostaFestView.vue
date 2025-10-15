<template>

  <div class="contenedor-principal">
    <h1>Sopela Kosta Fest</h1>
    <h2>Naturaleza, cultura y aventura en la costa</h2>

    <h3>Donde el mar, la ciencia y la creatividad se encuentran</h3>

    <p>El <strong>Sopela Kosta Fest</strong> es un festival que celebra el vínculo entre el mar, el deporte, la cultura y la naturaleza. Geobizi participa cada año con actividades educativas, creativas y de exploración adaptadas a todos los públicos.</p>

    <h3>Actividades que conectan con la costa</h3>

    <p>A lo largo de las diferentes ediciones, Geobizi ha dinamizado talleres y rutas que combinan divulgación científica, arte y juego. Desde <strong>talleres de brújulas vikingas</strong> o <strong>pulseras cauri</strong> hasta <strong>rutas geológicas y de fósiles</strong> o <strong>yincanas digitales</strong>, las propuestas invitan a descubrir la costa de Sopela de una forma original y participativa.</p>

    <p>También se han realizado <strong>talleres de mandalas</strong> y de <strong>pintar olas</strong>, donde la creatividad y la conexión con el entorno marino cobran protagonismo.</p>

    <p>Una experiencia donde aprender, crear y disfrutar del paisaje natural se dan la mano.</p>

    <h3>¿Por qué participar en Sopela Kosta Fest?</h3>

    <p>
      <img src="/imagenes/iconos/color/naturaleza.png" alt="Icono naturaleza" title="Naturaleza" class="icono" loading="lazy" />
      <strong>En contacto con la naturaleza</strong> – Actividades junto al mar que fomentan el respeto y la exploración del entorno.
    </p>
    <p>
      <img src="/imagenes/iconos/color/creativo.png" alt="Icono creativo" title="Creatividad" class="icono" loading="lazy" />
      <strong>Creatividad y arte</strong> – Talleres artísticos inspirados en la costa y en la cultura marina.
    </p>
    <p>
      <img src="/imagenes/iconos/color/aventura.png" alt="Icono aventura" title="Aventura y aprendizaje" class="icono" loading="lazy" />
      <strong>Aventura y aprendizaje</strong> – Rutas geológicas, fósiles y yincanas digitales para explorar y descubrir.
    </p>
    <p>
      <img src="/imagenes/iconos/color/familia.png" alt="Icono comunidad" title="Comunidad y participación" class="icono" loading="lazy" />
      <strong>Comunidad y participación</strong> – Actividades pensadas para disfrutar en grupo, en familia o con amigos.
    </p>

    <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/sopelakostafest/sopelakostafest1.avif"
          alt="Talleres y actividades de GeoBizi en Sopela Kosta Fest"
          title="Sopela Kosta Fest — imagen 1"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/sopelakostafest/sopelakostafest2.avif"
          alt="Participantes explorando la costa durante una ruta geológica"
          title="Sopela Kosta Fest — imagen 2"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/sopelakostafest/sopelakostafest3.avif"
          alt="Talleres creativos y artísticos en la playa"
          title="Sopela Kosta Fest — imagen 3"
          loading="lazy"
        />
      </div>
    </div>
        <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/sopelakostafest/sopelakostafest4.avif"
          alt="Talleres y actividades de GeoBizi en Sopela Kosta Fest"
          title="Sopela Kosta Fest — imagen 1"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/sopelakostafest/sopelakostafest5.avif"
          alt="Participantes explorando la costa durante una ruta geológica"
          title="Sopela Kosta Fest — imagen 2"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/sopelakostafest/sopelakostafest6.avif"
          alt="Talleres creativos y artísticos en la playa"
          title="Sopela Kosta Fest — imagen 3"
          loading="lazy"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/detalle-sopela-kosta-fest'
const ogImage = 'https://www.geobizi.com/imagenes/proyectos/sopelakostafest1.avif'

useHead({
  title: 'Sopela Kosta Fest — Actividades creativas y medioambientales | GeoBizi',
  meta: [
    { name: 'description', content: 'Sopela Kosta Fest: talleres, rutas y experiencias educativas en la costa. Actividades de GeoBizi para descubrir la naturaleza, la ciencia y la creatividad junto al mar.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'GeoBizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Sopela Kosta Fest — Actividades creativas y medioambientales | GeoBizi' },
    { property: 'og:description', content: 'Sopela Kosta Fest: talleres, rutas y experiencias educativas en la costa. Actividades de GeoBizi para descubrir la naturaleza, la ciencia y la creatividad junto al mar.' },
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
            "name": "GeoBizi",
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
            "name": "Sopela Kosta Fest — Actividades creativas y medioambientales | GeoBizi",
            "description": "Sopela Kosta Fest: talleres, rutas y experiencias educativas en la costa. Actividades de GeoBizi para descubrir la naturaleza, la ciencia y la creatividad junto al mar.",
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
