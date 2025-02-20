<template>
  <div class="contenedor-principal">
    <h1>Proyectos Digitales</h1>
    <p>
      En Geobizi, también estamos comprometidos con la innovación digital. Ofrecemos una variedad de proyectos digitales diseñados para conectar a las personas con el entorno natural de una manera interactiva y educativa.
    </p>

    <h2>Actividades Digitales</h2>
    <p>
      Aquí tienes algunas de las actividades digitales que ofrecemos. Todas nuestras actividades están diseñadas para ser accesibles y educativas.
      Si tienes algún interés especial, diseñamos una actividad digital a tu medida.
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
        <div class="lista-servicios">
          <h3>Yincana: Flysch Digital</h3>
          <p>
            Una actividad pensada para todos los públicos, familias, adultos, adolescentes, en grupo o en solitario. Con ayuda del móvil, irán resolviendo pistas y acertijos por la playa de Sopela hasta dar con la prueba final. 
            En el transcurso de las pruebas se irán moviendo por toda la playa mientras aprenden, descubren, se entretienen y disfrutan de una actividad diferente.
          </p>
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