<template>
    <div class="general-container">
      <h1>Artículos del blog</h1>
      <p>Estos son nuestros artículos de blog escritos especialmente para ti.</p>
      <p>Elige sobre qué quieres leer o aprender. Medioambiente, biodiversidad, naturaleza, actividades, novedades de Geobizi, y mucho más para elegir.</p>
      <div class="container">
        <div class="card" v-for="article in articles" :key="article.title" @click="goToDetail(article.link)">
          <h2>{{ article.title }}</h2>
          <img :src="article.image" alt="Artículo del blog">
          <p>{{ article.summary }}</p>
          <button @click.stop="goToDetail(article.link)">Leer +</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  
  const articles = ref([
    {
      title: 'Jornadas de Patrimonio Europeo 2023',
      summary: 'Llega octubre y con él las Jornadas de Patrimonio Europeas. Una oportunidad única para disfrutar de un montón de actividades relacionadas con el patrimonio en diferentes puntos de la comunidad...',
      link: 'blog/detalle-patrimonio',
      image: '/imagenes/blog/patrimonio.png',
    },
    {
      title: 'Free Tours: Definición, Funcionamiento y preguntas frecuentes',
      summary: 'Un Free Tour, también conocido como Tour Gratis, es un recorrido turístico guiado por los puntos más destacados de una ciudad...',
      link: 'blog/detalle-free-tours',
      image: '/imagenes/blog/free-tours.png',
    },
    {
      title: 'Centranthus Ruber (Valeriana Roja): Una Belleza Invasora en los Jardines',
      summary: 'En los últimos años, la preocupación por la propagación de especies invasoras ha crecido considerablemente. Una de las plantas que ha comenzado a destacar en este sentido es el Centranthus ruber...',
      link: 'blog/detalle-valeriana-roja',
      image: '/imagenes/blog/valeriana-roja.png',
    },
    {
      title: 'La formación de los estuarios: donde el mar y el río se encuentran',
      summary: 'Los estuarios son ecosistemas únicos y fascinantes que se forman en las desembocaduras de los ríos...',
      link: 'blog/detalle-estuarios',
      image: '/imagenes/blog/estuarios.png',
    },
    {
      title: 'La Importancia de las mariquitas en el medioambiente',
      summary: 'Las mariquitas pertenecen a la familia de los escarabajos, y existen miles de especies diferentes en todo el mundo...',
      link: 'blog/detalle-mariquitas',
      image: '/imagenes/blog/mariquitas.png',
    },
    {
      title: 'La Importancia de la Biodiversidad en Relación con el Cambio Climático',
      summary: 'La biodiversidad es la variedad de formas de vida en nuestro planeta, desde las más pequeñas bacterias hasta las majestuosas especies de mamíferos...',
      link: 'blog/detalle-biodiversidad',
      image: '/imagenes/blog/biodiversidad.png',
    },
    {
      title: 'El Sapito Corredor o Buffo Calamita: Un Tesoro Ecológico en Peligro',
      summary: 'El sapito corredor, es una especie de sapo nativa de gran parte de Europa...',
      link: 'blog/detalle-sapito',
      image: '/imagenes/blog/sapito.png',
    },
    {
      title: 'Carpobrotus edulis, invasora perjudicial',
      summary: 'La Carpobrotus edulis, una especie originaria de Sudáfrica que resulta ser invasora en muchas partes de nuestro planeta...',
      link: 'blog/detalle-carpobrotus',
      image: '/imagenes/blog/carpobrotus.png',
    },
    {
      title: 'Flora autóctona: la importancia de cuidarla',
      summary: 'Para conservar la biodiversidad de nuestro planeta y el equilibrio de los ecosistemas, es esencial proteger la flora autóctona...',
      link: 'blog/detalle-flora-autoctona',
      image: '/imagenes/blog/flora-autoctona.png',
    },
    {
      title: '¿Qué son los fósiles y cómo se forman?',
      summary: 'Los fósiles son restos o huellas de organismos que vivieron en la Tierra en el pasado...',
      link: 'blog/detalle-fosiles',
      image: '/imagenes/blog/fosiles.png',
    },
    {
      title: 'Día mundial de la Tierra',
      summary: 'Este año 2023, el Día de la Tierra se celebra bajo el lema “Invertir en nuestro planeta”...',
      link: 'blog/detalle-dia-tierra',
      image: '/imagenes/blog/dia-tierra.png',
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
  