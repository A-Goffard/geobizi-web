# Etapa 1: build de la app Vue
FROM node:18-alpine as build
WORKDIR /app
COPY . .
RUN npm install && npm run build

# Etapa 2: Nginx para servir los archivos
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf