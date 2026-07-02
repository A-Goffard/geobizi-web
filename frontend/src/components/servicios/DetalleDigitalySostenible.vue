<template>
  <div class="contenedor-principal">
    <h1>Proyectos Digitales y Sostenibilidad</h1>
    
    <p>¿Quién dijo que la tecnología y la naturaleza no se llevan bien? En Geobizi utilizo lo digital como una herramienta para acercar el medioambiente a las personas, siempre con una mirada consciente, responsable y transparente.</p>
    
    <p>Creemos que las herramientas digitales deben estar al servicio de las buenas ideas. Por eso, todos nuestros desarrollos nacen con una premisa clara: ser respetuosos, accesibles y, por supuesto, con una huella de carbono compensada.</p>

    <h2>¿Qué podemos hacer juntos?</h2>
    
    <div class="bloques-gestion">
        <div class="bloque-modalidad">
            <h3>Yincanas y Rutas Digitales</h3>
            <p>Convertimos un paseo por el monte o una visita a la costa en una aventura interactiva. Con el móvil como guía, planteamos retos y pruebas sobre el propio terreno para que descubrir la biodiversidad sea como jugar a un juego de exploración real.</p>
        </div>
        <div class="bloque-modalidad">
            <h3>Recursos Digitales Educativos</h3>
            <p>Diseñamos guías, fichas y materiales didácticos digitales pensados para docentes, familias y asociaciones. Recursos interactivos listos para usar, que facilitan el aprendizaje y hacen que el conocimiento de la naturaleza esté al alcance de un clic.</p>
        </div>
        <div class="bloque-modalidad">
            <h3>Webs Eficientes y Sostenibles</h3>
            <p>Desarrollamos páginas web a medida para cualquier empresa, particular o proyecto que quiera tener presencia en internet reduciendo su impacto ambiental. Creamos sitios optimizados, rápidos, que consumen menos energía y con compensación de la huella de carbono.</p>
        </div>
    </div>

    <h2>Ejemplos de nuestro trabajo digital</h2>
    <p>Nos gusta que la tecnología sea útil y fácil de usar. Algunos proyectos reales que ya están funcionando son:</p>
    <ul>
        <li><strong>Fichas Etnobotanicas de Enkarterri:</strong> Una herramienta interactiva y digital idónea para descubrir los secretos de las plantas de nuestra zona de manera visual y ágil. Puedes verla aquí: <router-link to="/fitxas-etnobotanicas-enkarterri">Guía Digital de Fichas Etnobotánicas</router-link>.</li>
        <li><strong>Flysch Digital:</strong> Una propuesta didáctica diferente para interpretar el entorno geológico de la costa de Bizkaia a través de dispositivos móviles.</li>
        <li><strong>Nuestra propia casa:</strong> Esta misma página web, pensada desde el principio para ser un punto de encuentro eficiente, limpio y lo más sostenible posible.</li>
    </ul>

    <section class="faq-section">
      <h2>Preguntas frecuentes</h2>
      <h3>¿Cómo se consigue que una web sea sostenible?</h3>
      <p>Optimizando el código para que las páginas carguen rápido y los servidores trabajen menos, reduciendo el tamaño de las imágenes sin perder calidad y eligiendo un diseño eficiente. Menos energía consumida se traduce en menos emisiones.</p>
      <h3>¿Son fáciles de usar vuestras yincanas o guías?</h3>
      <p>Sí, totalmente. Nos esforzamos mucho en que la tecnología sea intuitiva y sencilla para que cualquier persona, independientemente de sus conocimientos tecnológicos o de su edad, pueda disfrutar de la experiencia sin complicaciones.</p>
    </section>

    <div class="imagen-trio">
      <div><img class="img" src="/imagenes/servicios/digital/digital1.avif" alt="Tecnología en el campo" loading="lazy" /></div>
      <div><img class="img" src="/imagenes/servicios/digital/digital2.avif" alt="Aprendiendo con el móvil" loading="lazy" /></div>
      <div><img class="img" src="/imagenes/servicios/digital/digital3.avif" alt="Ruta interactiva" loading="lazy" /></div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/servicios/digital-sostenible'
useHead({
  title: 'Proyectos Digitales Sostenibles | Geobizi',
  meta: [{ name: 'description', content: 'Desarrollo de proyectos digitales sostenibles: yincanas interactivas, recursos educativos y páginas web eficientes con huella de carbono compensada.' }],
  link: [{ rel: 'canonical', href: pageUrl }]
})
</script>

<style scoped>
.faq-section { margin-top: 3rem; padding: 2rem; background: var(--megashoftgreen); border-radius: 0.5rem; }
</style>