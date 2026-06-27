<template>
    <div class="contenedor-principal">
        <h1>Nummulites: Las "monedas de piedra" del Flysch de Bizkaia</h1>

        <p>Si has paseado por los acantilados de Getxo, concretamente en la playa de Gorrondatxe (Azkorri), es muy
            probable que hayas caminado junto a miles de "monedas de piedra" sin darte cuenta. Estos pequeños discos
            incrustados en la roca son <strong>nummulites</strong>, unos de los fósiles más fascinantes y abundantes que
            podemos encontrar en el <a href="/detalle-flysch" title="Proyecto Flysch de Bizkaia">Flysch de Bizkaia</a>.
        </p>

        <h2>¿Qué es exactamente un Nummulites? El caparazón de una ameba gigante</h2>
        <p>A simple vista, por su forma lenticular y su caparazón calcáreo, muchas personas los confunden con pequeños
            caracoles o bivalvos marinos. Sin embargo, la realidad biológica es mucho más sorprendente: los nummulites
            eran <strong>foraminíferos bentónicos</strong>, es decir, organismos unicelulares (estaban formados por una
            sola célula).</p>

        <p>Lo asombroso de estos gigantes unicelulares es que segregaban carbonato cálcico para construir una compleja
            concha dividida internamente en decenas de cámaras. A medida que la célula crecía, iba edificando nuevas
            celdas formando una espiral perfecta que podía alcanzar varios centímetros de diámetro. ¡Una auténtica
            proeza arquitectónica para un organismo microscópico!</p>

        <h2>Testigos geológicos de un paraíso tropical</h2>
        <p>La presencia masiva de estos organismos en nuestras rocas es una de las mayores evidencias paleoclimáticas de
            la región. Los nummulites vivieron durante la época del <strong>Eoceno</strong> (hace aproximadamente entre
            50 y 40 millones de años), prosperando en ecosistemas de aguas cálidas, limpias y poco profundas.</p>

        <p>El hecho de que hoy encontremos bancos enteros de estos fósiles levantados en las capas verticales del flysch
            nos demuestra que, millones de años antes de la formación de los actuales acantilados, nuestra costa era un
            mar de clima tropical con condiciones similares a las del Caribe o el Indo-Pacífico actual.</p>

        <h2>El origen de su nombre y su vínculo con las pirámides</h2>
        <p>El término científico proviene del latín <em>"nummulus"</em>, que significa "moneda pequeña". Esta peculiar
            forma de lenteja o moneda ha generado diversas leyendas a lo largo de la historia de la humanidad.</p>

        <p>Un dato histórico fascinante es que las pirámides de Guiza en Egipto están construidas con bloques de caliza
            eocena repletos de restos de nummulites. El geógrafo griego Estrabón relató la antigua leyenda local que
            afirmaba que estas pequeñas incrustaciones circulares en las piedras de las pirámides eran, en realidad,
            lentejas petrificadas que se les habían caído a los esclavos durante su construcción.</p>

        <!-- CAJA DE RECURSOS (Llamada a la acción / Microscopio) -->
        <div class="caja-recurso">
            <h3>El Flysch al Microscopio</h3>
            <p>
                La geología hay que verla de cerca. En nuestras rutas guiadas por Getxo, nos equipamos con
                <strong>microscopios digitales portátiles</strong> para buscar, identificar y observar en directo la
                estructura interna de estos foraminíferos. Aprende a leer la historia de la Tierra en un entorno abierto
                y accesible.
            </p>
            <div class="botones-recurso">
                <a href="/calendario" class="proximas-actividades">Consultar fechas disponibles</a>
                <a href="/blog/flysch-bizkaia" class="btn-ver-mas">Leer más sobre el Flysch</a>
            </div>
        </div>

        <!-- REDES SOCIALES -->
        <p class="social-media"><b>¡Síguenos en redes sociales para descubrir más curiosidades geológicas y biológicas
                de nuestro entorno!</b></p>
        <div class="redes-sociales">
            <a href="https://www.instagram.com/geotxiki/" target="_blank" rel="noopener noreferrer"
                title="Geobizi en Instagram">
                <img src="/imagenes/iconos/instagram.png" alt="Geobizi en Instagram" class="social-icon"
                    loading="lazy" />
            </a>
            <a href="https://www.facebook.com/geobizirik/" target="_blank" rel="noopener noreferrer"
                title="Geobizi en Facebook">
                <img src="/imagenes/iconos/facebook.png" alt="Geobizi en Facebook" class="social-icon" loading="lazy" />
            </a>
            <a href="https://www.tiktok.com/@geobizi" target="_blank" rel="noopener noreferrer"
                title="Geobizi en TikTok">
                <img src="/imagenes/iconos/tiktok.png" alt="Geobizi en TikTok" class="social-icon" loading="lazy" />
            </a>
        </div>

        <!-- GALERÍA DE IMÁGENES -->
        <div class="imagen-trio">
            <div>
                <img class="img" src="/imagenes/blog/detalle/nummulites2.avif"
                    alt="Acumulación de fósiles de nummulites en la roca sedimentaria del flysch"
                    title="Fósiles de Nummulites en la roca" loading="lazy" />
            </div>
            <div>
                <img class="img" src="/imagenes/blog/detalle/nummulitescamaras.avif"
                    alt="Detalle microscópico de la espiral interna y las cámaras de un foraminífero bentónico"
                    title="Estructura interna del Nummulites" loading="lazy" />
            </div>
            <div>
                <img class="img" src="/imagenes/blog/detalle/nummulitescamaras2.avif"
                    alt="Participantes observando rocas en la playa de Azkorri con un microscopio digital"
                    title="Actividad: El Flysch al microscopio" loading="lazy" />
            </div>
        </div>
    </div>
</template>

<script setup>
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/blog/nummulites-flysch'
const ogImage = 'https://www.geobizi.com/imagenes/blog/detalle/nummulites1.avif'

useHead({
    title: 'Nummulites: Fósiles y geología en el Flysch de Bizkaia | Geobizi',
    meta: [
        { name: 'description', content: 'Descubre qué son los Nummulites, los foraminíferos gigantes que demuestran que la costa de Bizkaia fue un mar tropical durante el Eoceno.' },
        { name: 'robots', content: 'index, follow' },
        { name: 'author', content: 'Geobizi' },
        { name: 'theme-color', content: '#0b8a4c' },
        { name: 'language', content: 'es' },
        { property: 'og:title', content: 'Nummulites: Las monedas de piedra del Flysch de Bizkaia' },
        { property: 'og:description', content: 'Geología de Getxo: aprende sobre los fósiles unicelulares del Eoceno en nuestras rutas con microscopio.' },
        { property: 'og:type', content: 'article' },
        { property: 'og:url', content: pageUrl },
        { property: 'og:image', content: ogImage },
        { name: 'twitter:card', content: 'summary_large_image' }
    ],
    link: [
        { rel: 'canonical', href: pageUrl },
        { rel: 'image_src', href: ogImage }
    ],
    script: [
        {
            type: 'application/ld+json',
            children: JSON.stringify({
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": "Nummulites: Las monedas de piedra del Flysch de Bizkaia",
                "description": "Análisis geológico de los fósiles de foraminíferos en Getxo y su importancia paleoclimática.",
                "image": ogImage,
                "author": {
                    "@type": "Organization",
                    "name": "Geobizi",
                    "url": "https://www.geobizi.com"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "Geobizi",
                    "logo": {
                        "@type": "ImageObject",
                        "url": "https://www.geobizi.com/imagenes/GeobiziLogo.7ae1d6ce.png"
                    }
                },
                "datePublished": "2024-05-15T08:00:00+01:00",
                "dateModified": "2026-04-14T10:00:00+02:00",
                "mainEntityOfPage": {
                    "@type": "WebPage",
                    "@id": pageUrl
                }
            })
        }
    ]
})
</script>

<style scoped>
/* CAJA DE RECURSOS */
.caja-recurso {
    background-color: var(--megashoftgreen);
    border-left: 4px solid var(--shoftgreen);
    padding: 1.5rem;
    margin: 2.5rem 0;
    border-radius: 0 0.5rem 0.5rem 0;
}

.caja-recurso h3 {
    margin-top: 0;
    color: var(--lightgreen);
    font-size: 1.2rem;
}

.caja-recurso p {
    margin-bottom: 1.5rem;
    color: var(--darkgrey);
}

.botones-recurso {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}

.proximas-actividades {
    background-color: var(--supershoftgreen);
    color: var(--lightgreen);
    padding: 0.6rem 1.2rem;
    text-decoration: none;
    font-weight: bold;
    border-radius: 4px;
    transition: background-color 0.3s;
}

.proximas-actividades:hover {
    background-color: var(--shoftgreen);
    color: var(--white);
}

.btn-ver-mas {
    background-color: transparent;
    color: var(--lightgreen);
    padding: 0.6rem 1.2rem;
    text-decoration: none;
    font-weight: bold;
    border: 1px solid var(--shoftgreen);
    border-radius: 4px;
    transition: all 0.3s;
}

.btn-ver-mas:hover {
    background-color: var(--shoftgreen);
    color: white;
}

/* REDES SOCIALES */
.social-media {
    margin-top: 2rem;
    color: var(--darkgrey);
}

.redes-sociales {
    margin-left: 1rem;
    display: flex;
    align-items: center;
}

.social-icon {
    width: 2.5rem;
    margin-right: 1rem;
    margin-bottom: 1.5rem;
    transition: transform 0.3s;
}

.social-icon:hover {
    transform: scale(1.1);
}
</style>