<template>
  <div class="contenedor-principal">
    <h1>Actividades y Talleres</h1>
    <p>Diseñamos talleres prácticos y experiencias de educación ambiental; adaptamos contenidos, metodologías y duración
      según las edades y los objetivos pedagógicos o lúdicos de cada colectivo.</p>

    <!-- BLOQUE DE MODALIDADES DE TRABAJO -->
    <section class="modalidades-trabajo">
      <h2>Modalidades de Contratación</h2>
      <p>Trabajamos de forma transversal adaptando la metodología, los materiales y el idioma (euskera/castellano) en
        base a tres líneas operativas principales:</p>

      <div class="bloques-gestion">
        <div class="bloque-modalidad">
          <h3>Centros Escolares e Instituciones Educativas</h3>
          <p>Diseñamos talleres prácticos, formaciones específicas y salidas didácticas alineadas con el currículum
            escolar de Primaria, Secundaria y Bachillerato. Desarrollamos tanto intervenciones puntuales en el aula como
            programas continuos adaptados a unidades didácticas de ciencias naturales, ecología, medioambiente, geología
            y botánica.</p>
          <p class="ejemplo-referencia"><em>Ejemplo de colaboración:</em> Programas curriculares a medida sobre el
            impacto de la deforestación, talleres didácticos de biodiversidad activa en centros escolares de Mungia.</p>
        </div>

        <div class="bloque-modalidad">
          <h3>Proyectos Integrales de Divulgación Medioambiental</h3>
          <p>Creamos estrategias macro de dinamización ambiental para municipios, mancomunidades y territorios que
            buscan poner en valor su entorno y sensibilizar a su población. Coordinamos planes que unifican de forma
            transversal el aprendizaje en las aulas con jornadas prácticas de campo abiertas a toda la ciudadanía.</p>
          <p class="ejemplo-referencia"><em>Ejemplo de colaboración:</em> Coordinación y desarrollo del programa
            integral ZallaNatura, unificando la divulgación científica escolar con actividades prácticas y divulgativas
            abiertas al público general.</p>
        </div>

        <div class="bloque-modalidad">
          <h3>Talleres para Eventos y Ferias</h3>
          <p>Formatos dinámicos, adaptados y de corta duración idóneos para stands institucionales, ferias de flores, de
            sostenibilidad, jornadas culturales o dinámicas corporativas de <em>team building</em>. Diseñamos
            actividades de fuerte carga manipulativa y visual pensadas para entretener, concienciar y forjar vínculos
            cooperativos en grupos grandes.</p>
        </div>
      </div>
    </section>

    <hr class="separador-seccion" />

    <!-- BLOQUE DE TEMÁTICAS (TU CATÁLOGO ORIGINAL) -->
    <section class="catalogo-especialidades">
      <h2>Especialidades y Talleres Disponibles</h2>
      <p>A partir de nuestras modalidades de trabajo, puedes seleccionar y combinar diferentes contenidos técnicos de
        nuestro catálogo temático:</p>

      <h3>Talleres creativos y manuales</h3>
      <ul>
        <li>Reciclaje creativo</li>
        <li>Pintando figuras de yeso</li>
        <li>Patatroles</li>
        <li>Jabones y cosmética natural</li>
        <li>Ambientadores caseros</li>
        <li>Mariposas de madera</li>
        <li>Hojas de arcilla</li>
        <li>Prensa de flores</li>
        <li>Papel reciclado</li>
        <li>Herbario de pintura</li>
        <li>Eguzkilores</li>
      </ul>

      <h3>Talleres científicos y técnicos</h3>
      <ul>
        <li>Réplicas de fósil</li>
        <li>Planetas magnéticos</li>
        <li>Cianotipias</li>
        <li>Microscopio</li>
        <li>Geodas</li>
        <li>Brújulas</li>
      </ul>

      <h3>Talleres de naturaleza y jardinería</h3>
      <ul>
        <li>Bombas de semillas</li>
        <li>Casas de mariquitas</li>
        <li>Casas de mariposas</li>
        <li>Casas de insectos</li>
        <li>MacetoHuerto</li>
        <li>Huertos Urbanos</li>
        <li>Plantas medicinales</li>
        <li>Oasis de mariposas</li>
        <li>Biorregeneración colaborativa</li>
      </ul>
    </section>

    <!-- GALERÍA DE IMÁGENES -->
    <div class="imagen-trio">
      <div>
        <img class="img" src="/imagenes/servicios/actividades/actividades1.avif" alt="Actividad de reciclaje creativo"
          title="Actividad de reciclaje creativo — imagen 1" loading="lazy" />
      </div>
      <div>
        <img class="img" src="/imagenes/servicios/actividades/actividades2.avif" alt="Taller de huertos urbanos"
          title="Taller de huertos urbanos — imagen 2" loading="lazy" />
      </div>
      <div>
        <img class="img" src="/imagenes/servicios/actividades/actividades3.avif" alt="Taller de Eguzkilores"
          title="Taller de Eguzkilores — imagen 3" loading="lazy" />
      </div>
    </div>

    <div class="imagen-trio">
      <div>
        <img class="img" src="/imagenes/servicios/actividades/actividades4.avif" alt="Taller de papel reciclado"
          title="Taller de papel reciclado — imagen 1" loading="lazy" />
      </div>
      <div>
        <img class="img" src="/imagenes/servicios/actividades/actividades5.avif" alt="Taller de fósiles"
          title="Taller de fósiles — imagen 2" loading="lazy" />
      </div>
      <div>
        <img class="img" src="/imagenes/servicios/actividades/actividades6.avif" alt="Taller de bombas de semillas"
          title="Taller de bombas de semillas — imagen 3" loading="lazy" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/servicios/actividades'
useHead({
  title: 'Actividades y Talleres Ambientales | Geobizi',
  meta: [{ name: 'description', content: 'Programas y talleres ambientales de Geobizi: actividades curriculares para centros escolares y proyectos integrales locales.' }],
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