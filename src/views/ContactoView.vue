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
        <input type="tel" id="phone" v-model="formData.phone">
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
    </form>
  </div>
</div>
</template>

<script setup>
import { ref } from 'vue'

const formData = ref({
  name: '',
  email: '',
  phone: '',
  message: '',
  privacyAccepted: false
})

const submitForm = () => {
  if (!formData.value.privacyAccepted) {
    alert('Debes aceptar la política de privacidad para enviar el mensaje.')
    return
  }

  // Aquí puedes implementar el código para enviar el formulario
  // Por ejemplo, utilizando un servicio de backend o enviando un correo electrónico
  const messageData = {
    name: formData.value.name,
    email: formData.value.email,
    phone: formData.value.phone,
    message: formData.value.message
  }

  // Simulación de envío de correo electrónico
  const emailRecipient = 'geobizi@hotmail.com'
  const emailBody = `
    Nombre: ${messageData.name}\n
    Correo Electrónico: ${messageData.email}\n
    Teléfono: ${messageData.phone}\n
    Mensaje: ${messageData.message}
  `
  // Aquí podrías realizar el envío del correo electrónico utilizando tu backend o servicio apropiado
  console.log('Enviando correo electrónico a', emailRecipient, 'con el siguiente contenido:')
  console.log(emailBody)

  // Reiniciar el formulario después de enviar
  formData.value.name = ''
  formData.value.email = ''
  formData.value.phone = ''
  formData.value.message = ''
  formData.value.privacyAccepted = false

  alert('Mensaje enviado correctamente.')
}
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
  background-color: var(--supershoftgreen);
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
</style>
