<template>
  <div class="contenedor-principal">
    <h1>Actividades y Talleres para Aprender Disfrutando</h1>
    
    <p>En Geobizi nos encanta diseñar experiencias donde el aprendizaje y la diversión van de la mano. No hay dos grupos iguales, por eso adaptamos nuestros talleres y actividades a las edades, los intereses y los objetivos de cada persona que participa.</p>

    <!-- BLOQUE DE MODALIDADES DE TRABAJO -->
    <section class="modalidades-trabajo">
      <h2>¿Cómo organizamos nuestras actividades?</h2>
      <p>Nos adaptamos a lo que necesites, ya sea en euskera o castellano, y ajustamos el contenido para que encaje como un guante en vuestro proyecto o evento:</p>

      <div class="bloques-gestion">
        <div class="bloque-modalidad">
          <h3>Para Colegios e Institutos</h3>
          <p>Llevamos la naturaleza al aula y el aula a la naturaleza. Diseñamos talleres prácticos que encajan con lo que se trabaja en clase (Primaria, Secundaria o Bachillerato), haciendo que los conceptos de ciencia o medioambiente se entiendan mucho mejor tocando y experimentando.</p>
          <p>¿Quieres que preparemos un taller para tu centro educativo? ¿Prefieres un proyecto completo?</p>
          <router-link to="/contacto?servicio=talleres_colegios" class="btn-servicio">Preguntar sobre este servicio</router-link>
        </div>

        <div class="bloque-modalidad">
          <h3>Proyectos para Municipios y Entidades</h3>
          <p>Si buscas darle vida a un espacio natural o concienciar sobre el entorno, te ayudamos a crear estrategias completas. Nos gusta trabajar uniendo lo que se aprende en los talleres con actividades en el campo donde todos puedan participar.</p>
          <p>¿Quieres un proyecto para tu municipio o entidad? ¡Cuentanos!</p>
          <router-link to="/contacto?servicio=talleres_municipios" class="btn-servicio">Consulta qué podemos hacer</router-link>
        </div>

        <div class="bloque-modalidad">
          <h3>Talleres para Eventos y Ferias</h3>
          <p>¿Tienes un stand, una feria de flores o un evento de empresa? Preparamos dinámicas rápidas, visuales y muy participativas. El objetivo es que la gente se lo pase bien mientras descubre algo nuevo y se lleva un recuerdo especial.</p>
          <p>¿Quieres un taller para tu evento? ¿Uno para peques? ¿Una actividad para adultos? ¡Cuentanos!</p>
          <router-link to="/contacto?servicio=talleres_ferias" class="btn-servicio">Preguntar sin compromiso</router-link>
        </div>
      </div>
    </section>

    <hr class="separador-seccion" />

    <!-- CATÁLOGO -->
    <section class="catalogo-especialidades">
      <h2>Nuestro Catálogo de Talleres</h2>
      <p>Son muchas las propuestas que tenemos, pero siempre estamos abiertos a nuevas ideas. Aquí tienes lo que más solemos trabajar:</p>

      <h3>Creatividad con Naturaleza</h3>
      <ul>
        <li>Reciclaje creativo: damos una segunda vida a los materiales.</li>
        <li>Talleres de cosmética natural (jabones, ambientadores).</li>
        <li>Manualidades con elementos naturales: prensado de flores, hojas de arcilla o mariposas de madera.</li>
        <li>Creación de Eguzkilores.</li>
      </ul>

      <h3>Ciencia en las manos</h3>
      <ul>
        <li>Réplicas de fósiles: un viaje al pasado para entender la geología.</li>
        <li>Taller de microscopio: para descubrir el mundo invisible que nos rodea.</li>
        <li>Experimentos curiosos: desde planetas magnéticos hasta cianotipias.</li>
      </ul>

      <h3>Naturaleza y Huerto</h3>
      <ul>
        <li>Bombas de semillas y creación de huertos urbanos o escolares.</li>
        <li>Construcción de refugios para mariquitas, mariposas e insectos.</li>
        <li>Jardinería y plantas medicinales para conocer sus usos tradicionales.</li>
      </ul>
    </section>

    <!-- FAQ -->
    <section class="faq-section">
      <h2>Preguntas frecuentes</h2>
      <h3>¿Son actividades solo para niños?</h3>
      <p>¡Para nada! Adaptamos el contenido a todas las edades, desde educación infantil hasta grupos de adultos o empresas. La curiosidad no tiene edad.</p>
      <h3>¿Dónde se pueden realizar?</h3>
      <p>Donde prefiráis. Podemos ir a vuestro centro, local, o organizar la actividad en un entorno natural si preferís estar al aire libre.</p>
      <h3>¿Podemos personalizar el taller?</h3>
      <p>Por supuesto, esa es nuestra especialidad. Cuéntanos qué idea tienes y le damos forma juntos para que sea exactamente lo que buscáis.</p>
    </section>

    <!-- GALERÍA DE IMÁGENES -->
    <div class="imagen-trio">
      <div><img class="img" src="/imagenes/servicios/actividades/actividades1.avif" alt="Taller de reciclaje" title="Taller de reciclaje" loading="lazy" /></div>
      <div><img class="img" src="/imagenes/servicios/actividades/actividades2.avif" alt="Huerto urbano" title="Huerto urbano" loading="lazy" /></div>
      <div><img class="img" src="/imagenes/servicios/actividades/actividades3.avif" alt="Taller de Eguzkilores" title="Taller de Eguzkilores" loading="lazy" /></div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/servicios/actividades'
useHead({
  title: 'Talleres y Actividades Ambientales | Geobizi',
  meta: [{ name: 'description', content: 'Talleres prácticos y actividades ambientales adaptadas para colegios, eventos y proyectos locales. ¡Aprende disfrutando!' }],
  link: [{ rel: 'canonical', href: pageUrl }]
})
</script>

<style scoped>
.separador-seccion {
  margin: 3rem 0;
  border: 0;
  border-top: 1px solid var(--shoftgreen);
}

/* LISTAS CON HOJITAS */
.contenedor-principal ul {
  list-style-type: none;
  padding-left: 0;
}
.contenedor-principal li {
  position: relative;
  padding-left: 2rem;
  margin-bottom: 0.8rem;
  line-height: 1.5;
}
.contenedor-principal li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 2px;
  width: 1.2rem;
  height: 1.2rem;
  background-image: url('../../assets/Hojitas.png'); 
  background-size: contain;
  background-repeat: no-repeat;
}


</style>