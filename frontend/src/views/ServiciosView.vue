<template>
  <div class="general-container">
    <h1>Servicios de Divulgación y Educación Ambiental</h1>
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
  title: 'Servicios de Divulgación y Educación Ambiental | Geobizi',
  meta: [
    { name: 'description', content: 'Descubre nuestros servicios: rutas guiadas, talleres prácticos, consultoría educativa, proyectos digitales sostenibles y recursos didácticos a medida.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Servicios de Divulgación y Educación Ambiental | Geobizi' },
    { property: 'og:description', content: 'Rutas, talleres, consultoría educativa, proyectos digitales y recursos didácticos para colegios, empresas e instituciones.' },
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
            "@type": "WebPage",
            "url": pageUrl,
            "name": "Servicios de Divulgación y Educación Ambiental | Geobizi",
            "description": "Rutas guiadas, talleres ambientales, consultoría educativa, proyectos digitales sostenibles y recursos didácticos.",
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
    content: 'Rutas guiadas por la naturaleza, geología y botánica de Bizkaia. Experiencias cercanas y adaptadas a cada grupo.',
    link: '/detalle-rutas',
    image: '/imagenes/servicios/rutas/rutas.avif',
  },
  {
    title: 'Talleres y actividades',
    content: 'Talleres prácticos y educativos para colegios, eventos y proyectos locales. ¡Aprende experimentando!',
    link: '/detalle-actividades',
    image: '/imagenes/servicios/actividades/actividades.avif',
  },
  {
    title: 'Sensibilización y biorregeneración',
    content: 'Proyectos colaborativos para conectar personas y naturaleza mediante la restauración ambiental y la participación ciudadana.',
    link: '/detalle-sensibilizacion',
    image: '/imagenes/servicios/sensibilizacion/sensibilizacion.avif',
  },
  {
    title: 'Digital y sostenible',
    content: 'Yincanas digitales, recursos educativos online y desarrollo web eficiente con huella de carbono compensada.',
    link: '/detalle-digital',
    image: '/imagenes/servicios/digital/digital.avif',
  },
  {
    title: 'Formación y consultoría',
    content: 'Consultoría educativa (STEAM, DUA, Neurociencia) y formación técnica para centros, empresas y profesionales.',
    link: '/detalle-formacion',
    image: '/imagenes/servicios/formacion/formacion.avif',
  },
  {
    title: 'Recursos y descargas',
    content: 'Fichas didácticas, láminas imprimibles y guías de campo para apoyar el aprendizaje en cualquier entorno.',
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
