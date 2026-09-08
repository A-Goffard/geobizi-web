<template>
  <div class="general-container">
    <h1>Experiencia y Trayectoria</h1>
    <p class="intro-texto">
      A lo largo de los años, en Geobizi hemos colaborado mano a mano con ayuntamientos, centros educativos y grandes eventos, además de desarrollar iniciativas propias de divulgación científica y ambiental. Aquí puedes ver una muestra de nuestro recorrido.
    </p>

    <!-- BLOQUE 1: COLABORACIONES INSTITUCIONALES -->
    <section class="seccion-experiencia">
      <h2>Colaboraciones Institucionales</h2>
      <p class="sub-seccion-desc">Proyectos estratégicos y de continuidad con administraciones públicas:</p>
      
      <div class="container">
        <div class="card" v-for="item in institucionales" :key="item.title" @click="goToDetail(item.link)">
          <h2>{{ item.title }}</h2>
          <img :src="item.image" :alt="item.title + ' — imagen del proyecto'" :title="item.title" loading="lazy">
          <p>{{ item.description }}</p>
        </div>
      </div>
    </section>

    <!-- BLOQUE 2: FESTIVALES Y FERIAS -->
    <section class="seccion-experiencia">
      <h2>Festivales y Grandes Eventos</h2>
      <p class="sub-seccion-desc">Dinámicas, talleres y rutas en grandes citas culturales y ambientales:</p>
      
      <div class="container">
        <div class="card" v-for="item in eventos" :key="item.title" @click="goToDetail(item.link)">
          <h2>{{ item.title }}</h2>
          <img :src="item.image" :alt="item.title + ' — imagen del evento'" :title="item.title" loading="lazy">
          <p>{{ item.description }}</p>
        </div>
      </div>
    </section>

    <!-- BLOQUE 3: LÍNEAS PROPIAS / ITINERARIOS -->
    <section class="seccion-experiencia">
      <h2>Líneas Propias e Itinerarios</h2>
      <p class="sub-seccion-desc">Nuestros propios programas de divulgación geológica y ambiental:</p>
      
      <div class="container">
        <div class="card" v-for="item in propias" :key="item.title" @click="goToDetail(item.link)">
          <h2>{{ item.title }}</h2>
          <img :src="item.image" :alt="item.title + ' — imagen del proyecto'" :title="item.title" loading="lazy">
          <p>{{ item.description }}</p>
        </div>
      </div>
    </section>

    <!-- BLOQUE 4: GEOBIZI EN LOS MEDIOS -->
    <section class="seccion-experiencia medios-section">
      <h2>Geobizi en los Medios</h2>
      <p class="sub-seccion-desc">Cuando la radio, la prensa y la televisión se hacen eco de nuestro trabajo:</p>
      
      <div class="medios-grid">
        <div class="medio-card">
          <h3>📻 Entrevista en Radio</h3>
          <p>Conversamos sobre la historia geológica de nuestro planeta desde el punto de vista de nuestra ruta en el Flysch de Bizkaia en Getxo.</p>
          <a href="https://cadenaser.com/emisora/2020/08/28/radio_san_sebastian/1598613055_684629.html" target="_blank" class="btn-medio">Escuchar entrevista</a>
        </div>

        <div class="medio-card">
          <h3>📰 El Correo</h3>
          <p>Aparición en prensa escrita destacando iniciativas locales de sensibilización, conocimiento, protección del entorno y nuestras actividades.</p>
          <a href="https://www.elcorreo.com/planes/playa-descubrir-secretos-arenales-populares-20260807185045-nt.html?ref=https%3A%2F%2Fwww.elcorreo.com%2Fplanes%2Fplaya-descubrir-secretos-arenales-populares-20260807185045-nt.html" target="_blank" class="btn-medio">Leer noticia</a>
        </div>

        <div class="medio-card">
          <h3>📺 Minirreportaje en ETB</h3>
          <p>Reportaje en televisión mostrando sobre el terreno una de nuestras rutas geológicas sobre el Flysch de Bizkaia en Sopela.</p>
          <a href="https://www.eitb.eus/eu/telebista/programak/sukalerrian/bideoak/osoa/8955046/bideoa-sopelako-flyscharen-ingurua-ezagutu-dugu-geotxiki-enpresako-aintzaneren-eskutik/" class="btn-medio">Ver reportaje</a>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useHead } from '@vueuse/head'

const router = useRouter()

const pageUrl = 'https://www.geobizi.com/experiencia'
const ogImage = 'https://www.geobizi.com/imagenes/proyectos/proyectos-hero.avif'

useHead({
  title: 'Experiencia y Trayectoria | Geobizi',
  meta: [
    { name: 'description', content: 'Experiencia de Geobizi: colaboraciones institucionales con ayuntamientos, participación en grandes festivales, itinerarios propios y presencia en medios.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Experiencia y Trayectoria | Geobizi' },
    { property: 'og:description', content: 'Colaboraciones con instituciones, festivales y proyectos de educación ambiental realizados por Geobizi.' },
    { property: 'og:type', content: 'website' },
    { property: 'og:url', content: pageUrl },
    { property: 'og:image', content: ogImage }
  ],
  link: [
    { rel: 'canonical', href: pageUrl },
    { rel: 'image_src', href: ogImage },
    { rel: 'apple-touch-icon', href: '/apple-touch-icon.png', sizes: '180x180' }
  ]
})

// Categoría 1: Colaboraciones Institucionales
const institucionales = ref([
  {
    title: 'Zalla Natura',
    description: 'Un proyecto de biorregeneración colaborativa para mejorar el medioambiente en Zalla junto al Ayuntamiento y centros educativos.',
    link: '/detalle-zalla-natura',
    image: '/imagenes/proyectos/zallanatura/zallanatura.avif',
  }
])

// Categoría 2: Festivales y Ferias
const eventos = ref([
  {
    title: 'Semana Verde (Aste Berdea)',
    description: 'Actividades para el Ayuntamiento de Getxo: talleres medioambientales, rutas geológicas, hoteles de insectos y limpiezas de playa.',
    link: '/detalle-aste-berdea',
    image: '/imagenes/proyectos/asteberdea/semanaverde.avif',
  },
  {
    title: 'Sopela Kosta Fest',
    description: 'Talleres, rutas de fósiles, yincana digital y actividades familiares en la costa de Sopela.',
    link: '/detalle-sopela-kosta-fest',
    image: '/imagenes/proyectos/sopelakostafest/sopelakostafest.avif',
  }
])

// Categoría 3: Líneas Propias
const propias = ref([
  {
    title: 'Proyecto Integral: Flysch de Bizkaia',
    description: 'Divulgación geológica a través de rutas guiadas, yincanas digitales interactivas y material didáctico abierto.',
    link: '/detalle-flysch',
    image: '/imagenes/proyectos/flyschdigital/flyschdigital.avif',
  }
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
  padding-bottom: 4rem;
}

.intro-texto {
  font-size: 1.1rem;
  color: var(--darkgrey);
  margin-bottom: 2rem;
  line-height: 1.6;
}

.seccion-experiencia {
  margin-bottom: 3rem;
}

.seccion-experiencia h2 {
  font-size: 1.5rem;
  color: var(--green);
  border-bottom: 2px solid var(--shoftgreen);
  padding-bottom: 0.5rem;
  margin-bottom: 0.5rem;
}

.sub-seccion-desc {
  color: #666;
  font-size: 0.95rem;
  margin-bottom: 1.5rem;
}

.container {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: flex-start;
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

/* Estilos para la sección de medios */
.medios-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.medio-card {
  background-color: #f9fdfb;
  border: 1px solid var(--shoftgreen);
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.medio-card h3 {
  margin-top: 0;
  color: var(--green);
  font-size: 1.1rem;
}

.medio-card p {
  font-size: 0.9rem;
  color: var(--darkgrey);
  margin-bottom: 1rem;
}

@media (max-width: 613px) {
  .card {
    width: 100%;
  }
}
</style>