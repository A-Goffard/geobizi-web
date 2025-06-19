const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'frontend', 'src', 'assets', 'json', 'actividades.json');

const actividades = JSON.parse(fs.readFileSync(filePath, 'utf8'));

actividades.sort((a, b) => {
  // Ordena por fecha y hora
  const fechaA = new Date(`${a.fecha}T${a.hora || '00:00'}`);
  const fechaB = new Date(`${b.fecha}T${b.hora || '00:00'}`);
  return fechaA - fechaB;
});

// Reasigna ids consecutivos
actividades.forEach((actividad, idx) => {
  actividad.id = idx + 1;
});

fs.writeFileSync(filePath, JSON.stringify(actividades, null, 2), 'utf8');

console.log('Actividades ordenadas y ids corregidos.');
