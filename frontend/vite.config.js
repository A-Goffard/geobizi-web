import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  envPrefix: 'VITE_', // Asegúrate de que Vite use el prefijo correcto
});
