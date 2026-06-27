<template>
  <div class="contenedor-principal">
    <h1>Rutas Divulgativas</h1>
    <p>Realizamos rutas guiadas e itinerarios interpretativos relacionados con la naturaleza y las ciencias de la Tierra. Adaptamos la longitud, el lenguaje técnico y las dinámicas según las edades y los objetivos de cada colectivo.</p>

    <!-- BLOQUE DE MODALIDADES DE RUTAS -->
    <section class="modalidades-trabajo">
      <h2>Modalidades de Rutas</h2>
      
      <div class="bloques-gestion">
        <div class="bloque-modalidad">
          <h3>Rutas a Medida</h3>
          <p>Diseñamos rutas personalizadas exclusivas para centros escolares, asociaciones, empresas (<em>team building</em>), ayuntamientos y grupos privados. Los itinerarios se estructuran en función de los intereses específicos del cliente (geología, botánica, historia local).</p>
        </div>

        <div class="bloque-modalidad">
          <h3>Programas y Rutas Regulares (Fechas Garantizadas)</h3>
          <p>Actividades, itinerarios guiados y salidas de campo programadas con un calendario fijo e inscripción abierta para particulares, turismo familiar, colectivos reducidos y público <em>Silver</em>. Son experiencias orientadas a la ciencia ciudadana y el descubrimiento del entorno a través de la divulgación ambiental.</p>
          
          <div class="caja-recurso">
            <h3><strong>Campaña de Getxo — Inscripciones Abiertas</strong></h3>
            <p>
              Ya puedes reservar tu plaza para los servicios garantizados en el litoral de Getxo. Explora la costa en <b>"El Flysch al microscopio"</b> en la playa de Gorrondatxe (Azkorri) o descubre la biodiversidad nocturna con linternas de luz roja en las rutas de <b>"Naturgaua"</b>.
            </p>
            <p class="nota-subvencion">
              <em>*Nota: Estas rutas están <strong>parcialmente subvencionadas por el Ayuntamiento de Getxo</strong>, facilitando así el acceso a la divulgación científica y al conocimiento de nuestro patrimonio natural.</em>
            </p>
            <div class="botones-recurso">
              <a href="/calendario" class="proximas-actividades">Ver Fechas en Geobizi</a>
              <a href="https://www.getxo.eus/es/turismo/que-hacer/ruta-geologica-flysch" target="_blank" rel="noopener noreferrer" class="btn-ver-mas">Ver información en Getxo Turismo</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <hr class="separador-seccion" />

    <!-- RUTAS ESTANDARIZADAS -->
    <section class="catalogo-especialidades">
      <h2>Rutas Estandarizadas de Referencia</h2>
      <p>Estas son algunas de las rutas de nuestro catálogo que ofrecemos regularmente. Si tienes alguna idea o interés especial, podemos adaptar cualquiera de ellas a tu medida:</p>
      
      <ul>
        <li><strong>Flysch de Sopela:</strong> Ruta interpretativa para que descubras la formación de los acantilados y los secretos geológicos de esta zona costera única.</li>
        <li><strong>Ruta medioambiental en Azkorri:</strong> Itinerario por el entorno natural de Azkorri para conocer a fondo su flora, su fauna y sus ecosistemas dunares.</li>
        <li><strong>Identificación de árboles:</strong> Ruta botánica diseñada para aprender a identificar las especies arbóreas más comunes de nuestro entorno y sus características.</li>
        <li><strong>Plantas medicinales:</strong> Recorrido etnobotánico para conocer las plantas medicinales que nos rodean y sus usos tradicionales a lo largo de la historia.</li>
        <li><strong>Limpieza de playas:</strong> Ruta de voluntariado ambiental enfocada en la retirada responsable de residuos y la concienciación ecológica.</li>
        <li><strong>Ruta nocturna:</strong> Observación de la naturaleza desde una perspectiva diferente, descubriendo la fauna nocturna y los sonidos del bosque en la oscuridad.</li>
      </ul>
    </section>

    <!-- INFORMACIÓN PRÁCTICA -->
    <section class="info-practica">
      <h2>Información Práctica</h2>
      
      <h3>¿Qué incluyen nuestras rutas?</h3>
      <ul>
        <li>Servicio de guía especializado en divulgación.</li>
        <li>Material didáctico de apoyo y dinámicas participativas.</li>
        <li>Itinerarios personalizados por edad, idioma y objetivos de aprendizaje.</li>
      </ul>

      <h3>Recomendaciones de seguridad</h3>
      <ul>
        <li>Usa calzado adecuado para terreno irregular y ropa adaptada a la meteorología.</li>
        <li>Lleva siempre agua y protección solar.</li>
        <li>Ten en cuenta las recomendaciones de dificultad y desnivel específicas para cada ruta.</li>
        <li>Escucha y sigue siempre las instrucciones del guía.</li>
      </ul>
    </section>

    <!-- GALERÍA DE IMÁGENES -->
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
  title: 'Rutas Guiadas y Geoturismo | Geobizi',
  meta: [
    { name: 'description', content: 'Rutas guiadas geológicas, medioambientales y temáticas para colegios, asociaciones, empresas y público general. Rutas subvencionadas en Getxo.' },
    { property: 'og:title', content: 'Rutas Guiadas y Geoturismo | Geobizi' },
    { property: 'og:description', content: 'Rutas interpretativas (Flysch, botánica y nocturnas) con fechas garantizadas y a medida.' },
    { property: 'og:url', content: pageUrl },
    { property: 'og:image', content: ogImage }
  ],
  link: [{ rel: 'canonical', href: pageUrl }]
})
</script>

<style scoped>
.separador-seccion {
  margin: 3rem 0;
  border: 0;
  border-top: 1px solid var(--shoftgreen);
}

.caja-recurso {
  background-color: var(--megashoftgreen); 
  border-left: 4px solid var(--shoftgreen); 
  padding: 1.5rem;
  margin: 1.5rem 0 2.5rem 0;
  border-radius: 0 0.5rem 0.5rem 0;
}
.caja-recurso h3 {
  margin-top: 0;
  color: var(--lightgreen);
  font-size: 1.2rem;
}
.caja-recurso p {
  margin-bottom: 1rem;
  color: var(--darkgrey);
}
.nota-subvencion {
  font-size: 0.95rem;
  color: #2e7d32; /* Tono verde oscuro botánico */
}
.botones-recurso {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin-top: 1.5rem;
}
.proximas-actividades {
  background-color: var(--supershoftgreen);
  color: var(--lightgreen);
  padding: 0.6rem 1.2rem;
  text-decoration: none;
  font-weight: bold;
  border-radius: 4px;
  transition: background-color 0.3s;
}
.proximas-actividades:hover {
  background-color: var(--shoftgreen);
  color: var(--white);
}
.btn-ver-mas {
  background-color: transparent;
  color: var(--lightgreen);
  padding: 0.6rem 1.2rem;
  text-decoration: none;
  font-weight: bold;
  border: 1px solid var(--shoftgreen);
  border-radius: 4px;
  transition: all 0.3s;
}
.btn-ver-mas:hover {
  background-color: var(--shoftgreen);
  color: white;
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