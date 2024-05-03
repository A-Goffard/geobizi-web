<template>
    <header :class="{ 'scrolled-nav': scrolledNav }">
      <nav>
        <div class="branding">
          <img src="@/assets/GeobiziLogo.png" class="logo" alt="">
        </div>
        <ul v-show="!mobile" class="navigation">
          <li>
            <router-link class="NavButton link" :to="{name: 'inicio'}" @click="closeMobileNav">Inicio</router-link>
          </li>
          <li>
            <router-link class="NavButton link" :to="{name: 'filosofia'}" @click="closeMobileNav">Filosofía</router-link>
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
          <li>
            <router-link class="NavButton link" :to="{name: 'geotienda'}" @click="closeMobileNav">Geotienda</router-link>
          </li>
          <li>
            <router-link class="NavButton link" :to="{name: 'blog'}" @click="closeMobileNav">Blog</router-link>
          </li>
          <li>
            <router-link class="NavButton link" :to="{name: 'contacto'}" @click="closeMobileNav">Contacto</router-link>
          </li>
        </ul>
        <div class="icon">
            <button @click="toggleMobileNav" v-show="mobile">
                <img :class="{ 'icon-active': mobileNav }" src="@/assets/logoBurguer.png" class="hojitas" alt="">
            </button>
        </div>
        <transition name="mobile-nav">
          <ul v-show="mobileNav" class="dropdown-nav">
            <li>
              <router-link class="NavButton link" :to="{name: 'inicio'}" @click="closeMobileNav">Inicio</router-link>
            </li>
            <li>
              <router-link class="NavButton link" :to="{name: 'filosofia'}" @click="closeMobileNav">Filosofía</router-link>
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
            <li>
              <router-link class="NavButton link" :to="{name: 'geotienda'}" @click="closeMobileNav">Geotienda</router-link>
            </li>
            <li>
              <router-link class="NavButton link" :to="{name: 'blog'}" @click="closeMobileNav">Blog</router-link>
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
  };
  
  const updateScroll = () => {
    scrolledNav.value = window.scrollY > 50;
  };
  
  const checkScreen = () => {
    mobile.value = window.innerWidth <= 990;
    if (mobile.value) {
      mobileNav.value = false;
    }
  };
  
  onMounted(() => {
    window.addEventListener('resize', checkScreen);
    window.addEventListener('scroll', updateScroll);
  });
  
  onUnmounted(() => {
    window.removeEventListener('resize', checkScreen);
    window.removeEventListener('scroll', updateScroll);
  });
  
  checkScreen();
  </script>
  
  <style scoped lang="scss">
  header {
    box-sizing: border-box;
    background-color: rgb(255, 255, 255);
    z-index: 99;
    width: 100%;
    position: fixed;
    transition: 0.5s ease all;
  
    nav {
      position: relative;
      display: flex;
      flex-direction: row;
      padding: 0.5em 0;
      transition: 0.5s ease all;
      width: 98%;
      margin: 0rem 1rem;
  
      @media(min-width: 990px) {
        max-width: 1250px;
      }
  
      .branding {
        img {
          max-height: 5rem;
        }
      }
  
      .navigation {
        display: flex;
        align-items: center;
        flex: 1;
        justify-content: flex-end;
      }
  
      .icon {
        display: flex;
        align-items: center;
        position: absolute;
        top: 0;
        right: 0.5rem;
      }
  
      button {
        width: 4rem;
        cursor: pointer;
        transition: 0.8s ease all;
        background-color: transparent;
        border: none;
        margin: 0.5rem
      }
  
      .hojitas {
        width: 100%;
        transition: transform 0.5s ease;
      }
  
      .dropdown-nav {
        display: flex;
        flex-direction: column;
        position: fixed;
        width: 100%;
        max-width: 250px;
        height: 100%;
        background-color: rgb(255, 255, 255);
        top: 0;
        left: 0;
  
        li {
          margin-left: 1rem;
        }
      }
  
      .mobile-nav-enter-active,
      .mobile-nav-leave-active {
        transition: 1s ease all;
      }
  
      .mobile-nav-enter-from,
      .mobile-nav-leave-to {
        transform: translateX(-250px);
      }
  
      .mobile-nav-enter-to {
        transform: translateX(0);
      }
    }
  }
  
  .scrolled-nav {
    background-color: rgb(255, 255, 255,);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  
    nav {
      padding: 0.5rem 0;
  
      }
    }
  
  .link {
    font-weight: bold;
    color: #498536;
    position: relative;
    transform: 250s ease all;
  
    &:hover {
      color: #26B12C;
      border-color: #26B12C;
  
      &::after {
        content: '';
        position: absolute;
        left: 0;
        bottom: -3px;
        width: 100%;
        height: 2px;
        background-color: #26B12C;
      }
    }
  }
  
  li {
    
    padding: 0.5rem 0.5rem;
    margin-top: 0.2rem;
  }
  </style>
  