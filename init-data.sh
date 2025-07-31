#!/bin/bash
echo "Inicializando datos de ejemplo en Docker..."
docker-compose -f docker-compose.dev.yml exec backend python database/datos_ejemplo.py docker
echo "Datos creados. Reiniciando backend para aplicar cambios..."
docker-compose -f docker-compose.dev.yml restart backend
