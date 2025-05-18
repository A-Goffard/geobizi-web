<template>
  <div class="contenedor-principal">
    <h1 class="titulo">Tienda Online</h1>
    <div class="tabs">
      <button :class="{ active: activeTab === 'actividades' }" @click="activeTab = 'actividades'">Actividades</button>
      <button :class="{ active: activeTab === 'productos' }" @click="activeTab = 'productos'">Productos</button>
    </div>

    <div v-if="activeTab === 'actividades'" class="actividades">
      <div v-for="producto in actividadesPublicadas" :key="producto.id" class="producto">
        <h2>{{ producto.titulo }}</h2>
        <p>{{ producto.descripcion1 }}</p>
        <p>{{ producto.descripcion2 }}</p>
        <p class="precio">{{ producto.precio }} €</p>
        <div v-if="fechasDisponibles[producto.titulo] && fechasDisponibles[producto.titulo].length > 0">
          <label for="fecha">Fecha:</label>
          <select v-model="productoSeleccionado[producto.id].fecha" :id="'fecha-' + producto.id">
            <option v-for="fecha in fechasDisponibles[producto.titulo]" :key="fecha" :value="fecha">
              {{ fecha }}
            </option>
          </select>
        </div>
        <div>
          <label for="numPersonas">Nº de personas:</label>
          <input
            type="number"
            min="1"
            v-model.number="productoSeleccionado[producto.id].numPersonas"
            :id="'numPersonas-' + producto.id"
            style="width: 60px; margin-left: 0.5rem; height: 2rem;"
          />
        </div>
        <div v-if="producto.opciones && producto.opciones.length > 0">
          <label>Opciones adicionales:</label>
          <div v-for="opcion in producto.opciones" :key="opcion.nombre">
            <input
              type="checkbox"
              :id="'opcion-' + producto.id + '-' + opcion.nombre"
              :value="opcion"
              v-model="productoSeleccionado[producto.id].opciones"
            />
            <label :for="'opcion-' + producto.id + '-' + opcion.nombre">
              {{ opcion.nombre }} (+{{ opcion.precio }} €)
            </label>
          </div>
        </div>
        <button @click="agregarAlCarrito(producto, 'actividad')">Agregar al carrito</button>
      </div>
    </div>

    <div v-if="activeTab === 'productos'" class="productos">
      <div v-for="producto in productosPublicados" :key="producto.id" class="producto">
        <h2>{{ producto.nombre }}</h2>
        <p>{{ producto.descripcion }}</p>
        <p class="precio">{{ producto.precio }} €</p>
        <p>¡Gastos de envío gratis!</p>
        <button @click="agregarAlCarrito(producto, 'producto')">Agregar al carrito</button>
      </div>
    </div>

    <div class="carrito">
      <h2>Carrito de compras</h2>
      <div v-if="carrito.length > 0">
        <div v-for="item in carrito" :key="item.id + '-' + item.fecha" class="carrito-item">
          <p>
            {{ item.nombre }}<br>
            <span v-if="item.fecha">Fecha: {{ item.fecha }}</span>
          </p>
          <div>
            <p>
              Nº personas: {{ item.numPersonas }}<br>
              Precio unitario: {{ item.precioUnitario.toFixed(2) }} €<br>
              <span v-if="item.opciones && item.opciones.length > 0">
                Opciones adicionales:<br>
                <ul>
                  <li v-for="opcion in item.opciones" :key="opcion.nombre">
                    {{ opcion.nombre }} (+{{ opcion.precio }} €)
                  </li>
                </ul>
              </span>
              <strong>Total: {{ item.precioTotal.toFixed(2) }} €</strong><br>
              <span class="iva-desglose">
                (IVA 21%: {{ calcularIVA(item.precioTotal).toFixed(2) }} € | Base: {{ (item.precioTotal - calcularIVA(item.precioTotal)).toFixed(2) }} €)
              </span>
            </p>
            <button @click="eliminarDelCarrito(item.id, item.fecha)">Eliminar</button>
          </div>
        </div>
        <p class="total">
          Total: {{ totalCarrito.toFixed(2) }} €<br>
          Base imponible: {{ (totalCarrito - calcularIVA(totalCarrito)).toFixed(2) }} €<br>
          IVA (21%): {{ calcularIVA(totalCarrito).toFixed(2) }} €
        </p>
        <button @click="pagarCarrito">Pagar todo</button>
      </div>
      <p v-else>El carrito está vacío.</p>
    </div>
  </div>
</template>

<script setup>
import { computed, reactive, ref } from 'vue';
import { loadStripe } from '@stripe/stripe-js';
import actividades from '@/assets/json/actividades.json';
import productos from '@/assets/json/productos.json';

const stripePublicKey = process.env.VUE_APP_STRIPE_PUBLIC_KEY;

if (!stripePublicKey) {
  console.error('La clave pública de Stripe no está configurada. Verifica el archivo .env.');
  throw new Error('VUE_APP_STRIPE_PUBLIC_KEY no está definida.');
}

const stripePromise = loadStripe(stripePublicKey);

const activeTab = ref('actividades'); // Controlar la pestaña activa

// Filtrar actividades y productos que tienen "publicar" como true
// Mostrar solo una actividad por título (la más próxima en fecha)
const actividadesPublicadas = computed(() => {
  const map = new Map();
  actividades
    .filter(producto => producto.publicar)
    .forEach(producto => {
      if (
        !map.has(producto.titulo) ||
        new Date(producto.fecha) < new Date(map.get(producto.titulo).fecha)
      ) {
        map.set(producto.titulo, producto);
      }
    });
  return Array.from(map.values());
});
const productosPublicados = computed(() => productos.filter(producto => producto.publicar));

// Obtener las fechas disponibles para cada actividad (solo futuras)
const fechasDisponibles = computed(() => {
  const fechas = {};
  const hoy = new Date();
  actividades.forEach((actividad) => {
    if (!fechas[actividad.titulo]) {
      fechas[actividad.titulo] = [];
    }
    if (
      actividad.fecha &&
      new Date(actividad.fecha) >= new Date(hoy.getFullYear(), hoy.getMonth(), hoy.getDate())
    ) {
      fechas[actividad.titulo].push(actividad.fecha);
    }
  });
  return fechas;
});

// Almacenar la fecha seleccionada, opciones y número de personas para cada actividad
const productoSeleccionado = reactive(
  Object.fromEntries(
    actividadesPublicadas.value.map(producto => [
      producto.id,
      { fecha: '', opciones: [], numPersonas: 1 }
    ])
  )
);

// Carrito de compras
const carrito = reactive([]);

// Calcular IVA (21%)
const calcularIVA = (total) => total * 0.21;

// Agregar producto o actividad al carrito
const agregarAlCarrito = (producto, tipo) => {
  if (tipo === 'actividad') {
    const seleccion = productoSeleccionado[producto.id];
    if (!seleccion || !seleccion.fecha) {
      alert('Por favor, selecciona una fecha para la actividad.');
      return;
    }
    const numPersonas = seleccion.numPersonas > 0 ? seleccion.numPersonas : 1;
    const opcionesSeleccionadas = seleccion.opciones || [];
    const precioOpciones = opcionesSeleccionadas.reduce((total, opcion) => total + opcion.precio, 0);
    const precioUnitario = producto.precio + precioOpciones;
    const precioTotal = precioUnitario * numPersonas;

    carrito.push({
      id: producto.id,
      nombre: producto.titulo,
      precioUnitario,
      precioBase: producto.precio,
      precioTotal,
      numPersonas,
      fecha: seleccion.fecha,
      opciones: opcionesSeleccionadas,
      stripeIds: Array(numPersonas).fill(producto.stripeId).concat(
        opcionesSeleccionadas.flatMap(opcion => Array(numPersonas).fill(opcion.stripeId))
      )
    });

    // Reiniciar solo las opciones seleccionadas, pero mantener la fecha y número de personas
    productoSeleccionado[producto.id].opciones = [];
  } else if (tipo === 'producto') {
    carrito.push({
      id: producto.id,
      nombre: producto.nombre,
      precioUnitario: producto.precio,
      precioBase: producto.precio,
      precioTotal: producto.precio,
      numPersonas: 1,
      stripeIds: [producto.stripeId]
    });
  }
};

// Eliminar producto o actividad del carrito (por id y fecha)
const eliminarDelCarrito = (productoId, fecha) => {
  const index = carrito.findIndex(item => item.id === productoId && item.fecha === fecha);
  if (index !== -1) {
    carrito.splice(index, 1);
  }
};

// Calcular el total del carrito
const totalCarrito = computed(() => carrito.reduce((total, item) => total + item.precioTotal, 0));

// Pagar todos los productos y actividades del carrito
const pagarCarrito = async () => {
  if (carrito.length === 0) {
    alert('El carrito está vacío.');
    return;
  }

  const stripe = await stripePromise;
  stripe.redirectToCheckout({
    lineItems: carrito.flatMap(item =>
      item.stripeIds.map(stripeId => ({
        price: stripeId,
        quantity: 1
      }))
    ),
    mode: 'payment',
    successUrl: window.location.origin + '/success',
    cancelUrl: window.location.origin + '/cancel',
  }).then((result) => {
    if (result.error) {
      console.error(result.error.message);
    }
  });
};
</script>

<style scoped>
.contenedor-principal {
  padding-top: 7rem;
  background-color: rgb(255, 255, 255);
  padding-bottom: 2rem;
}

.titulo {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 2rem;
}

.tabs {
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
}

.tabs button {
  background-color: var(--lightgrey);
  border: none;
  padding: 0.5rem 1rem;
  margin: 0 0.5rem;
  cursor: pointer;
  border-radius: 4px;
}

.tabs button.active {
  background-color: var(--lightgreen);
  color: var(--white);
}

.productos, .actividades {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
}

.producto {
  border: 1px solid var(--supershoftgreen);
  padding: 1rem;
  border-radius: 8px;
  text-align: center;
  width: 300px;
}

.producto h2 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.producto .precio {
  font-size: 1.2rem;
  font-weight: bold;
  margin: 1rem 0;
}

.producto select {
  margin: 0.5rem 0;
  padding: 0.5rem;
  font-size: 1rem;
}

.producto label {
  display: inline-flex;
  align-items: center; 
  margin-bottom: 0.5rem; 
}

.producto input[type="checkbox"] {
  margin-right: 0.5rem; 
  accent-color: var(--darkgreen); 
}

.producto .extras {
  margin-top: 1rem; 
}

.producto button {
  background-color: var(--lightgreen);
  color: var(--white);
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
}

.producto button:hover {
  background-color: var(--darkgreen);
}

.carrito {
  margin-top: 2rem;
  padding: 1rem;
  border: 1px solid var(--shoftgreen);
  border-radius: 8px;
  background-color: var(--megashoftgreen);
}

.carrito h2 {
  text-align: center;
  margin-bottom: 1rem;
}

.carrito-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.carrito-item button {
  background-color: var(--lightgreen);
  color: var (--white);
  border: none;
  padding: 0.3rem 0.5rem;
  border-radius: 4px;
  cursor: pointer;
}

.carrito-item button:hover {
  background-color: var(--darkgreen);
}

.total {
  font-weight: bold;
  text-align: center;
  margin-top: 1rem;
}

.carrito button {
  background-color: var(--lightgreen);
  color: var(--white);
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
}

.carrito button:hover {
  background-color: var(--darkgreen);
}

.iva-desglose {
  font-size: 0.95em;
  color: var(--darkgrey);
}
</style>