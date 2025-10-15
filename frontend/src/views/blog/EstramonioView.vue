<template>
  <div class="contenedor-principal">
    <h1>Estramonio (Datura stramonium) en Azkorri: riesgos y precauciones</h1>
    <h2>Planta tóxica que conviene conocer: encontrada en Azkorri, frecuentada por familias y animales</h2>

    <h3>Introducción:</h3>
    <p>El <strong>estramonio</strong> (Datura stramonium) es una planta perteneciente a la familia de las solanáceas conocida por sus propiedades tóxicas. Aunque algunas partes han sido usadas tradicionalmente con fines medicinales, su consumo o manipulación puede ser muy peligroso.</p>

    <p>Es una planta que puede encontrarse de forma natural en zonas con mucha materia orgánica.</p>
    <p>En Azkorri hemos encontrado ejemplares en zonas accesibles donde pasan familias, niños y animales. Es importante reconocerla y evitar el contacto: no tocar, no arrancar frutos ni hojas y mantener a las mascotas alejadas.</p>

    <h3>Origen y distribución</h3>
    <p>El origen exacto del estramonio (Datura stramonium) es incierto, aunque se considera que el género <em>Datura</em> tiene su mayor diversidad en América Central y Sudamérica. La evidencia sugiere que el género pudo haberse originado en América Central y las Grandes Antillas, desde donde se expandió por América del Norte y del Sur.</p>
    <p>Hoy en día, el estramonio es una planta cosmopolita que crece en zonas cálidas y templadas de casi todo el planeta (excepto en los climas polares). Su amplia distribución se explica porque ha sido cultivado y se ha naturalizado con éxito en muchas regiones.</p>

    <h3>Riesgos y síntomas</h3>
    <p>El estramonio contiene alcaloides (como atropina, escopolamina) que pueden producir desde sequedad de boca, visión borrosa y confusión, hasta taquicardia, alucinaciones y en casos graves afectación respiratoria. Si alguien ha estado en contacto o ha ingerido la planta, buscar asistencia médica inmediatamente.</p>

    <h3>Primeros auxilios</h3>
    <p>No inducir el vómito salvo que lo indique un profesional sanitario. Lavar con agua las zonas de contacto y, si hay síntomas, trasladar a urgencias con información sobre la exposición. Mantener a los animales alejados y consultar al veterinario si muestran signos sospechosos.</p>

    <h3>Control y prevención</h3>
    <p>La gestión de ejemplares en zonas públicas debe dejarse a personal cualificado. En espacios naturales, favorecer la educación: señalizar o informar a la población local sobre la presencia y peligros de la planta.</p>

    <p>Recuerda: si ves estramonio en Azkorri o en otras áreas recreativas, no lo toques y avisa a los responsables del lugar si procede.</p>

    <div class="imagen-trio">
      <div>
        <img class="img" src="/imagenes/blog/detalle/estramonio1.avif" alt="Flor y fruto del estramonio" title="Datura stramonium — flor y fruto" loading="lazy" />
      </div>
      <div>
        <img class="img" src="/imagenes/blog/detalle/estramonio2.avif" alt="Planta de estramonio cerca de sendero" title="Estramonio en zona accesible" loading="lazy" />
      </div>
      <div>
        <img class="img" src="/imagenes/blog/detalle/estramonio3.avif" alt="Fruto espinoso de estramonio" title="Fruto del estramonio" loading="lazy" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/blog/detalle-estramonio'
const ogImage = 'https://www.geobizi.com/imagenes/blog/detalle/estramonio1.avif'

useHead({
  title: 'Estramonio en Azkorri — Riesgos y precauciones | GeoBizi',
  meta: [
    { name: 'description', content: 'Información sobre el estramonio (Datura stramonium) encontrado en Azkorri: origen, distribución, riesgos y precauciones. No tocar; mantener a niños y mascotas alejados.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'GeoBizi' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Estramonio en Azkorri — Riesgos y precauciones | GeoBizi' },
    { property: 'og:description', content: 'Conoce el origen probable, la distribución actual, los riesgos y qué hacer si hay contacto o ingestión accidental.' },
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
        "@context":"https://schema.org",
        "@graph":[
          {
            "@type":"Organization",
            "@id":"https://www.geobizi.com/#organization",
            "name":"GeoBizi",
            "url":"https://www.geobizi.com"
          },
          {
            "@type":"Article",
            "headline":"Estramonio (Datura stramonium) en Azkorri: riesgos y precauciones",
            "description":"Información sobre el estramonio encontrado en Azkorri, incluyendo su origen probable en América Central y las Grandes Antillas, su distribución actual y recomendaciones para evitar el contacto.",
            "author": { "@type":"Organization", "@id":"https://www.geobizi.com/#organization" },
            "mainEntityOfPage": { "@type":"WebPage", "@id": pageUrl },
            "image": { "@type":"ImageObject","url":ogImage }
          }
        ]
      })
    }
  ]
})
</script>

<style scoped>

</style>