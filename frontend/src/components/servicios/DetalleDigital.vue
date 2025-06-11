<template>
  <div class="contenedor-principal">
    <h1>Proyectos Digitales Medioambientales</h1>
    <p>
      En Geobizi desarrollamos proyectos digitales innovadores y personalizados para acercar el medioambiente a las personas de forma diferente, creativa y participativa.
    </p>

    <h2>¿Qué hacemos?</h2>
    <p>
      Creamos experiencias digitales únicas relacionadas con la naturaleza y la sostenibilidad: yincanas digitales, rutas interactivas, juegos educativos, retos online y actividades a medida para centros educativos, ayuntamientos, empresas y asociaciones.
    </p>
    <p>
      Si buscas una forma original de sensibilizar, educar o dinamizar en torno al medioambiente, diseñamos tu proyecto digital desde cero o adaptamos nuestras propuestas a tus necesidades.
    </p>

    <div class="horizontal">
      <div class="card-servicios">
        <div class="imagen-trio">
          <div>
            <img class="img" src="/imagenes/servicios/detalle/digital1.jpg" alt="Yincana Digital"/>
          </div>
          <div>
          <img class="img" src="/imagenes/servicios/detalle/digital2.jpg" alt="Yincana Digital"/>
          </div>
          <div>
          <img class="img" src="/imagenes/servicios/detalle/digital3.jpg" alt="Yincana Digital"/>
          </div>
        </div>
      </div>

      <!-- Puedes agregar más proyectos digitales aquí -->

    </div>
  </div>
</template>

<script setup>
// No hay lógica adicional para este artículo
</script>

<style scoped>
.imagen-trio{
  display: flex;
  gap: 1rem;
}

@media (max-width: 750px) {

  .imagen-trio{
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
}
</style>