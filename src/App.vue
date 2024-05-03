<template>
  <div>
    <Nav />
    <router-view></router-view>
  </div>
</template>
<script setup>
import Nav from './components/NavBar.vue';

</script>

<style>

* {
margin: 0;
padding: 0;
text-decoration: none;
list-style: none;
font-family: Avenir, Helvetica, Arial, sans-serif;
text-decoration: none;
box-sizing: border-box;
background-color: white;
}

h1,
h2,
h3 {
  color: #26B12C;
  margin: 1rem;
}
p {
  margin: 1rem;
}
</style>
