<template>
  <div class="general-container">
    <h1>Proyectos</h1>
          <p>Estos son algunos de nuestros proyectos:</p>
    <div class="container">
      <div class="card" v-for="project in projects" :key="project.title" @click="goToDetail(project.link)">
        <h2>{{ project.title }}</h2>
        <img :src="project.image" :alt="project.title + ' — imagen del proyecto'" :title="project.title" loading="lazy">
        <p>{{ project.description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useHead } from '@vueuse/head' // añadido

const router = useRouter()

const pageUrl = 'https://www.geobizi.com/projectos'
const ogImage = 'https://www.geobizi.com/imagenes/proyectos/projectos-hero.avif'

useHead({
  title: 'Proyectos | GeoBizi',
  meta: [
    { name: 'description', content: 'Proyectos de GeoBizi: restauración, educación ambiental y colaboraciones con instituciones.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'GeoBizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Proyectos | GeoBizi' },
    { property: 'og:description', content: 'Proyectos de restauración y educación ambiental realizados por GeoBizi.' },
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
        "@context":"https://schema.org",
        "@graph":[
          {
            "@type":"Organization",
            "@id":"https://www.geobizi.com/#organization",
            "name":"GeoBizi",
            "url":"https://www.geobizi.com",
            "logo": { "@type":"ImageObject","url":"https://www.geobizi.com/imagenes/GeobiziLogo.7ae1d6ce.png","width":1417,"height":313 },
            "sameAs":[
              "https://www.facebook.com/geobizirik/",
              "https://www.instagram.com/geotxiki/",
              "https://www.youtube.com/channel/UCw-C_J0y-jKHp7Zx92lsKfg"
            ]
          },
          {
            "@type":"WebPage",
            "url": pageUrl,
            "name":"Proyectos | GeoBizi",
            "description":"Proyectos de restauración y educación ambiental realizados por GeoBizi.",
            "inLanguage":"es",
            "isPartOf": { "@id": "https://www.geobizi.com/#organization" },
            "image": { "@type":"ImageObject","url":ogImage,"width":1080,"height":1080 }
          }
        ]
      })
    }
  ]
})

const projects = ref([
    {
    title: 'Zalla Natura',
    description: 'Un proyecto de biorregeneración colaborativa para mejorar el medioambiente en Zalla.',
    link: '/detalle-zalla-natura',
    image: '/imagenes/proyectos/zallanatura/zallanatura.avif',
  },
  {
    title: 'Ginkana del Flysch de Bizkaia',
    description: 'Una experiencia digital para explorar el Flysch de Bizkaia de manera interactiva.',
    link: '/detalle-flysch',
    image: '/imagenes/proyectos/flyschdigital/flyschdigital.avif',
  },
  {
    title: 'Semana Verde',
    description: 'Actividades de Aste Berdea: talleres medioambientales, rutas geológicas, hoteles de insectos y limpiezas de playa.',
    link: '/detalle-aste-berdea',
    image: '/imagenes/proyectos/asteberdea/semanaverde.avif',
  },
  {
    title: 'Sopela Kosta Fest',
    description: 'Talleres, rutas de fósiles, ginkana digital y actividades familiares en la costa de Sopela.',
    link: '/detalle-sopela-kosta-fest',
    image: '/imagenes/proyectos/sopelakostafest/sopelakostafest.avif',
  },
  {
    title: 'Día del Árbol',
    description: 'Talleres de bombas de semillas, identificación de árboles, limpiezas y actividades educativas para el Día del Árbol.',
    link: '/detalle-dia-arbol',
    image: '/imagenes/proyectos/diadelarbol/diadelarbol.avif',
  },
  {
    title: 'Semana de la Ciencia',
    description: 'Talleres, rutas y actividades educativas para acercar la ciencia y el medio ambiente a todos los públicos.',
    link: '/detalle-semana-ciencia',
    image: '/imagenes/proyectos/zientziaastea/semanaciencia.avif',
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
