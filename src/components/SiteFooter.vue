<template>
    <div class="contenedor-principal">


    <footer class="footer">
      <div class="links">
        <ul>
          <li><router-link to="/privacy-policy" class="link">Política de privacidad</router-link></li>
          <li><router-link to="/legal-notice" class="link">Aviso legal</router-link></li>
          <li><router-link to="/cancellation-policy" class="link">Política de cancelaciones</router-link></li>
        </ul>
      </div>
      <div class="copyright">
        <p>&copy; Geobizi 2024. Todos los derechos reservados.</p>
      </div>
      <div class="icons">
            <a href="https://www.facebook.com/geotxiki/" target="_blank"><img class="icon" src="imagenes/iconos/facebook.png" alt="facebook"></a>
            <a href="https://www.instagram.com/geotxiki/" target="_blank"><img class="icon" src="imagenes/iconos/instagram.png" alt="instagram"></a>
            <a href="https://www.linkedin.com/company/geobizi/" target="_blank"><img class="icon" src="imagenes/iconos/linkedin.png" alt="linkedin"></a>
            <a href="tel:+34677170921" target="_blank"><img class="icon" src="imagenes/iconos/telefono.png" alt="telefono"></a>
            <a href="https://www.youtube.com/channel/UCw-C_J0y-jKHp7Zx92lsKfg" target="_blank"><img class="icon" src="imagenes/iconos/youtube.png" alt="youtube"></a>
            <a href="mailto:geobizi@hotmail.com" target="_blank"><img class="icon" src="imagenes/iconos/mail.png" alt="mail"></a>
        </div>    
    </footer>
</div>
</template>

<script setup>
</script>

<style scoped>
.contenedor-principal {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
.footer {

    width: 75%;
    border-top: solid 1px #66ca47;
    padding: 1rem;
}

.links ul {
  list-style-type: none;
  padding: 0;
}

.links ul li {
  display: inline;
  margin-right: 1rem;
}

.icons {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  margin: 1rem;
}

.icon {
  width: 3rem;
}
.copyright,
.links {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  font-size: smaller;
}

.links ul {
    font-size: smaller;
}

.link {
  font-weight: bold;
  color: #498536;
  position: relative;
  transition: 250s ease all;
}

.link:hover {
  color: #26b12c;
  border-color: #26b12c;
  cursor: pointer;
}

.link:hover::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -3px;
  width: 100%;
  height: 2px;
  background-color: #26b12c;
  cursor: pointer;
}

@media (max-width: 500px) {

    .links ul {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 0.5rem;
    }
  }
</style>
