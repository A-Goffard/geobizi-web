# filepath: c:\Users\geotx\Desktop\Aintzane\Programacion\geobizi-web\frontend\Dockerfile
# Etapa de build
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Etapa de producción
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
# Elimina o comenta la siguiente línea si quieres probar con el nginx.conf por defecto
# COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
