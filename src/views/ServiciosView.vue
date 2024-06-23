<template>
    <div class="general-container">
      <h1>Servicios</h1>
      <div class="container">
        <div class="card" v-for="section in sections" :key="section.title" @click="goToDetail(section.link)">
          <h2>{{ section.title }}</h2>
          <img :src="section.image" alt="Servicios Geobizi">
          <p>{{ section.content }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  
  const sections = ref([
    {
      title: 'Para colegios y centros de enseñanza',
      content: 'Rutas geológicas, medioambientales, talleres, actividades mixtas, proyectos medioambientales para el colegios...',
      link: '/detalle-colegios',
      image: '/imagenes/servicios/coles.png',
    },
    {
      title: 'Asociaciones y empresas',
      content: 'Si lo necesitas, te preparamos una actividad temática en el campo o en tu local. Para trabajar los grupos y forjar vínculos, para aprender, para entretener.',
      link: '/detalle-asociaciones',
      image: '/imagenes/servicios/asociaciones.png',
    },
    {
      title: 'Instituciones',
      content: 'Si perteneces a un ayuntamiento, o cualquier otro tipo de institución, también tenemos algo para ti. ¿Quieres poner en valor el medio natural de tu entorno?¿Quieres una formación para tus ciudadanos o empresas?',
      link: '/detalle-instituciones',
      image: '/imagenes/servicios/ayuntas.png',
    },
    {
      title: 'Para familias',
      content: 'Si te gusta hacer cosas en familia, no te pierdas las actividades que tenemos programadas. También puedes juntarte con otras familias y pedir una actividad para todos.',
      link: '/detalle-familias',
      image: '/imagenes/servicios/familias.png',
    },
    {
      title: 'Para mayores',
      content: '¿Que si hacemos actividades para los más experimentados de la vida? Por supuesto que sí. Un taller, una ruta, un día de actividades. ¿Qué te apetece más?',
      link: '/detalle-mayores',
      image: '/imagenes/servicios/mayores.png',
    },
    {
      title: 'Población general',
      content: 'Siempre tenemos disponibles rutas y talleres para la población general. ¿Quieres contratar una ruta o un taller? Cuéntanos lo que quieres.',
      link: '/detalle-general',
      image: '/imagenes/servicios/general.png',
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
    border: 1px solid var(--ligthgrey);
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
  