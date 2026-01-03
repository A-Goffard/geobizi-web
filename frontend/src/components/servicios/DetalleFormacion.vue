<template>
  <div class="contenedor-principal">
    <h1>Formación y asesoramiento</h1>
    <p>Ofrecemos formaciones y asesoramiento en diversas áreas relacionadas con el medio ambiente, la sostenibilidad y otros ámbitos transversales.</p>
    <p>Tanto para empresas como para instituciones, adaptamos nuestros programas a las necesidades específicas de cada cliente.</p>
    <p>También ofrecemos formaciones para centros formativos.</p>

    <h2>Áreas de formación</h2>

    <ul>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Sensibilización medioambiental y participación ciudadana.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Sostenibilidad.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Comunicación efectiva.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Divulgación.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Didáctica de la ciencia.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Diseño de actividades.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Ecoturismo.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Técnicas de ocio y tiempo libre.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Gestión de equipos.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Diseño de espacios verdes.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Regeneración y seguimiento de proyectos.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Formación para docentes y monitores.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Técnicas de educación ambiental.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Metodologías activas de enseñanza.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Proyectos educativos.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Uso de la IA en la educación.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Herramientas digitales en la educación.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Gamificación.</li>
      <li><img src="imagenes/iconos/color/mariposita.png" alt="Mariposita" title="Mariposita" class="icono" loading="lazy" />Otras áreas relacionadas con el medio ambiente, la sostenibilidad y la educación.</li>
    </ul>

    <h2>Se realizan para</h2>
    <p>Ofrecemos formación para administraciones, colegios, asociaciones, empresas y centros de formación.</p>
        <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/servicios/formacion/formacion1.avif"
          alt="Ruta Flysch en Sopela — personas observando formaciones geológicas"
          title="Ruta Flysch en Sopela — imagen 1"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/servicios/formacion/formacion2.avif"
          alt="Personas identificando anfibios en un entorno natural"
          title="Ruta medioambiental en Azkorri — imagen 2"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/servicios/formacion/formacion3.avif"
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
const pageUrl = 'https://www.geobizi.com/servicios/formacion'
useHead({
  title: 'Formación | Geobizi',
  meta: [{ name: 'description', content: 'Formación en sensibilización ambiental, regeneración, gestión de espacios y formación para docentes y técnicos.' }],
  link: [{ rel: 'canonical', href: pageUrl }]
})
</script>

<style scoped>

.contenido-seccion ul {
  flex: 1;
  min-width: 220px;
  margin: 0;
  padding-left: 1.2rem;
}

.contenido-seccion > img {
  align-self: center;
}

.icono {
  width: 20px;
  height: 20px;
  margin-right: 8px;
  margin-bottom: 8px;
  vertical-align: middle;
}
</style>