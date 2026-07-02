<template>
  <div class="contenedor-principal">
    <h1>Formación, Asesoramiento y Consultoría Educativa</h1>
    
    <p>En Geobizi acompañamos a centros escolares, empresas y equipos profesionales en su transformación hacia modelos más sostenibles, digitales y humanos. No solo compartimos información, sino que diseñamos procesos de aprendizaje a medida.</p>

    <section class="bloques-gestion">
      <div class="bloque-modalidad">
        <h3>Consultoría Educativa (STEAM y Sostenibilidad)</h3>
        <p>Ayudamos a los centros a integrar la sostenibilidad en todas las asignaturas. Diseñamos proyectos coherentes para que el laboratorio sea un espacio STEAM activo, aplicando el Diseño Universal para el Aprendizaje (DUA) para asegurar que la educación sea realmente inclusiva para todo el alumnado.</p>
      </div>

      <div class="bloque-modalidad">
        <h3>Formación Profesional y Técnica</h3>
        <p>Ponemos nuestra experiencia en Lanbide y otros entornos formativos al servicio de tu equipo. Impartimos formación en áreas como ecoturismo, huertos urbanos y gestión del ocio, además de habilidades clave como la comunicación efectiva, el trabajo en equipo y el uso práctico de la IA.</p>
      </div>

      <div class="bloque-modalidad">
        <h3>Asesoramiento en Neuroeducación</h3>
        <p>Desde Geobizi, integramos la neurociencia aplicada para acompañar a familias y centros en la gestión de la neurodivergencia. Ofrecemos asesoramiento estratégico para entender y adaptar los entornos educativos a las necesidades reales de cada persona.</p>
      </div>
    </section>

    <h2>Áreas de especialidad</h2>
    <p>Nuestra formación se adapta siempre a vuestras necesidades, basándonos en nuestra experiencia en estos ámbitos:</p>
    
    <ul class="lista-formacion">
      <li><strong>Educación:</strong> Didáctica de la ciencia, metodologías activas y gamificación.</li>
      <li><strong>Innovación:</strong> Uso ético de la IA, herramientas digitales y diseño de espacios educativos.</li>
      <li><strong>Gestión y Equipos:</strong> Comunicación efectiva, roles de equipo y liderazgo.</li>
      <li><strong>Medioambiente:</strong> Ecoturismo, diseño de espacios verdes y regeneración.</li>
    </ul>

    <section class="faq-section">
      <h2>Preguntas frecuentes</h2>
      <h3>¿Cómo adaptáis la formación a un centro educativo?</h3>
      <p>Nos reunimos con el equipo docente para conocer a fondo su proyecto. No damos charlas genéricas; trabajamos sobre el currículum del centro para que los cambios sean reales y aplicables al aula desde el primer día.</p>
      <h3>¿La formación es presencial u online?</h3>
      <p>Nos adaptamos. Realizamos sesiones presenciales en centros y empresas, o sesiones de asesoramiento online si la dinámica del proyecto así lo requiere.</p>
    </section>

    <div class="imagen-trio">
      <div><img class="img" src="/imagenes/servicios/formacion/formacion1.avif" alt="Formación docente" loading="lazy" /></div>
      <div><img class="img" src="/imagenes/servicios/formacion/formacion2.avif" alt="Consultoría" loading="lazy" /></div>
      <div><img class="img" src="/imagenes/servicios/formacion/formacion3.avif" alt="Sesión de trabajo" loading="lazy" /></div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'
const pageUrl = 'https://www.geobizi.com/servicios/formacion'
useHead({
  title: 'Formación y Consultoría Educativa | Geobizi',
  meta: [{ name: 'description', content: 'Consultoría educativa en STEAM, sostenibilidad y neuroeducación. Formación a medida para centros docentes y empresas.' }],
  link: [{ rel: 'canonical', href: pageUrl }]
})
</script>

<style scoped>
.lista-formacion { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.faq-section { margin-top: 3rem; padding: 2rem; background: var(--megashoftgreen); border-radius: 0.5rem; }
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