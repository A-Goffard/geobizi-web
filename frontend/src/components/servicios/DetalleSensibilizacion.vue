<template>
  <div class="contenedor-principal">
    <h1>Proyectos de Sensibilización y Regeneración</h1>
    
    <p>En Geobizi nos mueve el deseo de conectar a las personas con el entorno que nos rodea. Por eso, diseñamos proyectos donde no solo hablamos de naturaleza, sino que nos remangamos para cuidarla y entenderla juntos.</p>
    
    <p>Buscamos ese "click" de conexión. Ya sea en un colegio, en una asociación o en una empresa, nuestro objetivo es que cada proyecto deje una huella positiva, creando un compromiso real y sentido con nuestro medio ambiente.</p>

    <h2>¿Cómo son nuestros proyectos?</h2>
    <p>No creemos en las recetas únicas. Cada grupo es un mundo, así que diseñamos actividades a medida: desde pequeñas acciones que generan impacto en un día, hasta programas que acompañan a lo largo del tiempo para ver crecer los resultados.</p>

    <section class="proyecto-destacado">
      <h2>Un caso de éxito: "Zalla Natura"</h2>
      <p>Nos hace especial ilusión recordar "Zalla Natura". Fue un proyecto precioso donde colaboramos con el ayuntamiento, colegios y vecinos de Zalla para recuperar y cuidar sus espacios naturales.</p>
      <p>Ver cómo el alumnado, las asociaciones y el personal del ayuntamiento trabajaban unidos por su entorno es lo que nos confirma que este es el camino.</p>
      <p>Puedes conocer más detalles en nuestra página de <router-link to="/detalle-zalla-natura">Zalla Natura</router-link> o ver nuestra sección completa de <router-link to="/proyectos">Proyectos realizados</router-link>.</p>
    </section>

    <h2>¿Para quién trabajamos?</h2>
    <p>Nuestra puerta está abierta a todo el mundo: desde centros educativos y asociaciones vecinales, hasta empresas que quieren apostar por la sostenibilidad y administraciones que buscan poner en valor su patrimonio natural.</p>

    <div class="centro-cta" style="margin-top: 2rem;">
      <router-link to="/contacto?servicio=sensibilizacion_proyectos" class="btn-servicio">Proponer/pedir un proyecto o iniciativa</router-link>
    </div>

    <!-- GALERÍA -->
    <div class="imagen-trio" style="margin-top: 2rem;">
      <div><img class="img" src="/imagenes/servicios/sensibilizacion/sensibilizacion1.avif" alt="Acción de regeneración" loading="lazy" /></div>
      <div><img class="img" src="/imagenes/servicios/sensibilizacion/sensibilizacion2.avif" alt="Participación ciudadana" loading="lazy" /></div>
      <div><img class="img" src="/imagenes/servicios/sensibilizacion/sensibilizacion3.avif" alt="Proyecto escolar" loading="lazy" /></div>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/servicios/sensibilizacion'
useHead({
  title: 'Sensibilización y Regeneración Ambiental | Geobizi',
  meta: [{ name: 'description', content: 'Proyectos colaborativos para conectar personas y naturaleza mediante la sensibilización y la restauración ambiental.' }],
  link: [{ rel: 'canonical', href: pageUrl }]
})
</script>

<style scoped></style>