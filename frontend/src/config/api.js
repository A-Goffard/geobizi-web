/* eslint-disable */
// URL base de la API con fallback seguro a local
export const API_BASE_URL = process.env.VUE_APP_API_URL || 'http://localhost:5000/api';

// Endpoints centralizados
export const ENDPOINTS = {
  ACTIVIDADES: `${API_BASE_URL}/actividades`,
  RESERVAS: `${API_BASE_URL}/reservas`,
  LISTA_ESPERA: `${API_BASE_URL}/lista-espera`,
  TOKEN: (token) => `${API_BASE_URL}/token/${token}`,
  ACEPTAR_ESPERA: (token) => `${API_BASE_URL}/token/${token}/aceptar-espera`
};