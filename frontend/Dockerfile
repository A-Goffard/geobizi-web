# filepath: c:\Users\geotx\Desktop\Aintzane\Programacion\geobizi-web\frontend\Dockerfile
# Etapa de build (para desarrollo y producción)
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
# NO ejecutes "RUN npm run build" aquí. Se hará solo para producción.

# Etapa de producción (nombrada "final")
FROM nginx:alpine AS final
COPY --from=build /app/nginx.conf /etc/nginx/nginx.conf
COPY --from=build /app/default.conf /etc/nginx/conf.d/default.conf
# Los archivos de la app se copiarán desde Dockerfile.prod
COPY --from=build /app/nginx.conf /etc/nginx/nginx.conf
COPY --from=build /app/default.conf /etc/nginx/conf.d/default.conf
# El CMD de Nginx se hereda de la imagen base, no es necesario re-declararlo
