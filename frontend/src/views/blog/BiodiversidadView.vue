<template>
  <div class="contenedor-principal">
    <h1>La Importancia de la Biodiversidad en la Lucha contra el Cambio Climático</h1>

    <p>
      La <strong>biodiversidad</strong> es la increíble variedad de formas de vida en
      nuestro planeta, desde las más pequeñas bacterias del suelo hasta las majestuosas
      especies de mamíferos y los frondosos bosques de nuestra geografía. Esta diversidad
      no es un simple catálogo de la naturaleza; es una red esencial para mantener el equilibrio de los ecosistemas y brindar una
      serie de beneficios fundamentales para la supervivencia humana. Sin embargo, la
      biodiversidad se encuentra gravemente amenazada debido a la actual crisis climática,
      lo que subraya la urgencia de actuar local y globalmente para preservarla.
    </p>

    <h2>El Impacto del Cambio Climático en la Biodiversidad</h2>
    <p>
      El <strong>cambio climático</strong> es uno de los mayores desafíos que
      enfrentamos en la actualidad. El aumento de las temperaturas globales, la alteración
      de los regímenes de lluvias y los eventos climáticos extremos (como sequías prolongadas
      o inundaciones) ya están alterando nuestros paisajes. Estos cambios rápidos destruyen hábitats,
      desincronizan los ciclos de polinización y migración, y empujan a numerosas especies vulnerables hacia la
      <strong>extinción</strong>.
    </p>

    <h2>La Biodiversidad: Nuestro Mejor Escudo Climático</h2>
    <p>
      Lejos de ser solo una víctima, la biodiversidad es nuestra herramienta más poderosa para la
      <strong>mitigación</strong> y adaptación al cambio climático. Los
      ecosistemas saludables, maduros y diversos tienen una enorme resiliencia (capacidad para resistir
      y recuperarse de los impactos).
    </p>
    <p>
      Los <strong>bosques autóctonos</strong> y las zonas húmedas actúan como inmensos sumideros de carbono,
      absorbiendo grandes cantidades de dióxido de carbono de la atmósfera y
      almacenándolo en la biomasa y el suelo. Proteger y restaurar estos espacios (como promovemos en proyectos locales tipo Zalla Natura) es la tecnología natural más eficiente para combatir el calentamiento global.
    </p>

    <h2>Seguridad Alimentaria y Diversidad Genética</h2>
    <p>
      La biodiversidad es también la base indiscutible de nuestra
      <strong>seguridad alimentaria</strong> y de una agricultura sostenible. Las
      variedades de cultivos locales y las especies animales domesticadas dependen de la
      <strong>diversidad genética</strong> silvestre. Si permitimos que el cambio climático y el monocultivo arrasen con esta diversidad, nuestros sistemas alimentarios serán extremadamente vulnerables a nuevas enfermedades y plagas, poniendo en riesgo el suministro global de alimentos.
    </p>

    <h2>Servicios Ecosistémicos Vitales para la Sociedad</h2>
    <p>
      Más allá del carbono y los alimentos, la biodiversidad nos regala
      <strong>servicios ecosistémicos</strong> invisibles pero vitales:
    </p>
    <ul>
      <li><strong>Polinización:</strong> Insectos como abejas, mariposas y mariquitas garantizan la reproducción de la flora y la producción de frutas y verduras.</li>
      <li><strong>Protección frente a desastres:</strong> Ecosistemas costeros (como los estuarios y marismas) y bosques de ribera actúan como esponjas y barreras naturales, mitigando el impacto de tormentas e inundaciones.</li>
      <li><strong>Regulación del ciclo del agua:</strong> Los bosques sanos filtran el agua, recargan los acuíferos y evitan la erosión y desertificación del suelo.</li>
    </ul>

    <h2>Un Círculo Vicioso o Virtuoso</h2>
    <p>
      La pérdida de biodiversidad y el cambio climático están estrechamente
      interconectados. El cambio climático destruye ecosistemas, lo que libera más carbono a la atmósfera y acelera aún más el calentamiento global. A su vez, un ecosistema degradado pierde su capacidad de protegernos frente a los extremos climáticos. Romper este círculo vicioso y convertirlo en uno virtuoso mediante la <strong>restauración ecológica</strong> es la gran tarea de nuestra generación.
    </p>

    <div class="caja-recurso">
      <h3>Pasa a la acción con Geobizi</h3>
      <p>
        Entender el problema es solo el primer paso. En Geobizi trabajamos activamente en la <strong>educación ambiental, la sensibilización y el desarrollo de proyectos locales</strong> para fomentar y proteger la biodiversidad de Bizkaia.
      </p>
      <div class="botones-recurso">
        <a href="/proyectos" class="proximas-actividades">Descubre nuestros Proyectos</a>
        <a href="/contacto" class="btn-ver-mas">Contacta con nosotros</a>
      </div>
    </div>

    <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/blog/detalle/mariposas.avif"
          alt="Mariposas observadas durante el proyecto Zalla Natura, excelentes bioindicadoras de la salud del ecosistema"
          title="Mariposas — biodiversidad local"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/blog/detalle/ajenuz.avif"
          alt="Flor de Ajenuz en su hábitat natural, un ejemplo de la importante flora autóctona local"
          title="Ajenuz — flora autóctona"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/blog/detalle/plantando.avif"
          alt="Grupo de personas participando en una plantación comunitaria para la restauración de hábitats"
          title="Plantación comunitaria — restauración"
          loading="lazy"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

// URL optimizada (coincide con el router)
const pageUrl = 'https://www.geobizi.com/blog/biodiversidad'
const ogImage = 'https://www.geobizi.com/imagenes/blog/detalle/mariposas.avif'

useHead({
  // Título SEO
  title: 'La Importancia de la Biodiversidad frente al Cambio Climático | Geobizi',
  meta: [
    { name: 'description', content: 'Descubre cómo la biodiversidad es nuestro mejor escudo contra la crisis climática y por qué proteger y restaurar los ecosistemas es clave para nuestro futuro.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Biodiversidad y Cambio Climático: Nuestro futuro interconectado | Geobizi' },
    { property: 'og:description', content: 'Explora la conexión vital entre ecosistemas saludables y la mitigación de la crisis climática.' },
    { property: 'og:type', content: 'article' },
    { property: 'og:url', content: pageUrl },
    { property: 'og:image', content: ogImage },
    { name: 'twitter:card', content: 'summary_large_image' },
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
        "headline": "La Importancia de la Biodiversidad en Relación con el Cambio Climático",
        "description": "Explora la relación entre biodiversidad y cambio climático, los servicios ecosistémicos vitales y estrategias de conservación y restauración.",
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
          // Redes sociales, incluido TikTok
          "sameAs": [
            "https://www.facebook.com/geobizirik/",
            "https://www.instagram.com/geotxiki/",
            "https://www.tiktok.com/@geobizi",
            "https://www.youtube.com/channel/UCw-C_J0y-jKHp7Zx92lsKfg"
          ]
        },
        // Fechas requeridas para el Schema Article
        "datePublished": "2023-11-05T08:00:00+01:00",
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
/* Reutilizamos los estilos corporativos para la caja CTA y botones */
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