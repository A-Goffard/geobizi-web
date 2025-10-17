<template>
  <div class="contenedor-principal">
    <h1>Rutas divulgativas</h1>
    <p>Hacemos rutas guiadas interpretativas relacionadas con la naturaleza,adaptadas a intereses y niveles: geológicas , medioambientales y temáticas.</p>
    <p>Adaptamos la longitud, el lenguaje y las actividades según el colectivo.</p>
    <p>Diseñamos rutas personalizadas a medida.</p>
    <p>También tenemos rutas ya diseñadas y estandarizadas.</p>

    <h2>Rutas estandarizadas y ejemplos</h2>
    <p>Estas son algunas de las rutas que ofrecemos. Si tienes alguna idea o interés especial, podemos diseñar una ruta a tu medida.</p>
    
    <h4>Flysch de Sopela</h4>
    <p>Ruta interpretativa por el Flysch de Sopela, para que descubras los secretos geológicos de esta zona única.</p>

    <h4>Ruta medioambiental en Azkorri</h4>
    <p>Ruta interpretativa por el entorno natural de Azkorri, para conocer su flora, fauna y ecosistemas.</p>

    <h4>Identificación de árboles</h4>
    <p>Ruta para aprender a identificar los árboles más comunes de nuestro entorno y sus características.</p>

    <h4>Plantas medicinales</h4>
    <p>Ruta para conocer las plantas medicinales de nuestro entorno y sus usos tradicionales.</p>

    <h4>Limpieza de playas</h4>
    <p>Ruta de voluntariado para la limpieza de playas y concienciación medioambiental.</p>
    
    <h4>Ruta nocturna</h4>
    <p>Ruta nocturna para observar la naturaleza desde una perspectiva diferente, descubriendo la fauna nocturna y los sonidos de la noche.</p>

    <h2>Qué incluyen</h2>
    <p>Guía</p>
    <p>Material didáctico y actividades participativas</p>
    <p>Itinerarios personalizados por edad, idioma y objetivos</p>

    <h2>Recomendaciones de seguridad</h2>
    <p> Usa calzado y ropa adecuados, agua y protección solar. </p>
    <p>Tened en cuenta las recomendaciones específicas para cada tipo de ruta.</p> 
    <p>Escuchad al guía.</p>

    <h2>Se realizan para</h2>
    <p>Centros escolares, asociaciones, empresas, ayuntamientos y público general.</p>

    <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/servicios/rutas/ruta1.avif"
          alt="Ruta Flysch en Sopela — personas observando formaciones geológicas"
          title="Ruta Flysch en Sopela — imagen 1"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/servicios/rutas/ruta2.avif"
          alt="Personas identificando anfibios en un entorno natural"
          title="Ruta medioambiental en Azkorri — imagen 2"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/servicios/rutas/ruta3.avif"
          alt="Ruta escolar por Azkorri"
          title="Ruta escolar por Azkorri — imagen 3"
          loading="lazy"
        />
      </div>
    </div>
</div>

</template>

<script setup>
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/servicios/rutas'
const ogImage = 'https://www.geobizi.com/imagenes/servicios/detalle/sopela.avif'

useHead({
  title: 'Rutas guiadas | GeoBizi',
  meta: [
    { name: 'description', content: 'Rutas guiadas geológicas, medioambientales y temáticas para colegios, asociaciones, empresas y público general. Itinerarios adaptados.' },
    { property: 'og:title', content: 'Rutas guiadas | GeoBizi' },
    { property: 'og:description', content: 'Rutas interpretativas (Flysch, naturaleza y temáticas) adaptadas por edad y objetivos.' },
    { property: 'og:url', content: pageUrl },
    { property: 'og:image', content: ogImage }
  ],
  link: [{ rel: 'canonical', href: pageUrl }]
})
</script>

<style scoped>
</style>