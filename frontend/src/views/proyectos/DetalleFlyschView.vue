<template>

    <div class="contenedor-principal">
      <h1>Flysch Digital</h1>
      <h2>Yincana Interactiva</h2>
      
      <h3>Donde la aventura, la tecnología y la naturaleza se unen</h3>

      <p>¿Imaginas explorar un paisaje espectacular mientras resuelves enigmas digitales con tu móvil? Flysch Digital es una experiencia única que combina lo mejor de una yincana tradicional con la emoción de las nuevas tecnologías.</p>
      <h3>Una aventura para todos</h3>

      <p>Una actividad pensada para todos los públicos, familias, grupos de amigos, adultos, adolescentes, turistas... Con ayuda del móvil, irán resolviendo pistas y acertijos por la playa de Sopela hasta dar con la prueba final.</p>
      <p>En el transcurso de las pruebas se irán moviendo por toda la zona mientras aprenden, descubren, se entretienen y disfrutan de una actividad diferente.</p>
      <p>Es un proyecto adaptable a otros entonos que resulta original y divertido.</p>
      <p>La actividad se puede realizar en euskera o castellano.</p>
      <p>Una posibilidad interesante para los que les gusta hacer algo diferente.</p>

      <h3>¿Quieres una yincana digital personalizada?</h3>
      <p>¡Creamos yincanas a medida para cualquier lugar! Contáctanos y diseñaremos una experiencia única adaptada a tu entorno.</p>
      
      <h3>¿Por qué elegir Flysch Digital?</h3>
      <p>
        <img src="/imagenes/iconos/color/estrellitas.png" alt="Icono actividad original" title="Original" class="icono" loading="lazy" />
        <strong>Actividad original</strong> – No es solo un paseo, es una experiencia interactiva.
      </p>      
      <p>
        <img src="/imagenes/iconos/color/adaptable.png" alt="Icono adaptable" title="Adaptable" class="icono" loading="lazy" />
        <strong>Adaptable</strong> – Podemos personalizarla para otros entornos (montañas, ciudades, parques naturales…).</p>
      <p>
        <img src="/imagenes/iconos/color/multilingue.png" alt="Icono multilingüe" title="Multilingüe" class="icono" loading="lazy" />
        <strong>Multilingüe</strong> – Disponible en euskera y castellano (otros idiomas bajo consulta).</p>
      <p>
        <img src="/imagenes/iconos/color/libro.png" alt="Icono educativo" title="Educativo" class="icono" loading="lazy" />
        <strong>Educativo y entretenido</strong> – Perfecto para colegios, empresas o grupos de ocio.</p>

      <div class="imagen-trio">
      <div>
              <img
        class="img"
        src="/imagenes/proyectos/flyschdigital/flyschdigital1.avif"
        alt="Flysch Digital — yincana interactiva en la costa"
        title="Flysch Digital — imagen 1"
        loading="lazy"
      />
      </div>
      <div>
              <img
        class="img"
        src="/imagenes/proyectos/flyschdigital/flyschdigital2.avif"
        alt="Participantes resolviendo pruebas de la yincana digital"
        title="Flysch Digital — imagen 2"
        loading="lazy"
      />
      </div>
      <div>
              <img
        class="img"
        src="/imagenes/proyectos/flyschdigital/flyschdigital3.avif"
        alt="Exploración del flysch y descubrimiento de fósiles"
        title="Flysch Digital — imagen 3"
        loading="lazy"
      />
      </div>

    </div>
    </div>
  </template>
  
  <script setup>
import { useHead } from '@vueuse/head' // añadido

const pageUrl = 'https://www.geobizi.com/detalle-flysch'
const ogImage = 'https://www.geobizi.com/imagenes/proyectos/flyschdigital1.avif'

useHead({
  title: 'Flysch Digital — Yincana interactiva | Geobizi',
  meta: [
    { name: 'description', content: 'Flysch Digital: yincana interactiva para explorar el Flysch de Bizkaia. Actividad educativa y divertida para familias, colegios y grupos.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Flysch Digital — Yincana interactiva | Geobizi' },
    { property: 'og:description', content: 'Flysch Digital: yincana interactiva para explorar el Flysch de Bizkaia. Actividad educativa y divertida para familias, colegios y grupos.' },
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
            "name": "Flysch Digital — Yincana interactiva | Geobizi",
            "description": "Flysch Digital: yincana interactiva para explorar el Flysch de Bizkaia. Actividad educativa y divertida para familias, colegios y grupos.",
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