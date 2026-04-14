<template>
  <div class="contenedor-principal">
    <h1>¿Qué son los fósiles y cómo se forman?</h1>

    <p>Los <strong>fósiles</strong> son los restos, huellas o evidencias de organismos (animales, plantas o microbios) que vivieron en la Tierra en el pasado. Estos increíbles "mensajes en la piedra" son fundamentales para que los paleontólogos puedan comprender la <strong>evolución</strong> de la vida en nuestro planeta y cómo han cambiado los ecosistemas a lo largo de millones de años.</p>
    
    <h2>El mágico proceso de la fosilización</h2>
    <p>Para que un ser vivo se convierta en fósil, debe darse una serie de coincidencias casi milagrosas. Generalmente, cuando un organismo muere, se descompone o es devorado. Sin embargo, la fosilización ocurre cuando esos restos quedan rápidamente enterrados bajo capas de arena, barro o ceniza, aislándolos del oxígeno y frenando su descomposición.</p>
    
    <p>Con el paso del tiempo, el peso de los sedimentos y el agua subterránea someten a los restos a procesos químicos y físicos que los preservan. Los más comunes son:</p>

    <ul>
      <li><strong>Mineralización (Petrificación):</strong> Es el proceso más habitual. A medida que el hueso o la madera original se disuelve lentamente, los minerales presentes en el agua (como el sílice o el calcio) ocupan su lugar. El resultado es una réplica exacta del organismo original, ¡pero hecha de piedra!</li>
      <li><strong>Preservación en ámbar:</strong> Ocurre cuando pequeños insectos o restos vegetales quedan atrapados en la resina pegajosa de los árboles prehistóricos. La resina se endurece y se convierte en ámbar, conservando al organismo intacto con un detalle asombroso.</li>
      <li><strong>Congelación:</strong> En zonas de permafrost (hielo permanente), se han hallado mamuts enteros conservando no solo los huesos, sino también la piel, los órganos y el pelo.</li>
    </ul>
    
    <h2>No todo son huesos de dinosaurio</h2>
    <p>Cuando pensamos en fósiles, a menudo nos imaginamos gigantescos esqueletos de dinosaurios, pero la realidad es mucho más diversa:</p>
    <ul>
      <li><strong>Microfósiles:</strong> Caparazones de menos de 1 milímetro pertenecientes a plancton prehistórico (muy comunes en los acantilados de nuestra costa vasca).</li>
      <li><strong>Fósiles vegetales:</strong> Impresiones perfectas de hojas de helechos gigantes o troncos petrificados.</li>
      <li><strong>Icnitas:</strong> A veces, lo que se fosiliza no es el animal en sí, sino una <em>marca de su actividad</em>. Esto incluye huellas de pisadas conservadas en el barro solidificado, madrigueras e incluso excrementos fosilizados (coprolitos).</li>
    </ul>
    
    <h2>El trabajo de los Paleontólogos</h2>
    <p>Para encontrar fósiles, los paleontólogos exploran las rocas sedimentarias expuestas en acantilados, desiertos y montañas. Cada capa de roca actúa como la página de un libro de historia geológica. Al estudiar los fósiles encontrados en capas específicas, los científicos pueden reconstruir cómo era el clima, qué animales convivían y cómo se relacionaban hace millones de años.</p>

    <div class="caja-recurso">
      <h3>¡Conviértete en Paleontólogo por un día!</h3>
      <p>
        La mejor forma de aprender ciencia es tocándola. En las actividades y talleres de Geobizi te enseñamos fósiles reales traídos de diferentes partes del mundo y te enseñamos a analizarlos "in situ". Además, en nuestros <strong>talleres infantiles</strong>, los más pequeños podrán crear sus propias réplicas de fósiles para llevárselas a casa.
      </p>
<div class="botones-recurso">
        <a href="/calendario" class="proximas-actividades">Ver próximas actividades</a>
        <a href="/contacto" class="btn-ver-mas">Pedir información para grupos</a>
      </div>
    </div>

    <p class="social-media"><b>¿Te animas a experimentar con nosotros? ¡Síguenos en redes sociales para ver nuestros próximos talleres!</b></p>
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
          src="/imagenes/blog/detalle/fosil1.avif"
          alt="Fósil de un ammonite perfectamente conservado incrustado en roca sedimentaria"
          title="Fósil mineralizado en roca"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/blog/detalle/fosil2.avif"
          alt="Niños participando en un taller didáctico de Geobizi creando réplicas de fósiles con escayola"
          title="Taller infantil de réplicas de fósiles"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/blog/detalle/fosil3.avif"
          alt="Fotografía macro mostrando el detalle de las texturas preservadas en un fósil antiguo"
          title="Texturas y detalles de un fósil"
          loading="lazy"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

// URL optimizada (coincide con el router)
const pageUrl = 'https://www.geobizi.com/blog/fosiles'
const ogImage = 'https://www.geobizi.com/imagenes/blog/detalle/fosil1.avif'

useHead({
  // Título SEO
  title: '¿Qué son los Fósiles y cómo se forman? | Divulgación Geobizi',
  meta: [
    { name: 'description', content: 'Aprende qué son los fósiles, cómo se produce la fosilización (mineralización, ámbar, icnitas) y descubre nuestros talleres de paleontología para niños.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: '¿Qué son los fósiles y cómo se forman? | Geobizi' },
    { property: 'og:description', content: 'Descubre los secretos de la paleontología, el proceso de fosilización y nuestros talleres educativos.' },
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
        "headline": "¿Qué son los fósiles y cómo se forman?",
        "description": "Explicación sencilla y didáctica sobre qué son los fósiles, procesos de formación como la mineralización y su importancia paleontológica.",
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
        "datePublished": "2023-08-15T08:00:00+01:00",
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