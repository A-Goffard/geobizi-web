<template>
  <div class="contenedor-principal">
    <h1>Proyecto: Flysch de Bizkaia</h1>
    <h2>Geología, Educación y Tecnología en la Costa Vasca</h2>
    
    <p>El <strong>Flysch de Bizkaia</strong> es uno de los patrimonios geológicos más impresionantes de la costa cantábrica. Para dar a conocer su valor incalculable de forma rigurosa y amena, en Geobizi hemos desarrollado un proyecto integral de divulgación que abarca desde la exploración sobre el terreno hasta la innovación digital.</p>

    <hr class="separador-seccion" />

    <section class="secciones">
      <h2>Nuestras Líneas de Acción en el Flysch</h2>

      <!-- LÍNEA 1: YINCANA DIGITAL -->
      <div class="bloque-accion">
        <h3>1. Flysch Digital: Yincana Interactiva</h3>
        <p>¿Imaginas explorar un paisaje espectacular mientras resuelves enigmas digitales con tu dispositivo móvil? <strong>Flysch Digital</strong> es una experiencia única que combina lo mejor de una yincana tradicional de orientación con la tecnología actual.</p>
        <p>Pensada para familias, colegios y grupos, los participantes recorren la playa de Sopela resolviendo pistas y acertijos geológicos. Durante el transcurso de las pruebas, se mueven por la zona mientras aprenden a identificar estratos y fósiles de manera totalmente interactiva y lúdica. La actividad está disponible en euskera y castellano.</p>
      </div>

      <!-- LÍNEA 2: RUTAS GUIADAS -->
      <div class="bloque-accion">
        <h3>2. Geoturismo y Rutas Geológicas</h3>
        <p>Ofrecemos rutas guiadas interpretativas por los acantilados de Sopela y Getxo (Gorrondatxe / Azkorri). Lejos de una simple caminata, enseñamos a los asistentes a "leer las rocas", interpretando la orogenia alpina, identificando fósiles y microfósiles e integrando el uso de herramientas científicas como el microscopio de campo.</p>
        <p>Diseñamos itinerarios adaptados al currículo de centros escolares y programas de ciencia ciudadana respaldados por instituciones locales.</p>
      </div>

      <!-- LÍNEA 3: MATERIAL DIDÁCTICO (Descarga) -->
      <div class="bloque-accion">
        <h3>3. Recursos Didácticos Abiertos</h3>
        <p>Como parte de nuestro compromiso con la educación ambiental, hemos elaborado material técnico y didáctico para que docentes, educadores y familias puedan preparar su visita o profundizar en los conceptos geológicos en el aula.</p>
        
        <!-- Tarjeta de Descarga Integrada -->
        <div class="contenedor-descarga">
          <a href="/descargas/documentos/Flyschbizkaia-didactica.pdf" download="Flyschbizkaia-didactica.pdf" class="card-descarga">
            <img src="/descargas/miniaturas/flyschbizkaia-didactica.avif" alt="Portada Guía Didáctica Flyschbizkaia" loading="lazy">
            <div class="info-descarga">
              <h4>Guía Didáctica: Flysch de Bizkaia</h4>
              <p>Documento de apoyo educativo en formato PDF.</p>
              <span class="btn-falso">Descargar Archivo</span>
            </div>
          </a>
        </div>
      </div>
    </section>

    <hr class="separador-seccion" />

    <h3>¿Por qué elegir nuestro proyecto integral?</h3>
    <ul>
      <li><strong>Rigor científico:</strong> Contenidos estructurados por profesionales de la geología y la educación.</li>
      <li><strong>Innovación:</strong> Integración fluida de herramientas digitales (yincanas móviles) en entornos naturales.</li>
      <li><strong>Adaptabilidad:</strong> Capacidad de escalar el proyecto y la yincana a otros entornos geológicos o municipios.</li>
      <li><strong>Multilingüe:</strong> Materiales y dinamización disponibles en euskera y castellano.</li>
    </ul>

    <!-- GALERÍA DE IMÁGENES -->
    <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/flyschdigital/flyschdigital1.avif"
          alt="Flysch Digital — yincana interactiva en la costa"
          title="Flysch Digital — Yincana"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/flyschdigital/flyschdigital2.avif"
          alt="Participantes resolviendo pruebas de la yincana digital con el móvil"
          title="Resolución de pruebas digitales"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/flyschdigital/flyschdigital3.avif"
          alt="Exploración del flysch de Bizkaia y descubrimiento de fósiles"
          title="Exploración geológica"
          loading="lazy"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/detalle-flysch'
const ogImage = 'https://www.geobizi.com/imagenes/proyectos/flyschdigital/flyschdigital1.avif'

useHead({
  title: 'Proyecto Flysch de Bizkaia: Geoturismo y Yincana Digital | Geobizi',
  meta: [
    { name: 'description', content: 'Proyecto integral sobre el Flysch de Bizkaia (Flyschbizkaia): rutas geológicas, yincana digital interactiva y descarga de guías didácticas.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Proyecto Flysch de Bizkaia: Geoturismo y Educación | Geobizi' },
    { property: 'og:description', content: 'Explora el Flysch de Bizkaia con nuestra yincana digital, rutas guiadas y recursos educativos descargables.' },
    { property: 'og:type', content: 'article' },
    { property: 'og:url', content: pageUrl },
    { property: 'og:image', content: ogImage },
    { name: 'twitter:card', content: 'summary_large_image' }
  ],
  link: [
    { rel: 'canonical', href: pageUrl },
    { rel: 'image_src', href: ogImage }
  ],
  script: [
    {
      type: 'application/ld+json',
      children: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "WebPage",
        "url": pageUrl,
        "name": "Proyecto Flysch de Bizkaia: Geoturismo y Yincana Digital | Geobizi",
        "description": "Proyecto integral sobre el Flysch de Bizkaia: rutas geológicas, yincana digital interactiva y descarga de guías didácticas.",
        "inLanguage": "es",
        "isPartOf": {
          "@type": "Organization",
          "@id": "https://www.geobizi.com/#organization",
          "name": "Geobizi",
          "url": "https://www.geobizi.com"
        },
        "image": { "@type": "ImageObject", "url": ogImage, "width": 1080, "height": 1080 }
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

.separador-seccion {
  margin: 2.5rem 0;
  border: 0;
  border-top: 1px solid var(--shoftgreen);
}

.bloque-accion {
  margin-bottom: 2.5rem;
}

.bloque-accion h3 {
  color: var(--darkgreen);
  margin-bottom: 1rem;
}

/* ESTILOS PARA LA TARJETA DE DESCARGA */
.contenedor-descarga {
  margin-top: 1.5rem;
  max-width: 450px;
}

.card-descarga {
  display: flex;
  align-items: center;
  background-color: var(--megashoftgreen);
  border: 1px solid var(--shoftgreen);
  border-radius: 0.5rem;
  padding: 1rem;
  text-decoration: none;
  color: inherit;
  transition: transform 0.3s, box-shadow 0.3s;
}

.card-descarga:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.card-descarga img {
  width: 90px;
  height: auto;
  border-radius: 4px;
  margin-right: 1.5rem;
  object-fit: cover;
}

.info-descarga h4 {
  margin: 0 0 0.5rem 0;
  color: var(--darkgreen);
  font-size: 1.1rem;
}

.info-descarga p {
  margin: 0 0 1rem 0;
  font-size: 0.9rem;
  color: var(--darkgrey);
}

.btn-falso {
  background-color: var(--shoftgreen);
  color: white;
  padding: 0.4rem 0.8rem;
  border-radius: 4px;
  font-size: 0.85rem;
  font-weight: bold;
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