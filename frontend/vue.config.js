const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    // Configuración del proxy para el servidor de desarrollo de Vue
    proxy: {
      // Solo las peticiones que empiecen con /api serán redirigidas
      '^/api': {
        // ...será redirigida al contenedor del backend
        target: 'http://backend:5000',
        changeOrigin: true,
        logLevel: 'debug', // Muestra logs detallados del proxy en la terminal
        // Reescribimos la ruta para quitar /api antes de enviarla al backend
      },
    }
  }
})
