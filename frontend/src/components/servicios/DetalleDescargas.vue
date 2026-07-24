<template>
  <div class="contenedor-principal">
    <h1>Recursos y Descargas</h1>
    
    <p>Compartimos con vosotros una selección de materiales educativos que hemos ido creando con mucho cariño. Son recursos pensados para apoyar el aprendizaje en el aula, en casa o durante nuestras rutas.</p>
    
    <p>Si utilizáis alguno y os resulta útil, ¡nos encantaría saberlo! Y recordad que, si necesitáis algo más específico, podemos diseñar materiales didácticos a vuestra medida: desde láminas hasta recursos digitales interactivos.</p>

    <h2>Nuestra selección</h2>

    <h3>Guías y herramientas interactivas</h3>
    <div class="container">
      <router-link to="/fitxas-etnobotanicas-enkarterri" class="card">
        <img src="/imagenes/etnobotanica/catalogo-botanico.avif" alt="Catálogo digital de fichas etnobotánicas" loading="lazy">
        <p class="card-text">Guía Digital interactiva: Fichas Etnobotánicas y Herbario de Euskal Herria</p>
      </router-link>
    </div>

    <h3>Láminas didácticas (para imprimir)</h3>
    <div class="container">
      <a href="/descargas/laminas/cartel-geologia.png" download class="card" @click="registrarDescarga('cartel-geologia')">
        <img src="/descargas/miniaturas/Cartel-geologia.avif" alt="Cartel de geología" loading="lazy">
        <p class="card-text">Cartel sobre las salidas de geología</p>
      </a>
      <a href="/descargas/laminas/polinizadores.avif" download class="card" @click="registrarDescarga('lamina-polinizadores')">
        <img src="/descargas/laminas/polinizadores.avif" alt="Lámina de polinizadores" loading="lazy">
        <p class="card-text">Lámina de polinizadores</p>
      </a>
      <a href="/descargas/laminas/mariposas.avif" download class="card" @click="registrarDescarga('lamina-mariposas-diurnas')">
        <img src="/descargas/laminas/mariposas.avif" alt="Lámina de mariposas" loading="lazy">
        <p class="card-text">Lámina de mariposas diurnas</p>
      </a>
      <a href="/descargas/laminas/mariposas-nocturnas.avif" download class="card" @click="registrarDescarga('lamina-mariposas-nocturnas')">
        <img src="/descargas/laminas/mariposas-nocturnas.avif" alt="Lámina de mariposas nocturnas" loading="lazy">
        <p class="card-text">Lámina de mariposas nocturnas</p>
      </a>
      <a href="/descargas/laminas/arboles1.avif" download class="card" @click="registrarDescarga('lamina-arboles')">
        <img src="/descargas/laminas/arboles1.avif" alt="Lámina de hojas" loading="lazy">
        <p class="card-text">Lámina de hojas de árboles (Euskera/Castellano)</p>
      </a>
    </div>

    <h3>Documentos y unidades didácticas</h3>
    <div class="container">
      <a href="/descargas/documentos/Flyschbizkaia-didactica.pdf" download class="card" @click="registrarDescarga('documento-flysch')">
        <img src="/descargas/miniaturas/flyschbizkaia-didactica.avif" alt="Documento didáctico" loading="lazy">
        <p class="card-text">Documento didáctico sobre Flysch Bizkaia</p>
      </a>
    </div>

    <h2>¿Necesitas algo a medida?</h2>
    <p>Podemos diseñar materiales personalizados para colegios, asociaciones o entidades locales. Si necesitas láminas, folletos o un recurso digital muy específico, cuéntanos tu idea y nos ponemos manos a la obra.</p>
    
    <div class="centro-cta">
      <router-link to="/contacto?servicio=material_medida" class="btn-servicio">Pedir material a medida</router-link>
    </div>
  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/servicios/descargas'
useHead({
  title: 'Recursos Didácticos y Descargas | Geobizi',
  meta: [{ name: 'description', content: 'Descarga láminas didácticas, guías interactivas y material educativo para explorar la naturaleza de Bizkaia.' }],
  link: [{ rel: 'canonical', href: pageUrl }]
})

// Función para registrar las descargas en Google Analytics
const registrarDescarga = (nombreRecurso) => {
  if (typeof window.gtag === 'function') {
    window.gtag('event', 'descargar_recurso', {
      'event_category': 'Descargas',
      'event_label': nombreRecurso
    });
  }
}
</script>

<style scoped>
/* 1. CAMBIO PRINCIPAL: Usamos columnas en lugar de flexbox */
.container {
  /* display: flex;  <-- ELIMINADO */
  /* flex-wrap: wrap; <-- ELIMINADO */
  
  column-count: 3; /* Número de columnas en PC */
  column-gap: 2rem; /* Espacio entre columnas */
  
  /* Para que no se pegue a los bordes */
  width: 100%; 
}

.general-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  padding-top: 7rem;
  padding-left: 2rem;
  padding-right: 2rem;
  padding-bottom: 2rem;
}

/* 2. CAMBIO EN LA TARJETA: Evitar que se partan */
.card {
  width: 100%; /* Ocupa el ancho de su columna */
  margin-bottom: 2rem; /* Espacio debajo de cada tarjeta */
  
  padding: 20px;
  background-color: var(--megashoftgreen);
  border: 1px solid var(--shoftgreen);
  border-radius: 0.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
  cursor: pointer;
  
  text-decoration: none;
  color: inherit;
  
  /* IMPORTANTE: Para que una tarjeta no se corte entre dos columnas */
  break-inside: avoid; 
  display: inline-block; /* Ayuda a mantener la integridad en algunos navegadores */
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.card h2 {
  margin-top: 0;
}

.card-text {
  color: var(--darkgrey);
  margin-top: 1rem;
  font-weight: bold;
}

/* 3. CAMBIO EN IMAGEN: Quitar restricciones de altura */
img {
  width: 100%;
  border-radius: 0.5rem;
  
  height: auto; /* IMPORTANTE: Deja que la altura sea natural */
  display: block; /* Elimina espacios extraños debajo de la imagen */
  
  /* aspect-ratio: 16/9; <-- ELIMINADO: Esto es lo que forzaba el recorte */
  /* object-fit: cover; <-- ELIMINADO: Ya no necesitamos recortar */
}

/* 4. RESPONSIVE: Ajustar columnas según pantalla */
@media (max-width: 900px) {
  .container {
    column-count: 2; /* 2 columnas en tablets */
  }
}

@media (max-width: 600px) {
  .container {
    column-count: 1; /* 1 columna en móvil */
  }
}
</style>