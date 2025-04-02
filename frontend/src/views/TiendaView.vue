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
        <h3>Información del producto</h3>
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
        <button @click="agregarAlCarrito(producto, 'producto')">Agregar al carrito</button>
      </div>
    </div>

    <div class="carrito">
      <h2>Carrito de compras</h2>
      <div v-if="carrito.length > 0">
        <div v-for="item in carrito" :key="item.id" class="carrito-item">
          <p>{{ item.nombre }} - {{ item.precioTotal }} €</p>
          <p v-if="item.fecha">Fecha seleccionada: {{ item.fecha }}</p>
          <p v-if="item.opciones && item.opciones.length > 0">
            Opciones adicionales:
            <ul>
              <li v-for="opcion in item.opciones" :key="opcion.nombre">
                {{ opcion.nombre }} (+{{ opcion.precio }} €)
              </li>
            </ul>
          </p>
          <button @click="eliminarDelCarrito(item.id)">Eliminar</button>
        </div>
        <p class="total">Total: {{ totalCarrito }} €</p>
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
const actividadesPublicadas = computed(() => actividades.filter(producto => producto.publicar));
const productosPublicados = computed(() => productos.filter(producto => producto.publicar));

// Obtener las fechas disponibles para cada actividad
const fechasDisponibles = computed(() => {
  const fechas = {};
  actividades.forEach((actividad) => {
    if (!fechas[actividad.titulo]) {
      fechas[actividad.titulo] = [];
    }
    if (actividad.fecha) {
      fechas[actividad.titulo].push(actividad.fecha);
    }
  });
  return fechas;
});

// Almacenar la fecha seleccionada y opciones adicionales para cada actividad
const productoSeleccionado = reactive(
  Object.fromEntries(actividadesPublicadas.value.map(producto => [producto.id, { fecha: '', opciones: [] }]))
);

// Carrito de compras
const carrito = reactive([]);

// Agregar producto o actividad al carrito
const agregarAlCarrito = (producto, tipo) => {
  if (tipo === 'actividad') {
    const seleccion = productoSeleccionado[producto.id];
    if (!seleccion || !seleccion.fecha) {
      alert('Por favor, selecciona una fecha para la actividad.');
      return;
    }

    const opcionesSeleccionadas = seleccion.opciones || [];
    const precioOpciones = opcionesSeleccionadas.reduce((total, opcion) => total + opcion.precio, 0);

    carrito.push({
      id: producto.id,
      nombre: producto.titulo,
      precioBase: producto.precio,
      precioTotal: producto.precio + precioOpciones,
      fecha: seleccion.fecha, // Mantener la fecha seleccionada
      opciones: opcionesSeleccionadas,
      stripeIds: [producto.stripeId, ...opcionesSeleccionadas.map(opcion => opcion.stripeId)]
    });

    // Reiniciar solo las opciones seleccionadas, pero mantener la fecha
    productoSeleccionado[producto.id].opciones = [];
  } else if (tipo === 'producto') {
    carrito.push({
      id: producto.id,
      nombre: producto.nombre,
      precioBase: producto.precio,
      precioTotal: producto.precio,
      stripeIds: [producto.stripeId]
    });
  }
};

// Eliminar producto o actividad del carrito
const eliminarDelCarrito = (productoId) => {
  const index = carrito.findIndex(item => item.id === productoId);
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
  margin: 0.5rem 0; /* Añadir margen alrededor del selector de fechas */
  padding: 0.5rem;
  font-size: 1rem;
}

.producto label {
  display: inline-flex; /* Asegurar que el checkbox y el texto estén en la misma línea */
  align-items: center; /* Alinear verticalmente el checkbox y el texto */
  margin-bottom: 0.5rem; /* Añadir margen inferior entre las opciones */
}

.producto input[type="checkbox"] {
  margin-right: 0.5rem; /* Añadir margen entre el checkbox y el texto */
  accent-color: var(--darkgreen); /* Cambiar el color del checkbox cuando está seleccionado */
}

.producto .extras {
  margin-top: 1rem; /* Añadir margen superior para separar los extras del resto */
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
</style>