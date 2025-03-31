<template>
  <div class="calendario">
    <div class="navegacion">
      <button class="elegir" @click="mesAnterior">&lt;</button>
      <h3>{{ meses[mesActual].nombre }}</h3>
      <button class="elegir" @click="mesSiguiente">&gt;</button>
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
            <div v-for="actividad in dia.actividades" 
                 :key="actividad.titulo" 
                 class="punto" 
                 :style="{ backgroundColor: actividad.color }"
                 @mouseover="mostrarTooltip(actividad, $event)"
                 @mouseleave="ocultarTooltip">
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Tooltip -->
    <div v-if="tooltip.visible" class="tooltip" :style="{ top: tooltip.y + 'px', left: tooltip.x + 'px' }">
      <strong>{{ tooltip.titulo }}</strong><br>
      <span>{{ tooltip.hora }}</span>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
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
const tooltip = ref({ visible: false, titulo: "", hora: "", x: 0, y: 0 });

// Mes actual
const mesActual = ref(new Date().getMonth());

// Función para obtener los días del mes con sus actividades
const getDiasDelMes = (mesIndex) => {
  const year = 2025;
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

// Mostrar tooltip
const mostrarTooltip = (actividad, event) => {
  tooltip.value = { visible: true, titulo: actividad.titulo, hora: actividad.hora, x: event.pageX + 10, y: event.pageY + 10 };
};

// Ocultar tooltip
const ocultarTooltip = () => {
  tooltip.value.visible = false;
};

// Cambiar al mes anterior
const mesAnterior = () => {
  if (mesActual.value > 0) {
    mesActual.value--;
  }
};

// Cambiar al mes siguiente
const mesSiguiente = () => {
  if (mesActual.value < 11) {
    mesActual.value++;
  }
};

onMounted(() => {
  console.log("Calendario cargado");
});
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
  justify-content: space-between;
  width: 20.65rem;
  margin-bottom: 1rem;
}

.mes {
  width: 20.65rem;
  margin: 1rem;
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
  position: absolute;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 5px;
  border-radius: 4px;
  font-size: 12px;
  pointer-events: none;
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