<template>
    <div class="general-container">
      <h1>Servicios</h1>
      <div class="container">
        <div class="card" v-for="section in sections" :key="section.title" @click="goToDetail(section.link)">
          <h2>{{ section.title }}</h2>
          <img :src="section.image" :alt="section.title" :title="section.title" loading="lazy">
          <p>{{ section.content }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useHead } from '@vueuse/head'
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  
  const pageUrl = 'https://www.geobizi.com/servicios'
  const ogImage = 'https://www.geobizi.com/imagenes/servicios/servicios-hero.avif'
  
  useHead({
    title: 'Servicios | Geobizi',
    meta: [
      { name: 'description', content: 'Servicios de Geobizi: rutas, talleres, formaciones y proyectos medioambientales para colegios, empresas e instituciones.' },
      { name: 'robots', content: 'index, follow' },
      { name: 'author', content: 'Geobizi' },
      { name: 'theme-color', content: '#0b8a4c' },
      { name: 'language', content: 'es' },
      { property: 'og:title', content: 'Servicios | Geobizi' },
      { property: 'og:description', content: 'Rutas, talleres, formaciones y proyectos medioambientales para colegios, empresas e instituciones.' },
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
              "name": "Servicios | Geobizi",
              "description": "Rutas, talleres y proyectos medioambientales para colegios, empresas e instituciones.",
              "inLanguage": "es",
              "isPartOf": { "@id": "https://www.geobizi.com/#organization" },
              "image": { "@type": "ImageObject", "url": ogImage, "width": 1080, "height": 1080 }
            }
          ]
        })
      }
    ]
  })
  
  const router = useRouter()
  
  const sections = ref([
   {
      title: 'Rutas divulgativas',
      content: 'Rutas geológicas, medioambientales, limpiezas de playas, interpretación de la fauna y flora... Tenemos algunas ya preparadas y otras las diseñamos a tu medida.',
      link: '/detalle-rutas',
      image: '/imagenes/servicios/rutas/rutas.avif',
    },
    {
      title: 'Talleres y actividades',
      content: 'Si lo necesitas, preparamos una actividad o taller para un evento, una feria etc., para realizar en el campo o en tu local. Para trabajar en grupo y forjar vínculos, para aprender, para entretener.',
      link: '/detalle-actividades',
      image: '/imagenes/servicios/actividades/actividades.avif',
    },
    {
      title: 'Proyectos de sensibilización y biorregeneración',
      content: 'Diseñamos proyectos de sensibilización ambiental y biorregeneración para colegios, asociaciones, empresas e instituciones. ¿Quieres poner en valor el medio natural de tu entorno?',
      link: '/detalle-sensibilizacion',
      image: '/imagenes/servicios/sensibilizacion/sensibilizacion.avif',
    },
    {
      title: 'Digital y sostenible',
      content: 'El mundo digital y el natural pueden estar unidos y por ese camino ofrecemos yincanas digitales, creación y mantenimiento de páginas web con compensación de carbono y material didáctico digital relacionado con la naturaleza y el medioambiente.',
      link: '/detalle-digital',
      image: '/imagenes/servicios/digital/digital.avif',
    },
    {
      title: 'Formación',
      content: 'También ofrecemos formaciones para empresas, instituciones o centros formativos. Medioambiente, sostenibilidad, educación ambiental, comunicación, herramientas digitales, IA, gamificación...',
      link: '/detalle-formacion',
      image: '/imagenes/servicios/formacion/formacion.avif',
    },
    {
      title: 'Descargas y recursos',
      content: 'Material digital didáctico o lúdico relacionado con la naturaleza y el medioambiente para descargar. Recursos para docentes, fichas de actividades, juegos educativos...',
      link: '/detalle-descargas',
      image: '/imagenes/servicios/descargas/descargas.avif',
    }
  ])
  
  const goToDetail = (link) => {
    router.push(link)
  }

  
  </script>
  
  <style scoped>
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
  }
  </style>
