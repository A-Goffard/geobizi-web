<template>
  <div class="contenedor-principal">
    <h1>Rutas Guiadas y de Naturaleza en Bizkaia</h1>
    
    <p>La historia de la tierra está escrita en las rocas de Bizkaia. En Geobizi, convertimos el paisaje en un aula abierta donde aprendemos juntos a leer las rocas, observar los fósiles y disfrutar del entorno de forma activa, respetuosa y muy cercana.</p>

    <p>Hacemos rutas guiadas pensadas para compartir y descubrir. Nos adaptamos a cada grupo para que, tengas la edad que tengas, te lleves a casa una experiencia llena de curiosidades y buenos momentos.</p>

    <!-- BLOQUE DE MODALIDADES DE RUTAS -->
    <section class="modalidades-trabajo">
      <h2>¿Cómo nos gusta trabajar?</h2>
      <div class="bloques-gestion">
        <div class="bloque-modalidad">
          <h3>Rutas a Medida</h3>
          <p>Diseñamos salidas pensadas para ti. Ya seas un grupo de amigos, un colegio, una asociación o una empresa buscando una actividad diferente, nos sentamos contigo y preparamos el recorrido, el ritmo y el contenido para que encaje perfectamente con lo que buscas.</p>
          <router-link to="/contacto?servicio=rutas_a_medida" class="btn-servicio">Pedir ruta a medida</router-link>
        </div>

        <div class="bloque-modalidad">
          <h3>Rutas con Calendario (Fecha fija)</h3>
          <p>Son salidas que organizamos con fecha fija y donde cualquiera puede apuntarse. Es la oportunidad ideal para conocernos, disfrutar de la naturaleza en grupo y aprender algo nuevo sobre nuestro entorno.</p>
          
          <div class="caja-recurso">
            <h3>Campaña de Getxo: "El Flysch al microscopio"</h3>
            <p>Ya puedes reservar tu plaza para nuestras salidas por el litoral de Getxo. Explora la costa en <b>la playa de Azkorri</b> o descubre la biodiversidad cuando cae el sol en nuestras rutas nocturnas <b>"Naturgaua"</b>.</p>
            <p class="nota-subvencion"><em>*Estas rutas cuentan con el apoyo del Ayuntamiento de Getxo para acercar la naturaleza a todo el mundo.</em></p>
            <div class="botones-recurso">
              <router-link to="/calendario" class="proximas-actividades">Ver Fechas</router-link>
              <a href="https://www.getxo.eus/es/turismo/que-hacer/ruta-geologica-flysch" target="_blank" rel="noopener noreferrer" class="btn-ver-mas">Info en Getxo Turismo</a>
            </div>
            <div style="margin-top: 1rem;">
              <router-link to="/contacto?servicio=rutas_calendario" class="btn-servicio">Para resolver dudas</router-link>
            </div>
          </div>
        </div>
      </div>
    </section>

    <hr class="separador-seccion" />

    <!-- CATÁLOGO RUTAS -->
    <section class="catalogo-especialidades">
      <h2>Catálogo de Rutas</h2>
      <p>Aquí tienes algunas de nuestras propuestas favoritas. Si tienes otra idea en mente, ¡cuéntanosla y la diseñamos juntos!</p>
      
      <ul>
        <li><strong>Flysch de Sopela:</strong> Un paseo para descubrir cómo se formaron nuestros acantilados y qué secretos geológicos esconden.</li>
        <li><strong>Ruta medioambiental en Azkorri:</strong> Un recorrido por las dunas, la playa y los acantilados para conocer de cerca las plantas y animales que viven allí.</li>
        <li><strong>Ruta Etnobotánica:</strong> Un paseo para aprender sobre las plantas medicinales que nos rodean y cómo se han usado tradicionalmente desde siempre.</li>
        <li><strong>Identificación de árboles:</strong> Un taller al aire libre para fijarnos en la forma de las hojas, los colores y las curiosidades de los árboles de nuestra zona.</li>
        <li><strong>Limpieza de playas:</strong> Salidas de voluntariado donde, además de cuidar el entorno, hablamos sobre el impacto de los residuos en nuestros ecosistemas.</li>
        <li><strong>Ruta nocturna (Naturgaua):</strong> Salimos a descubrir los secretos del bosque cuando cae el sol, escuchando con calma todos los sonidos de la naturaleza.</li>
      </ul>
    </section>

    <!-- FAQ -->
    <section class="faq-section">
      <h2>Preguntas frecuentes</h2>
      <h3>¿Son rutas aptas para niños?</h3>
      <p>¡Por supuesto! Adaptamos lo que contamos y el ritmo para que los más pequeños (y los no tan pequeños) disfruten y aprendan sin darse cuenta. Queremos que sea una experiencia divertida para todos.</p>
      <h3>¿Qué nivel de dificultad tienen?</h3>
      <p>Las rutas se adaptan a lo que necesitéis. Podemos hacer desde un paseo tranquilo y cómodo para caminar sin prisa, hasta una ruta con un poquito más de caminata si os apetece hacer ejercicio.</p>
      <h3>¿Qué equipo necesito llevar?</h3>
      <p>Lo más importante es que traigas calzado cómodo (botas o zapatillas con buen agarre), algo de abrigo o protección para el sol según el día, y agua. Del resto del equipo (lupas, guías, etc.) nos encargamos nosotros.</p>
    </section>

    <hr class="separador-seccion" />

    <!-- INFORMACIÓN PRÁCTICA -->
    <section class="info-practica">
      <h2>Información Práctica</h2>
      <h3>¿Qué incluyen nuestras rutas?</h3>
      <ul>
        <li>Acompañamiento y explicaciones durante todo el recorrido.</li>
        <li>Material de apoyo (lupas, fichas, guías) para que nadie se pierda ningún detalle.</li>
        <li>Un itinerario hecho a vuestra medida según intereses y edades.</li>
      </ul>

      <h3>Consejos para disfrutar al máximo</h3>
      <ul>
        <li>Ven con ganas de observar y disfrutar.</li>
        <li>Trae ropa cómoda y adaptada a la previsión del tiempo.</li>
        <li>¡No te olvides del agua y algo de protección solar!</li>
        <li>Sigue siempre las indicaciones de seguridad para que la ruta sea perfecta.</li>
      </ul>
    </section>

    <!-- GALERÍA -->
    <div class="imagen-trio">
      <div><img class="img" src="/imagenes/servicios/rutas/ruta1.avif" alt="Grupo disfrutando de la ruta del Flysch" title="Ruta Flysch" loading="lazy" /></div>
      <div><img class="img" src="/imagenes/servicios/rutas/ruta2.avif" alt="Observando naturaleza en Azkorri" title="Ruta Azkorri" loading="lazy" /></div>
      <div><img class="img" src="/imagenes/servicios/rutas/ruta3.avif" alt="Ruta escolar disfrutando" title="Ruta escolar" loading="lazy" /></div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'
const pageUrl = 'https://www.geobizi.com/servicios/rutas'
const ogImage = 'https://www.geobizi.com/imagenes/servicios/detalle/sopela.avif'

useHead({
  title: 'Rutas Guiadas y Naturaleza | Geobizi',
  meta: [
    { name: 'description', content: 'Rutas guiadas por la naturaleza, geología y botánica de Bizkaia. Experiencias cercanas y adaptadas para todos.' },
    { property: 'og:title', content: 'Rutas Guiadas y Naturaleza | Geobizi' },
    { property: 'og:description', content: 'Rutas interpretativas por Bizkaia: Flysch, botánica y rutas nocturnas. ¡Ven a descubrir el entorno con nosotros!' },
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