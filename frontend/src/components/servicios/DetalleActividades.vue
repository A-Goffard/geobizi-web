<template>
    <div class="contenedor-principal">
        <h1>Actividades y Talleres</h1>
        <p>Diseñamos talleres prácticos y experiencias en la naturaleza; adaptamos contenidos y duración según edades y
            objetivos.</p>

        <h2>Talleres creativos y manuales</h2>
        <ul>
            <li>Reciclaje creativo</li>
            <li>Pintando figuras de yeso</li>
            <li>Patatroles</li>
            <li>Jabones y cosmética natural</li>
            <li>Ambientadores caseros</li>
            <li>Mariposas de madera</li>
            <li>Hojas de arcilla</li>
            <li>Prensa de flores</li>
            <li>Papel reciclado</li>
            <li>Herbario de pintura</li>
            <li>Eguzkilores</li>
        </ul>

        <h2>Talleres científicos y técnicos</h2>
        <ul>
            <li>Réplicas de fósil</li>
            <li>Planetas magnéticos</li>
            <li>Cianotipias</li>
            <li>Microscopio</li>
            <li>Geodas</li>
            <li>Brújulas</li>
        </ul>

        <h2>Talleres de naturaleza y jardinería</h2>
        <ul>
            <li>Bombas de semillas</li>
            <li>Casas de mariquitas</li>
            <li>Casas de mariposas</li>
            <li>Casas de insectos</li>
            <li>MacetoHuerto</li>
            <li>Huertos Urbanos</li>
            <li>Plantas medicinales</li>
            <li>Oasis de mariposas</li>
            <li>Biorregeneración colaborativa</li>
        </ul>

        <h2>Se realizan para</h2>
        <p>Estas actividades se ofrecen para colegios, asociaciones, empresas, administraciones y público general.
            Adaptamos metodología, idioma (euskera/castellano), materiales y duración según el tipo de colectivo y
            objetivos.</p>
        
        <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/servicios/actividades/actividades1.avif"
          alt="Actividad de reciclaje creativo"
          title="Actividad de reciclaje creativo — imagen 1"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/servicios/actividades/actividades2.avif"
          alt="Taller de huertos urbanos"
          title="Taller de huertos urbanos — imagen 2"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/servicios/actividades/actividades3.avif"
          alt="Taller de Eguzkilores"
          title="Taller de Eguzkilores — imagen 3"
          loading="lazy"
        />
      </div>
    </div>

            <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/servicios/actividades/actividades4.avif"
          alt="Taller de papel reciclado"
          title="Taller de papel reciclado — imagen 1"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/servicios/actividades/actividades5.avif"
          alt="Taller de fósiles"
          title="Taller de fósiles — imagen 2"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/servicios/actividades/actividades6.avif"
          alt="Taller de bombas de semillas"
          title="Taller de bombas de semillas — imagen 3"
          loading="lazy"
        />
      </div>
    </div>

    </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'
const pageUrl = 'https://www.geobizi.com/servicios/actividades'
useHead({
    title: 'Actividades y Talleres | Geobizi',
    meta: [{ name: 'description', content: 'Talleres y actividades: reciclaje creativo, cianotipias, bombas de semillas, rutas, huertos urbanos y formaciones para distintos colectivos.' }],
    link: [{ rel: 'canonical', href: pageUrl }]
})
</script>

<style scoped>
/* ...existing code... */
</style>