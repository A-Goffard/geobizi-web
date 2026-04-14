<template>
  <div class="contenedor-principal">
    <h1>Flora Autóctona: La importancia vital de cuidarla y restaurarla</h1>
    
    <p>Para conservar la <strong>biodiversidad</strong> de nuestro planeta y garantizar el equilibrio de los ecosistemas, es esencial proteger nuestra <strong>flora autóctona</strong>. Definimos como flora autóctona o nativa a aquella que se encuentra en un territorio de manera natural y que ha evolucionado durante miles de años adaptándose al clima, a la orografía y a las condiciones específicas del suelo de la región (en nuestro caso, el clima y los suelos de Bizkaia y la cornisa cantábrica).</p>

    <h2>¿Por qué son tan importantes las plantas nativas?</h2>
    <p>Las especies vegetales propias de un lugar no son solo el "decorado" del paisaje; son el motor del ecosistema. Sus beneficios son irremplazables:</p>
    <ul>
      <li><strong>Base alimentaria:</strong> Son el alimento específico de innumerables insectos (polinizadores), aves y mamíferos locales que han evolucionado junto a ellas.</li>
      <li><strong>Hábitat ideal:</strong> Proporcionan el refugio perfecto para la fauna nativa, permitiendo su nidificación y desarrollo.</li>
      <li><strong>Resiliencia climática:</strong> Al estar adaptadas históricamente a nuestro clima, soportan mejor las sequías estivales o las fuertes lluvias sin necesidad de riegos artificiales o cuidados extra.</li>
      <li><strong>Protección del suelo:</strong> Sus sistemas de raíces previenen la erosión de laderas y riberas de forma mucho más eficiente que las especies ornamentales.</li>
    </ul>

    <h2>El peligro silencioso de las especies exóticas</h2>
    <p>Lamentablemente, la falta de conciencia, la globalización y el impacto humano han hecho que muchas especies autóctonas estén hoy en día en peligro. Las plantas exóticas (especies foráneas introducidas por el ser humano para jardinería o explotación, como la Uña de gato, el Plumero de la Pampa o ciertas coníferas) compiten agresivamente por la luz, el agua y los nutrientes.</p>
    
    <p>Al no tener depredadores naturales en nuestro territorio, estas especies invasoras se descontrolan y acaban desplazando a la flora autóctona, silenciando el bosque y alterando drásticamente el <strong>equilibrio natural del ecosistema</strong>.</p>

    <h2>Restauración Ecológica: Devolver la vida al territorio</h2>
    <p>A la hora de proteger nuestro entorno, no basta solo con conservar las manchas de bosque nativo que aún nos quedan; debemos ser proactivos y <strong>recuperar</strong> los espacios que han sido degradados, deforestados o invadidos. La siembra y plantación de especies autóctonas mediante proyectos de restauración es fundamental para sanar la tierra.</p>
    
    <p>Es responsabilidad de todos —administraciones, empresas y ciudadanos— promover la <strong>educación ambiental</strong> y crear conciencia sobre el valor de nuestros robledales, hayedos, encinares cantábricos y marismas.</p>

    <div class="caja-recurso">
      <h3>¿Te unes a nuestras Plantaciones Regenerativas?</h3>
      <p>
        Una de las formas más bonitas y directas de ayudar al medioambiente es participando en una <strong>plantación regenerativa o voluntariado ambiental</strong>. En Geobizi organizamos jornadas colaborativas para reestructurar suelos degradados plantando flora autóctona. Conocerás a personas con tus mismas inquietudes, disfrutarás de la naturaleza y dejarás un legado vivo para el futuro.
      </p>
      <div class="botones-recurso">
        <a href="/proyectos" class="proximas-actividades">Descubre nuestros Proyectos</a>
        <a href="/contacto" class="btn-ver-mas">Apúntate como voluntario/a</a>
      </div>
    </div>

    <p class="social-media"><b>¡Síguenos en nuestras redes sociales para enterarte de las próximas fechas de plantación y voluntariado!</b></p>
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
          src="/imagenes/blog/detalle/plantacion1.avif"
          alt="Voluntarios preparando el terreno para una plantación con especies de flora autóctona"
          title="Preparación del terreno - Flora autóctona"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/blog/detalle/plantacion2.avif"
          alt="Restauración de un hábitat degradado mediante la reforestación con plantas nativas"
          title="Restauración ecológica"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/blog/detalle/plantacion3.avif"
          alt="Grupo de personas colaborando en una jornada de voluntariado ambiental plantando árboles locales"
          title="Voluntariado ambiental"
          loading="lazy"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

// URL optimizada (coincide con el router)
const pageUrl = 'https://www.geobizi.com/blog/flora-autoctona'
const ogImage = 'https://www.geobizi.com/imagenes/blog/detalle/plantacion1.avif'

useHead({
  // Título SEO
  title: 'Flora Autóctona: Conservación y Restauración Ecológica | Geobizi',
  meta: [
    { name: 'description', content: 'Descubre por qué es vital proteger la flora autóctona frente a las especies invasoras y cómo puedes participar en las plantaciones regenerativas de Geobizi.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Flora Autóctona: El motor de nuestra biodiversidad | Geobizi' },
    { property: 'og:description', content: 'Aprende sobre la importancia ecológica de las plantas nativas y apúntate a nuestros voluntariados de restauración.' },
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
        "headline": "Flora autóctona: la importancia vital de cuidarla y restaurarla",
        "description": "Por qué proteger la flora autóctona es clave para la biodiversidad local, los peligros de las plantas invasoras y métodos para recuperar ecosistemas degradados.",
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
        "datePublished": "2023-10-22T08:00:00+01:00",
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
  width: 2.5rem; 
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