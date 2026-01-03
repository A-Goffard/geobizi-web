<template>
  <div class="general-container">
    <h1>Información y Recursos</h1>

    

    <div class="construction-container">
  <div class="message-box">
    <h1>Próximamente</h1>
    <p>Estamos cultivando esta sección...</p>
    <div>
            <img src="/imagenes/iconos/Hojitas.png" alt="" class="leaf leaf-1">
      <img src="/imagenes/iconos/Hojitas.png" alt="" class="leaf leaf-2">
      <img src="/imagenes/iconos/Hojitas.png" alt="" class="leaf leaf-3">
    </div>

  </div>



</div>

    <!-- <div class="container">
      <div class="card" v-for="section in sections" :key="section.title" @click="goToDetail(section.link)">
        <h2>{{ section.title }}</h2>
        <img :src="section.image" :alt="section.title" :title="section.title" loading="lazy">
        <p>{{ section.content }}</p>
      </div>
    </div> -->
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'
// import { ref } from 'vue'
// import { useRouter } from 'vue-router'

// CAMBIO 1: URL y metadatos base actualizados para la nueva sección
const pageUrl = 'https://www.geobizi.com/informacion' // O el nombre que decidas ponerle
const ogImage = 'https://www.geobizi.com/imagenes/informacion/hero-info.avif' // Imagen destacada para esta sección

useHead({
  title: 'Recursos e Información | Geobizi',
  meta: [
    { name: 'description', content: 'Centro de información de Geobizi: Artículos, guías de naturaleza, noticias sobre medioambiente y recursos didácticos.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Recursos e Información | Geobizi' },
    { property: 'og:description', content: 'Artículos, guías y novedades sobre proyectos medioambientales.' },
    { property: 'og:type', content: 'website' },
    { property: 'og:url', content: pageUrl },
    { property: 'og:image', content: ogImage }
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
            }
          },
          {
            "@type": "CollectionPage", // Cambiado a CollectionPage ya que es un listado de info
            "url": pageUrl,
            "name": "Recursos e Información | Geobizi",
            "description": "Centro de recursos, artículos y guías sobre medioambiente.",
            "inLanguage": "es",
            "isPartOf": { "@id": "https://www.geobizi.com/#organization" },
            "image": { "@type": "ImageObject", "url": ogImage, "width": 1080, "height": 1080 }
          }
        ]
      })
    }
  ]
})

// const router = useRouter()

// CAMBIO 2: Nuevas secciones informativas
// Ajusta los títulos, contenidos y links a lo que necesites desarrollar
// const sections = ref([
//   {
//     title: 'Blog y Artículos',
//     content: 'Artículos de opinión, curiosidades sobre geología y reflexiones sobre la educación ambiental actual.',
//     link: '/blog', // Ruta donde listarás los artículos
//     image: '/imagenes/info/blog.avif',
//   },
//   {
//     title: 'Guías de Naturaleza',
//     content: 'Fichas técnicas sobre flora, fauna y formaciones geológicas locales para aprender a identificar nuestro entorno.',
//     link: '/guias-naturaleza',
//     image: '/imagenes/info/guias.avif',
//   },
//   {
//     title: 'Proyectos Realizados',
//     content: 'Memoria de actividades y proyectos de biorregeneración llevados a cabo en colegios y empresas.',
//     link: '/proyectos-realizados',
//     image: '/imagenes/info/proyectos.avif',
//   },
//   {
//     title: 'Novedades Geobizi',
//     content: 'Últimas noticias sobre nuestra cooperativa, apariciones en prensa y nuevos convenios de colaboración.',
//     link: '/novedades',
//     image: '/imagenes/info/novedades.avif',
//   },
//   {
//     title: 'Recursos Didácticos',
//     content: 'Material de apoyo teórico para docentes y educadores que quieran profundizar en nuestras metodologías.',
//     link: '/recursos-didacticos',
//     image: '/imagenes/info/recursos.avif',
//   },
//   {
//     title: 'Galería Multimedia',
//     content: 'Recopilación de vídeos y fotografías de nuestras salidas, talleres y formaciones.',
//     link: '/galeria',
//     image: '/imagenes/info/galeria.avif',
//   }
// ])

// const goToDetail = (link) => {
//   router.push(link)
// }
</script>

<style scoped>
/* Se mantienen los mismos estilos para conservar la identidad visual de la web */
.container {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
}

.general-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  padding-top: 7rem;
  padding-left: 2rem;
  padding-right: 2rem;
  padding-bottom: 2rem;
}

.card {
  width: 300px;
  padding: 20px;
  /* Asegúrate de que estas variables CSS existan en tu archivo global */
  background-color: var(--megashoftgreen);
  border: 1px solid var(--shoftgreen);
  border-radius: 0.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
  cursor: pointer;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.card h2 {
  margin-top: 0;
}

.card p {
  color: var(--darkgrey);
}
img {
  width: 100%;
  border-radius: 0.5rem;
  /* Añadido object-fit para asegurar que las imágenes se vean bien si tienen tamaños distintos */
  object-fit: cover;
  aspect-ratio: 16/9; 
}





/* La parte de en construcción con las hojas animadas */

.construction-container {
  position: relative; /* Para poder colocar las hojas flotando alrededor */
  min-height: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden; /* Para que si una hoja se sale no rompa la web */
  text-align: center;
  padding: 2rem;
}

.message-box {
  z-index: 10; /* El texto por encima */
  background: rgba(255, 255, 255, 0.9);
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

.message-box h1 {
  color: var(--darkPurple);
  margin-bottom: 0.5rem;
}

.message-box p {
  color: #666;
}

/* ESTILO BASE DE LA HOJA */
.leaf {

  width: 50px; /* Ajusta el tamaño según tu imagen */
  height: auto;
  opacity: 0.8;
  
  /* LA CLAVE DEL REALISMO: */
  transform-origin: 40% 97%;
  animation: wind-sway 3s ease-in-out infinite alternate;
}

/* POSICIONES Y TIEMPOS DISTINTOS */
/* Hoja 1: Arriba a la izquierda, movimiento lento */
.leaf-1 {
  width: 7rem;
  transform: rotate(-5deg);
  animation-duration: 4s; /* Más lenta */
}

/* Hoja 2: Arriba a la derecha, movimiento un poco más rápido */
.leaf-2 {

  width: 5.25rem; 
    opacity: 0.75;
  animation-duration: 2.5s; 
  animation-delay: 0.5s; /* Empieza un poco más tarde */
}

/* Hoja 3: Abajo cerca del texto */
.leaf-3 {
  width: 6rem;
  opacity: 0.85;
  animation-duration: 3.5s;
  animation-delay: 1s;
}

/* LA ANIMACIÓN DEL VIENTO */
@keyframes wind-sway {
  0% {
    transform: rotate(-10deg); /* Se inclina a la izquierda */
  }
  100% {
    transform: rotate(10deg); /* Se inclina a la derecha */
  }
}


</style>