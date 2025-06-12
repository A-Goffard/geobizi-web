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
<h3>Donde la aventura, la tecnología y la naturaleza se unen</h3>

      <p>¿Imaginas explorar un paisaje espectacular mientras resuelves enigmas digitales con tu móvil? Podemos crear una experiencia única que combina lo mejor de una yincana tradicional con la emoción de las nuevas tecnologías.</p>
      <h3>Una aventura para todos</h3>

      <p>Una actividad pensada para todos los públicos, familias, grupos de amigos, adultos, adolescentes, turistas... Con ayuda del móvil, irán resolviendo pistas y acertijos por la playa de Sopela hasta dar con la prueba final.</p>
      <p>En el transcurso de las pruebas se irán moviendo por toda la zona mientras aprenden, descubren, se entretienen y disfrutan de una actividad diferente.</p>
      <p>Es un proyecto adaptable a diferentes entonos y que resulta original y divertido.</p>
      <p>La actividad se puede realizar en euskera o castellano.</p>
      <p>Una posibilidad interesante para los que les gusta hacer algo diferente.</p>

      <h3>¿Quieres una yincana digital personalizada?</h3>
      <p>¡Creamos yincanas a medida para cualquier lugar! Contáctanos y diseñaremos una experiencia única adaptada a tu entorno.</p>
      
      <h3>¿Por qué elegir una actividad Digital?</h3>
      <p>
        <img src="/imagenes/iconos/color/estrellitas.png" alt="Original" class="icono" />
        <strong>Actividad original</strong> – No es solo un paseo, es una experiencia interactiva.
      </p>      
      <p>
        <img src="/imagenes/iconos/color/adaptable.png" alt="Adaptable" class="icono" />
        <strong>Adaptable</strong> – Podemos personalizarla para otros entornos (montañas, ciudades, parques naturales…).</p>
      <p>
        <img src="/imagenes/iconos/color/multilingue.png" alt="Multilingüe" class="icono" />
        <strong>Multilingüe</strong> – Disponible en euskera y castellano (otros idiomas bajo consulta).</p>
      <p>
        <img src="/imagenes/iconos/color/libro.png" alt="Educativo" class="icono" />
        <strong>Educativo y entretenido</strong> – Perfecto para colegios, empresas, ayuntamientos o grupos de ocio.</p>

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
.icono {
  width: 20px;
  height: 20px;
  margin-right: 8px;
  vertical-align: middle;
}
@media (max-width: 750px) {

  .imagen-trio{
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
}
</style>