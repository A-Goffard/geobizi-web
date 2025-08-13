<template>
  <div class="contenedor-principal">
    <h1>Zalla Natura</h1>
    <h2>Bio-Regeneración Comunitaria</h2>
    <h3>Revitalizando ecosistemas, conectando personas</h3>
    <p>
      En un mundo donde la naturaleza clama por ayuda, Zalla Natura surge como un proyecto innovador que une sostenibilidad, educación ambiental y acción comunitaria. No solo buscamos restaurar espacios naturales, sino también crear vínculos entre las personas y su entorno, fomentando un futuro más verde y consciente.
    </p>

    <section class="presentation">
      <img src="imagenes/proyectos/zallanatura/zallanatura1.avif" alt="Imagen destacada del proyecto Zalla Natura" class="img" loading="lazy" />
      <div>
        <h2>Sobre el Proyecto</h2>
        <p>
          Zalla Natura es una iniciativa impulsada por el ayuntamiento de Zalla en colaboración con Geobizi para fomentar la sostenibilidad, promover la biodiversidad y la conservación del medio ambiente en la región de Zalla. A través de actividades comunitarias, buscamos crear un impacto positivo en nuestro entorno natural.
        </p>
        <p>
          En las actividades participan personas comprometidas con el medioambiente, centros escolares, la residencia y otras asociaciones como Enkarnatura, TxikiLur, o Zerynthia.
        </p>
      </div>
    </section>

    <section class="secciones">
      <h2>Actividades Realizadas</h2>
      <div class="contenido-seccion">
        <ul>
          <li><img src="imagenes/iconos/color/maripositaV.png" alt="Mariposita" class="icono" loading="lazy" />Networking inicial</li>
          <li><img src="imagenes/iconos/color/maripositaV.png" alt="Mariposita" class="icono" loading="lazy" />Presentación del proyecto</li>
          <li><img src="imagenes/iconos/color/maripositaV.png" alt="Mariposita" class="icono" loading="lazy" />Plantación y lanzamiento de bombas de semillas en Landabaso eskola</li>
          <li><img src="imagenes/iconos/color/maripositaV.png" alt="Mariposita" class="icono" loading="lazy" />Ruta para conocer los árboles de Zalla</li>
          <li><img src="imagenes/iconos/color/maripositaV.png" alt="Mariposita" class="icono" loading="lazy" />Taller de pintar mariposas</li>
          <li><img src="imagenes/iconos/color/maripositaV.png" alt="Mariposita" class="icono" loading="lazy" />Creación de un oasis de mariposas en el parque de Lusa, taller de bombas de semillas y pintado de mariposas de madera</li>
          <li><img src="imagenes/iconos/color/maripositaV.png" alt="Mariposita" class="icono" loading="lazy" />Lanzamiendo de bombas de semillas y creación de zonas de NO siega en la zona de Tepeyac</li>
          <li><img src="imagenes/iconos/color/maripositaV.png" alt="Mariposita" class="icono" loading="lazy" />Huerto urbano con Mimetiz eskola en la residencia</li>
          <li><img src="imagenes/iconos/color/maripositaV.png" alt="Mariposita" class="icono" loading="lazy" />Creación de hotel y casas de insectos y plantación de banda floral en Ibarra</li>
          <li><img src="imagenes/iconos/color/maripositaV.png" alt="Mariposita" class="icono" loading="lazy" />Colocación de hotel de insectos y cartel en el osasis de mariposas Tximeleku y manualidades infantiles</li>
        </ul>
        <img src="imagenes/proyectos/zallanatura/zallanatura2.avif" alt="Imagen de actividades realizadas" class="img" loading="lazy" />
      </div>
    </section>

    <section class="secciones">
      <div class="contenido-seccion">
        <div>
          <h2>Resultados Obtenidos</h2>
          <p>Hemos sembrado y lanzado miles de semillas de más de 20 especies de plantas.</p>
          <p>Hemos preparado un oasis de mariposas sembrando diferentes plantas adecuadas para las mariposas adultas y orugas.</p>
          <p>Hemos plantado pimientos, piparras, tomates, acelgas y lechugas variadas en la residencia "Zalla'Ko Eguzki"</p>
          <p>Hemos involucrado a más de 150 personas en el proyecto.</p>
          <p>Hemos creado y colocado dos hoteles de insectos y 16 casitas.</p>
        </div>
        <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="imagenes/proyectos/zallanatura/zallanatura3.avif"
          alt="Imagen del proyecto Zalla Natura"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="imagenes/proyectos/zallanatura/zallanatura4.avif"
          alt="Imagen del proyecto Zalla Natura"
          loading="lazy"
        />
      </div>
      <div>
        <img
          class="img"
          src="imagenes/proyectos/zallanatura/zallanatura5.avif"
          alt="Imagen del proyecto Zalla Natura"
          loading="lazy"
        />
      </div>
    </div>
      </div>
    </section>

  </div>
</template>

<script setup>
</script>

<style scoped>
.contenedor-principal {
  padding-top: 7rem;
  background-color: rgb(255, 255, 255);
  padding-bottom: 2rem;
}

.presentation {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  gap: 2rem;
  margin: 2rem 0;
}

.img {
  max-width: 350px;
  width: 100%;
  border-radius: 0.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  /* margin: 0 0.5rem ; */
  /* Centrado vertical en pantallas grandes */
  align-self: center;
}

.presentation > div {
  flex: 1;
  min-width: 220px;
}

.secciones {
  margin: 2.5rem 0;
}

.contenido-seccion {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  gap: 2rem;
}

.contenido-seccion ul {
  flex: 1;
  min-width: 220px;
  margin: 0;
  padding-left: 1.2rem;
}

.contenido-seccion > img {
  align-self: center;
}

.icono {
  width: 20px;
  height: 20px;
  margin-right: 8px;
  vertical-align: middle;
}

@media (max-width: 1021px) {
  .imagen-trio {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    gap: 1.2rem !important;
    width: 100%;
  }
  .imagen-trio > div {
    width: 100%;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
  }
}

@media (max-width: 900px) {
  .presentation {
    flex-direction: column;
    align-items: center;
    gap: 1.2rem;
  }
  .img {
    margin-left: auto;
    margin-right: auto;
    display: block;
    align-self: unset;
  }
  .contenido-seccion > img {
    margin-left: auto;
    margin-right: auto;
    display: block;
    align-self: unset;
  }
}
</style>