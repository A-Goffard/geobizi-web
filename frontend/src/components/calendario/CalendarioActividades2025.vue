<template>
  <div class="calendario">
    <div class="navegacion">
      <div class="anio-selector">
        <button class="elegir" @click="anioAnterior">&lt;</button>
        <span class="anio">{{ anioActual }}</span>
        <button class="elegir" @click="anioSiguiente">&gt;</button>
      </div>
      <div class="mes-selector">
        <button class="elegir" @click="mesAnterior">&lt;</button>
        <h3>{{ meses[mesActual].nombre }}</h3>
        <button class="elegir" @click="mesSiguiente">&gt;</button>
      </div>
    </div>

    <div class="mes">
      <!-- Días de la semana -->
      <div class="grid">
        <div v-for="dia in diasSemana" :key="dia" class="dia-semana">
          {{ dia }}
        </div>

        <!-- Días del mes -->
        <div v-for="dia in getDiasDelMes(mesActual)" :key="dia.fecha || 'vacio-' + mesActual" 
             class="dia" :class="{ vacio: !dia.numero }">
          <span v-if="dia.numero" class="numero">{{ dia.numero }}</span>

          <div class="puntos">
            <div
              v-for="actividad in dia.actividades"
              :key="actividad.titulo"
              class="punto"
              :style="{ backgroundColor: actividad.color, cursor: 'pointer' }"
              @mouseover="!isMobile && mostrarTooltip(actividad, $event)"
              @mouseleave="!isMobile && ocultarTooltip()"
              @touchstart.prevent="isMobile && mostrarTooltip(actividad, $event)"
              @click="irAReserva(actividad, $event)"
              title="Reservar esta actividad"
            ></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Tooltip -->
    <div
      v-if="tooltip.visible"
      class="tooltip"
      :style="{ top: tooltip.y + 'px', left: tooltip.x + 'px', maxWidth: '180px', zIndex: 1000 }"
      @click="isMobile && irAReserva(tooltip.actividad, $event)"
    >
      <strong>{{ tooltip.titulo }}</strong><br>
      <span>{{ tooltip.hora }}</span>
      <div v-if="isMobile" style="font-size:11px; margin-top:4px; color:#ccc;">Toca de nuevo para reservar</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import actividadesData from "@/assets/json/actividades.json";

// Lista de meses
const meses = ref([
  { nombre: "Enero" }, { nombre: "Febrero" }, { nombre: "Marzo" },
  { nombre: "Abril" }, { nombre: "Mayo" }, { nombre: "Junio" },
  { nombre: "Julio" }, { nombre: "Agosto" }, { nombre: "Septiembre" },
  { nombre: "Octubre" }, { nombre: "Noviembre" }, { nombre: "Diciembre" }
]);

// Días de la semana
const diasSemana = ref(["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]);

// Tooltip
const tooltip = ref({ visible: false, titulo: "", hora: "", x: 0, y: 0, actividad: null });

// Año y mes actual
const anioActual = ref(new Date().getFullYear());
const mesActual = ref(new Date().getMonth());

const router = useRouter();

const irAReserva = (actividad, event) => {
  if (isMobile.value) {
    // Si el tooltip no está visible o es de otra actividad, solo muestra el tooltip
    if (!tooltip.value.visible || tooltip.value.actividad !== actividad) {
      mostrarTooltip(actividad, event);
      return;
    }
    // Si el tooltip ya está visible para esta actividad, navega
    ocultarTooltip();
    const hoy = new Date();
    const fechaActividad = new Date(actividad.fecha + 'T' + (actividad.hora || '00:00'));
    if (fechaActividad >= hoy) {
      if (actividad.reservas) {
        router.push({ name: 'reservaActividad', params: { id: actividad.id } });
      } else {
        router.push({ name: 'reservas' });
      }
    }
  } else {
    // Desktop: navega directamente
    const hoy = new Date();
    const fechaActividad = new Date(actividad.fecha + 'T' + (actividad.hora || '00:00'));
    if (fechaActividad >= hoy) {
      if (actividad.reservas) {
        router.push({ name: 'reservaActividad', params: { id: actividad.id } });
      } else {
        router.push({ name: 'reservas' });
      }
    }
  }
};

// Función para obtener los días del mes con sus actividades
const getDiasDelMes = (mesIndex) => {
  const year = anioActual.value;
  const primerDiaSemana = new Date(year, mesIndex, 1).getDay(); // 0 = Domingo, 1 = Lunes, etc.
  const diasEnMes = new Date(year, mesIndex + 1, 0).getDate();
  let dias = [];

  // Ajustar para que la semana empiece en Lunes
  const primerDiaIndex = primerDiaSemana === 0 ? 6 : primerDiaSemana - 1;

  // Añadir espacios vacíos antes del primer día del mes
  for (let i = 0; i < primerDiaIndex; i++) {
    dias.push({ numero: null, fecha: null, actividades: [] });
  }

  // Añadir los días del mes con actividades
  for (let i = 1; i <= diasEnMes; i++) {
    const fecha = `${year}-${(mesIndex + 1).toString().padStart(2, "0")}-${i.toString().padStart(2, "0")}`;
    const actividades = actividadesData.filter(a => a.fecha === fecha);
    dias.push({ numero: i, fecha, actividades });
  }

  return dias;
};

// Detecta móvil por tamaño de pantalla o touch
const isMobile = ref(false);

onMounted(() => {
  isMobile.value = window.innerWidth <= 600 || 'ontouchstart' in window;
  window.addEventListener('resize', () => {
    isMobile.value = window.innerWidth <= 600 || 'ontouchstart' in window;
  });
  console.log("Calendario cargado");
});

// Mostrar tooltip
const mostrarTooltip = (actividad, event) => {
  if (isMobile.value) {
    // Centra el tooltip en móvil y ajusta para que no se salga
    let x = event.touches ? event.touches[0].clientX : event.clientX;
    let y = event.touches ? event.touches[0].clientY : event.clientY;
    // Ajuste para que no se salga de la pantalla
    const tooltipWidth = 180;
    const tooltipHeight = 60;
    const padding = 10;
    if (x + tooltipWidth > window.innerWidth) x = window.innerWidth - tooltipWidth - padding;
    if (y + tooltipHeight > window.innerHeight) y = window.innerHeight - tooltipHeight - padding;
    tooltip.value = { visible: true, titulo: actividad.titulo, hora: actividad.hora, x, y, actividad };
  } else {
    // Desktop: igual que antes, pero ajusta si se sale
    let x = event.pageX + 10;
    let y = event.pageY + 10;
    const tooltipWidth = 180;
    const tooltipHeight = 60;
    if (x + tooltipWidth > window.innerWidth) x = window.innerWidth - tooltipWidth - 10;
    if (y + tooltipHeight > window.innerHeight) y = window.innerHeight - tooltipHeight - 10;
    tooltip.value = { visible: true, titulo: actividad.titulo, hora: actividad.hora, x, y, actividad };
  }
};

// Ocultar tooltip
const ocultarTooltip = () => {
  tooltip.value.visible = false;
  tooltip.value.actividad = null;
};

// Cambiar al mes anterior
const mesAnterior = () => {
  if (mesActual.value > 0) {
    mesActual.value--;
  } else {
    mesActual.value = 11;
    anioActual.value--;
  }
};

// Cambiar al mes siguiente
const mesSiguiente = () => {
  if (mesActual.value < 11) {
    mesActual.value++;
  } else {
    mesActual.value = 0;
    anioActual.value++;
  }
};

// Cambiar al año anterior
const anioAnterior = () => {
  anioActual.value--;
};

// Cambiar al año siguiente
const anioSiguiente = () => {
  anioActual.value++;
};
</script>

<style scoped>
.calendario {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.navegacion {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 22rem;
  margin-bottom: 1rem;
  gap: 1.2rem;
}

.anio-selector {
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 7.5rem;
  max-width: 7.5rem;
  gap: 0.5rem;
}

.mes-selector {
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 11rem;
  max-width: 11rem;
  gap: 0.5rem;
}

.anio {
  font-size: 1.2rem;
  margin: 0 0.5rem;
  display: inline-block;
  width: 3rem;
  text-align: center;
}

.mes-selector h3 {
  margin: 0 0.5rem;
  min-width: 6rem;
  text-align: center;
  font-size: 1.1rem;
  font-weight: bold;
}

.mes {
  width: 100%;       
  max-width: 22rem; 
  margin: 1rem 0;    
  padding: 0 10px;  
  box-sizing: border-box;
}

.grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 0.3rem;
  background-color: var(--supershoftgreen);
  padding: 0.7rem;
  border-radius: 0.5rem;
}

/* Días de la semana */
.dia-semana {
  font-weight: bold;
  text-align: center;
  padding: 0.2rem;
  background-color: var(--shoftgreen);
  border-radius: 0.2rem;
}

/* Estilo para cada día del mes */
.dia {
  width: 40px;
  height: 40px;
  background: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  position: relative;
}

/* Espacios vacíos */
.dia.vacio {
  background: none;
  pointer-events: none;
}

/* Números de los días */
.numero {
  font-size: 14px;
  font-weight: bold;
}

/* Contenedor de puntos */
.puntos {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 5px;
}

/* Puntos de colores */
.punto {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  margin: 1px;
}

/* Tooltip */
.tooltip {
  position: fixed;
  background: rgba(0, 0, 0, 0.85);
  color: white;
  padding: 7px 12px;
  border-radius: 4px;
  font-size: 13px;
  pointer-events: auto;
  z-index: 1000;
  max-width: 180px;
  word-break: break-word;
  box-sizing: border-box;
}
@media (max-width: 600px) {
  .tooltip {
    font-size: 14px;
    padding: 10px 14px;
    max-width: 90vw;
  }
}

.elegir {
  background-color: var(--shoftgreen);
  color: var(--black);
  font-size: 1rem;
  font-weight: bold;
  border: none;
  border-radius: 4px;
  padding: 0.5rem;
  cursor: pointer;
}
</style>