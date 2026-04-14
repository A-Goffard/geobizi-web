<template>
    <div class="contenedor-principal">
        <h1>La formación de los estuarios: Donde el río y el mar se abrazan</h1>

        <p>Los <strong>estuarios</strong> son <strong>ecosistemas únicos</strong> y fascinantes que se forman en las desembocaduras de los ríos, donde las aguas dulces y saladas se mezclan. Estas áreas costeras son de gran importancia tanto para la <strong>vida acuática</strong> como para los seres humanos, ya que albergan una <strong>biodiversidad excepcional</strong> y brindan una serie de servicios ecosistémicos vitales.</p>

        <p>En nuestro entorno más cercano, en la costa vasca, tenemos ejemplos magníficos de este fenómeno geológico y biológico, como la <strong>Ría de Urdaibai</strong> (Reserva de la Biosfera) o el <strong>estuario de Plentzia</strong>. Vamos a descubrir sus características distintivas y su papel crucial en el <strong>equilibrio ecológico</strong>.</p>

        <h2>Características principales de los estuarios</h2>
        <p>Los <strong>estuarios</strong> son el punto exacto de encuentro entre el <strong>agua dulce y salada</strong>. Estas áreas geográficas se caracterizan por su constante variación de <strong>salinidad</strong> y por estar fuertemente influenciadas por las <strong>mareas</strong>, lo que les confiere unas condiciones ambientales muy exigentes pero ricas. Desde pequeñas bahías hasta amplias rías, los estuarios presentan una gran variedad de tamaños y formas.</p>

        <h2>¿Cómo se forma un estuario?</h2>
        <p>Los procesos de <strong>formación de los estuarios</strong> son graduales. Todo comienza con la erosión y el transporte de <strong>sedimentos</strong> (arenas, limos y arcillas) por parte del río en su viaje desde las montañas. Al acercarse al océano, la pendiente disminuye y la fuerza de las <strong>mareas</strong> frena la corriente del río. Esta pérdida de velocidad provoca que los sedimentos caigan al fondo y se acumulen, creando <strong>bancos de arena</strong>, marismas y llanuras intermareales que cambian de aspecto cada seis horas.</p>

        <h2>La danza de las mareas</h2>
        <p>La <strong>influencia de las mareas</strong> es el verdadero motor del estuario. Durante la pleamar (marea alta), el océano empuja el agua salada tierra adentro, inundando las marismas. Durante la bajamar (marea baja), el río recupera su fuerza y empuja el agua dulce hacia el mar. Este constante "lavado" y mezcla de nutrientes convierte a los estuarios en una de las zonas más fértiles del planeta.</p>

        <h2>Importancia ecológica: Las "guarderías" del mar</h2>
        <p>La mezcla de aguas crea hábitats únicos que funcionan como verdaderas <strong>"guarderías" marinas</strong>. Muchos peces, crustáceos y moluscos acuden a desovar a los estuarios porque sus aguas tranquilas y ricas en nutrientes ofrecen un refugio seguro para los alevines. Además, son puntos de descanso y alimentación cruciales para miles de <strong>aves migratorias</strong> en sus largos viajes continentales. Por si fuera poco, la vegetación de las marismas actúa como un filtro natural, purificando el agua antes de que llegue al mar abierto.</p>

        <h2>Amenazas y conservación</h2>
        <p>A pesar de su incalculable valor, los estuarios son ecosistemas extremadamente vulnerables a la presión humana. Las principales amenazas a las que se enfrentan hoy en día son:</p>
        <ul>
            <li><strong>La contaminación:</strong> Vertidos industriales, plásticos y exceso de fertilizantes agrícolas que bajan por el río.</li>
            <li><strong>La presión urbanística:</strong> La desecación de marismas para construir puertos, paseos o edificaciones reduce drásticamente el espacio natural.</li>
            <li><strong>El cambio climático:</strong> El aumento del nivel del mar amenaza con ahogar las zonas intermareales.</li>
        </ul>

        <div class="caja-recurso">
            <h3>Acercamos la ciencia a las aulas y a la calle</h3>
            <p>
                La conservación de ecosistemas tan complejos como los estuarios solo es posible a través de la <strong>educación medioambiental</strong>. En Geobizi desarrollamos programas de sensibilización, talleres didácticos y salidas de campo para que estudiantes y familias comprendan y valoren nuestro entorno natural.
            </p>
            <div class="botones-recurso">
                <a href="/servicios" class="proximas-actividades">Descubre nuestros Servicios</a>
                <a href="/contacto" class="btn-ver-mas">Contacta con nosotros</a>
            </div>
        </div>

        <div class="imagen-trio">
            <div>
                <img class="img" src="/imagenes/blog/detalle/estuario1.avif" alt="Vista aérea de un estuario mostrando los canales y la mezcla de agua dulce y salada" title="Morfología de un estuario" loading="lazy" />
            </div>
            <div>
                <img class="img" src="/imagenes/blog/detalle/estuario2.avif" alt="Bandada de aves alimentándose en la zona intermareal de una marisma" title="Aves en la marisma" loading="lazy" />
            </div>
            <div>
                <img class="img" src="/imagenes/blog/detalle/estuario3.avif" alt="Detalle de flora adaptada a la salinidad (plantas halófitas) en un entorno costero" title="Flora de estuario" loading="lazy" />
            </div>
        </div>
    </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

// URL optimizada (coincide con el router)
const pageUrl = 'https://www.geobizi.com/blog/estuarios'
const ogImage = 'https://www.geobizi.com/imagenes/blog/detalle/estuario1.avif'

useHead({
  // Título SEO
  title: 'La formación de los Estuarios: Ecología y Biodiversidad | Geobizi',
  meta: [
    { name: 'description', content: 'Descubre qué son los estuarios, cómo se forman en la desembocadura de los ríos y por qué son vitales para la biodiversidad y la costa de Bizkaia.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Estuarios: Donde el río y el mar se abrazan | Geobizi' },
    { property: 'og:description', content: 'Conoce la dinámica de las mareas, la formación de las marismas y la importancia ecológica de los estuarios.' },
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
        "headline": "La formación de los estuarios: donde el mar y el río se encuentran",
        "description": "Qué son los estuarios, su formación, dinámica de mareas, importancia ecológica y amenazas para la biodiversidad costera.",
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
          // AÑADIDO TIKTOK AL SCHEMA
          "sameAs": [
            "https://www.facebook.com/geobizirik/",
            "https://www.instagram.com/geotxiki/",
            "https://www.tiktok.com/@geobizi",
            "https://www.youtube.com/channel/UCw-C_J0y-jKHp7Zx92lsKfg"
          ]
        },
        // Fechas requeridas para SEO (puedes ajustar la fecha de publicación original)
        "datePublished": "2023-09-10T08:00:00+01:00",
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