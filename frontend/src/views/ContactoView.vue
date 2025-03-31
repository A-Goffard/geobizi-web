<template>
  <div class="contenedor-principal">
    <div class="contact-container">
      <h1>Contacto</h1>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="name">Nombre:</label>
          <input type="text" id="name" v-model="formData.name" required>
        </div>
        <div class="form-group">
          <label for="email">Correo Electrónico:</label>
          <input type="email" id="email" v-model="formData.email" required>
        </div>
        <div class="form-group">
          <label for="phone">Teléfono:</label>
          <input type="tel" id="phone" v-model="formData.phone" required>
        </div>
        <div class="form-group">
          <label for="message">Mensaje:</label>
          <textarea id="message" v-model="formData.message" required></textarea>
        </div>
        <div class="horizontalC">
          <input type="checkbox" id="privacy" v-model="formData.privacyAccepted" required>
          <label for="privacy">
            He leído y acepto la 
            <a href="/politica-de-privacidad" target="_blank">política de privacidad</a>.
          </label>
        </div>
        <div class="center">
          <button type="submit">Enviar mensaje</button>
        </div>
        <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const formData = ref({
  name: '',
  email: '',
  phone: '',
  message: '',
  privacyAccepted: false
});

const successMessage = ref('');
const errorMessage = ref('');

const submitForm = () => {
  successMessage.value = '';
  errorMessage.value = '';

  fetch('https://formspree.io/f/xanedzed', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(formData.value)
  })
    .then(response => {
      if (response.ok) {
        successMessage.value = 'Mensaje enviado correctamente.';
        formData.value = {
          name: '',
          email: '',
          phone: '',
          message: '',
          privacyAccepted: false
        };
      } else {
        throw new Error('Error al enviar el mensaje.');
      }
    })
    .catch(error => {
      errorMessage.value = 'Hubo un error al enviar el mensaje. Por favor, inténtalo de nuevo.';
      console.error('Error:', error);
    });
};
</script>

<style scoped>
.contenedor-principal {
  padding-top: 7rem;
  background-color: rgb(255, 255, 255);
  padding-bottom: 2rem;
}
.contact-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 2rem;
  border: 1px solid var(--shoftgreen);
  border-radius: 8px;
  box-shadow: 0px 0px 10px rgba(49, 49, 49, 0.7);
  padding-bottom: 2rem;
}
.horizontalC { 
  margin: 1rem;
  display: flex;
  flex-direction: row;
  gap: 1rem;
}
.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  font-weight: bold;
}

input[type="text"],
input[type="email"],
input[type="tel"],
textarea {
  width: 100%;
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid var(--shoftgreen);
  background-color: var(--megashoftgreen);
  border-radius: 4px;
}

button {
  padding: 0.75rem 1rem;
  background-color: var(--green);
  color: var(--white);
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: var(--lightgreen);
}

a{
  color: var(--green);
}

.center {
  display: flex;
  justify-content: center;

}

.success-message {
  color: var(--green);
  text-align: center;
  margin-top: 1rem;
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 1rem;
}

@media (max-width: 613px) {
  .contact-container {
    padding: 1rem;
    margin: 0.5rem;
  }
}
</style>