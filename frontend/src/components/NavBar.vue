<template>
    <header :class="{ 'scrolled-nav': scrolledNav }">
      <nav>
        <div class="branding">
          <router-link :to="{name: 'inicio'}">
            <img src="@/assets/GeobiziLogo.png" class="logo" alt="">
          </router-link>
        </div>
        <ul v-show="!mobile" class="navigation">
          <li>
            <router-link class="NavButton link" :to="{name: 'inicio'}" @click="closeMobileNav">Inicio</router-link>
          </li>
          <li>
            <router-link class="NavButton link" :to="{name: 'servicios'}" @click="closeMobileNav">Servicios</router-link>
          </li>
          <li>
            <router-link class="NavButton link" :to="{name: 'calendario'}" @click="closeMobileNav">Calendario</router-link>
          </li>
          <li>
            <router-link class="NavButton link" :to="{name: 'reservas'}" @click="closeMobileNav">Reservas</router-link>
          </li>
          <!-- <li>
            <router-link class="NavButton link" :to="{name: 'tienda'}" @click="closeMobileNav">Tienda</router-link>
          </li> -->
          <li>
            <router-link class="NavButton link" :to="{name: 'blog'}" @click="closeMobileNav">Blog</router-link>
          </li>
          <li>
            <router-link class="NavButton link" :to="{name: 'projectos'}" @click="closeMobileNav">Proyectos</router-link>
          </li>
          <li>
            <router-link class="NavButton link" :to="{name: 'contacto'}" @click="closeMobileNav">Contacto</router-link>
          </li>
        </ul>
        <div class="icon">
            <button @click="toggleMobileNav" v-show="mobile">
                <img :class="{ 'icon-active': mobileNav }" src="@/assets/Hojitas.png" class="hojitas" alt="">
            </button>
        </div>
        <transition name="mobile-nav">
          <ul v-show="mobileNav" class="dropdown-nav">
            <li>
              <router-link class="NavButton link" :to="{name: 'inicio'}" @click="closeMobileNav">Inicio</router-link>
            </li>
            <li>
              <router-link class="NavButton link" :to="{name: 'servicios'}" @click="closeMobileNav">Servicios</router-link>
            </li>
            <li>
              <router-link class="NavButton link" :to="{name: 'calendario'}" @click="closeMobileNav">Calendario</router-link>
            </li>
            <li>
              <router-link class="NavButton link" :to="{name: 'reservas'}" @click="closeMobileNav">Reservas</router-link>
            </li>
            <!-- <li>
              <router-link class="NavButton link" :to="{name: 'tienda'}" @click="closeMobileNav">Tienda</router-link>
            </li> -->
            <li>
              <router-link class="NavButton link" :to="{name: 'blog'}" @click="closeMobileNav">Blog</router-link>
            </li>
            <li>
              <router-link class="NavButton link" :to="{name: 'projectos'}" @click="closeMobileNav">Proyectos</router-link>
            </li>
            <li>
              <router-link class="NavButton link" :to="{name: 'contacto'}" @click="closeMobileNav">Contacto</router-link>
            </li>

          </ul>
        </transition>
      </nav>
    </header>
  </template>
  
  <script setup>
  import { ref, onMounted, onUnmounted } from 'vue';
  
  const mobileNav = ref(false);
  const mobile = ref(true);
  const scrolledNav = ref(false);
  
  const toggleMobileNav = () => {
    mobileNav.value = !mobileNav.value;
    const hojitasIcon = document.querySelector('.hojitas');
    if (hojitasIcon) {
        hojitasIcon.style.transform = mobileNav.value ? 'rotate(45deg)' : 'rotate(0deg)';
    }
};
  
const closeMobileNav = () => {
  mobileNav.value = false;
  const hojitasIcon = document.querySelector('.hojitas');
  if (hojitasIcon) {
    hojitasIcon.style.transform = 'rotate(0deg)';
  }
};
  
  const updateScroll = () => {
    scrolledNav.value = window.scrollY > 50;
  };
  
  const checkScreen = () => {
    mobile.value = window.innerWidth <= 940;
    if (mobile.value) {
      mobileNav.value = false;
    }
  };

  const closeOnClickOutside = (event) => {
  const nav = document.querySelector('.dropdown-nav');
  const button = document.querySelector('.icon button');

  if (mobileNav.value && nav && !nav.contains(event.target) && button && !button.contains(event.target)) {
    closeMobileNav();
  }
};

  onMounted(() => {
  window.addEventListener('resize', checkScreen);
  window.addEventListener('scroll', updateScroll);
  document.addEventListener('click', closeOnClickOutside);
 });
  
 onUnmounted(() => {
  window.removeEventListener('resize', checkScreen);
  window.removeEventListener('scroll', updateScroll);
  document.removeEventListener('click', closeOnClickOutside);
});
  
  checkScreen();
  </script>
  
  <style scoped>
  header {
    box-sizing: border-box;
    background-color: var(--white);
    z-index: 99;
    width: 100%;
    position: fixed;
    height: 3.5rem;
    transition: 0.5s ease all;
  }

  header nav {
    position: relative;
    display: flex;
    flex-direction: row;
    padding: 0.5em 0;
    transition: 0.5s ease all;
    width: 100%;
    margin: 0rem 0rem;
  }
  
  header nav .branding img {
    max-height: 5rem;
  }
  
  header nav .navigation {
    display: flex;
    align-items: center;
    flex: 1;
    justify-content: right;
  }
  
  header nav .icon {
    display: flex;
    align-items: center;
    position: absolute;
    top: 0.1rem;
    right: 0.5rem;
  }
  
  header nav button {
    width: 4rem;
    cursor: pointer;
    transition: 0.8s ease all;
    background-color: transparent;
    border: none;
    margin: 0.5rem;
  }
  
  header nav .hojitas {
    width: 100%;
    transition: transform 0.5s ease;
  }
  
  header nav .dropdown-nav {
    display: flex;
    flex-direction: column;
    position: fixed;
    width: 100%;
    max-width: 250px;
    height: 100%;
    background-color: var(--white);
    top: 0;
    left: 0;
    padding-top: 1rem;
  }
  
  header nav .dropdown-nav li {
    margin-left: 1rem;
  }
  
  header nav .mobile-nav-enter-active,
  header nav .mobile-nav-leave-active {
    transition: 1s ease all;
  }
  
  header nav .mobile-nav-enter-from,
  header nav .mobile-nav-leave-to {
    transform: translateX(-250px);
  }
  
  header nav .mobile-nav-enter-to {
    transform: translateX(0);
  }
  
  .scrolled-nav {
    background-color: rgba(255, 255, 255, 1);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  }
  
  .scrolled-nav nav {
    padding: 0.5rem 0;
  }
  
  .link {
    font-weight: bold;
    color: var(--green);
    position: relative;
    transition: 250s ease all;
  }
  
  .link:hover {
    color: var(--lightgreen);
    border-color: var(--lightgreen);
    cursor: pointer;
  }
  
  .link:hover::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: -3px;
    width: 100%;
    height: 2px;
    background-color: var(--lightgreen);
    cursor: pointer;
  }

  ul{
    margin: 0;
  }
  
  li {
    padding: 0.5rem 0.5rem;
    margin-top: 0.2rem;
  }

  .logo {
    position: absolute;
    height: 2.8rem;
  }
  @media (min-width: 1024px) {
    li {
      padding: 0.5rem 1.5rem;
    }
  }
  @media (min-width: 768px) {
    li {
      padding: 0.5rem 1rem;
    }
  }

  </style>



