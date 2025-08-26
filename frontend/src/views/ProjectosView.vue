<template>
  <div class="general-container">
    <h1>Proyectos</h1>
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
const ogImage = 'https://www.geobizi.com/imagenes/proyectos/plantacion4.avif' // imagen representativa

useHead({
  title: 'Proyectos Ambientales y Digitales | GeoBizi',
  meta: [
    { name: 'description', content: 'Proyectos de GeoBizi: experiencias digitales, biorregeneración y acciones comunitarias para mejorar el medioambiente. Conoce nuestros proyectos y participa.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'GeoBizi' },
    { name: 'publisher', content: 'GeoBizi' },
    { name: 'keywords', content: 'proyectos medioambientales, biorregeneración, experiencias digitales, GeoBizi' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Proyectos Ambientales y Digitales | GeoBizi' },
    { property: 'og:description', content: 'Proyectos de GeoBizi: experiencias digitales, biorregeneración y acciones comunitarias para mejorar el medioambiente.' },
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
            "name": "GeoBizi",
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
            "@type": "WebPage",
            "url": pageUrl,
            "name": "Proyectos Ambientales y Digitales | GeoBizi",
            "description": "Proyectos de GeoBizi: experiencias digitales, biorregeneración y acciones comunitarias para mejorar el medioambiente.",
            "inLanguage": "es",
            "isPartOf": { "@id": "https://www.geobizi.com/#organization" },
            "image": { "@type": "ImageObject", "url": ogImage }
          }
        ]
      })
    }
  ]
})

const projects = ref([
  {
    title: 'Ginkana del Flysch de Bizkaia',
    description: 'Una experiencia digital para explorar el Flysch de Bizkaia de manera interactiva.',
    link: '/detalle-flysch',
    image: '/imagenes/proyectos/flyschdigital.avif',
  },
  {
    title: 'Zalla Natura',
    description: 'Un proyecto de biorregeneración colaborativa para mejorar el medioambiente en Zalla.',
    link: '/detalle-zalla-natura',
    image: '/imagenes/proyectos/plantacion4.avif',
  },
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
