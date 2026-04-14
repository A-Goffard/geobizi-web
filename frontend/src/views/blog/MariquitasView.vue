<template>
  <div class="contenedor-principal">
    <h1>La Importancia de las <strong>Mariquitas</strong> en la Biodiversidad y el Medioambiente</h1>

    <p>Las mariquitas, también conocidas como catarinas, vaquitas de San Antonio o <em>marigorringo</em> (en Euskadi), son pequeños insectos que han capturado la atención y el cariño de muchas personas en todo el mundo. Sin embargo, su importancia no se limita solo a su apariencia encantadora. Estas diminutas criaturas desempeñan un papel fundamental en el <strong>equilibrio ecológico</strong> de nuestros ecosistemas, jardines y huertas.</p>

    <p>Pertenecen a la familia de los escarabajos (coccinélidos), y existen miles de especies diferentes. Son conocidas por sus brillantes colores (rojo, naranja, amarillo) y sus distintivas manchas negras, que varían según la especie y sirven como advertencia para sus depredadores de que "saben mal". Aunque cada una tiene su aspecto único, todas las mariquitas comparten características y comportamientos que las hacen inmensamente <strong>valiosas para el medioambiente</strong>.</p>

    <h2>Las Mariquitas como Control Biológico de Plagas</h2>
    <p>Una de las principales razones por las que las mariquitas son tan valoradas, especialmente en la agricultura ecológica y los huertos urbanos, es su voraz apetito. Estos pequeños insectos, tanto en su fase adulta como en estado de larva, se alimentan principalmente de pulgones, unos diminutos insectos chupadores de savia que pueden devastar cultivos enteros.</p>
    
    <p>Al consumir pulgones en cantidades masivas (una sola mariquita puede comer hasta 5.000 pulgones a lo largo de su vida), ayudan a controlar las poblaciones de estos insectos y previenen infestaciones severas. Al actuar como depredadoras naturales, las mariquitas ejercen un excelente <strong>control biológico</strong>, evitando o reduciendo la necesidad de utilizar pesticidas químicos que dañan el medioambiente, contaminan la tierra y matan a otros insectos beneficiosos.</p>

    <h2>Ventajas Ecológicas de las Mariquitas</h2>
    <p>La presencia de marigorringos es sinónimo de un entorno sano. Sus principales aportaciones son:</p>
    
    <h3>1. Aliadas de la Huerta y los Jardines:</h3>
    <ul>
        <li><strong>Sustituyen a los químicos:</strong> Mantienen a raya plagas de pulgones, cochinillas y ácaros de forma 100% natural.</li>
        <li><strong>Protección de plantas:</strong> Ayudan a mantener sanos los cultivos agrícolas y las plantas ornamentales sin dejar residuos tóxicos.</li>
    </ul>
    
    <h3>2. Polinización Secundaria:</h3>
    <ul>
        <li><strong>Apoyo a la Fertilización:</strong> Aunque son famosas por cazar pulgones, algunas especies de mariquitas también se alimentan de néctar y polen, contribuyendo, de forma secundaria, a la polinización cruzada de las flores.</li>
    </ul>

    <h3>3. Bioindicadoras de Calidad Ambiental:</h3>
    <ul>
        <li><strong>Salud del Hábitat:</strong> Las mariquitas son muy sensibles a la contaminación y a los pesticidas. Una población sana de mariquitas en tu jardín es un excelente indicador de que tu entorno está libre de tóxicos.</li>
    </ul>

    <div class="caja-recurso">
      <h3>Protege a las mariquitas con nuestros Talleres y Casitas</h3>
      <p>
        El comportamiento y ciclo de vida de las mariquitas despiertan una enorme curiosidad entre los más pequeños. Por ello, en Geobizi tenemos talleres diseñados para enseñar educación ambiental mientras fabricamos y decoramos <strong>"Hoteles de Insectos" y casitas para mariquitas</strong>. ¡Así les ofrecemos refugio durante el invierno!
      </p>
      <div class="botones-recurso">
        <a href="/servicios" class="proximas-actividades">Descubre nuestros talleres infantiles</a>
        <a href="/contacto" class="btn-ver-mas">Contacta con nosotros</a>
      </div>
    </div>

    <p class="social-media"><b>¡Anímate a seguirnos en redes sociales para no perderte nuestras actividades!</b></p>
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
        <img class="img" src="/imagenes/blog/detalle/mariquita1.avif" alt="Mariquita adulta roja con manchas negras posada sobre una hoja verde" title="Mariquita — control biológico" loading="lazy" />
      </div>
      <div>
        <img class="img" src="/imagenes/blog/detalle/mariquita2.avif" alt="Taller infantil de educación ambiental construyendo hoteles de insectos y casitas para mariquitas" title="Taller — casitas para mariquitas" loading="lazy" />
      </div>
      <div>
        <img class="img" src="/imagenes/blog/detalle/mariquita3.avif" alt="Detalle de varias mariquitas buscando pulgones en su hábitat natural" title="Mariquitas en su hábitat" loading="lazy" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

// URL optimizada (coincide con el router)
const pageUrl = 'https://www.geobizi.com/blog/mariquitas'
const ogImage = 'https://www.geobizi.com/imagenes/blog/detalle/mariquita1.avif'

useHead({
  // Título SEO
  title: 'La Importancia de las Mariquitas: Control Biológico | Geobizi',
  meta: [
    { name: 'description', content: 'Descubre por qué las mariquitas (marigorringo) son esenciales como control biológico contra pulgones en huertas, su valor ecológico y nuestros talleres infantiles.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Las Mariquitas: Aliadas de la biodiversidad y la huerta | Geobizi' },
    { property: 'og:description', content: 'Control biológico, educación ambiental y talleres infantiles sobre mariquitas ofrecidos por Geobizi.' },
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
        "headline": "La Importancia de las Mariquitas en el medioambiente y la biodiversidad",
        "description": "Descubre por qué las mariquitas son esenciales como depredadoras de pulgones y bioindicadoras de salud ambiental.",
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
          // Redes sociales (TikTok añadido)
          "sameAs": [
            "https://www.facebook.com/geobizirik/",
            "https://www.instagram.com/geotxiki/",
            "https://www.tiktok.com/@geobizi",
            "https://www.youtube.com/channel/UCw-C_J0y-jKHp7Zx92lsKfg"
          ]
        },
        // Fechas requeridas para SEO
        "datePublished": "2024-03-10T08:00:00+01:00",
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
/* Iconos de redes sociales */
.social-icon {
  width: 2.5rem;
  margin: 0.5rem 1rem 1.5rem 0;
  transition: transform 0.3s;
}
.social-icon:hover {
  transform: scale(1.1);
}

.social-media {
  margin-top: 2rem;
  color: var(--darkgrey);
}
.redes-sociales{
  margin-left: 1rem;
}
/* Caja de recursos (Tienda/Talleres) */
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