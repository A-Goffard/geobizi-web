<template>
  <div>
    <div class="contenedor-cabecero">
      <div class="contenedor-intro">
        <h1>Geobizi: Ciencia, Naturaleza e Inclusión</h1>
        <h2>Tu asesoría pedagógica y divulgación científica en Bizkaia</h2>
        <p>Diseñamos experiencias de aprendizaje significativas. Combinamos educación ambiental, neuroeducación y rigor científico para conectar personas con la naturaleza de forma accesible y equitativa.</p>
      </div>
    </div>

    <div class="contenedor-principal">
      <div class="contenedor-historia">
        <div class="cont-texto">
          <h2>Misión pedagógica</h2>
          <h3>Naturaleza, ciencia y bienestar inclusivo</h3>
          <p>Somos una asesoría pedagógica medioambiental especializada en divulgación científica y diseño de experiencias que eliminan barreras. Nuestro objetivo es que toda persona, independientemente de sus capacidades, pueda conectar con el medio natural desde el respeto y la curiosidad.</p>
          <p>Desarrollamos soluciones personalizadas para el sector educativo, instituciones públicas, entidades privadas y familias, aplicando metodologías de Diseño Universal para el Aprendizaje (DUA).</p>
          <p>Fomentamos la conciencia ambiental mediante proyectos de biorregeneración colaborativa, transformando la teoría en acción práctica y científica.</p>
        </div>
        <div>
          <img class="imagendiv" src="/imagenes/inicio/mision.avif" alt="Divulgación científica inclusiva" title="Geobizi - Ciencia en mano" loading="lazy">
        </div>
      </div>

      <div class="contenedor-historia">
        <div>
          <img class="imagendiv" src="/imagenes/inicio/esencia.avif" alt="Aprendizaje activo en la naturaleza" title="Aprendizaje práctico" loading="lazy">
        </div>
        <div class="cont-texto">
          <h2>Nuestra esencia</h2>
          <h3>Conocimiento compartido y accesible</h3>
          <p>Creemos que la ciencia es el vehículo para una ciudadanía crítica y responsable. Nuestras actividades no son un entretenimiento pasajero; son intervenciones educativas diseñadas con rigor, donde la interacción directa con la materia facilita la interiorización de conceptos sostenibles.</p>
          <p>La curiosidad es un derecho, no un privilegio. Por eso, integramos los Objetivos de Desarrollo Sostenible (ODS) y la perspectiva de la neuroeducación en cada ruta, taller o proyecto de restauración que ejecutamos.</p>
        </div>
      </div>

      <div class="contenedor-historia">
        <div class="cont-texto">
          <h2>El equipo</h2>
          <h3>Multidisciplinar, científico y diverso</h3>
          <p>Geobizi es el punto de encuentro entre la educación, la ciencia, la tecnología y la comunicación. Contamos con un equipo principal de alta cualificación y una red extendida de colaboradores expertos que enriquecen nuestra visión.</p>
          <p>Trabajamos desde la transversalidad para ofrecer un asesoramiento que cumple con los más altos estándares de calidad, garantizando que el acceso al conocimiento ambiental sea una realidad para todos los grupos sociales.</p>
        </div>
        <div>
          <img class="imagendiv" src="/imagenes/inicio/equipo.avif" alt="Equipo multidisciplinar trabajando" title="Equipo Geobizi" loading="lazy">
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
  title: 'Geobizi — Naturaleza desde el corazón',
  meta: [
    { name: 'description', content: 'Geobizi diseña experiencias medioambientales: rutas, talleres y proyectos para colegios, empresas, instituciones y público general.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'publisher', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Geobizi — Naturaleza desde el corazón' },
    { property: 'og:description', content: 'Geobizi diseña experiencias medioambientales: rutas, talleres y proyectos para colegios, empresas, instituciones y público general.' },
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
            "name": "Geobizi — Naturaleza desde el corazón",
            "description": "Geobizi diseña experiencias medioambientales: rutas, talleres y proyectos para colegios, empresas, instituciones y público general.",
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