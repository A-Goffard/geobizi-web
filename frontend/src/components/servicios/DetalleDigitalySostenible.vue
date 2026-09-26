<template>
  <div class="contenedor-principal">
    <h1>Geobizi TIK <span class="sub-siglas">(Teknologia, Informazioa eta Komunikazioa)</span></h1>
    
    <p class="intro-destacada">¿Quién dijo que la tecnología y la naturaleza no se llevan bien? A través de <strong>Geobizi TIK</strong> aunamos el desarrollo tecnológico y la digitalización con criterios de eficiencia, sostenibilidad y menor huella de carbono.</p>
    
    <p>Ofrecemos soluciones digitales avanzadas tanto para proyectos de divulgación ambiental y educativa como para administraciones públicas, ayuntamientos y entidades que necesiten modernizar sus portales web y optimizar la gestión operativa de sus eventos y aforos.</p>

    <h2>Nuestras Soluciones Digitales</h2>
    
    <div class="bloques-gestion">
        <div class="bloque-modalidad">
            <h3>Portales Web y Gestión de Festivales</h3>
            <p>Diseño y desarrollo de páginas web institucionales bilingües y sistemas avanzados de inscripción online. Incluye gestión de aforos limitados, enlaces personalizados de cancelación automática, reapertura de plazas y paneles móviles de control de asistencia para entidades colaboradoras y equipos de coordinación municipal.</p>
            <router-link to="/contacto?servicio=digital_webs" class="btn-servicio mleft">Consultar desarrollo web y gestión</router-link>
        </div>
        <div class="bloque-modalidad">
            <h3>Yincanas y Rutas Digitales</h3>
            <p>Convertimos un paseo por el entorno o una visita cultural en una aventura interactiva. Con el dispositivo móvil como guía, integramos retos sobre el terreno para hacer el descubrimiento del medio natural mucho más dinámico y gamificado.</p>
            <router-link to="/contacto?servicio=digital_yincanas" class="btn-servicio mleft">Preguntar sobre yincanas</router-link>
        </div>
        <div class="bloque-modalidad">
            <h3>Recursos Digitales Educativos</h3>
            <p>Diseño de guías interactivas, fichas y materiales didácticos digitales pensados para docentes, centros educativos y asociaciones, facilitando herramientas listas para utilizarse en el aula o en salidas de campo.</p>
            <router-link to="/contacto?servicio=digital_recursos" class="btn-servicio mleft">Preguntar sobre recursos digitales</router-link>
        </div>
    </div>

    <h2>Proyectos y Casos de Éxito</h2>
    <p>La tecnología adquiere valor cuando se aplica con eficacia en el mundo real. Algunos de nuestros trabajos destacados son:</p>
    <ul>
        <li><strong>EGEO:</strong> Desarrollo de proyectos web a medida orientados a la optimización técnica y la accesibilidad digital: <a href="https://egeo.eus/" target="_blank" rel="noopener noreferrer">https://egeo.eus/</a>.</li>
        <li><strong>Fichas Etnobotánicas de Enkarterri:</strong> Herramienta interactiva y digital para descubrir la flora local de forma visual y ágil. Puedes verla aquí: <router-link to="/fitxas-etnobotanicas-enkarterri">Guía Digital de Fichas Etnobotánicas</router-link>.</li>
        <li><strong>Flysch Digital:</strong> Propuesta didáctica basada en tecnologías móviles para interpretar la geología de la costa de Bizkaia.</li>
    </ul>

    <section class="faq-section">
      <h2>Preguntas frecuentes</h2>
      <h3>¿Qué ventajas aporta el sistema de reservas y gestión de Geobizi TIK para eventos?</h3>
      <p>Reduce drásticamente la carga de trabajo administrativo del personal organizador. Al permitir que los propios usuarios cancelen mediante un enlace seguro, las plazas se liberan automáticamente para otras personas interesadas, y los colaboradores disponen de un panel móvil sencillo para supervisar la asistencia en tiempo real.</p>
      <h3>¿Cómo se garantiza la sostenibilidad de los desarrollos web?</h3>
      <p>Optimizando el código para lograr tiempos de carga mínimos, reduciendo el consumo energético de los servidores, comprimiendo los recursos gráficos sin perder calidad y trabajando bajo arquitecturas ligeras con compensación de huella de carbono.</p>
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
  title: 'Geobizi TIK - Soluciones Digitales y Web | Geobizi',
  meta: [{ name: 'description', content: 'Soluciones tecnológicas con Geobizi TIK: desarrollo web institucional, sistemas avanzados de inscripción y cancelación para eventos, yincanas interactivas y webs eficientes.' }],
  link: [{ rel: 'canonical', href: pageUrl }]
})
</script>

<style scoped>
.sub-siglas {
  font-size: 1.1rem;
  font-weight: normal;
  color: var(--green);
  display: block;
  margin-top: 0.3rem;
}

.intro-destacada {
  font-size: 1.1rem;
  font-weight: 500;
}

.faq-section {
  margin-top: 3rem;
  padding: 2rem;
  background: var(--megashoftgreen);
  border-radius: 0.5rem;
}

</style>