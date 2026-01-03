<template>
  <div class="contenedor-principal general-container"> <h1>Recursos y descargas</h1>
    <p>Aquí encontrarás una selección de materiales educativos y recursos para descargar.</p>
    <p>Si los usas y crees que están bien y merecen la pena, acuérdate de nosotros.</p>
    <p>También podemos personalizar y diseñar materiales didácticos a medida.</p>

    <h2>Material disponible</h2>

    <h3>Láminas</h3>

    <div class="container">
      
      <a 
        href="/descargas/laminas/cartel-geologia.png" 
        download="cartel-geologia.png" 
        class="card"
      >
        <img src="/descargas/miniaturas/Cartel-geologia.avif" alt="Lámina de hojas de arboles" loading="lazy">
        <p class="card-text">Cartel sobre las salidas de la geología</p>
      </a>

            <a 
        href="/descargas/laminas/polinizadores.avif" 
        download="polinizadores.avif" 
        class="card"
      >
        <img src="/descargas/laminas/polinizadores.avif" alt="Lámina de polinizadores" loading="lazy">
        <p class="card-text">Lámina de polinizadores</p>
      </a>

            <a 
        href="/descargas/laminas/mariposas.avif" 
        download="mariposas.avif" 
        class="card"
      >
        <img src="/descargas/laminas/mariposas.avif" alt="Lámina de mariposas" loading="lazy">
        <p class="card-text">Lámina de mariposas</p>
      </a>

                  <a 
        href="/descargas/laminas/mariposas-nocturnas.avif" 
        download="mariposas-nocturnas.avif" 
        class="card"
      >
        <img src="/descargas/laminas/mariposas-nocturnas.avif" alt="Lámina de mariposas nocturnas" loading="lazy">
        <p class="card-text">Lámina de mariposas nocturnas</p>
      </a>

            <a 
        href="/descargas/laminas/arboles1.avif" 
        download="arboles1.avif" 
        class="card"
      >
        <img src="/descargas/laminas/arboles1.avif" alt="Lámina de hojas de arboles" loading="lazy">
        <p class="card-text">Lámina de hojas de árboles en euskera y castellano</p>
      </a>

    </div>

       <h3>Documentos</h3>

           <div class="container">
      
      <a 
        href="/descargas/documentos/Flyschbizkia-didactica.pdf" 
        download="Flyschbizkia-didactica.pdf" 
        class="card"
      >
        <img src="/descargas/miniaturas/flyschbizkaia-didactica.avif" alt="Lámina de hojas de arboles" loading="lazy">
        <p class="card-text">Documento didáctico sobre Flyschbizkia</p>
      </a>



    </div>

    <h2>Se realizan para</h2>
    <p>Podemos diseñar materiales a medida según las necesidades de cada cliente.</p>
    <p>Pueden ser en formatos diferentes como láminas, folletos o recursos digitales interactivos por ejemplo.</p>
    <p>Los materiales están pensados para colegios, asociaciones, entidades locales y público general.</p>

  </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'
const pageUrl = 'https://www.geobizi.com/servicios/descargas'
useHead({
  title: 'Recursos y descargas | Geobizi',
  meta: [{ name: 'description', content: 'Fichas didácticas, guías de campo y materiales descargables para apoyar rutas, talleres y proyectos educativos.' }],
  link: [{ rel: 'canonical', href: pageUrl }]
})
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