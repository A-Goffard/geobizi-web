<template>
  <div class="contenedor-principal">
    <h1><strong>Centranthus ruber</strong> (Valeriana Roja): Una Belleza Invasora en Nuestros Jardines</h1>
    
    <p>En los últimos años, la preocupación por la propagación de <strong>especies exóticas invasoras</strong> ha crecido considerablemente en Bizkaia. Una de las plantas que ha comenzado a destacar negativamente en este sentido es el <strong>Centranthus ruber</strong>, comúnmente conocido como <strong>valeriana roja</strong> o valeriana roja espinosa. Aunque su apariencia encantadora la ha convertido en una elección popular en jardinería, esta planta ha demostrado tener un impacto devastador en los ecosistemas locales.</p>

    <h2>Origen y Apariencia de la Valeriana Roja</h2>
    <p>El <em>Centranthus ruber</em> es nativo de regiones de la cuenca mediterránea, pero se ha expandido rápidamente por colinas, laderas y bordes de carreteras en todo el mundo. Su atractiva apariencia, con vistosos racimos de flores que van desde el rosa claro hasta el rojo carmesí intenso, ha hecho que sea una opción muy apreciada en <strong>jardines privados</strong> y rotondas urbanas.</p>
    <p>Además de su belleza, su increíble capacidad para crecer en suelos pobres o entre grietas de muros, sumada a su gran resistencia a las sequías, contribuyen a su popularidad entre los aficionados a la jardinería. Sin embargo, esa misma resistencia es lo que la hace tan peligrosa.</p>

    <h2>Riesgo de Invasión y Mecanismos de Propagación</h2>
    <p>Lo que inicialmente podría considerarse una planta de fácil cuidado, pronto se transforma en un <strong>problema medioambiental grave</strong>. La valeriana roja tiene una asombrosa capacidad para propagarse rápidamente y establecer poblaciones densas en áreas naturales protegidas.</p>

    <p>Su éxito como planta invasora se basa en dos estrategias letales para la flora autóctona:</p>
    <ul>
      <li><strong>Producción masiva de semillas:</strong> Genera miles de semillas aladas que son dispersadas fácilmente por el viento a grandes distancias, permitiéndole colonizar nuevas áreas rápidamente.</li>
      <li><strong>Tolerancia extrema:</strong> Soporta la salinidad del mar, suelos rocosos y variaciones climáticas, dándole una ventaja competitiva enorme sobre nuestras especies locales más delicadas.</li>
    </ul>

    <h2>El Impacto Ecológico en el Entorno</h2>
    <p>La proliferación descontrolada de la valeriana roja no es solo un problema estético. Sus consecuencias alteran por completo el equilibrio de nuestros ecosistemas:</p>
    <ul>
      <li><strong>Desplazamiento de flora autóctona:</strong> Monopoliza la luz, el agua y el espacio, asfixiando a las plantas nativas e impidiendo su crecimiento.</li>
      <li><strong>Alteración de polinizadores:</strong> Al acaparar la atención de insectos polinizadores, otras plantas autóctonas dejan de reproducirse.</li>
      <li><strong>Modificación del suelo:</strong> Cambia la estructura química y la dinámica de nutrientes del suelo, dificultando aún más la supervivencia de las especies locales.</li>
    </ul>

    <h2>Manejo, Prevención y Jardinería Responsable</h2>
    <p>Para frenar el avance de la valeriana roja, es fundamental la concienciación. Si ya tienes esta planta en tu jardín, es vital <strong>cortar las flores marchitas antes de que formen semillas</strong> para evitar que el viento las propague hacia los montes cercanos. La mejor prevención es siempre optar por <strong>plantas autóctonas</strong> en nuestros jardines, apoyando así la biodiversidad local sin poner en riesgo los hábitats naturales.</p>

    <div class="alerta-importante">
      <p><strong>⚠️ Aviso de Especie Invasora en La Galea (Getxo)</strong><br>
      Recientemente, desde el equipo de Geobizi hemos detectado la aparición de esta especie invasora a lo largo del <strong>paseo de La Galea</strong>, un espacio natural protegido donde realizamos muchas de nuestras rutas divulgativas. Ya hemos dado el aviso oficial a las autoridades competentes del Ayuntamiento y la Diputación para su pronta erradicación, buscando proteger este valioso entorno costero (aunque por el momento sin éxito).</p>
    </div>

    <div class="caja-recurso">
      <h3>Combate las Especies Invasoras con Educación Ambiental</h3>
      <p>
        El primer paso para proteger nuestra biodiversidad es saber reconocer qué especies no pertenecen a nuestros ecosistemas. En Geobizi desarrollamos <strong>talleres de sensibilización y proyectos de educación ambiental</strong> para colegios, ayuntamientos y familias. Aprende a identificar y gestionar de forma responsable la flora de tu entorno.
      </p>
      <div class="botones-recurso">
        <a href="/servicios" class="proximas-actividades">Ver nuestros programas educativos</a>
        <a href="/contacto" class="btn-ver-mas">Contacta para organizar un taller</a>
      </div>
    </div>

    <div class="imagen-trio">
      <div>
        <img class="img" src="/imagenes/blog/detalle/valeriana1.avif" alt="Ejemplar de valeriana roja (Centranthus ruber) floreciendo en un muro de piedra" title="Centranthus ruber en entorno urbano" loading="lazy" />
      </div>
      <div>
        <img class="img" src="/imagenes/blog/detalle/valeriana2.avif" alt="Matorral denso de valeriana roja propagándose de forma invasiva en un entorno natural" title="Invasión de valeriana roja" loading="lazy" />
      </div>
      <div>
        <img class="img" src="/imagenes/blog/detalle/valeriana3.avif" alt="Fotografía macro de las pequeñas flores rojas y rosadas del Centranthus ruber" title="Detalle floral del Centranthus ruber" loading="lazy" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

// URL optimizada (coincide con el router)
const pageUrl = 'https://www.geobizi.com/blog/valeriana-roja'
const ogImage = 'https://www.geobizi.com/imagenes/blog/detalle/valeriana1.avif'

useHead({
  // Título SEO
  title: 'Valeriana Roja (Centranthus ruber): Especie Invasora en Bizkaia | Geobizi',
  meta: [
    { name: 'description', content: 'Descubre por qué la Valeriana Roja (Centranthus ruber) es una peligrosa especie invasora para los ecosistemas de Bizkaia. Cómo identificarla y evitar su propagación.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Valeriana Roja: De bonita flor de jardín a amenaza ecológica | Geobizi' },
    { property: 'og:description', content: 'El impacto ecológico de la Valeriana Roja (Centranthus ruber) y su reciente aparición en los acantilados de La Galea.' },
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
        "headline": "Centranthus Ruber (Valeriana Roja): Una Belleza Invasora en los Jardines",
        "description": "Conoce el riesgo invasor de Centranthus ruber (valeriana roja), su impacto en los ecosistemas locales y medidas preventivas.",
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
          // AÑADIDO TIKTOK AQUÍ TAMBIÉN
          "sameAs": [
            "https://www.facebook.com/geobizirik/",
            "https://www.instagram.com/geotxiki/",
            "https://www.tiktok.com/@geobizi",
            "https://www.youtube.com/channel/UCw-C_J0y-jKHp7Zx92lsKfg"
          ]
        },
        // Fechas requeridas para SEO
        "datePublished": "2024-05-20T08:00:00+01:00",
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
/* Reutilizamos los estilos corporativos */
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