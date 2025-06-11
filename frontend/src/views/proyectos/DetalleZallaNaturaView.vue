<template>
  <div class="contenedor-principal">
    <h1>Zalla Natura</h1>
    <h2>Bio-Regeneración Comunitaria</h2>
    <h3>Revitalizando ecosistemas, conectando personas</h3>
    <p>
      En un mundo donde la naturaleza clama por ayuda, Zalla Natura surge como un proyecto innovador que une sostenibilidad, educación ambiental y acción comunitaria. No solo buscamos restaurar espacios naturales, sino también crear vínculos entre las personas y su entorno, fomentando un futuro más verde y consciente.
    </p>

    <section class="presentation">
      <img src="images/zalla-natura-main.jpg" alt="Imagen destacada del proyecto Zalla Natura" class="img-principal" />
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
          <li>Networking inicial</li>
          <li>Presentación del proyecto</li>
          <li>Plantación y lanzamiento de bombas de semillas en Landabaso eskola</li>
          <li>Ruta para conocer los árboles de Zalla</li>
          <li>Creación de un oasis de mariposas en el parque de Lusa</li>
          <li>Taller de pintar mariposas</li>
        </ul>
        <img src="images/actividades-realizadas.jpg" alt="Imagen de actividades realizadas" class="img-seccion" />
      </div>
    </section>

    <section class="secciones">
      <h2>Actividades Pendientes</h2>
      <div class="contenido-seccion">
        <ul>
          <li>Lanzamiendo de bombas de semillas y creación de zonas de NO siega en la zona de Tepeyac</li>
          <li>Huerto urbano con Mimetiz eskola y la residencia</li>
          <li>Ruta de reconocimiento de la evolución del impacto</li>
          <li>Exposición final y cierre</li>
        </ul>
        <img src="images/actividades-pendientes.jpg" alt="Imagen de actividades pendientes" class="img-seccion" />
      </div>
    </section>

    <section class="secciones">
      <div class="contenido-seccion">
        <div>
          <h2>Resultados Obtenidos</h2>
          <p>Hasta ahora, hemos plantado o lanzado miles de semillas de más de 20 especies de plantas.</p>
          <p>Hemos preparado un oasis de mariposas sembrando diferentes plantas adecuadas para las mariposas adultas y orugas.</p>
          <p>xxx</p>
        </div>
        <img src="images/resultados-obtenidos.jpg" alt="Imagen de resultados obtenidos" class="img-seccion" />
      </div>
    </section>

    <div class="imagen-trio">
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/zallanatura2.png"
          alt="Imagen del proyecto Zalla Natura"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/zallanatura.png"
          alt="Imagen del proyecto Zalla Natura"
        />
      </div>
      <div>
        <img
          class="img"
          src="/imagenes/proyectos/zallanatura1.png"
          alt="Imagen del proyecto Zalla Natura"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
// No hay lógica adicional para este artículo
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

.img-principal {
  max-width: 350px;
  width: 100%;
  border-radius: 0.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
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

.img-seccion {
  max-width: 250px;
  width: 100%;
  border-radius: 0.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

/* .imagen-trio {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  margin-top: 2.5rem;
  flex-wrap: wrap;
} */
/* 
.img {
  max-width: 180px;
  width: 100%;
  border-radius: 0.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
} */

/* @media (max-width: 900px) {
  .presentation,
  .contenido-seccion,
  .imagen-trio {
    flex-direction: column;
    align-items: center;
    gap: 1.2rem;
  }
  .img-principal,
  .img-seccion,
  .img {
    max-width: 100%;
  }
} */
.icono {
  width: 20px;
  height: 20px;
  margin-right: 8px;
  vertical-align: middle;
}
</style>