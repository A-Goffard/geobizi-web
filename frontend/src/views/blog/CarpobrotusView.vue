<template>
  <div class="contenedor-principal">
    <h1>Uña de Gato (<em>Carpobrotus edulis</em>): Una invasora letal en nuestras costas</h1>
    
    <p>A pesar de su atractivo aspecto, sus hermosas flores y su increíble capacidad para crecer en condiciones difíciles, el <strong>Carpobrotus edulis</strong> (comúnmente conocido como <strong>Uña de gato</strong>) es una de las plantas más perjudiciales para los ecosistemas litorales. Originaria de Sudáfrica, esta especie suculenta se ha convertido en una amenaza global.</p>
    
    <h2>¿Qué es la Uña de Gato y por qué se expandió?</h2>
    <p>Su nombre científico proviene del griego <em>karpos</em> (fruta) y <em>brota</em> (comestible), junto al epíteto latino <em>edulis</em> (comestible), ya que produce un fruto similar a una baya que tradicionalmente se ha utilizado para hacer mermeladas.</p>
    
    <p>El <em>Carpobrotus edulis</em> crece formando matas densas y compactas, tejiendo una alfombra de hojas carnosas de color verde azulado. Sus flores son grandes y brillantes, con espectaculares pétalos amarillos, rosas o púrpuras. Esta belleza, sumada a su resistencia extrema frente a la salinidad, la sequía y los vientos costeros, motivó que durante décadas se plantara de forma intencionada en jardines, taludes y dunas de arena para fijar el terreno en Europa, América y Australia.</p>

    <h2>El devastador impacto ecológico</h2>
    <p>Hoy en día sabemos que esa capacidad de adaptación tiene un precio altísimo para la biodiversidad local. Su rápida propagación genera graves daños ambientales:</p>
    
    <ul>
      <li><strong>Asfixia de la flora autóctona:</strong> Al formar un manto continuo y denso, impide que la luz llegue al suelo, desplazando por completo a las plantas nativas de dunas y acantilados (muchas de ellas endémicas y protegidas).</li>
      <li><strong>Alteración química del suelo:</strong> Modifica el pH del terreno, acidificándolo y haciéndolo inhóspito para otras especies incluso después de haber sido arrancada.</li>
      <li><strong>Aceleración de la erosión:</strong> Paradójicamente, aunque se plantó para fijar taludes, su peso excesivo cuando acumula agua a menudo provoca el colapso y desprendimiento de las laderas.</li>
    </ul>

    <div class="alerta-importante">
      <p><strong>⚠️ Especie prohibida por Ley en España</strong><br>
      Debido a su enorme potencial colonizador, el <em>Carpobrotus edulis</em> está incluido en el <strong>Catálogo Español de Especies Exóticas Invasoras</strong> (Real Decreto 630/2013). En España está terminantemente prohibida su introducción en el medio natural, así como su posesión, transporte, tráfico y comercio. ¡Por favor, nunca la plantes en tu jardín ni arranques esquejes para llevarte a casa!</p>
    </div>

    <h2>Control, Erradicación y Restauración</h2>
    <p>En lugares como la costa de Bizkaia, los esfuerzos para controlar esta invasora se centran en campañas de eliminación física manual (el uso de maquinaria pesada o herbicidas suele dañar aún más el frágil ecosistema costero). Tras su retirada, es vital realizar una labor de <strong>restauración ecológica</strong>, replantando especies autóctonas que devuelvan el equilibrio a la zona.</p>

    <div class="caja-recurso">
      <h3>Sensibilización y Voluntariado Ambiental</h3>
      <p>
        La erradicación de especies invasoras como la uña de gato requiere de muchas manos y concienciación ciudadana. En Geobizi impulsamos <strong>jornadas de voluntariado y proyectos de educación ambiental</strong> en el litoral (como nuestras actividades en Sopela Kosta Fest o Aste Berdea) para proteger nuestra costa.
      </p>
      <div class="botones-recurso">
        <a href="/proyectos" class="proximas-actividades">Conoce nuestros Proyectos</a>
        <a href="/contacto" class="btn-ver-mas">Únete o pide información</a>
      </div>
    </div>

    <p class="social-media"><b>¡Síguenos en redes sociales para participar en nuestras próximas jornadas de limpieza y voluntariado ambiental!</b></p>
    <div class="redes-sociales">
      <a href="https://www.instagram.com/geotxiki/" target="_blank" rel="noopener noreferrer" title="Geobizi en Instagram">
        <img src="/imagenes/iconos/instagram.png" alt="Geobizi en Instagram" class="social-icon" loading="lazy" />
      </a>
      <a href="https://www.facebook.com/geobizirik/" target="_blank" rel="noopener noreferrer" title="Geobizi en Facebook">
        <img src="/imagenes/iconos/facebook.png" alt="Geobizi en Facebook" class="social-icon" loading="lazy" />
      </a>
      <a href="https://www.tiktok.com/@geobizi" target="_blank" rel="noopener noreferrer" title="Geobizi en TikTok">
        <img src="/imagenes/iconos/tiktok.png" alt="Geobizi en TikTok" class="social-icon" loading="lazy" />
      </a>
    </div>

    <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/blog/detalle/carpobrotus1.avif"
          alt="Gran extensión de Uña de gato (Carpobrotus edulis) invadiendo un ecosistema de dunas costeras"
          title="Invasión de Uña de gato en la costa"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/blog/detalle/carpobrotus2.avif"
          alt="Detalle de las flores amarillas y rosadas del Carpobrotus edulis asfixiando a la flora local"
          title="Flores de Carpobrotus edulis"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/blog/detalle/carpobrotus3.avif"
          alt="Voluntarios trabajando en la retirada manual de la planta invasora para restaurar el hábitat"
          title="Labores de erradicación y restauración"
          loading="lazy"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

// URL optimizada (coincide con el router)
const pageUrl = 'https://www.geobizi.com/blog/carpobrotus'
const ogImage = 'https://www.geobizi.com/imagenes/blog/detalle/carpobrotus1.jpeg'

useHead({
  // Título SEO combinando nombre común y científico
  title: 'Uña de Gato (Carpobrotus edulis): Planta Invasora | Geobizi',
  meta: [
    { name: 'description', content: 'Descubre por qué la Uña de Gato (Carpobrotus edulis) es una planta invasora letal para las costas y dunas. Aprende a identificarla y los métodos para erradicarla.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Uña de Gato: La peligrosa invasión del litoral | Geobizi' },
    { property: 'og:description', content: 'Impacto ecológico de la Uña de gato (Carpobrotus edulis) y nuestras acciones de voluntariado ambiental para proteger la costa.' },
    { property: 'og:type', content: 'article' },
    { property: 'og:url', content: pageUrl },
    { property: 'og:image', content: ogImage },
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:image', content: ogImage }
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
        "@type": "Article",
        "headline": "Uña de Gato (Carpobrotus edulis): Una invasora letal en nuestras costas",
        "description": "Impacto ecológico devastador de la Uña de Gato en los ecosistemas litorales, su estatus legal en España y técnicas de restauración ambiental.",
        "image": ogImage,
        "author": {
          "@type": "Organization",
          "name": "Geobizi",
          "url": "https://www.geobizi.com"
        },
        "publisher": {
          "@type": "Organization",
          "name": "Geobizi",
          "logo": {
            "@type": "ImageObject",
            "url": "https://www.geobizi.com/imagenes/GeobiziLogo.7ae1d6ce.png"
          },
          "sameAs": [
            "https://www.facebook.com/geobizirik/",
            "https://www.instagram.com/geotxiki/",
            "https://www.tiktok.com/@geobizi",
            "https://www.youtube.com/channel/UCw-C_J0y-jKHp7Zx92lsKfg"
          ]
        },
        // Fechas requeridas para el Schema Article
        "datePublished": "2024-04-10T08:00:00+01:00",
        "dateModified": "2026-04-14T10:00:00+02:00",
        "mainEntityOfPage": {
          "@type": "WebPage",
          "@id": pageUrl
        }
      })
    }
  ]
})
</script>

<style scoped>
/* ALERTA VISUAL */
.alerta-importante {
  background-color: var(--yellow);
  border-left: 5px solid var(--orange);
  padding: 1rem;
  margin: 1.5rem 0;
  border-radius: 4px;
}
.alerta-importante p {
  color: #856404;
  margin: 0;
}

/* CAJA DE RECURSOS */
.caja-recurso {
  background-color: var(--megashoftgreen); 
  border-left: 4px solid var(--shoftgreen); 
  padding: 1.5rem;
  margin: 2.5rem 0;
  border-radius: 0 0.5rem 0.5rem 0;
}
.caja-recurso h3 {
  margin-top: 0;
  color: var(--lightgreen);
  font-size: 1.2rem;
}
.caja-recurso p {
  margin-bottom: 1.5rem;
  color: var(--darkgrey);
}
.botones-recurso {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
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

/* REDES SOCIALES */
.social-media {
  margin-top: 2rem;
  color: var(--darkgrey);
}
.redes-sociales {
  margin-left: 1rem;
  display: flex;
  align-items: center;
}
.social-icon {
  width: 2.5rem; /* Ligeramente ajustado para alinear bien */
  margin-right: 1rem;
  margin-bottom: 1.5rem;
  transition: transform 0.3s;
}
.social-icon:hover {
  transform: scale(1.1);
}

/* Este apartado es para las listas con hojitas */

/* Quitar los puntos por defecto de la lista */
.contenedor-principal ul {
  list-style-type: none;
  padding-left: 0;
}

/* Dar espacio a la izquierda para que quepa el icono */
.contenedor-principal li {
  position: relative;
  padding-left: 2rem; /* Espacio para las hojitas */
  margin-bottom: 0.8rem;
  line-height: 1.5;
}

/* Insertar la imagen de las hojitas */
.contenedor-principal li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 2px;
  width: 1.2rem;
  height: 1.2rem;
  
  /* AQUÍ ESTÁ EL CAMBIO MÁGICO: subimos dos carpetas (../../) */
  background-image: url('../../assets/Hojitas.png'); 
  
  background-size: contain;
  background-repeat: no-repeat;
}
</style>