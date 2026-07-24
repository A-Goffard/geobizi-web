<template>
  <div class="contenedor-principal">
    <div class="contact-container">
      <h1>Contacto</h1>
      
      <!-- Aviso visual opcional para que sepas qué servicio están consultando si vienen de un botón -->
      <p v-if="servicioOrigen" class="aviso-servicio">
        Estás consultando sobre: <strong>{{ formatearNombreServicio(servicioOrigen) }}</strong>
      </p>

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
            <a href="/politica-de-privacidad" target="_blank" rel="noopener noreferrer" title="Política de privacidad de Geobizi">política de privacidad</a>.
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
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useHead } from '@vueuse/head';

const route = useRoute();
const servicioOrigen = ref('');

// Al cargar la página, leemos si viene un servicio en la URL (ej: ?servicio=talleres_colegios)
onMounted(() => {
  if (route.query.servicio) {
    servicioOrigen.value = route.query.servicio;
  }
});

// Función para poner bonito el nombre del servicio en el aviso visual
const formatearNombreServicio = (slug) => {
  const mapaServicios = {
    'talleres_colegios': 'Talleres para Colegios e Institutos',
    'talleres_municipios': 'Proyectos para Municipios y Entidades',
    'talleres_ferias': 'Talleres para Eventos y Ferias',
    'material_medida': 'Material Didáctico a Medida',
    'digital_yincanas': 'Yincanas y Rutas Digitales',
    'digital_recursos': 'Recursos Digitales Educativos',
    'digital_webs': 'Webs Eficientes y Sostenibles',
    'formacion_consultoria': 'Consultoría Educativa (STEAM)',
    'formacion_tecnica': 'Formación Profesional y Técnica',
    'formacion_neuroeducacion': 'Asesoramiento en Neuroeducación',
    'rutas_a_medida': 'Rutas Guiadas a Medida',
    'rutas_calendario': 'Rutas con Calendario (Fecha Fija)',
    'sensibilizacion_proyectos': 'Proyectos de Sensibilización y Regeneración'
  };
  return mapaServicios[slug] || slug;
};

const pageUrl = 'https://www.geobizi.com/contacto'
const ogImage = 'https://www.geobizi.com/imagenes/contacto/contacto-hero.avif'

useHead({
  title: 'Contacto | Geobizi',
  meta: [
    { name: 'description', content: 'Contacto de Geobizi: reservas, colaboraciones y consultas sobre actividades y proyectos medioambientales.' },
    { name: 'robots', content: 'index, follow' },
    { name: 'author', content: 'Geobizi' },
    { name: 'theme-color', content: '#0b8a4c' },
    { name: 'language', content: 'es' },
    { property: 'og:title', content: 'Contacto | Geobizi' },
    { property: 'og:description', content: 'Contacto de Geobizi para reservas, colaboraciones y consultas.' },
    { property: 'og:type', content: 'website' },
    { property: 'og:url', content: pageUrl },
    { property: 'og:image', content: ogImage }
  ],
  link: [
    { rel: 'canonical', href: pageUrl },
    { rel: 'image_src', href: ogImage },
    { rel: 'apple-touch-icon', href: '/apple-touch-icon.png', sizes: '180x180' }
  ],
  script: [
    {
      type: 'application/ld+json',
      children: JSON.stringify({
        "@context":"https://schema.org",
        "@graph":[
          {
            "@type":"Organization",
            "@id":"https://www.geobizi.com/#organization",
            "name":"Geobizi",
            "url":"https://www.geobizi.com",
            "logo": { "@type":"ImageObject","url":"https://www.geobizi.com/imagenes/GeobiziLogo.7ae1d6ce.png","width":1417,"height":313 },
            "sameAs":[
              "https://www.facebook.com/geobizirik/",
              "https://www.instagram.com/geotxiki/",
              "https://www.youtube.com/channel/UCw-C_J0y-jKHp7Zx92lsKfg"
            ]
          },
          {
            "@type":"ContactPage",
            "url": pageUrl,
            "name":"Contacto | Geobizi",
            "description":"Formulario y datos de contacto para reservas, colaboraciones y consultas.",
            "inLanguage":"es",
            "isPartOf": { "@id": "https://www.geobizi.com/#organization" },
            "image": { "@type":"ImageObject","url":ogImage,"width":1080,"height":1080 }
          }
        ]
      })
    }
  ]
})

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

  // Preparamos los datos incluyendo el servicio de origen para que te llegue en el email
  const datosParaEnviar = {
    ...formData.value,
    'Servicio Consultado': servicioOrigen.value ? formatearNombreServicio(servicioOrigen.value) : 'Contacto General / Sin especificar'
  };

  fetch('https://formspree.io/f/xanedzed', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(datosParaEnviar)
  })
    .then(response => {
      if (response.ok) {
        successMessage.value = 'Mensaje enviado correctamente.';
        
        // --- REGISTRAR EVENTO EN GOOGLE ANALYTICS ---
        if (typeof window.gtag === 'function') {
          window.gtag('event', 'enviar_contacto', {
            'event_category': 'Contacto',
            'servicio_consultado': servicioOrigen.value || 'general'
          });
        }

        formData.value = {
          name: '',
          email: '',
          phone: '',
          message: '',
          privacyAccepted: false
        };
        servicioOrigen.value = ''; // Limpiamos el origen
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
.aviso-servicio {
  background-color: var(--megashoftgreen);
  border-left: 4px solid var(--shoftgreen);
  padding: 0.75rem;
  margin-bottom: 1.5rem;
  font-size: 0.95rem;
  border-radius: 4px;
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
    padding-left: 1rem;
    padding-right: 1rem;
    margin: 0.5rem;
  }
}
</style>