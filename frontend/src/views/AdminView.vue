<template>
    <div class="contenedor-principal admin-contenedor">
        <!-- 1. LOGIN -->
        <div v-if="!autenticado" class="login-wrapper print-hide">
            <div class="card login-card">
                <div class="login-header">
                    <h2>🌿 Acceso Administración</h2>
                    <p class="login-subtexto">Panel interno de gestión de actividades y reservas</p>
                </div>

                <form @submit.prevent="iniciarSesion" class="login-form" autocomplete="off">
                    <div class="campo-grupo">
                        <label for="admin-pass">Contraseña:</label>
                        <input id="admin-pass" name="admin-pass" type="password" v-model="password"
                            placeholder="Introduce la contraseña" class="input-geobizi" autocomplete="current-password"
                            data-lpignore="true" required autofocus />
                    </div>

                    <div v-if="errorLogin" class="mensaje-error-box">
                        <span>⚠️ {{ errorLogin }}</span>
                    </div>

                    <div class="acciones-botones">
                        <button type="submit" class="btn-submit" :disabled="cargando">
                            {{ cargando ? 'Verificando...' : 'Entrar al Panel' }}
                        </button>
                    </div>
                </form>
            </div>
        </div>

        <!-- 2. PANEL INTERNO -->
        <div v-else class="panel-interno">
            <!-- CABECERA -->
            <header class="panel-topbar print-hide">
                <div>
                    <h1>Gestión de Actividades</h1>
                    <span class="badge general">Sesión activa</span>
                </div>
                <div class="topbar-acciones">
                    <button @click="cambiarPestana('actividades')"
                        :class="['btn-secundario', { 'tab-activa': pestanaActiva === 'actividades' }]">
                        📅 Actividades
                    </button>
                    <button @click="cerrarSesion" class="btn-alerta">
                        Cerrar Sesión
                    </button>
                </div>
            </header>

            <!-- PESTAÑA: ACTIVIDADES -->
            <section v-if="pestanaActiva === 'actividades'" class="seccion-panel print-hide">
                <div class="barra-herramientas">
                    <h2>Actividades programadas ({{ actividades.length }})</h2>
                    <div style="display: flex; gap: 0.6rem;">
                        <button @click="descargarCopiaJson" class="btn-secundario"
                            title="Descargar copia del archivo JSON">
                            📥 Descargar JSON
                        </button>
                        <button @click="abrirModalCrear" class="btn-guardar">
                            ➕ Nueva Actividad
                        </button>
                    </div>
                </div>

                <div v-if="cargando" class="estado-caja">
                    <p class="mensaje-estado">Cargando datos...</p>
                </div>

                <div v-else class="tabla-contenedor">
                    <table class="tabla-geobizi">
                        <thead>
                            <tr>
                                <th @click="ordenarPor('id')" class="th-ordenable">ID {{ getIconoOrden('id') }}</th>
                                <th @click="ordenarPor('fecha')" class="th-ordenable">Fecha y Hora {{
                                    getIconoOrden('fecha') }}</th>
                                <th @click="ordenarPor('titulo')" class="th-ordenable">Actividad {{
                                    getIconoOrden('titulo') }}</th>
                                <th @click="ordenarPor('ubicacion')" class="th-ordenable">Ubicación {{
                                    getIconoOrden('ubicacion') }}</th>
                                <th @click="ordenarPor('aforo')" class="th-ordenable">Aforo {{ getIconoOrden('aforo') }}
                                </th>
                                <th @click="ordenarPor('publicar')" class="th-ordenable">Estado {{
                                    getIconoOrden('publicar') }}</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="act in actividadesOrdenadas" :key="act.id">
                                <td><strong>#{{ act.id }}</strong></td>
                                <td>
                                    <div class="texto-fecha">{{ formatearFecha(act.fecha) }}</div>
                                    <div class="texto-hora">{{ act.hora }}</div>
                                </td>
                                <td>
                                    <strong>{{ act.titulo }}</strong>
                                    <div class="texto-precio">
                                        {{ act.precio ? act.precio + ' €' : 'Gratuito' }}
                                        <span v-if="act.proyecto" class="badge-proyecto">• {{ act.proyecto }}</span>
                                    </div>
                                </td>
                                <td>{{ act.ubicacion || '—' }}</td>
                                <td>
                                    <div class="barra-aforo-fondo">
                                        <div class="barra-aforo-progreso"
                                            :style="{ width: Math.min(100, ((act.plazas_ocupadas || 0) / act.plazas_totales) * 100) + '%' }">
                                        </div>
                                    </div>
                                    <span class="texto-aforo">
                                        <strong>{{ act.plazas_ocupadas || 0 }}</strong> / {{ act.plazas_totales }}
                                        plazas
                                        <span v-if="act.total_espera > 0" class="espera-contador">
                                            ({{ act.total_espera }} en espera)
                                        </span>
                                    </span>
                                </td>
                                <td>
                                    <span
                                        :class="['badge-estado', (act.publicar === 1 || act.publicar === true) ? 'estado-publicado' : 'estado-oculto']">
                                        {{ (act.publicar === 1 || act.publicar === true) ? 'Publicada' : 'Oculta' }}
                                    </span>
                                </td>
                                <td class="col-acciones">
                                    <button @click="verParticipantes(act.id)" class="btn-servicio"
                                        title="Ver lista de inscritos">
                                        👥 Asistentes
                                    </button>
                                    <button @click="abrirModalEditar(act)" class="btn-mini-accion"
                                        title="Editar actividad">
                                        ✏️
                                    </button>
                                    <button @click="duplicarActividad(act)" class="btn-mini-accion"
                                        title="Duplicar como nueva">
                                        📋
                                    </button>
                                    <button @click="abrirModalEliminar(act)" class="btn-mini-accion btn-mini-eliminar"
                                        title="Eliminar actividad">
                                        🗑️
                                    </button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>

            <!-- PESTAÑA: PARTICIPANTES -->
            <section v-if="pestanaActiva === 'participantes'" class="seccion-panel">
                <div class="barra-herramientas">
                    <h2>Actividades programadas ({{ actividades.length }})</h2>
                    <div style="display: flex; gap: 0.6rem;">
                        <button @click="descargarCopiaJson" class="btn-secundario"
                            title="Descargar copia del archivo JSON">
                            📥 Descargar JSON
                        </button>
                        <button @click="abrirModalCrear" class="btn-guardar">
                            ➕ Nueva Actividad
                        </button>
                    </div>
                </div>

                <!-- CABECERA EXCLUSIVA IMPRESIÓN -->
                <div class="print-solo print-cabecera-documento">
                    <div class="print-fila-superior">
                        <img src="/imagenes/GeobiziLogo.7ae1d6ce.png" alt="Geobizi" class="print-logo-oficial" />
                        <div class="print-datos-emision">
                            <h2>Control de Asistencia</h2>
                            <span class="print-sub-fecha">Fecha de emisión: {{ fechaActualFormateada }}</span>
                        </div>
                    </div>

                    <div class="print-caja-ficha">
                        <div class="print-item"><strong>Actividad:</strong> {{ detalleActividad.actividad?.titulo }}
                        </div>
                        <div class="print-item"><strong>Fecha y Horario:</strong> {{
                            formatearFecha(detalleActividad.actividad?.fecha) }} a las {{
                                detalleActividad.actividad?.hora }}</div>
                        <div class="print-item"><strong>Lugar de encuentro:</strong> {{
                            detalleActividad.actividad?.ubicacion || '—' }}</div>
                        <div class="print-item"><strong>Asistencia:</strong> {{ totalPersonasConfirmadas }} plazas
                            confirmadas de {{ detalleActividad.actividad?.plazas_totales }}</div>
                    </div>
                </div>

                <h3 class="print-hide">✅ Asistentes Confirmados ({{ detalleActividad.reservas?.length || 0 }} reservas)
                </h3>

                <div v-if="detalleActividad.reservas?.length === 0" class="caja-vacia print-hide">
                    No hay reservas registradas para esta actividad.
                </div>

                <div v-else class="tabla-contenedor print-tabla-box">
                    <table class="tabla-geobizi tabla-imprimible">
                        <thead>
                            <tr>
                                <th class="print-col-check print-solo">Asist.</th>
                                <th>Titular de la reserva</th>
                                <th>Teléfono</th>
                                <th>Plazas</th>
                                <th>Detalle de Asistentes</th>
                                <th>Fotos</th>
                                <th>Observaciones</th>
                                <th class="print-hide">Acción</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="res in detalleActividad.reservas" :key="res.id">
                                <td class="print-col-check print-solo">
                                    <div class="check-impresion">[ &nbsp; ]</div>
                                </td>
                                <td>
                                    <strong>{{ res.nombre_contacto || res.nombre }} {{ res.apellidos_contacto ||
                                        res.apellidos }}</strong>
                                </td>
                                <td>
                                    <a :href="'tel:' + (res.phone || res.telefono)">{{ res.phone || res.telefono }}</a>
                                </td>
                                <td><strong>{{ res.num_personas }}</strong></td>
                                <td>
                                    <ul class="lista-desglose">
                                        <li v-for="(p, idx) in res.participantes" :key="idx">
                                            {{ p.nombre }} {{ p.apellidos }} ({{ p.edad }} años)
                                        </li>
                                    </ul>
                                </td>
                                <td>
                                    <span :class="['tag-permiso', res.permiso_fotos ? 'tag-si' : 'tag-no']">
                                        {{ res.permiso_fotos ? 'Sí' : 'No' }}
                                    </span>
                                </td>
                                <td class="col-observaciones">{{ res.observaciones || '—' }}</td>
                                <td class="print-hide">
                                    <button @click="cancelarReservaAdmin(res.id)" class="btn-destructivo-sm"
                                        title="Anular plaza">
                                        Anular
                                    </button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- LISTA DE ESPERA -->
                <div v-if="detalleActividad.lista_espera?.length > 0" class="bloque-espera print-hide">
                    <h3 style="color: var(--darkamber); margin-top: 2rem;">
                        ⏳ Lista de Espera ({{ detalleActividad.lista_espera.length }} reservas en cola)
                    </h3>
                    <div class="tabla-contenedor">
                        <table class="tabla-geobizi">
                            <thead>
                                <tr>
                                    <th>Turno</th>
                                    <th>Contacto</th>
                                    <th>Plazas solicitadas</th>
                                    <th>Fecha de registro</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="(esp, idx) in detalleActividad.lista_espera" :key="esp.id">
                                    <td><strong>#{{ idx + 1 }}</strong></td>
                                    <td>
                                        <strong>{{ esp.nombre_contacto || esp.nombre }} {{ esp.apellidos_contacto ||
                                            esp.apellidos }}</strong>
                                        <div class="texto-hora">{{ esp.phone || esp.telefono }} | {{ esp.email }}</div>
                                    </td>
                                    <td><strong>{{ esp.num_personas }} plazas</strong></td>
                                    <td>{{ esp.fecha_registro || esp.fecha_creacion || '—' }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </section>

            <!-- 3. MODAL: CREAR / EDITAR / CLONAR -->
            <div v-if="modalActividadAbierto" class="modal-overlay print-hide"
                @click.self="modalActividadAbierto = false">
                <div class="modal-tarjeta modal-ancho">
                    <header class="modal-top">
                        <h3 class="modal-titulo-exito">
                            {{ modoEdicion ? 'Editar Actividad #' + formActividad.id : 'Nueva Actividad' }}
                        </h3>
                        <button @click="modalActividadAbierto = false" class="btn-cerrar">&times;</button>
                    </header>

                    <form @submit.prevent="guardarActividad" class="formulario-modal" autocomplete="off">
                        <div class="grid-campos-scroll">
                            <div class="campo-grupo col-completa">
                                <label>Título de la actividad *</label>
                                <input type="text" v-model="formActividad.titulo" class="input-geobizi" required />
                            </div>

                            <div class="campo-grupo">
                                <label>Fecha (YYYY-MM-DD) *</label>
                                <input type="date" v-model="formActividad.fecha" class="input-geobizi" required />
                            </div>

                            <div class="campo-grupo">
                                <label>Horario *</label>
                                <input type="text" v-model="formActividad.hora" placeholder="10:30 a 13:00"
                                    class="input-geobizi" required />
                            </div>

                            <div class="campo-grupo">
                                <label>Ubicación / Punto de encuentro *</label>
                                <input type="text" v-model="formActividad.ubicacion" class="input-geobizi" required />
                            </div>

                            <div class="campo-grupo">
                                <label>Aforo (Plazas Totales) *</label>
                                <input type="number" v-model.number="formActividad.plazas_totales" min="1"
                                    class="input-geobizi" required />
                            </div>

                            <div class="campo-grupo">
                                <label>Precio (€) [0 para gratuito]</label>
                                <input type="number" step="0.5" v-model.number="formActividad.precio"
                                    class="input-geobizi" />
                            </div>

                            <div class="campo-grupo">
                                <label>Proyecto asociado</label>
                                <input type="text" v-model="formActividad.proyecto" placeholder="zalla, flysch, general"
                                    class="input-geobizi" />
                            </div>

                            <div class="campo-grupo col-completa">
                                <label>Descripción corta</label>
                                <textarea v-model="formActividad.descripcion" rows="2" class="input-geobizi"></textarea>
                            </div>

                            <div class="campo-grupo col-completa">
                                <label>Detalles / Recomendaciones</label>
                                <textarea v-model="formActividad.detalles" rows="3" class="input-geobizi"></textarea>
                            </div>

                            <!-- IMAGEN 1: PORTADA -->
                            <div class="campo-grupo col-completa selector-imagen-bloque">
                                <div class="etiqueta-fila">
                                    <label><strong>Imagen 1 — Portada Principal:</strong></label>
                                    <button type="button" @click="copiarImagenAhover" class="btn-link-sm"
                                        v-if="formActividad.imagen1">
                                        ➡️ Usar también como imagen hover
                                    </button>
                                </div>
                                <div class="fila-subida">
                                    <input type="text" v-model="formActividad.imagen1" class="input-geobizi" />
                                    <input type="file" ref="fileInput1" @change="(e) => subirImagen(e, 'imagen1')"
                                        style="display: none;" accept="image/*" />
                                    <button type="button" @click="$refs.fileInput1.click()" class="btn-secundario">📁
                                        Subir foto</button>
                                    <button type="button" @click="abrirBiblioteca('imagen1')" class="btn-secundario">🖼️
                                        Biblioteca</button>
                                </div>
                                <div v-if="formActividad.imagen1" class="preview-linea">
                                    <img :src="formActividad.imagen1" alt="Portada" class="mini-preview"
                                        @error="marcarErrorImagen" />
                                    <span>Ruta activa: {{ formActividad.imagen1 }}</span>
                                </div>
                            </div>

                            <!-- IMAGEN 2: HOVER -->
                            <div class="campo-grupo col-completa selector-imagen-bloque">
                                <label><strong>Imagen 2 — Efecto Hover (Al pasar el ratón):</strong></label>
                                <div class="fila-subida">
                                    <input type="text" v-model="formActividad.imagen2" class="input-geobizi" />
                                    <input type="file" ref="fileInput2" @change="(e) => subirImagen(e, 'imagen2')"
                                        style="display: none;" accept="image/*" />
                                    <button type="button" @click="$refs.fileInput2.click()" class="btn-secundario">📁
                                        Subir foto</button>
                                    <button type="button" @click="abrirBiblioteca('imagen2')" class="btn-secundario">🖼️
                                        Biblioteca</button>
                                </div>
                                <div v-if="formActividad.imagen2" class="preview-linea">
                                    <img :src="formActividad.imagen2" alt="Hover" class="mini-preview"
                                        @error="marcarErrorImagen" />
                                    <span>Ruta activa: {{ formActividad.imagen2 }}</span>
                                </div>
                            </div>

                            <!-- BIBLIOTECA -->
                            <div v-if="mostrarGaleria" class="campo-grupo col-completa galeria-seccion">
                                <div class="galeria-header">
                                    <span>Seleccionar para <strong>{{ campoDestinoGaleria === 'imagen1' ? 'Imagen 1' :
                                        'Imagen 2' }}</strong>:</span>
                                    <button type="button" @click="mostrarGaleria = false"
                                        class="btn-cerrar-mini">&times;</button>
                                </div>
                                <div class="galeria-desplegable">
                                    <div v-for="img in imagenesDisponibles" :key="img.url" class="galeria-miniatura"
                                        @click="seleccionarDeBiblioteca(img.url)">
                                        <img :src="img.url" :alt="img.nombre" />
                                        <span>{{ img.nombre }}</span>
                                    </div>
                                </div>
                            </div>

                            <!-- CASILLAS SINCRONIZADAS -->
                            <div class="campo-grupo col-completa fila-checks">
                                <label class="check-etiqueta">
                                    <input type="checkbox" v-model="formActividad.publicar" /> Publicar actividad en la
                                    web
                                </label>
                                <label class="check-etiqueta">
                                    <input type="checkbox" v-model="formActividad.reservas" /> Habilitar formulario de
                                    reserva
                                </label>
                            </div>
                        </div>

                        <div class="modal-acciones-fijas">
                            <button type="button" @click="modalActividadAbierto = false"
                                class="btn-secundario">Cancelar</button>
                            <button type="submit" class="btn-guardar" :disabled="guardando">
                                {{ guardando ? 'Guardando...' : (modoEdicion ? 'Actualizar Actividad' : 'Guardar Actividad') }}
                            </button>
                        </div>
                    </form>
                </div>
            </div>

            <!-- 4. MODAL DE CONFIRMACIÓN PARA ELIMINAR ACTIVIDAD -->
            <div v-if="modalEliminarAbierto" class="modal-overlay print-hide"
                @click.self="modalEliminarAbierto = false">
                <div class="modal-tarjeta">
                    <div class="modal-icono">🗑️</div>
                    <h3 class="modal-titulo">¿Eliminar actividad definitivamente?</h3>

                    <div class="modal-alerta-box">
                        <p class="modal-alerta-texto">
                            <strong>Atención:</strong> Estás a punto de borrar la actividad <strong>#{{
                                actividadAEliminar?.id }} - {{ actividadAEliminar?.titulo }}</strong>.
                        </p>
                        <p class="modal-subtexto" style="margin: 0; color: var(--darkyellow);">
                            Esta acción es irreversible y eliminará también todas las reservas, plazas y fichas de
                            participantes asociadas a esta fecha.
                        </p>
                    </div>

                    <div class="modal-acciones">
                        <button type="button" @click="modalEliminarAbierto = false" class="btn-secundario"
                            :disabled="eliminando">
                            Cancelar
                        </button>
                        <button type="button" @click="confirmarEliminarActividad" class="btn-destructivo"
                            :disabled="eliminando">
                            {{ eliminando ? 'Borrando...' : 'Sí, eliminar actividad' }}
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useHead } from '@vueuse/head';

useHead({
    title: 'Gestión Geobizi — Panel de Control',
    meta: [{ name: 'robots', content: 'noindex, nofollow, noarchive' }]
});

const getAdminApiUrl = () => {
    const envUrl = process.env.VUE_APP_API_URL;
    if (!envUrl) return 'http://localhost:5000/api/admin';
    const limpia = envUrl.replace(/\/+$/, '');
    return limpia.endsWith('/api') ? `${limpia}/admin` : `${limpia}/api/admin`;
};

const ADMIN_API = getAdminApiUrl();

const autenticado = ref(false);
const password = ref('');
const errorLogin = ref('');
const cargando = ref(false);
const guardando = ref(false);
const eliminando = ref(false);

const pestanaActiva = ref('actividades');
const actividades = ref([]);
const detalleActividad = ref({});

// Control de eliminación
const modalEliminarAbierto = ref(false);
const actividadAEliminar = ref(null);

const columnaOrden = ref('fecha');
const direccionOrden = ref('desc');

function ordenarPor(columna) {
    if (columnaOrden.value === columna) {
        direccionOrden.value = direccionOrden.value === 'asc' ? 'desc' : 'asc';
    } else {
        columnaOrden.value = columna;
        direccionOrden.value = (columna === 'fecha' || columna === 'id') ? 'desc' : 'asc';
    }
}

function getIconoOrden(columna) {
    if (columnaOrden.value !== columna) return '↕';
    return direccionOrden.value === 'asc' ? '▲' : '▼';
}

const actividadesOrdenadas = computed(() => {
    return [...actividades.value].sort((a, b) => {
        let valA = a[columnaOrden.value];
        let valB = b[columnaOrden.value];

        if (columnaOrden.value === 'fecha') {
            valA = `${a.fecha || ''} ${a.hora || ''}`;
            valB = `${b.fecha || ''} ${b.hora || ''}`;
        } else if (columnaOrden.value === 'titulo' || columnaOrden.value === 'ubicacion') {
            valA = (valA || '').toString().toLowerCase();
            valB = (valB || '').toString().toLowerCase();
            const comp = valA.localeCompare(valB, 'es');
            return direccionOrden.value === 'asc' ? comp : -comp;
        } else if (columnaOrden.value === 'aforo') {
            valA = a.plazas_ocupadas || 0;
            valB = b.plazas_ocupadas || 0;
        }

        if (valA < valB) return direccionOrden.value === 'asc' ? -1 : 1;
        if (valA > valB) return direccionOrden.value === 'asc' ? 1 : -1;
        return 0;
    });
});

const totalPersonasConfirmadas = computed(() => {
    if (!detalleActividad.value.reservas) return 0;
    return detalleActividad.value.reservas.reduce((acc, r) => acc + (r.num_personas || 0), 0);
});

const fechaActualFormateada = computed(() => {
    const hoy = new Date();
    return hoy.toLocaleDateString('es-ES', { day: '2-digit', month: '2-digit', year: 'numeric' });
});

const modalActividadAbierto = ref(false);
const modoEdicion = ref(false);
const mostrarGaleria = ref(false);
const campoDestinoGaleria = ref('imagen1');
const imagenesDisponibles = ref([]);

const formActividad = ref({
    id: null,
    titulo: '',
    fecha: '',
    hora: '',
    ubicacion: '',
    color: '#0b8a4c',
    descripcion: '',
    detalles: '',
    oharrak: '',
    precio: 0,
    imagen1: '/imagenes/actividades/default.jpg',
    imagen2: '/imagenes/actividades/default.jpg',
    tipo: 'general',
    proyecto: 'general',
    publicar: true,
    stripeId: null,
    reservas: true,
    tipoReserva: 'web',
    linkReserva: null,
    estadoReserva: 'disponible',
    plazas_totales: 20
});

function getAuthHeaders() {
    const token = localStorage.getItem('geobizi_admin_token');
    return {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
    };
}

async function iniciarSesion() {
    cargando.value = true;
    errorLogin.value = '';
    try {
        const res = await fetch(`${ADMIN_API}/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ password: password.value })
        });

        const data = await res.json().catch(() => ({}));
        if (!res.ok) throw new Error(data.detail || 'Contraseña incorrecta');

        localStorage.setItem('geobizi_admin_token', data.token);
        autenticado.value = true;
        password.value = '';
        await cargarActividades();
    } catch (err) {
        errorLogin.value = err.message.includes('fetch')
            ? 'No se pudo conectar con el backend.'
            : err.message;
    } finally {
        cargando.value = false;
    }
}

function cerrarSesion() {
    localStorage.removeItem('geobizi_admin_token');
    autenticado.value = false;
}

async function cargarActividades() {
    cargando.value = true;
    try {
        const res = await fetch(`${ADMIN_API}/actividades`, { headers: getAuthHeaders() });
        if (res.status === 401) return cerrarSesion();
        actividades.value = await res.json();
    } catch (err) {
        alert('Error al sincronizar: ' + err.message);
    } finally {
        cargando.value = false;
    }
}

async function verParticipantes(actividadId) {
    cargando.value = true;
    try {
        const res = await fetch(`${ADMIN_API}/actividades/${actividadId}/participantes`, { headers: getAuthHeaders() });
        const data = await res.json().catch(() => ({}));
        if (!res.ok) throw new Error(data.detail || 'Error al obtener participantes.');
        detalleActividad.value = data;
        pestanaActiva.value = 'participantes';
    } catch (err) {
        alert(err.message);
    } finally {
        cargando.value = false;
    }
}

function abrirModalCrear() {
    modoEdicion.value = false;
    formActividad.value = {
        id: null,
        titulo: '',
        fecha: '',
        hora: '10:00 a 13:00',
        ubicacion: '',
        color: '#0b8a4c',
        descripcion: '',
        detalles: '',
        oharrak: '',
        precio: 0,
        imagen1: '/imagenes/actividades/default.jpg',
        imagen2: '/imagenes/actividades/default.jpg',
        tipo: 'general',
        proyecto: 'general',
        publicar: true,
        stripeId: null,
        reservas: true,
        tipoReserva: 'web',
        linkReserva: null,
        estadoReserva: 'disponible',
        plazas_totales: 20
    };
    mostrarGaleria.value = false;
    modalActividadAbierto.value = true;
}

// SINCRONIZACIÓN BOOLEANA EXACTA PARA EL MODAL DE EDICIÓN
function abrirModalEditar(act) {
    modoEdicion.value = true;
    formActividad.value = {
        ...act,
        publicar: act.publicar === 1 || act.publicar === true || act.publicar === '1',
        reservas: act.reservas === 1 || act.reservas === true || act.reservas === '1'
    };
    mostrarGaleria.value = false;
    modalActividadAbierto.value = true;
}

function duplicarActividad(act) {
    modoEdicion.value = false;
    const copia = { ...act };
    delete copia.id;
    delete copia.total_reservas;
    delete copia.total_espera;
    delete copia.plazas_confirmadas;
    copia.plazas_ocupadas = 0;
    copia.fecha = '';

    formActividad.value = {
        ...copia,
        publicar: copia.publicar === 1 || copia.publicar === true || copia.publicar === '1',
        reservas: copia.reservas === 1 || copia.reservas === true || copia.reservas === '1'
    };
    mostrarGaleria.value = false;
    modalActividadAbierto.value = true;
}

function copiarImagenAhover() {
    formActividad.value.imagen2 = formActividad.value.imagen1;
}

async function guardarActividad() {
    guardando.value = true;
    try {
        const esEdit = modoEdicion.value;
        const url = esEdit ? `${ADMIN_API}/actividades/${formActividad.value.id}` : `${ADMIN_API}/actividades`;
        const method = esEdit ? 'PUT' : 'POST';

        const payload = { ...formActividad.value };
        if (!esEdit) delete payload.id;

        if (payload.imagen1 && !payload.imagen1.startsWith('/') && !payload.imagen1.startsWith('http')) {
            payload.imagen1 = '/' + payload.imagen1;
        }
        if (payload.imagen2 && !payload.imagen2.startsWith('/') && !payload.imagen2.startsWith('http')) {
            payload.imagen2 = '/' + payload.imagen2;
        }

        const res = await fetch(url, {
            method,
            headers: getAuthHeaders(),
            body: JSON.stringify(payload)
        });

        const data = await res.json().catch(() => ({}));
        if (!res.ok) throw new Error(data.detail || 'Fallo al procesar la solicitud.');

        modalActividadAbierto.value = false;
        await cargarActividades();
    } catch (err) {
        alert(err.message);
    } finally {
        guardando.value = false;
    }
}

// GESTIÓN DE BORRADO DE ACTIVIDAD
function abrirModalEliminar(act) {
    actividadAEliminar.value = act;
    modalEliminarAbierto.value = true;
}

async function confirmarEliminarActividad() {
    if (!actividadAEliminar.value) return;
    eliminando.value = true;
    try {
        const res = await fetch(`${ADMIN_API}/actividades/${actividadAEliminar.value.id}`, {
            method: 'DELETE',
            headers: getAuthHeaders()
        });
        const data = await res.json().catch(() => ({}));
        if (!res.ok) throw new Error(data.detail || 'No se pudo eliminar la actividad.');

        modalEliminarAbierto.value = false;
        actividadAEliminar.value = null;
        await cargarActividades();
    } catch (err) {
        alert(err.message);
    } finally {
        eliminando.value = false;
    }
}

async function cancelarReservaAdmin(reservaId) {
    if (!confirm('¿Seguro que deseas anular esta reserva? Se reasignará la plaza al siguiente turno de espera.')) return;

    try {
        const res = await fetch(`${ADMIN_API}/reservas/${reservaId}`, {
            method: 'DELETE',
            headers: getAuthHeaders()
        });
        if (!res.ok) throw new Error('Error al anular la reserva.');
        await verParticipantes(detalleActividad.value.actividad.id);
    } catch (err) {
        alert(err.message);
    }
}

async function subirImagen(event, campoDestino) {
    const file = event.target.files[0];
    if (!file) return;

    const nombreSugerido = file.name.substring(0, file.name.lastIndexOf('.')) || file.name;
    const nombrePersonalizado = prompt('Nombre para guardar la foto (sin extensión):', nombreSugerido);

    if (nombrePersonalizado === null) {
        event.target.value = '';
        return;
    }

    const formData = new FormData();
    formData.append('archivo', file);
    if (nombrePersonalizado.trim()) {
        formData.append('nombre_personalizado', nombrePersonalizado.trim());
    }

    try {
        const token = localStorage.getItem('geobizi_admin_token');
        const res = await fetch(`${ADMIN_API}/upload-imagen`, {
            method: 'POST',
            headers: { 'Authorization': `Bearer ${token}` },
            body: formData
        });
        const data = await res.json();
        if (!res.ok) throw new Error(data.detail || 'Error al subir la imagen.');

        formActividad.value[campoDestino] = data.url;
        alert(`Imagen guardada como: ${data.nombre}`);
    } catch (err) {
        alert(err.message);
    } finally {
        event.target.value = '';
    }
}

async function abrirBiblioteca(campo) {
    campoDestinoGaleria.value = campo;
    try {
        const res = await fetch(`${ADMIN_API}/imagenes`, { headers: getAuthHeaders() });
        imagenesDisponibles.value = await res.json();
        mostrarGaleria.value = true;
    } catch (err) {
        alert('Error al abrir la biblioteca: ' + err.message);
    }
}

async function descargarCopiaJson() {
    try {
        const token = localStorage.getItem('geobizi_admin_token');
        const res = await fetch(`${ADMIN_API}/descargar-json`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        if (!res.ok) throw new Error('No se pudo generar la copia del archivo');

        const blob = await res.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `actividades_${new Date().toISOString().slice(0, 10)}.json`;
        document.body.appendChild(a);
        a.click();
        a.remove();
        window.URL.revokeObjectURL(url);
    } catch (err) {
        alert('Error al descargar: ' + err.message);
    }
}

function seleccionarDeBiblioteca(url) {
    formActividad.value[campoDestinoGaleria.value] = url;
    mostrarGaleria.value = false;
}

function marcarErrorImagen(event) {
    event.target.src = '/imagenes/actividades/default.jpg';
}

function formatearFecha(f) {
    if (!f) return '';
    const [y, m, d] = f.split('-');
    return `${d}/${m}/${y}`;
}

function cambiarPestana(p) {
    pestanaActiva.value = p;
}

function imprimirLista() {
    window.print();
}

onMounted(() => {
    const token = localStorage.getItem('geobizi_admin_token');
    if (token) {
        autenticado.value = true;
        cargarActividades();
    }
});
</script>

<style scoped>
.admin-contenedor {
    min-height: 85vh;
    padding-left: 1.5rem;
    padding-right: 1.5rem;
}

.login-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 3rem 1rem;
}

.login-card {
    width: 100%;
    max-width: 440px;
    background-color: var(--megashoftgreen);
    border: 1px solid var(--shoftgreen);
    border-radius: 0.5rem;
    padding: 2.5rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.login-header {
    text-align: center;
    margin-bottom: 1.8rem;
}

.login-header h2 {
    color: var(--darkgreen);
    margin: 0 0 0.5rem 0;
    font-size: 1.5rem;
}

.login-subtexto {
    color: var(--grey);
    font-size: 0.9rem;
    margin: 0;
}

.campo-grupo {
    display: flex;
    flex-direction: column;
    gap: 0.3rem;
    margin-bottom: 0.9rem;
}

.campo-grupo label {
    font-weight: bold;
    font-size: 0.85rem;
    color: var(--darkgrey);
}

.etiqueta-fila {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.btn-link-sm {
    background: none;
    border: none;
    color: var(--green);
    font-size: 0.8rem;
    font-weight: bold;
    cursor: pointer;
    text-decoration: underline;
}

.btn-link-sm:hover {
    color: var(--darkgreen);
}

.input-geobizi {
    padding: 0.65rem 0.85rem;
    border: 1px solid var(--lightgrey);
    border-radius: 4px;
    font-family: inherit;
    font-size: 0.9rem;
    outline: none;
    background-color: var(--white);
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.input-geobizi:focus {
    border-color: var(--green);
    box-shadow: 0 0 0 3px rgba(38, 177, 44, 0.15);
}

.mensaje-error-box {
    background-color: var(--supershoftbrownred);
    border-left: 4px solid var(--brownred);
    color: var(--brownred);
    padding: 0.8rem 1rem;
    border-radius: 4px;
    font-size: 0.9rem;
    font-weight: 500;
    margin-bottom: 1.2rem;
}

.panel-topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid var(--shoftgreen);
    padding-bottom: 1.2rem;
    margin-bottom: 2rem;
}

.panel-topbar h1 {
    margin: 0 0 0.4rem 0;
    font-size: 1.8rem;
}

.topbar-acciones {
    display: flex;
    gap: 0.8rem;
    align-items: center;
}

.tab-activa {
    background-color: var(--darkgreen) !important;
    color: var(--white) !important;
}

.barra-herramientas {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.2rem;
}

.barra-herramientas h2 {
    margin: 0;
}

.tabla-contenedor {
    background-color: var(--white);
    border: 1px solid var(--shoftgreen);
    border-radius: 0.5rem;
    overflow-x: auto;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    margin-bottom: 2rem;
}

.tabla-geobizi {
    width: 100%;
    border-collapse: collapse;
    text-align: left;
    font-size: 0.9rem;
}

.tabla-geobizi th {
    background-color: var(--megashoftgreen);
    color: var(--darkgreen);
    padding: 0.9rem 1rem;
    font-weight: bold;
    border-bottom: 1px solid var(--shoftgreen);
}

.th-ordenable {
    cursor: pointer;
    user-select: none;
}

.th-ordenable:hover {
    background-color: var(--supershoftgreen);
}

.tabla-geobizi td {
    padding: 0.85rem 1rem;
    border-bottom: 1px solid #edf2ed;
    vertical-align: middle;
}

.tabla-geobizi tr:hover {
    background-color: #fbfdfb;
}

.texto-fecha {
    font-weight: bold;
    color: var(--darkgrey);
}

.texto-hora {
    font-size: 0.8rem;
    color: var(--grey);
    margin-top: 2px;
}

.texto-precio {
    font-size: 0.85rem;
    color: var(--green);
    font-weight: bold;
}

.badge-proyecto {
    color: var(--grey);
    font-weight: normal;
    margin-left: 4px;
}

.barra-aforo-fondo {
    width: 100px;
    height: 8px;
    background-color: var(--lightgrey);
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 4px;
}

.barra-aforo-progreso {
    height: 100%;
    background-color: var(--green);
}

.texto-aforo {
    font-size: 0.85rem;
    color: var(--darkgrey);
}

.espera-contador {
    color: var(--amber);
    font-weight: bold;
    font-size: 0.8rem;
    margin-left: 3px;
}

.badge-estado {
    padding: 3px 8px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: bold;
}

.estado-publicado {
    background-color: var(--supershoftgreen);
    color: var(--darkgreen);
}

.estado-oculto {
    background-color: var(--lightgrey);
    color: var(--grey);
}

.col-acciones {
    display: flex;
    gap: 0.4rem;
    align-items: center;
}

.btn-mini-accion {
    border: 1px solid var(--lightgrey);
    background: var(--white);
    padding: 0.4rem 0.55rem;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.btn-mini-accion:hover {
    border-color: var(--green);
    background-color: var(--megashoftgreen);
}

.btn-mini-eliminar {
    border-color: var(--lightbrownred);
    background-color: var(--supershoftbrownred);
}

.btn-mini-eliminar:hover {
    background-color: var(--brownred);
    color: var(--white);
}

.btn-destructivo-sm {
    background-color: var(--brownred);
    color: var(--white);
    border: none;
    padding: 0.35rem 0.75rem;
    border-radius: 4px;
    font-size: 0.8rem;
    font-weight: bold;
    cursor: pointer;
}

.btn-destructivo-sm:hover {
    opacity: 0.9;
}

.lista-desglose {
    margin: 0;
    padding-left: 1.2rem;
    list-style: disc;
    font-size: 0.85rem;
}

.lista-desglose li {
    margin: 2px 0;
    color: var(--darkgrey);
}

.tag-permiso {
    display: inline-block;
    padding: 2px 7px;
    border-radius: 4px;
    font-weight: bold;
    font-size: 0.75rem;
}

.tag-si {
    background-color: var(--supershoftgreen);
    color: var(--darkgreen);
}

.tag-no {
    background-color: var(--lightgrey);
    color: var(--grey);
}

.caja-vacia {
    background-color: var(--white);
    border: 1px dashed var(--lightgrey);
    border-radius: 0.5rem;
    padding: 2.5rem;
    text-align: center;
    color: var(--grey);
}

/* MODALES */
.modal-overlay {
    position: fixed;
    inset: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.6);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 2000;
    padding: 1.5rem;
}

.modal-tarjeta.modal-ancho {
    max-width: 760px;
    width: 100%;
    max-height: 88vh;
    display: flex;
    flex-direction: column;
    padding: 1.5rem 2rem;
    text-align: left;
    background-color: var(--white);
    border-radius: 0.5rem;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
    overflow: hidden;
}

.modal-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--shoftgreen);
    padding-bottom: 0.8rem;
    margin-bottom: 1rem;
    flex-shrink: 0;
}

.btn-cerrar {
    background: none;
    border: none;
    font-size: 1.8rem;
    cursor: pointer;
    color: var(--grey);
    line-height: 1;
}

.formulario-modal {
    display: flex;
    flex-direction: column;
    flex: 1;
    overflow: hidden;
    min-height: 0;
}

.grid-campos-scroll {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.7rem 1rem;
    overflow-y: auto;
    padding-right: 0.6rem;
    margin-bottom: 1rem;
    flex: 1;
}

.col-completa {
    grid-column: span 2;
}

.fila-subida {
    display: flex;
    gap: 0.6rem;
    align-items: center;
}

.preview-linea {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin-top: 0.4rem;
    font-size: 0.8rem;
    color: var(--grey);
}

.mini-preview {
    width: 48px;
    height: 48px;
    object-fit: cover;
    border-radius: 4px;
    border: 1px solid var(--shoftgreen);
}

.galeria-seccion {
    background-color: #f7faf7;
    border: 1px solid var(--shoftgreen);
    border-radius: 6px;
    padding: 0.8rem;
    margin-top: 0.5rem;
}

.galeria-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.85rem;
    color: var(--darkgreen);
    margin-bottom: 0.6rem;
}

.btn-cerrar-mini {
    background: none;
    border: none;
    font-size: 1.2rem;
    cursor: pointer;
    color: var(--grey);
}

.galeria-desplegable {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(95px, 1fr));
    gap: 0.6rem;
    max-height: 150px;
    overflow-y: auto;
    padding: 0.2rem;
}

.galeria-miniatura {
    cursor: pointer;
    border: 1px solid var(--lightgrey);
    border-radius: 4px;
    padding: 3px;
    text-align: center;
    background-color: var(--white);
    transition: border-color 0.2s ease;
}

.galeria-miniatura:hover {
    border-color: var(--green);
}

.galeria-miniatura img {
    width: 100%;
    height: 50px;
    object-fit: cover;
    border-radius: 2px;
}

.galeria-miniatura span {
    font-size: 0.65rem;
    color: var(--darkgrey);
    display: block;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin-top: 2px;
}

.fila-checks {
    display: flex;
    gap: 1.5rem;
    margin-top: 0.4rem;
}

.check-etiqueta {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.9rem;
    cursor: pointer;
}

.modal-acciones-fijas {
    display: flex;
    gap: 1rem;
    justify-content: flex-end;
    border-top: 1px solid var(--shoftgreen);
    padding-top: 1rem;
    flex-shrink: 0;
    background-color: var(--white);
}

.print-solo {
    display: none;
}

@media (max-width: 768px) {
    .panel-topbar {
        flex-direction: column;
        align-items: flex-start;
        gap: 1rem;
    }

    .grid-campos-scroll {
        grid-template-columns: 1fr;
    }

    .col-completa {
        grid-column: span 1;
    }

    .fila-checks {
        flex-direction: column;
        gap: 0.6rem;
    }
}
</style>

<!-- REGLAS GLOBALES DE IMPRESIÓN (OCULTA APP.VUE Y BLINDA FORMATO) -->
<style>
@media print {
    @page {
        size: A4 portrait;
        margin: 1.2cm;
    }

    header,
    nav,
    footer,
    #app>header,
    #app>nav,
    #app>footer,
    .contenedor-cabecero,
    .cookie-banner,
    .aviso-cookies,
    div[class*="cookie"],
    div[id*="cookie"],
    .print-hide {
        display: none !important;
    }

    body,
    html,
    #app,
    main,
    .contenedor-principal,
    .admin-contenedor {
        background: #ffffff !important;
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
        min-height: auto !important;
        font-size: 10pt !important;
        color: #000000 !important;
    }

    .print-solo {
        display: block !important;
    }

    .print-cabecera-documento {
        display: block !important;
        border-bottom: 2px solid #000000 !important;
        padding-bottom: 10px !important;
        margin-bottom: 14px !important;
    }

    .print-fila-superior {
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
    }

    .print-logo-oficial {
        max-height: 48px !important;
        width: auto !important;
        object-fit: contain !important;
    }

    .print-datos-emision {
        text-align: right !important;
    }

    .print-datos-emision h2 {
        font-size: 14pt !important;
        margin: 0 !important;
        color: #000000 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }

    .print-sub-fecha {
        font-size: 9pt !important;
        color: #444444 !important;
    }

    .print-caja-ficha {
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        gap: 4px 14px !important;
        margin-top: 10px !important;
        font-size: 9.5pt !important;
        background-color: #fafafa !important;
        border: 1px solid #dddddd !important;
        padding: 8px 10px !important;
        border-radius: 4px !important;
    }

    .print-item strong {
        color: #000000 !important;
    }

    .tabla-contenedor.print-tabla-box {
        border: 1px solid #000000 !important;
        box-shadow: none !important;
        margin: 0 !important;
        overflow: visible !important;
    }

    .tabla-imprimible {
        width: 100% !important;
        border-collapse: collapse !important;
        font-size: 9pt !important;
    }

    .tabla-imprimible th {
        background-color: #f2f2f2 !important;
        color: #000000 !important;
        border: 1px solid #000000 !important;
        padding: 6px 8px !important;
        font-weight: bold !important;
        text-align: left !important;
    }

    .tabla-imprimible td {
        border: 1px solid #cccccc !important;
        padding: 6px 8px !important;
        color: #000000 !important;
        vertical-align: middle !important;
    }

    .print-col-check {
        display: table-cell !important;
        width: 40px !important;
        text-align: center !important;
    }

    .check-impresion {
        font-family: monospace !important;
        font-size: 11pt !important;
        font-weight: bold !important;
    }

    .col-observaciones {
        max-width: 170px !important;
        word-break: break-word !important;
    }

    .lista-desglose {
        padding-left: 12px !important;
        margin: 0 !important;
    }

    .lista-desglose li {
        margin: 0 !important;
        font-size: 8.5pt !important;
    }

    .tag-permiso {
        border: 1px solid #000000 !important;
        background: none !important;
        color: #000000 !important;
        padding: 1px 4px !important;
        font-size: 8pt !important;
    }

    tr {
        page-break-inside: avoid !important;
    }
}
</style>