<template>
    <div class="contenedor-principal">
      <Calendario />
      <div class="leyendaContenedor">
        <h1>Calendario de actividades programadas de Geobizi</h1>
        <h3>Leyenda</h3>
        <div class="leyenda">
        <div class="leyenda-item">
          <span class="punto leyenda-punto" style="background-color: orange;"></span>
          <span>Azkorri al microscopio</span>
        </div>
        <div class="leyenda-item">
          <span class="punto leyenda-punto" style="background-color: green;"></span>
          <span>Árboles de Getxo</span>
        </div>
        <div class="leyenda-item">
          <span class="punto leyenda-punto" style="background-color: blue;"></span>
          <span>Actividad de Zalla Natura</span>
        </div>
        <div class="leyenda-item">
          <span class="punto leyenda-punto" style="background-color: purple;"></span>
          <span>Otras actividades</span>
        </div>
      </div>

      <div class="definicionActividad">


        <h2>Azkorri al microscopio</h2>
        <h3>Ruta Medioambiental por la Costa de Getxo: Descubre la Naturaleza y su Historia</h3>
        <p>¡Bienvenidos a una fascinante ruta medioambiental por la costa de Getxo!</p>
        <p>Os invitamos a un recorrido educativo y entretenido donde podréis conocer de cerca la flora y fauna de la región, y aprender sobre la geología y el impacto de los humanos en el entorno. Esta actividad es perfecta para toda la familia y está diseñada tanto para adultos, como para familias con niños y niñas a partir de 4 años.</p>
        <h3>¿Qué exploraremos?</h3>
        <ul>
          <li>
            Flora Costera: Observaremos y aprenderemos a identificar las plantas autóctonas e invasoras de la costa, utilizando microscopios para descubrir sus detalles más diminutos.
          </li>
          <li>
            Geología Asombrosa: Conoceremos el "clavo de oro" y su importancia, exploraremos el flysch de Bizkaia y, si tenemos suerte, encontraremos algún fósil que nos conecte con el pasado remoto de la Tierra.
          </li>
          <li>
            Fauna Característica: Identificaremos los animales más representativos de la zona y hablaremos de sus hábitats y comportamientos.
          </li>
          <li>
            Entornos de Protección: Visitaremos áreas protegidas como la del sapito corredor, la zona trasdunar y los brezales costeros, entendiendo su importancia para el ecosistema.
          </li>
          <li>
            Impacto Humano y Antropoceno: Reflexionaremos sobre el impacto de las actividades humanas en el entorno natural y cómo podemos contribuir a su conservación.
          </li>
        </ul>
        <p>Al finalizar la ruta, los pequeños exploradores recibirán un detalle como recuerdo de esta maravillosa experiencia.</p>
        <p>¡No os perdáis esta oportunidad de conectar con la naturaleza y aprender en familia en la impresionante costa de Getxo!</p>
        <p>Es una actividad parcialmente subvencionada por el ayuntamiento de Getxo.</p>




      <h2>Árboles de Getxo</h2>
        <h3>Descubre los árboles de Getxo en Familia: Una Aventura Natural</h3>
        <p>¡Bienvenidas familias exploradoras!</p>
        <p>Os invitamos a una experiencia única en la naturaleza, donde podréis aprender a identificar árboles y descubrir sus secretos sin causarles daño. Nuestro paseo educativo está diseñado tanto para adultos,como para familias con niños y niñas a partir de 4 años, y es una oportunidad perfecta para que toda la familia disfrute y aprenda junta.</p>
        <h3>¿Qué haremos?</h3>
        <ul>
          <li>
            Identificación de Árboles: Aprenderemos a reconocer distintas especies de árboles observando sus hojas, cortezas y flores.          </li>
          <li>
            Edad de los Árboles: Sin necesidad de cortar ni dañar el árbol, os enseñaremos técnicas para estimar su edad.          </li>
          <li>
            Microscopio Natural: Observaremos elementos naturales del entorno como troncos, hojas, flores y líquenes a través del microscopio, descubriendo un mundo nuevo y fascinante a pequeña escala.
          </li>
        </ul>
        <p>Al final de la actividad, todos los pequeños y pequeñas exploradores recibirán un detalle como recuerdo de esta maravillosa experiencia.</p>
        <p>¡No os perdáis esta oportunidad de conectar con la naturaleza y aprender en familia!</p>
        <p>Espero que te sirva de inspiración para tu actividad. ¡Que disfrutes mucho la ruta!</p>
        <p>Es una actividad parcialmente subvencionada por el ayuntamiento de Getxo.</p>



        
      </div>

      </div>
    </div>
</template>

<script setup>
import Calendario from '@/components/calendario/CalendarioActividades2025.vue'
import { useHead } from '@vueuse/head' // añadido

const pageUrl = 'https://www.geobizi.com/calendario'
const ogImage = 'https://www.geobizi.com/imagenes/proyectos/zallanatura/zallanatura2.avif'

useHead({
  title: 'Calendario de Actividades | Geobizi',
  meta: [
    { name: 'description', content: 'Consulta el calendario de Geobizi: rutas, talleres y actividades familiares y educativas. Reserva plazas y revisa fechas, horarios y ubicaciones.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'publisher', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Calendario de Actividades | Geobizi' },
    { property: 'og:description', content: 'Consulta el calendario de Geobizi: rutas, talleres y actividades familiares y educativas. Reserva plazas y revisa fechas, horarios y ubicaciones.' },
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
            "name": "Calendario de Actividades | Geobizi",
            "description": "Consulta el calendario de Geobizi: rutas, talleres y actividades familiares y educativas. Reserva plazas y revisa fechas, horarios y ubicaciones.",
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
  .contenedor-principal {
    padding-top: 7rem;
    background-color: rgb(255, 255, 255);
    padding-bottom: 2rem;
  }

  .leyendaContenedor {
    margin-left: 3rem;
  }
  .leyenda {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin: 2rem;
}

.leyenda-item {
  display: flex;
  align-items: center;
  gap: 10px;
}

.punto {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  display: inline-block;
}
  
@media (min-width: 950px) {
  .contenedor-principal {
    max-width: 1200px;
    margin: 0 auto; /* Centra el contenido */
  }
}
</style>