<template>
    <div class="contenedor-principal">
      <h1>Carpobrotus edulis, planta invasora muy perjudicial</h1>
      <h2>Carpobrotus edulis, una especie originaria de Sudáfrica que resulta ser invasora en muchas partes de nuestro planeta.</h2>
      
      <h3>Introducción:</h3>
      <p>A pesar de su atractivo aspecto y su capacidad para crecer en condiciones difíciles, <strong>Carpobrotus edulis</strong> puede ser extremadamente perjudicial para los ecosistemas locales. Es conocida como <strong>Uña de gato</strong> y su nombre científico viene del griego karpos (fruta) y brota (comestible) que significa "con frutos comestibles" y edulis es un epíteto latino que significa "comestible".</p>
      
      <p><strong>Carpobrotus edulis</strong> es una planta suculenta que crece en matas densas y compactas de hojas carnosas de color verde-azulado. Las flores son grandes y brillantes, con pétalos de color amarillo, rosa o rojo. La planta produce un fruto comestible similar a una baya que se utiliza a menudo en mermeladas y conservas.</p>
      
      <p>La planta es muy resistente y puede sobrevivir en una amplia gama de condiciones, incluyendo suelos pobres y secos, así como en zonas costeras y de dunas de arena. Esta capacidad de adaptación ha permitido que <strong>Carpobrotus edulis</strong> se propague rápidamente en muchos lugares, incluyendo Europa, América del Norte, Australia y Nueva Zelanda.</p>
      
      <p>Sin embargo, a pesar de su atractivo y de sus cualidades adaptativas, <strong>Carpobrotus edulis</strong> puede ser muy dañina para los ecosistemas locales. Su rápida propagación y su capacidad para desplazar a las plantas nativas pueden reducir la <strong>diversidad vegetal</strong> y afectar la fauna local.</p>
      
      <p>Además, <strong>Carpobrotus edulis</strong> también puede tener un impacto en la <strong>erosión del suelo</strong> y en la propagación de incendios. Debido a que forma densas matas y reduce la <strong>diversidad vegetal</strong>, la planta puede aumentar la cantidad de combustible disponible para los incendios forestales.</p>
      
      <p>En muchos lugares, los esfuerzos para controlar <strong>Carpobrotus edulis</strong> se han centrado en la eliminación física de la planta y en la restauración de los ecosistemas locales. Esto puede implicar la eliminación manual de las plantas, el uso de herbicidas o la introducción de especies nativas para competir con <strong>Carpobrotus edulis</strong>.</p>
      
      <p>Es una de las especies incluidas en el Catálogo Español de Especies Exóticas Invasoras, (regulado por el Real Decreto 630/2013, de 2 de agosto). En España está prohibida su introducción en el medio natural, posesión, transporte, tráfico y comercio.</p>
      
      <p>Por lo tanto, a pesar de que la <strong>Carpobrotus edulis</strong> puede ser una planta atractiva y resistente, también puede tener un impacto significativo en los ecosistemas locales. Es importante tomar medidas para controlar su propagación y restaurar la <strong>diversidad vegetal</strong> en las áreas afectadas por su presencia.</p>
      
      <p>Por favor, no siembres o propagues plantas invasoras. ¡Pueden hacer mucho daño!</p>
      <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/blog/detalle/carpobrotus1.jpeg"
          alt="Carpobrotus edulis — manto invasor en dunas y costas"
          title="Carpobrotus edulis — invasora en dunas"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/blog/detalle/carpobrotus2.jpg"
          alt="Carpobrotus edulis desplazando flora nativa"
          title="Impacto de Carpobrotus en flora autóctona"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/blog/detalle/carpobrotus3.jpg"
          alt="Ejemplo de control y restauración tras Carpobrotus"
          title="Control y restauración tras presencia de Carpobrotus"
          loading="lazy"
        />
      </div>

    </div>
    </div>
  </template>
  
  <script setup>
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/blog/detalle-carpobrotus'
const ogImage = 'https://www.geobizi.com/imagenes/blog/detalle/carpobrotus1.jpeg'

useHead({
  title: 'Carpobrotus edulis — Planta invasora | Geobizi',
  meta: [
    { name: 'description', content: 'Impacto ecológico de Carpobrotus edulis y medidas de control para proteger la biodiversidad costera.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Carpobrotus edulis — Planta invasora | Geobizi' },
    { property: 'og:description', content: 'Cómo identificar, controlar y restaurar áreas afectadas por Carpobrotus edulis.' },
    { property: 'og:type', content: 'article' },
    { property: 'og:url', content: pageUrl },
    { property: 'og:image', content: ogImage },
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:image', content: ogImage }
  ],
  link: [
    { rel: 'canonical', href: pageUrl },
    { rel: 'image_src', href: ogImage },
    { rel: 'apple-touch-icon', href: '/apple-touch-icon.png', sizes: '180x180' }
  ],
  script: [
    {
      type: 'application/ld+json',
      children: JSON.stringify({
        "@context":"https://schema.org",
        "@graph":[
          {
            "@type":"Organization",
            "@id":"https://www.geobizi.com/#organization",
            "name":"Geobizi",
            "url":"https://www.geobizi.com",
            "logo": { "@type":"ImageObject","url":"https://www.geobizi.com/imagenes/GeobiziLogo.7ae1d6ce.png","width":1417,"height":313 },
            "sameAs":[
              "https://www.facebook.com/geobizirik/",
              "https://www.instagram.com/geotxiki/",
              "https://www.youtube.com/channel/UCw-C_J0y-jKHp7Zx92lsKfg"
            ]
          },
          {
            "@type":"Article",
            "headline":"Carpobrotus edulis, planta invasora muy perjudicial",
            "description":"Impacto ecológico de Carpobrotus edulis y medidas de control para proteger la biodiversidad costera.",
            "author": { "@type":"Organization", "@id":"https://www.geobizi.com/#organization" },
            "mainEntityOfPage": { "@type":"WebPage", "@id": pageUrl },
            "image": { "@type":"ImageObject","url":ogImage,"width":1080,"height":1080 },
            "inLanguage":"es"
          }
        ]
      })
    }
  ]
})
  </script>
  
  <style scoped>

  </style>