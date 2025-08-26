<template>
    <footer>
      <div class="footer-content">
        <ul class="footer-links">
          <li>
            <router-link class="footer-link" :to="{ name: 'privacidad' }" title="Política de privacidad">Política de privacidad</router-link>
          </li>
          <li>
            <router-link class="footer-link" :to="{ name: 'aviso' }" title="Aviso legal">Aviso legal</router-link>
          </li>
          <li>
            <router-link class="footer-link" :to="{ name: 'cancelaciones' }" title="Política de cancelaciones">Política de cancelaciones</router-link>
          </li>
        </ul>
        <div class="social-media">
          <a href="mailto:geobizi@hotmail.com" title="Enviar correo a GeoBizi">
            <img src="@/assets/icons/mail.png" alt="Email" class="social-icon" title="Email" loading="lazy" />
          </a>
          <a href="tel:+34677170921" title="Llamar a GeoBizi">
            <img src="@/assets/icons/telephone.png" alt="Phone" class="social-icon" title="Teléfono" loading="lazy" />
          </a>
          <a href="https://www.facebook.com/geobizirik/" target="_blank" rel="noopener noreferrer" title="GeoBizi en Facebook">
            <img src="@/assets/icons/facebook.png" alt="Facebook" class="social-icon" title="Facebook" loading="lazy" />
          </a>
          <a href="https://www.youtube.com/channel/UCw-C_J0y-jKHp7Zx92lsKfg" target="_blank" rel="noopener noreferrer" title="GeoBizi en YouTube">
            <img src="@/assets/icons/youtube.png" alt="YouTube" class="social-icon" title="YouTube" loading="lazy" />
          </a>
          <a href="https://www.instagram.com/geotxiki/" target="_blank" rel="noopener noreferrer" title="GeoBizi en Instagram">
            <img src="@/assets/icons/instagram.png" alt="Instagram" class="social-icon" title="Instagram" loading="lazy" />
          </a>
        </div>
        <p class="copyright">© Geobizi 2024. Todos los derechos reservados.</p>
        <div>
          <img class="compensacion" src="@/assets/icons/compensacionGeobizi.avif" alt="Sello de impacto compensado de Geobizi" title="Sello de impacto compensado de Geobizi" loading="lazy">
        </div>
      </div>
    </footer>
  </template>
  
  <script setup>
  </script>
  
  <style scoped>
  footer {
    background-color: var(--white);
    padding: 2rem;
    text-align: center;
    box-shadow: 0 -4px 6px -1px rgba(0, 0, 0, 0.1), 0 -2px 4px -1px rgba(0, 0, 0, 0.06);
  }
  
  .footer-content {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .footer-links {
    list-style: none;
    display: flex;
    gap: 2rem;
    margin-bottom: 1rem;
  }
  
  .footer-link {
    font-weight: bold;
    color: var(--green);
    text-decoration: none;
    transition: color 0.3s ease;
  }
  
  .footer-link:hover {
    color: var(--lightgreen);
  }
  
  .social-media {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
  }
  
  .social-icon {
    width: 24px;
    height: 24px;
    transition: transform 0.3s ease;
  }
  
  .social-icon:hover {
    transform: scale(1.1);
  }
  
  .copyright {
    color: var(--darkgrey);
  }

  .compensacion {
    width: 10rem;
    height: auto;
    margin-top: 0.5rem;
  }
  </style>
