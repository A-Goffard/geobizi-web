Ejemplo de fetch (JavaScript) para panel local. Reemplaza API_KEY por tu clave local (no la subas a git).

```javascript
// Configuración del panel local
const API_BASE = "http://localhost:5000";
const API_KEY = "valor_de_tu_ADMIN_API_KEY";

// Listar actividades (admin)
async function listarActividadesAdmin() {
  const res = await fetch(`${API_BASE}/api/admin/actividades`, {
    headers: { "X-API-KEY": API_KEY }
  });
  if (!res.ok) throw new Error("Error: " + res.status);
  return await res.json();
}

// Crear actividad (admin)
async function crearActividad(payload) {
  const res = await fetch(`${API_BASE}/api/admin/actividades`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-API-KEY": API_KEY
    },
    body: JSON.stringify(payload)
  });
  return res;
}
```
