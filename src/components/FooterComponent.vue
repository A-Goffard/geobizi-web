<template>
    <footer>
      <div class="footer-content">
        <ul class="footer-links">
          <li>
            <router-link class="footer-link" :to="{ name: 'privacidad' }">Política de privacidad</router-link>
          </li>
          <li>
            <router-link class="footer-link" :to="{ name: 'aviso' }">Aviso legal</router-link>
          </li>
          <li>
            <router-link class="footer-link" :to="{ name: 'cancelaciones' }">Política de cancelaciones</router-link>
          </li>
        </ul>
        <div class="social-media">
          <a href="mailto:geobizi@hotmail.com">
            <img src="@/assets/icons/mail.png" alt="Email" class="social-icon" />
          </a>
          <a href="tel:+34677170921">
            <img src="@/assets/icons/telephone.png" alt="Phone" class="social-icon" />
          </a>
          <a href="https://www.facebook.com/geobizirik/" target="_blank">
            <img src="@/assets/icons/facebook.png" alt="Facebook" class="social-icon" />
          </a>
          <a href="https://www.youtube.com/channel/UCw-C_J0y-jKHp7Zx92lsKfg" target="_blank">
            <img src="@/assets/icons/youtube.png" alt="YouTube" class="social-icon" />
          </a>
          <a href="https://www.instagram.com/geotxiki/" target="_blank">
            <img src="@/assets/icons/instagram.png" alt="Instagram" class="social-icon" />
          </a>
        </div>
        <p class="copyright">© Geobizi 2024. Todos los derechos reservados.</p>
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
    color: var(--ligthgreen);
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
  </style>
  