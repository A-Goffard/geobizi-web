<template>
    <div class="general-container">
      <h1>Artículos del blog</h1>
      <p>Estos son nuestros artículos de blog escritos especialmente para ti.</p>
      <p>Elige sobre qué quieres leer o aprender. Medioambiente, biodiversidad, naturaleza, actividades, novedades de Geobizi, y mucho más para elegir.</p>
      <div class="container">
        <div class="card" v-for="article in articles" :key="article.title" @click="goToDetail(article.link)">
          <h2>{{ article.title }}</h2>
          <img :src="article.image" :alt="article.title + ' — imagen del artículo'" :title="article.title" loading="lazy">
          <p>{{ article.summary }}</p>
          <button @click.stop="goToDetail(article.link)" :title="'Leer ' + article.title">Leer +</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { useHead } from '@vueuse/head' // añadido
  
  const router = useRouter()
  
  const pageUrl = 'https://www.geobizi.com/blog'
  const ogImage = 'https://www.geobizi.com/imagenes/blog/patrimonio.avif' // representativa
  
  useHead({
    title: 'Blog — Artículos sobre naturaleza y medioambiente | Geobizi',
    meta: [
      { name: 'description', content: 'Artículos y recursos de Geobizi sobre medioambiente, biodiversidad, rutas y actividades educativas. Lee nuestros posts y aprende sobre naturaleza.' },
      { name: 'robots', content: 'index, follow' },
      { name: 'author', content: 'Geobizi' },
      { name: 'publisher', content: 'Geobizi' },
      { name: 'keywords', content: 'blog medioambiente, artículos naturaleza, Geobizi, biodiversidad, rutas' },
      { name: 'language', content: 'es' },
      { property: 'og:title', content: 'Blog — Artículos sobre naturaleza y medioambiente | Geobizi' },
      { property: 'og:description', content: 'Artículos y recursos de Geobizi sobre medioambiente, biodiversidad, rutas y actividades educativas.' },
      { property: 'og:type', content: 'website' },
      { property: 'og:url', content: pageUrl },
      { property: 'og:image', content: ogImage },
      { name: 'twitter:card', content: 'summary_large_image' },
      { name: 'twitter:image', content: ogImage },
    ],
    link: [
      { rel: 'canonical', href: pageUrl },
      { rel: 'image_src', href: ogImage }
    ],
    script: [
      {
        type: 'application/ld+json',
        children: JSON.stringify({
          "@context": "https://schema.org",
          "@graph": [
            {
              "@type": "Organization",
              "name": "Geobizi",
              "url": "https://www.geobizi.com",
              "logo": "https://www.geobizi.com/imagenes/GeobiziLogo.7ae1d6ce.png",
              "sameAs": [
                "https://www.facebook.com/geobizirik/",
                "https://www.instagram.com/geotxiki/",
                "https://www.youtube.com/channel/UCw-C_J0y-jKHp7Zx92lsKfg"
              ],
              "@id": "https://www.geobizi.com/#organization"
            },
            {
              "@type": "Blog",
              "url": pageUrl,
              "name": "Blog — Geobizi",
              "description": "Artículos y recursos de Geobizi sobre medioambiente, biodiversidad, rutas y actividades educativas.",
              "inLanguage": "es",
              "isPartOf": { "@id": "https://www.geobizi.com/#organization" },
              "image": { "@type": "ImageObject", "url": ogImage }
            }
          ]
        })
      }
    ]
  })
  
  const articles = ref([
    {
      title: 'Flysch Bizkaia: Geoturismo y Geología de la Costa Vasca',
      summary: 'Descubre el Flysch de Bizkaia con Geobizi. Rutas de geoturismo y divulgación geológica en la costa vasca. Aprende la historia de la Tierra en sus rocas.',
      link: 'blog/detalle-flysch-bizkaia',
      image: '/imagenes/blog/detalle/flyschbizkaia/flyschbizkaia.avif',
    },
        {
      title: 'Estramonio (Datura stramonium) en Azkorri: riesgos y precauciones',
      summary: 'He encontrado estramonio en Azkorri. Muchas familias y animales pasan por allí: conoce la planta, sus riesgos y por qué no debes tocarla.',
      link: 'blog/detalle-estramonio',
      image: '/imagenes/blog/detalle/estramonio3.avif',
    },
    {
      title: 'Free Tours: Definición, Funcionamiento y preguntas frecuentes',
      summary: 'Un Free Tour, también conocido como Tour Gratis, es un recorrido turístico guiado por los puntos más destacados de una ciudad...',
      link: 'blog/detalle-free-tours',
      image: '/imagenes/blog/free-tours.avif',
    },
    {
      title: 'Centranthus Ruber (Valeriana Roja): Una Belleza Invasora en los Jardines',
      summary: 'En los últimos años, la preocupación por la propagación de especies invasoras ha crecido considerablemente. Una de las plantas que ha comenzado a destacar en este sentido es el Centranthus ruber...',
      link: 'blog/detalle-valeriana-roja',
      image: '/imagenes/blog/valeriana-roja.avif',
    },
    {
      title: 'La formación de los estuarios: donde el mar y el río se encuentran',
      summary: 'Los estuarios son ecosistemas únicos y fascinantes que se forman en las desembocaduras de los ríos...',
      link: 'blog/detalle-estuarios',
      image: '/imagenes/blog/estuarios.avif',
    },
    {
      title: 'La Importancia de las mariquitas en el medioambiente',
      summary: 'Las mariquitas pertenecen a la familia de los escarabajos, y existen miles de especies diferentes en todo el mundo...',
      link: 'blog/detalle-mariquitas',
      image: '/imagenes/blog/mariquitas.avif',
    },
    {
      title: 'La Importancia de la Biodiversidad en Relación con el Cambio Climático',
      summary: 'La biodiversidad es la variedad de formas de vida en nuestro planeta, desde las más pequeñas bacterias hasta las majestuosas especies de mamíferos...',
      link: 'blog/detalle-biodiversidad',
      image: '/imagenes/blog/biodiversidad.avif',
    },
    {
      title: 'El Sapito Corredor o Buffo Calamita: Un Tesoro Ecológico en Peligro',
      summary: 'El sapito corredor, es una especie de sapo nativa de gran parte de Europa...',
      link: 'blog/detalle-sapito',
      image: '/imagenes/blog/sapito.avif',
    },

    {
      title: 'Carpobrotus edulis, invasora perjudicial',
      summary: 'La Carpobrotus edulis, una especie originaria de Sudáfrica que resulta ser invasora en muchas partes de nuestro planeta...',
      link: 'blog/detalle-carpobrotus',
      image: '/imagenes/blog/carpobrotus.avif',
    },
    {
      title: 'Flora autóctona: la importancia de cuidarla',
      summary: 'Para conservar la biodiversidad de nuestro planeta y el equilibrio de los ecosistemas, es esencial proteger la flora autóctona...',
      link: 'blog/detalle-flora-autoctona',
      image: '/imagenes/blog/flora-autoctona.avif',
    },
    {
      title: '¿Qué son los fósiles y cómo se forman?',
      summary: 'Los fósiles son restos o huellas de organismos que vivieron en la Tierra en el pasado...',
      link: 'blog/detalle-fosiles',
      image: '/imagenes/blog/fosiles.avif',
    },
    {
      title: 'Día mundial de la Tierra',
      summary: 'Este año 2023, el Día de la Tierra se celebra bajo el lema “Invertir en nuestro planeta”...',
      link: 'blog/detalle-dia-tierra',
      image: '/imagenes/blog/dia-tierra.avif',
    },
    {
      title: 'Jornadas de Patrimonio Europeo 2023',
      summary: 'Llega octubre y con él las Jornadas de Patrimonio Europeas. Una oportunidad única para disfrutar de un montón de actividades relacionadas con el patrimonio en diferentes puntos de la comunidad...',
      link: 'blog/detalle-patrimonio',
      image: '/imagenes/blog/patrimonio.avif',
    },
  ])
  
  const goToDetail = (link) => {
    router.push(link)
  }
  </script>
  
  <style scoped>
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
  
  .container {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    justify-content: center;
  }
  
  .card {
    width: 300px;
    padding: 20px;
    background-color: var(--megashoftgreen);
    border: 1px solid var(--shoftgreen);
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .card img {
    max-width: 100%;
    height: auto;
    border-radius: 4px;
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
    text-align: center;
  }
  
  .card button {
    margin-top: auto;
    margin-bottom: 0.5rem;
    padding: 10px 20px;
    border: none;
    border-radius: 0.5rem;
    background-color: var(--green);
    color: #fff;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .card button:hover {
    background-color: var(--lightgreen);
  }
  </style>
