<template>
    <div class="contenedor-principal">
      <h1>Flora autóctona: la importancia de cuidarla</h1>
      

      <p>Para conservar la <strong>biodiversidad</strong> de nuestro planeta y el equilibrio de los ecosistemas, es esencial proteger la <strong>flora autóctona</strong>. La <strong>flora autóctona</strong> es aquella que se encuentra en un territorio de manera natural, adaptada al clima y al suelo de la región. Estas plantas son esenciales para la fauna local, ya que son la base de su alimentación y proporcionan el hábitat ideal para su desarrollo.</p>
      
      <p>Lamentablemente, la falta de conciencia y el impacto humano han hecho que muchas especies autóctonas estén en peligro de extinción. Las plantas exóticas, introducidas por el ser humano, compiten por los mismos recursos naturales y pueden desplazar a la <strong>flora autóctona</strong>, alterando el <strong>equilibrio natural del ecosistema</strong>.</p>
      
      <p>A la hora de proteger la <strong>flora autóctona</strong>, no solo se trata de conservar la que ya hay, sino también recuperarla en los espacios en los que ha sido degradada o desplazada. La plantación de especies autóctonas y su cultivo responsable es fundamental para recuperar el <strong>equilibrio del ecosistema</strong> y evitar la <strong>erosión del suelo</strong>.</p>
      
      <p>Es responsabilidad de cada uno de nosotros cuidar y proteger la <strong>flora autóctona</strong>, respetando su ciclo de vida y evitando su deterioro. Se deben promover políticas públicas de protección y conservación, fomentar la <strong>educación ambiental</strong> y crear conciencia social sobre la importancia de mantener la diversidad y el equilibrio del ecosistema.</p>
      
      <p>Proteger la <strong>flora autóctona</strong> es esencial para el mantenimiento del <strong>equilibrio ecológico</strong>, la conservación de la <strong>biodiversidad</strong> y el bienestar de la sociedad. Cada uno de nosotros podemos hacer nuestra parte para preservar y cuidar nuestro entorno natural para las generaciones futuras.</p>
      
      <p>¿Te animas a participar en una <strong>plantación regenerativa</strong>? Es una buena manera de ayudar a reestructurar suelos degradados y reequilibrar el <strong>ecosistema natural</strong> de la zona. En este tipo de actividades colaborativas, conocerás personas con tus mismas inquietudes y ayudarás a la restauración de los ecosistemas mientras disfrutas en buena compañía.</p>
      <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/blog/detalle/plantacion1.avif"
          alt="Plantación con especies autóctonas para restauración de hábitats"
          title="Plantación con especies autóctonas"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/blog/detalle/plantacion2.avif"
          alt="Restauración de hábitat con plantas nativas"
          title="Restauración con especies autóctonas"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/blog/detalle/plantacion3.avif"
          alt="Voluntariado plantando especies locales"
          title="Voluntariado — plantación"
          loading="lazy"
        />
      </div>

      </div>
    </div>
  </template>
  
  <script setup>
import { useHead } from '@vueuse/head' // añadido

const pageUrl = 'https://www.geobizi.com/blog/detalle-flora-autoctona'
const ogImage = 'https://www.geobizi.com/imagenes/blog/detalle/plantacion1.avif'

useHead({
  title: 'Flora autóctona: la importancia de cuidarla | Geobizi',
  meta: [
    { name: 'description', content: 'Por qué proteger la flora autóctona es clave para la biodiversidad local y métodos para recuperarla en espacios degradados.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Flora autóctona: la importancia de cuidarla | Geobizi' },
    { property: 'og:description', content: 'Protección y restauración de flora autóctona para conservar biodiversidad y servicios ecosistémicos.' },
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
            "headline":"Flora autóctona: la importancia de cuidarla",
            "description":"Por qué proteger la flora autóctona es clave para la biodiversidad local y métodos para recuperarla en espacios degradados.",
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