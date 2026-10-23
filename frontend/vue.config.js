const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    port: 8080,
    proxy: {
      '^/api': {
        target: 'http://backend:5000',
        changeOrigin: true
      },
      '^/uploads': {
        target: 'http://backend:5000',
        changeOrigin: true
      }
    }
  }
})