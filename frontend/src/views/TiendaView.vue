<template>
  <div class="contenedor-principal">
    <h1 class="titulo">Tienda Online</h1>
    <div class="productos">
      <div v-for="producto in productos" :key="producto.id" class="producto">
        <h2>{{ producto.nombre }}</h2>
        <p>{{ producto.descripcion }}</p>
        <p class="precio">{{ producto.precio }} €</p>
        <button @click="comprarProducto(producto.id)">Comprar</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { loadStripe } from '@stripe/stripe-js'; // Importar el SDK de Stripe

const productos = ref([
  { id: 1, nombre: 'Actividad 1', descripcion: 'Descripción de la actividad 1', precio: 20 },
  { id: 2, nombre: 'Artículo 1', descripcion: 'Descripción del artículo 1', precio: 15 },
  // ...agregar más productos si es necesario
]);

const stripePublicKey = 'tu-clave-publica-de-stripe'; // Reemplaza con tu clave pública de Stripe
const stripePromise = loadStripe(stripePublicKey); // Cargar Stripe de forma asíncrona

const comprarProducto = async (productoId) => {
  const producto = productos.value.find(p => p.id === productoId);
  if (!producto) return;

  const stripe = await stripePromise; // Esperar a que Stripe esté listo
  stripe.redirectToCheckout({
    lineItems: [{ price: productoId, quantity: 1 }], // Asegúrate de configurar los precios en Stripe
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

.productos {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
}

.producto {
  border: 1px solid var(--lightgrey);
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
</style>