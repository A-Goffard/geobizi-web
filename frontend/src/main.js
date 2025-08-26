import { createApp } from 'vue';
import { createHead } from '@vueuse/head'; // 1. Importar
import App from './App.vue';
import router from './router';

const app = createApp(App);
const head = createHead(); // 2. Crear una instancia

app.use(router);
app.use(head); // 3. Usar la instancia en la app

app.mount('#app');
