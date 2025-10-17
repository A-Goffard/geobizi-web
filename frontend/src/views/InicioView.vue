<template>
  <div>
      <div class="contenedor-cabecero">


<div class="contenedor-intro">
  <h1>Geobizi, naturaleza desde el corazón</h1>
  <h2>Una empresa nacida del amor a la naturaleza y las ganas de compartir</h2>
  <h3>Diseñamos experiencias medioambientales únicas</h3>
  <p>Desarrollamos e implementamos actividades a medida para que disfrutes, desconectes, aprendas y sobre todo, compartamos, siempre con el foco en la naturaleza y el medioambiente.</p>
</div>

</div>
  <div class="contenedor-principal">




    <div class="contenedor-historia">
      <div class="cont-texto">
        <h2>Historia y misión</h2>
        <h3>Medioambiente y bienestar</h3>
        <p>Una asesoría pedagógica medioambiental especializada en la formación, divulgación científica y medioambiental y el diseño de experiencias centradas en la naturaleza para que conectes con el mundo desde el respeto y el conocimiento.</p>
        <p>Desde nuestros inicios hemos trabajado con mucho cariño para ofrecerte las mejores experiencias hasta llegar a lo que es hoy en día Geobizi. </p>
        <p>Desarrollamos formaciones, rutas, talleres y experiencias personalizadas para niñas y niños, particulares, perfiles silver, empresas públicas o privadas, colegios u otros centros formativos, instituciones...</p>
        <p>También diseñamos proyectos de sensibilización y biorregeneración colaborativos para mejorar el entorno natural y fomentar la conciencia ambiental.</p>
        <p>Pensamos que todo tipo de personas, grupos y edades diferentes deben tener acceso a la educación medioambiental y todos los beneficios sociales, naturales y de salud que lleva unidos. Es por ello que adaptamos unos objetivos similares a una diversidad de grupos.</p>
        <p>Nuestras actividades son sostenibles, inclusivas, coeducativas y no discriminatorias.</p>
      </div>

      <div>
        <img class="imagendiv" src="/imagenes/inicio/mision.avif" alt="Mariposas en una mano" title="Mariposas en una mano" loading="lazy">
      </div>
    </div>

    <div class="contenedor-historia">
      <div>
      <img class="imagendiv" src="/imagenes/inicio/esencia.avif" alt="Familia plantando un árbol" title="Familia plantando un árbol" loading="lazy">
      </div>
      <div class="cont-texto">
        <h2>Esencia</h2>
        <h3>Creemos en el conocimiento compartido</h3>
        <p>La ciencia y el conocimiento son el vehículo para acercar a las personas a la naturaleza de una forma respetuosa y sostenible.</p>
        <p>La base para llevar el aprendizaje al hecho es generando una dinámica que permita interiorizar de forma divertida y práctica los conocimientos y conceptos necesarios para crear hábitos de vida sostenibles y respetar la curiosidad natural del ser humano.</p>
        <p>Hacer las cosas uno mismo e interactuar con la materia facilita la interiorización además de ayudar a desarrollar otras habilidades y herramientas sociales y mentales.</p>
        <p>Las actividades medioambientales no son un mero entretenimiento y con esa premisa muy presente siempre realizamos nuestras actividades con una calidad y atención especial y siempre teniendo en cuenta el medioambiente y los ODSs.</p>
      </div>

    </div>

    <div class="contenedor-historia">
      <div class="cont-texto">
        <h2>Nuestro equipo</h2>
        <h3>Multidisciplinar y colaborativo</h3>
        <p>Somos un equipo de asesoramiento y de trabajo multidisciplinar de alta cualificación, que colaboramos y trabajamos conjuntamente para satisfacer tus necesidades y mejorar constantemente nuestros servicios.</p>
        <p>Nuestro equipo no se limita a Geobizi. Además de los compañeros/as que formamos el equipo principal, tenemos otros muchos colaboradores que nos apoyan, ayudan, asesoran, y comparten con nosotros su sabiduría y expertise.</p>
        <p>Profesionales de la educación, la ciencia, la comunicación y la tecnología forman parte de Geobizi.</p>
      </div>

      <div>
        <img class="imagendiv" src="/imagenes/inicio/equipo.avif" alt="Manos en la naturaleza" title="Manos en la naturaleza" loading="lazy">
      </div>
    </div>
  </div>


  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head' // { añadido }

const pageUrl = 'https://www.geobizi.com/'
const ogImage = 'https://www.geobizi.com/imagenes/inicio/mision.avif'

useHead({
  title: 'GeoBizi — Naturaleza desde el corazón',
  meta: [
    { name: 'description', content: 'GeoBizi diseña experiencias medioambientales: rutas, talleres y proyectos para colegios, empresas, instituciones y público general.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'GeoBizi' },
    { name: 'publisher', content: 'GeoBizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'GeoBizi — Naturaleza desde el corazón' },
    { property: 'og:description', content: 'GeoBizi diseña experiencias medioambientales: rutas, talleres y proyectos para colegios, empresas, instituciones y público general.' },
    { property: 'og:type', content: 'website' },
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
            "name": "GeoBizi — Naturaleza desde el corazón",
            "description": "GeoBizi diseña experiencias medioambientales: rutas, talleres y proyectos para colegios, empresas, instituciones y público general.",
            "inLanguage": "es",
            "isPartOf": { "@id": "https://www.geobizi.com/#organization" },
            "image": {
              "@type": "ImageObject",
              "url": ogImage,
              "width": 1080,
              "height": 1080
            }
          }
        ]
      })
    }
  ]
})
</script>

<style scoped>
.contenedor-secundario {
  max-width: 1200px;
    margin: 0 auto;
}
.contenedor-cabecero {
  padding: 5rem;
  background-image: url('@/../public/imagenes/background/6.avif');
  background-size: cover; 
  background-position: center; 
  background-color: var(--darkgreen); 
}
.contenedor-intro {
  max-width: 40rem;
  padding: 2rem;
  background-color: white;
  border-radius: 0.5rem;
}
.contenedor-historia {
  display: flex;
  align-items: center;
}

.imagendiv {

  width: 100%;
  border-radius: 0.5rem;
}

@media (max-width: 550px) {
  .contenedor-historia {
    flex-direction: column;
  }
}

@media (max-width: 420px) {
.contenedor-cabecero {
  padding: 2rem;
}
}

</style>