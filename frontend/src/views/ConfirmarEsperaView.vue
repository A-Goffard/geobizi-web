<template>
  <div class="container-confirmar">
    <div class="card-confirmacion">

      <!-- Estado 1: Procesando la confirmación -->
      <div v-if="cargando" class="estado-caja">
        <div class="modal-icono">⏳</div>
        <h2 class="titulo-confirmar">Validando tu plaza...</h2>
        <p class="texto-cargando">Estamos confirmando tu turno en la lista de espera.</p>
      </div>

      <!-- Estado 2: Éxito (plaza asegurada) -->
      <div v-else-if="exito" class="estado-caja">
        <div class="modal-icono">🌿</div>
        <h2 class="titulo-exito">¡Plaza confirmada con éxito!</h2>
        <p class="mensaje-estado mensaje-exito">{{ mensaje }}</p>
        <p class="texto-sub">
          Tu reserva ya está activa en el sistema. Te hemos enviado un correo con todos los detalles y recomendaciones para la actividad.
        </p>
        <div class="acciones-botones">
          <button @click="router.push('/calendario')" class="btn-accion">
            Ver más actividades
          </button>
        </div>
      </div>

      <!-- Estado 3: Error o plazo expirado -->
      <div v-else class="estado-caja">
        <div class="modal-icono">⚠️</div>
        <h2 class="titulo-error">No se pudo confirmar la plaza</h2>
        <p class="mensaje-estado mensaje-error">{{ mensaje }}</p>
        <p class="texto-sub">
          Si el plazo de respuesta ha vencido, las plazas se habrán ofrecido automáticamente al siguiente grupo de la lista de espera.
        </p>
        <div class="acciones-botones">
          <button @click="router.push('/calendario')" class="btn-secundario">
            Volver al calendario
          </button>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const cargando = ref(true);
const exito = ref(false);
const mensaje = ref('');
const token = route.query.token;

onMounted(async () => {
  if (!token) {
    cargando.value = false;
    exito.value = false;
    mensaje.value = 'El enlace no es válido o no incluye ningún token de confirmación.';
    return;
  }

  try {
    const res = await fetch(`http://localhost:5000/api/token/${token}/aceptar-espera`, {
      method: 'POST'
    });

    const data = await res.json();

    if (res.ok) {
      exito.value = true;
      mensaje.value = data.message || 'Tu reserva ha sido confirmada correctamente.';
    } else {
      exito.value = false;
      mensaje.value = data.detail || 'No ha sido posible confirmar la plaza.';
    }
  } catch (err) {
    exito.value = false;
    mensaje.value = 'Error al conectar con el servidor. Inténtalo de nuevo más tarde.';
  } finally {
    cargando.value = false;
  }
});
</script>

<style scoped>
.container-confirmar {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 12rem);
  padding: 7rem 1.5rem 3rem 1.5rem;
  background-color: var(--white);
  box-sizing: border-box;
}

.card-confirmacion {
  width: 100%;
  max-width: 520px;
  background-color: var(--white);
  border: 1px solid var(--shoftgreen);
  border-radius: 0.5rem;
  padding: 2.5rem 2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  text-align: center;
}

.titulo-confirmar {
  color: var(--darkgrey);
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-size: 1.4rem;
}

.titulo-exito {
  color: var(--darkgreen);
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-size: 1.4rem;
}

.titulo-error {
  color: var(--brownred);
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-size: 1.4rem;
}

.texto-cargando,
.texto-sub {
  color: var(--darkgrey);
  line-height: 1.5;
  margin: 0.5rem 0 1.5rem 0;
  font-size: 0.95rem;
}
</style>