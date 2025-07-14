# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Comando para ejecutar la app en producción (ej. gunicorn)
# Para desarrollo, el comando se sobreescribe en docker-compose.dev.yml
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
