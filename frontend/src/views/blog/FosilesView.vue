<template>
    <div class="contenedor-principal">
      <h1>¿Qué son los fósiles y cómo se forman?</h1>

      <p>Los <strong>fósiles</strong> son restos o huellas de organismos que vivieron en la Tierra en el pasado. Estos restos son importantes para comprender la <strong>evolución</strong> de la vida en nuestro planeta y cómo han cambiado los ecosistemas a lo largo del tiempo.</p>
      
      <p>Se forman cuando los restos o marcas de vida de un organismo se conservan en sedimentos que se acumulan. Los restos se entierran y se someten a una serie de procesos químicos y físicos que pueden preservarlos a lo largo del tiempo.</p>
      
      <p>Uno de los procesos más comunes es la <strong>mineralización</strong>, en la que los restos se reemplazan por minerales a medida que se disuelve la materia orgánica o los elementos que conforman el organismo. Esto crea una réplica mineralizada, que puede durar millones de años. Otro proceso conocido es la <strong>preservación en ámbar</strong>, donde los organismos se quedan atrapados en la savia de los árboles y se conservan a lo largo del tiempo.</p>
      
      <p>Los <strong>fósiles</strong> pueden ser restos de animales, plantas e incluso microorganismos. Los restos pueden ser muy pequeños, como dientes o huesos, incluso caparazones de menos de 1 mm o muy grandes, como los restos de dinosaurios. También pueden ser huellas, como las huellas de pies de animales que se conservan en rocas sedimentarias o marcas de vida (<strong>Icnitas</strong>).</p>
      
      <p>¡Este proceso puede preservar no solo los huesos o caparazones, sino también los tejidos blandos y las plumas!</p>
      
      <p>Para encontrar <strong>fósiles</strong>, los paleontólogos exploran rocas sedimentarias y buscan signos de vida antigua. A menudo, se encuentran en capas geológicas específicas que se formaron en diferentes períodos de tiempo. Al estudiar estos <strong>fósiles</strong>, los científicos pueden aprender sobre la historia de la vida en la Tierra y cómo ha cambiado a lo largo del tiempo.</p>
      
      <p>Los <strong>fósiles</strong> son importantes para entender cómo ha evolucionado la vida en nuestro planeta. A través de la preservación de restos y huellas de organismos antiguos, los científicos pueden aprender sobre la <strong>diversidad de la vida</strong> en diferentes épocas y cómo los ecosistemas han cambiado a lo largo del tiempo e incluso saber cómo vivían y se relacionaban en el pasado diferentes especies.</p>
      
      <p>En nuestras actividades, puedes ver diferentes tipos de <strong>fósiles</strong> “in situ”, traídos, e incluso puedes participar en los talleres de creación de <strong>fósiles</strong> y réplicas. Puedes ver las próximas actividades a las que te puedes apuntar en nuestra tienda online: <a href="https://www.geobizi.com/geotienda/" target="_blank">https://www.geobizi.com/geotienda/</a></p>
      
      <p>¿Te animas a experimentar con nosotr@s?</p>
      <div class="imagen-trio">
      <div>
              <img
        class="img"
        src="/imagenes/blog/detalle/fosil1.avif"
        alt="Fósil en sedimento — ejemplo de conservación"
        title="Fósil — ejemplo en campo"
        loading="lazy"
      />
      </div>
      <div>
              <img
        class="img"
        src="/imagenes/blog/detalle/fosil2.avif"
        alt="Taller de réplicas de fósiles — actividad didáctica"
        title="Taller de fósiles — réplica"
        loading="lazy"
      />
      </div>
      <div>
              <img
        class="img"
        src="/imagenes/blog/detalle/fosil3.avif"
        alt="Detalle de un fósil — textura y forma preservada"
        title="Detalle de fósil"
        loading="lazy"
      />
      </div>

      </div>
    </div>
  </template>
  
  <script setup>
import { useHead } from '@vueuse/head' // añadido

const pageUrl = 'https://www.geobizi.com/blog/detalle-fosiles'
const ogImage = 'https://www.geobizi.com/imagenes/blog/detalle/fosil1.avif'

useHead({
  title: '¿Qué son los fósiles y cómo se forman? | GeoBizi',
  meta: [
    { name: 'description', content: 'Explicación sencilla sobre qué son los fósiles, procesos de formación y su importancia para la paleontología.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'GeoBizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: '¿Qué son los fósiles y cómo se forman? | GeoBizi' },
    { property: 'og:description', content: 'Aprende sobre la formación de fósiles y su relevancia científica para comprender la historia de la vida.' },
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
            "name":"GeoBizi",
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
            "headline":"¿Qué son los fósiles y cómo se forman?",
            "description":"Explicación sencilla sobre qué son los fósiles, procesos de formación y su importancia para la paleontología.",
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