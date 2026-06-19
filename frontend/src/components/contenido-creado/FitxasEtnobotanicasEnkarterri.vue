<template>
  <div class="contenedor-principal general-container">
    <h1>Guía Digital: Fichas Etnobotánicas</h1>
    <p>Consulta nuestro catálogo científico de especies identificadas en las rutas de biodiversidad de Geobizi. Una herramienta digital optimizada para su uso en dispositivos móviles en pleno campo.</p>
    
    <div class="busqueda-filtros">
      <input 
        v-model="searchQuery" 
        type="text" 
        placeholder="🔍 Buscar planta (ej. Hipérico, Llantén, Taraxacum...)" 
        class="input-busqueda"
      />
    </div>

    <div v-if="filteredPlantas.length === 0" class="no-results">
      <p>No se han encontrado plantas que coincidan con la búsqueda.</p>
    </div>

    <!-- Catálogo de Plantas en Columnas CSS Nativas -->
    <div class="container">
      <div v-for="planta in filteredPlantas" :key="planta.id" class="card card-planta">
        <img :src="planta.img" :alt="planta.nombre" loading="lazy">
        <div class="info-planta">
          <h3>{{ planta.nombre }} <span class="nombre-cientifico">({{ planta.cientifico }})</span></h3>
          <p class="tag-euskera" v-if="planta.euskera">Euskera: <strong>{{ planta.euskera }}</strong></p>
          
          <div class="bloque-contenido">
            <h4>⚡ SUPERPODER / CURIOSIDAD:</h4>
            <p>{{ planta.superpoder }}</p>
          </div>

          <div class="bloque-contenido">
            <h4>🌿 PARTE QUE SE USA:</h4>
            <p>{{ planta.parte }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Sección Especial: Sabiduría Etnobotánica (Anexo del PDF) -->
    <div class="seccion-anexos">
      <h2 class="titulo-anexo">Sabiduría Etnobotánica de Campo</h2>
      
      <div class="anexo-grid">
        <!-- Cataplasma -->
        <div class="anexo-tarjeta">
          <h3>🌿 Cataplasma Express de Auxilio</h3>
          <p>Un remedio de emergencia que imita la sabiduría de los antiguos pastores cuando sufrían un golpe, picadura o rozadura en el monte. Un laboratorio vivo que aprovecha la fuerza de la planta fresca al instante.</p>
          
          <div class="ingredientes-box">
            <h4>Ingredientes de la Ruta (Efecto Sinérgico)</h4>
            <ul>
              <li><strong>Llantén (Hojas):</strong> La gran "tirita" del camino. Contiene aucubina y mucílagos que desinfectan y regeneran.</li>
              <li><strong>Gordolobo (Hojas):</strong> El escudo antiinflamatorio. Aporta flavonoides que rebajan la hinchazón.</li>
              <li><strong>Hierbabuena (Hojas):</strong> El analgésico natural. El mentol aporta un "efecto frío" que calma el dolor.</li>
              <li><strong>Saúco o malva (Flores):</strong> El suavizante epidérmico. Calma la piel irritada.</li>
            </ul>
          </div>

          <h4>Procedimiento en 4 Pasos:</h4>
          <ol>
            <li><strong>Trocear:</strong> Limpiar las hojas y trocearlas con las manos para liberar los jugos.</li>
            <li><strong>Machacar:</strong> Introducir en mortero con una pizca de sal (rompe las células) y machacar hasta lograr una pasta oscura.</li>
            <li><strong>Emulsionar:</strong> Añadir una cucharadita de aceite (oliva/almendras) para atrapar los principios activos.</li>
            <li><strong>Aplicar:</strong> Colocar sobre una gasa y aplicar sobre la piel.</li>
          </ol>
          <div class="nota-alerta">
            <strong>⚠️ NOTA:</strong> Contiene el agua de la planta viva. No se puede guardar en tarros ya que se pudriría. Es de uso inmediato en la recolección.
          </div>
        </div>

        <!-- Buenas prácticas -->
        <div class="anexo-tarjeta">
          <h3>🌍 Pautas de Recolección Sostenible</h3>
          
          <h4>1. Código de Ética de la Recolección</h4>
          <ul>
            <li><strong>La Regla del 20%:</strong> Nunca recolectes más de una quinta parte de las plantas sanas de una misma zona. Deja cantidad para que se regenere y alimente a la fauna local.</li>
            <li><strong>Cero Raíces:</strong> A menos que sea estrictamente necesario (ej. Zarzaparrilla), recolecta solo partes aéreas realizando cortes limpios. No arranques de raíz.</li>
            <li><strong>Zonas Limpias:</strong> Evita carreteras, vías de tren o zonas contaminadas por animales. Busca ejemplares sanos.</li>
            <li><strong>El Momento Óptimo:</strong> Mañana soleada, sin rocío. Nunca recojas plantas mojadas o se pudrirán.</li>
          </ul>

          <h4>2. El Arte del Secado</h4>
          <ul>
            <li><strong>En Manojos (Hojas/Tallos):</strong> Atar en pequeños ramos y colgar boca abajo en lugar cálido, seco, oscuro y ventilado. La oscuridad evita que la clorofila se degrade.</li>
            <li><strong>En Bandejas (Flores/Hojas grandes):</strong> Estirar en una sola capa sobre rejilla o papel absorbente en lugar sombrío.</li>
            <li><strong>El Punto Crucial:</strong> Están listas cuando al tocarlas crujen como papel y los tallos se quiebran limpiamente.</li>
            <li><strong>Almacenamiento:</strong> Guardar en tarros de cristal herméticos (mejor vidrio opaco), en lugar fresco y oscuro. Etiquetar con nombre y fecha. Consumir antes de un año.</li>
          </ul>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useHead } from '@vueuse/head'

const pageUrl = 'https://www.geobizi.com/fitxas-etnobotanicas-enkarterri'
useHead({
  title: 'Guía Digital: Fichas Etnobotánicas y Plantas Medicinales | Geobizi',
  meta: [{ name: 'description', content: 'Consulta en tiempo real el catálogo de plantas de Bizkaia: Hipérico, Caléndula, Llantén... descubre sus superpoderes medicinales y pautas de recolección sostenible.' }],
  link: [{ rel: 'canonical', href: pageUrl }]
})

const searchQuery = ref('')

// Base de datos de las 20 plantas extraídas del PDF
const plantas = ref([
  {
    id: 1,
    nombre: 'Hipérico',
    cientifico: 'Hypericum perforatum',
    euskera: '',
    img: '/imagenes/etnobotanica/hiperico.png',
    superpoder: 'Si frotas sus flores amarillas entre los dedos, verás que secretan un líquido de color rojo sangre llamado hipericina. Las abuelas la utilizaban tradicionalmente en ungüentos para el cuidado de quemaduras, heridas y otras afecciones de la piel.',
    parte: 'Se recogen las flores amarillas y las hojas más tiernas situadas justo debajo de ellas, donde se concentran gran parte de los compuestos.'
  },
  {
    id: 2,
    nombre: 'Caléndula',
    cientifico: 'Calendula officinalis',
    euskera: '',
    img: '/imagenes/etnobotanica/calendula.png',
    superpoder: 'Conocida como el "reloj del sol" porque sus flores se abren al amanecer y se cierran al atardecer. Es un auténtico imán para los polinizadores y una de las plantas más apreciadas en cosmética natural por sus propiedades calmantes y protectoras para la piel.',
    parte: 'Se recolectan los capítulos florales enteros (las flores de color naranja o amarillo intenso) cuando están completamente abiertos y reciben pleno sol.'
  },
  {
    id: 3,
    nombre: 'Milenrama',
    cientifico: 'Achillea millefolium',
    euskera: 'Odol-belar',
    img: '/imagenes/etnobotanica/milenrama.png',
    superpoder: 'En euskera la llamamos odol-belar (hierba de la sangre). Cuenta la leyenda que el héroe Aquiles la usaba para sanar los cortes de sus soldados. Ha sido utilizada tradicionalmente para favorecer la limpieza de heridas y la recuperación de la piel.',
    parte: 'Se cortan las sumidades floridas (los ramilletes de flores blancas o rosadas) junto con sus hojas plumosas que parecen pequeños helechos.'
  },
  {
    id: 4,
    nombre: 'Llantén Mayor',
    cientifico: 'Plantago major',
    euskera: '',
    img: '/imagenes/etnobotanica/llanten-mayor.png',
    superpoder: 'Es la gran "tirita viva" de los caminos de Bizkaia. Crece incluso en terrenos muy pisados y ha sido utilizada tradicionalmente para aliviar pequeñas irritaciones de la piel, picaduras y rozaduras durante los paseos por el monte.',
    parte: 'Se utilizan las hojas frescas y sanas de la base de la planta, fácilmente reconocibles por sus marcados nervios longitudinales.'
  },
  {
    id: 5,
    nombre: 'Romero',
    cientifico: 'Salvia rosmarinus',
    euskera: '',
    img: '/imagenes/etnobotanica/romero.png',
    superpoder: 'Su intenso aroma estimula los sentidos y tradicionalmente se ha empleado para favorecer la circulación, aliviar la sensación de cansancio muscular y conservar preparados herbales gracias a sus compuestos antioxidantes.',
    parte: 'Se cortan las ramitas tiernas con sus hojas en forma de aguja y, cuando es posible, también las pequeñas flores azuladas.'
  },
  {
    id: 6,
    nombre: 'Tomillo',
    cientifico: 'Thymus vulgaris',
    euskera: '',
    img: '/imagenes/etnobotanica/tomillo.png',
    superpoder: 'Su aceite esencial contiene timol, una sustancia muy apreciada por sus propiedades antisépticas. Tradicionalmente se ha utilizado para ayudar a combatir infecciones respiratorias, proteger heridas y fortalecer el organismo.',
    parte: 'Se recolectan las sumidades floridas, es decir, los extremos de los tallos con hojas y pequeñas flores rosadas o blanquecinas, al comienzo de la floración.'
  },
  {
    id: 7,
    nombre: 'Espino Blanco',
    cientifico: 'Crataegus monogyna',
    euskera: 'Ote-zuri',
    img: '/imagenes/etnobotanica/espino-blanco.png',
    superpoder: 'Es conocido como el "árbol del corazón" en la tradición herbal europea. Desde hace siglos se ha empleado para favorecer el bienestar cardiovascular y aportar sensación de calma. Además, sus ramas espinosas ofrecen refugio y protección a numerosas aves.',
    parte: 'Se recolectan las sumidades floridas y las hojas jóvenes durante la primavera, cuando la planta se encuentra en plena floración.'
  },
  {
    id: 8,
    nombre: 'Hinojo',
    cientifico: 'Foeniculum vulgare',
    euskera: 'Fennel',
    img: '/imagenes/etnobotanica/hinojo.png',
    superpoder: 'Una planta de intenso aroma anisado. Sus semillas han sido utilizadas tradicionalmente para favorecer la digestión y aliviar las molestias digestivas. En la cultura popular se le atribuyeron propiedades para mantener alejados algunos insectos.',
    parte: 'Se recogen sus umbelas llenas de semillas verdes o secas a finales de verano, que es donde se concentra todo su poder digestivo.'
  },
  {
    id: 9,
    nombre: 'Lavanda',
    cientifico: 'Lavandula angustifolia',
    euskera: '',
    img: '/imagenes/etnobotanica/lavanda.png',
    superpoder: 'Es una planta muy apreciada en cosmética natural por su aroma relajante y por los usos tradicionales asociados al cuidado de la piel. También se ha empleado para favorecer la relajación y aliviar pequeñas molestias cutáneas.',
    parte: 'Se cortan las espigas florales alargadas de color lila o morado cuando los capullos empiezan a abrirse a principios de verano.'
  },
  {
    id: 10,
    nombre: 'Salvia',
    cientifico: 'Salvia officinalis',
    euskera: '',
    img: '/imagenes/etnobotanica/salvia.png',
    superpoder: 'Su nombre procede del latín salvare (salvar), reflejando la enorme estima que despertó durante siglos. Es una planta muy aromática utilizada tradicionalmente por sus propiedades antisépticas y por su capacidad para favorecer la recuperación de la piel.',
    parte: 'Se recogen principalmente las hojas de color verde grisáceo y tacto aterciopelado, donde se concentran la mayoría de sus aceites esenciales.'
  },
  {
    id: 11,
    nombre: 'Menta',
    cientifico: 'Mentha piperita',
    euskera: '',
    img: '/imagenes/etnobotanica/menta.png',
    superpoder: 'Su gran especialidad es el frescor analgésico. Al aplicarla sobre la piel cansada o dolorida, genera un efecto frío inmediato que duerme el dolor de los golpes. Además, aporta una fragancia limpia y vital que transforma por completo el aroma de los aceites.',
    parte: 'Se aprovechan las hojas frescas de los tallos jóvenes, recolectadas preferiblemente a primera hora de la mañana antes de que apriete el calor.'
  },
  {
    id: 12,
    nombre: 'Manzanilla',
    cientifico: 'Matricaria chamomilla',
    euskera: '',
    img: '/imagenes/etnobotanica/manzanilla.png',
    superpoder: 'Es el bálsamo de la suavidad. Esta pequeña flor silvestre es reconocida tradicionalmente por sus propiedades calmantes y antiinflamatorias. Es idónea para tratar las pieles más delicadas, aliviar las quemaduras del sol y reducir la hinchazón.',
    parte: 'Se recolectan únicamente las cabezuelas florales amarillas y blancas, evitando cortar los tallos largos para no cargar la prensa en exceso.'
  },
  {
    id: 13,
    nombre: 'Malva',
    cientifico: 'Malva sylvestris',
    euskera: '',
    img: '/imagenes/etnobotanica/malva.png',
    superpoder: 'El secreto de la malva reside en sus mucílagos, una especie de gelatina natural que se activa al humedecerla. Este gel actúa como una capa protectora y suavizante que hidrata las pieles secas, calma las irritaciones y ayuda a sanar eccemas rebeldes.',
    parte: 'Se recolectan tanto las vistosas flores de color púrpura con venas oscuras como las hojas tiernas con forma de mano.'
  },
  {
    id: 14,
    nombre: 'Ortiga Mayor',
    cientifico: 'Urtica dioica',
    euskera: '',
    img: '/imagenes/etnobotanica/ortiga-mayor.png',
    superpoder: 'Aunque todos la esquivan porque sus pelos urticantes pican al tocarla, es una de las plantas más ricas en hierro, minerales y vitaminas. En la pomada pierde su picor y se convierte en una aliada excelente para nutrir la piel y activar el riego.',
    parte: 'Se recogen las cuatro hojas superiores de los brotes más tiernos, utilizando siempre guantes para evitar la reacción urticante en el taller.'
  },
  {
    id: 15,
    nombre: 'Diente de León',
    cientifico: 'Taraxacum officinale',
    euskera: '',
    img: '/imagenes/etnobotanica/diente-leon.png',
    superpoder: 'Famosa entre los niños por sus "abuelitos". Esta planta tradicionalmente se ha asociado al apoyo de las funciones hepáticas y digestivas. Aporta a los ungüentos antioxidantes que ayudan a purificar la piel y a regenerar los tejidos envejecidos.',
    parte: 'Se utilizan las hojas basales con bordes dentados y las brillantes flores amarillas antes de que se transformen en globos de semillas.'
  },
  {
    id: 16,
    nombre: 'Margarita Silvestre',
    cientifico: 'Bellis perennis',
    euskera: '',
    img: '/imagenes/etnobotanica/margarita.png',
    superpoder: 'Es considerada el "árnica" de las campas de Enkarterri. Esta pequeña flor que tapiza nuestros prados tiene la maravillosa propiedad de absorber los moratones, rebajar los edemas causados por torceduras y acelerar la curación de los traumatismos leves.',
    parte: 'Se recogen las flores completas con sus pétalos blancos y centro amarillo, presionándolas firmemente boca abajo en el proceso de prensado.'
  },
  {
    id: 17,
    nombre: 'Saponaria',
    cientifico: 'Saponaria officinalis',
    euskera: '',
    img: '/imagenes/etnobotanica/saponaria.png',
    superpoder: 'Conocida tradicionalmente como la "hierba jabonera", sus raíces y hojas producen saponinas, sustancias que generan espuma natural al mezclarse con agua. En la medicina popular se empleaba para limpiar heridas infectadas y calmar afecciones cutáneas crónicas.',
    parte: 'Se recolectan las hojas de los tallos intermedios y las flores de color rosa pálido que se abren a finales de la primavera.'
  },
  {
    id: 18,
    nombre: 'Saúco',
    cientifico: 'Sambucus nigra',
    euskera: 'Intsusa',
    img: '/imagenes/etnobotanica/sauco.png',
    superpoder: 'Es el árbol protector del folklore vasco, plantado junto a los caseríos para alejar las tormentas. Sus flores tienen propiedades medicinales extraordinarias para suavizar la piel sensible, mitigar las manchas cutáneas y calmar mucosas inflamadas.',
    parte: 'Se cortan las umbelas o ramilletes planos formados por decenas de pequeñas y olorosas flores blancas de sutil aroma dulce.'
  },
  {
    id: 19,
    nombre: 'Nogal',
    cientifico: 'Juglans regia',
    euskera: '',
    img: '/imagenes/etnobotanica/nogal.png',
    superpoder: 'Las hojas del nogal son ricas en taninos y juglona, dos componentes que actúan como potentes antifúngicos y astringentes naturales. Son perfectas en los ungüentos para combatir infecciones por hongos en la piel, detener pequeñas infecciones y combatir el sudor.',
    parte: 'Se seleccionan las hojas compuestas de color verde intenso, descartando aquellas que muestren manchas oscuras o sequedad por el sol.'
  },
  {
    id: 20,
    nombre: 'Zarza',
    cientifico: 'Rubus fruticosus',
    euskera: '',
    img: '/imagenes/etnobotanica/zarza.png',
    superpoder: 'Más allá de darnos deliciosas moras al final del verano, la zarza es una planta medicinal muy valiosa. Sus brotes tiernos son altamente astringentes, lo que significa que ayudan a contraer los tejidos de la piel, cerrando heridas y cicatrizando eccemas.',
    parte: 'Se recolectan con mucho cuidado las hojas más jóvenes y los brotes tiernos de los extremos, retirando los pequeños aguijones.'
  },
  {
    id: 21,
    nombre: 'Hiedra',
    cientifico: 'Hedera helix',
    euskera: '',
    img: '/imagenes/etnobotanica/hiedra.png',
    superpoder: 'Es una planta trepadora muy resistente que simboliza la permanencia y la inmortalidad. En la medicina popular se añadía en dosis muy pequeñas y controladas a los preparados externos destinados a aliviar molestias musculares y articulares.',
    parte: 'Se utilizan únicamente una o dos hojas adultas de color verde oscuro, manipulándolas siempre con precaución y para uso externo y controlado.'
  },
  {
    id: 22,
    nombre: 'Laurel',
    cientifico: 'Laurus nobilis',
    euskera: '',
    img: '/imagenes/etnobotanica/laurel.png',
    superpoder: 'El laurel contiene aceites esenciales con propiedades antiinflamatorias y analgésicas muy destacadas. Su incorporación al ungüento ayuda a calmar los dolores de las articulaciones y aporta un aroma balsámico protector.',
    parte: 'Se eligen las hojas maduras, duras y brillantes de los arbustos, que rompen muy bien sus células al ser machacadas en el mortero.'
  },
  {
    id: 23,
    nombre: 'Pulmonaria',
    cientifico: 'Pulmonaria officinalis',
    euskera: '',
    img: '/imagenes/etnobotanica/pulmonaria.png',
    superpoder: 'Sus hojas verdes están llenas de manchas blancas que, según los antiguos botánicos, recordaban a unos pulmones sanos. Por ello, se usaba tradicionalmente para calmar la tos y limpiar los bronquios. Además, sus flores cambian de color rosa a azul al envejecer.',
    parte: 'Se recolectan las hojas basales manchadas y sus llamativas flores tubulares de dos colores durante la primavera.'
  },
  {
    id: 24,
    nombre: 'Achicoria',
    cientifico: 'Cichorium intybus',
    euskera: 'Txikoria',
    img: '/imagenes/etnobotanica/achicoria.png',
    superpoder: 'Es la planta de los "ojos azules". Sus preciosas flores solo se abren por la mañana. En épocas de necesidad en los pueblos, sus raíces se tostaban y se machacaban para hacer un sustituto del café sin cafeína que ayudaba a digerir mejor las comidas.',
    parte: 'Se aprovechan sus características flores de color azul celeste y, para remedios profundos, su larga raíz pivotante.'
  },
  {
    id: 25,
    nombre: 'Hierbabuena',
    cientifico: 'Mentha spicata',
    euskera: '',
    img: '/imagenes/etnobotanica/hierbabuena.png',
    superpoder: 'Es la prima hermana más dulce de la menta y la reina de las huertas de Bizkaia. Tradicionalmente utilizada para favorecer la digestión y aliviar molestias digestivas. Su aroma fresco e intenso es un potente repelente natural contra los mosquitos molestos.',
    parte: 'Se cortan los tallos jóvenes y las hojas frescas y rugosas justo antes de que la planta empiece a florecer.'
  },
  {
    id: 26,
    nombre: 'Verbena',
    cientifico: 'Verbena officinalis',
    euskera: '',
    img: '/imagenes/etnobotanica/verbena.png',
    superpoder: 'Considerada una planta sagrada por los antiguos druidas, quienes la llamaban "la hierba de los hechizos". En la tradición popular se utilizaba como un escudo contra el dolor de cabeza y para calmar los nervios, el estrés y las preocupaciones del día a día.',
    parte: 'Se recoge la planta entera florecida (tallos rígidos con sus pequeñísimas y discretas flores de color lila pálido).'
  },
  {
    id: 27,
    nombre: 'Llantén Menor',
    cientifico: 'Plantago lanceolata',
    euskera: 'Ezorri-belar',
    img: '/imagenes/etnobotanica/llanten-menor.png',
    superpoder: 'Aunque ya tenemos el Llantén Mayor en la pomada, esta variedad de hojas estrechas como lanzas es vital en Enkarterri. Tradicionalmente empleado para aliviar la tos y favorecer el cuidado de pequeñas heridas o inflamaciones.',
    parte: 'Se recolectan sus hojas alargadas y estrechas que crecen en forma de roseta pegadas a ras de suelo.'
  },
  {
    id: 28,
    nombre: 'Cola de Caballo',
    cientifico: 'Equisetum arvense',
    euskera: 'Ezruts',
    img: '/imagenes/etnobotanica/cola-caballo.png',
    superpoder: 'Es un auténtico fósil viviente, ya existía mucho antes de la aparición de las plantas con flores actuales. No produce flores ni semillas, sino esporas. Es muy rica en silicio, por lo que tradicionalmente se ha utilizado para fortalecer tejidos como huesos, uñas y cabello.',
    parte: 'Se recolectan los tallos estériles de color verde, que recuerdan a pequeños pinos o colas de caballo.'
  },
  {
    id: 29,
    nombre: 'Cymbalaria / Palomilla',
    cientifico: 'Cymbalaria muralis',
    euskera: '',
    img: '/imagenes/etnobotanica/cymbalaria.png',
    superpoder: 'Su superpoder es la "fototropía inversa": sus flores buscan el sol, pero una vez polinizadas, el tallo se tuerce hacia la sombra para esconder sus semillas en las grietas de la piedra. Tradicionalmente se usaba para calmar inflamaciones y sabañones.',
    parte: 'Se recolecta la planta entera (tallos finos, hojas con forma de hiedra y sus pequeñas flores de color lila con centro amarillo) que se prensa con gran facilidad.'
  },
  {
    id: 30,
    nombre: 'Ombligo de Venus',
    cientifico: 'Umbilicus rupestris',
    euskera: 'Melorri',
    img: '/imagenes/etnobotanica/ombligo-venus.png',
    superpoder: 'Sus hojas son redondas y tienen un hoyuelo en el centro que parece un ombligo. Almacenan tanta agua que en los caseríos se usaban como tiritas naturales: se les quitaba la piel fina y se ponían sobre las heridas para refrescar y curar.',
    parte: 'Se utilizan sus hojas carnosas y circulares. Al ser muy gruesas, en el taller hay que prensarlas con mucho papel absorbente para que no se pudran.'
  },
  {
    id: 31,
    nombre: 'Amapola',
    cientifico: 'Papaver rhoeas',
    euskera: 'Loborri',
    img: '/imagenes/etnobotanica/amapola.png',
    superpoder: 'Su gran superpoder es la relajación. Contiene sustancias primas de la familia de la adormidera, pero mucho más suaves, que las abuelas utilizaban en infusiones florales para calmar los ataques de tos seca, los nervios y ayudar a los niños a dormir mejor.',
    parte: 'Se recogen únicamente los delicados pétalos de color rojo intenso, justo cuando la flor se acaba de abrir, ya que se caen con mucha facilidad.'
  },
  {
    id: 32,
    nombre: 'Endrino',
    cientifico: 'Prunus spinosa',
    euskera: 'Basaran',
    img: '/imagenes/etnobotanica/endrino.png',
    superpoder: 'Sus ramas espinosas ofrecen refugio a numerosos pájaros y sus frutos, las endrinas, son la base del tradicional pacharán. Tanto las flores como los frutos han tenido diversos usos en la medicina popular y la alimentación tradicional.',
    parte: 'Se recolectan las flores blancas en primavera, empleadas en infusiones de efecto laxante suave, y los frutos maduros en otoño para elaborar pacharán.'
  },
  {
    id: 33,
    nombre: 'Bolsa de Pastor',
    cientifico: 'Capsella bursa-pastoris',
    euskera: 'Txorrata',
    img: '/imagenes/etnobotanica/bolsa-pastor.png',
    superpoder: 'Se llama así porque sus frutos tienen forma de corazón que recuerda a las antiguas bolsas de cuero de los pastores. Es tradicionalmente conocida por sus propiedades hemostáticas y utilizada para ayudar a controlar pequeños sangrados.',
    parte: 'Se recolecta la parte aérea entera (tallos, hojas y sus curiosos frutos con forma de corazón) justo durante la época de floración.'
  },
  {
    id: 34,
    nombre: 'Higuera',
    cientifico: 'Ficus carica',
    euskera: 'Pikondo',
    img: '/imagenes/etnobotanica/higuera.png',
    superpoder: 'Su látex es ese "líquido blanco" pegajoso que brota al cortar una hoja o un higo verde. Se ha utilizado tradicionalmente para tratar verrugas de la piel, pero ¡cuidado!: es fotosensible y bajo el sol puede provocar reacciones y quemaduras graves en la piel.',
    parte: 'Se aprovecha el látex blanco que exuda el tallo al cortar una hoja fresca, aplicándolo con muchísimo cuidado solo encima de la verruga.'
  },
  {
    id: 35,
    nombre: 'Trébol Morado',
    cientifico: 'Trifolium pratense',
    euskera: 'Hirusta gorri',
    img: '/imagenes/etnobotanica/trebol-morado.png',
    superpoder: 'Su gran superpoder es que es riquísimo en isoflavonas, unas sustancias que ayudan a calmar los desarreglos del cuerpo y limpian la piel de eccemas y rojeces. Además, sus raíces atrapan el nitrógeno del aire y alimentan la tierra del prado.',
    parte: 'Se cortan únicamente las vistosas cabezuelas florales de color rosa violáceo, presionándolas bien de lado en el proceso de prensado.'
  },
  {
    id: 36,
    nombre: 'Zarzaparrilla',
    cientifico: 'Smilax aspera',
    euskera: 'Sasi-mizpira',
    img: '/imagenes/etnobotanica/zarzaparrilla.png',
    superpoder: 'Es la planta "liana" de los setos cantábricos, llena de espinas para trepar. Es uno de los mejores depurativos de la sangre que existen. De hecho, con su raíz se fabricaba la receta original de la conocida bebida de refresco antes de que existieran las colas industriales.',
    parte: 'Tradicionalmente se desentierra su raíz para hacer recetas secretas de muchos licores de hierbas tradicionales, elixires y digestivos de curación.'
  },
  {
    id: 37,
    nombre: 'Gordolobo',
    cientifico: 'Verbascum thapsus',
    euskera: 'Ostaza',
    img: '/imagenes/etnobotanica/gordolobo.png',
    superpoder: 'Sus grandes hojas son increíblemente suaves y aterciopeladas. Su gran superpoder es ser un potente antiinflamatorio: calma los dolores de oído y rebaja la hinchazón de la piel, además de abrir los bronquios y atrapar la tos seca cuando estamos resfriados.',
    parte: 'Se recolectan sus grandes hojas aterciopeladas y sus vistosas flores de color amarillo brillante que crecen en una gran vara vertical.'
  },
  {
    id: 38,
    nombre: 'Hierba de San Roberto',
    cientifico: 'Geranium robertianum',
    euskera: 'Zaingorri',
    img: '/imagenes/etnobotanica/hierba-san-roberto.png',
    superpoder: 'Es conocida como la "hierba de la salud". Su fuerte olor resinoso actúa como un excelente repelente natural de mosquitos. Tradicionalmente se usaba para limpiar heridas, frenar pequeñas hemorragias y enjuagar las encías inflamadas.',
    parte: 'Se recolecta la planta entera en flor (hojas muy recortadas que se vuelven rojizas en verano y sus pequeñas flores fucsias de cinco pétalos).'
  },
  {
    id: 39,
    nombre: 'Celidonia',
    cientifico: 'Chelidonium majus',
    euskera: 'Ziridonia',
    img: '/imagenes/etnobotanica/celidonia.png',
    superpoder: 'Expulsa un látex de color naranja brillante que brota al romper sus tallos y que imita a la perfección el color del yodo de farmacia. Su látex se ha empleado tradicionalmente sobre verrugas, aunque debe utilizarse con precaución por su potencial irritante.',
    parte: 'Se utiliza el látex anaranjado fresco que exuda el tallo al cortarlo. Al ser un líquido vivo, es una ficha ideal para observar y experimentar en directo en el campo.'
  },
  {
    id: 40,
    nombre: 'Viperina',
    cientifico: 'Echium vulgare',
    euskera: 'Suge-belar',
    img: '/imagenes/etnobotanica/viperina.png',
    superpoder: 'Se llama "vivorera" porque sus flores parecen la boca abierta de una serpiente con lengua bífida. En la medicina popular se le atribuyeron usos relacionados con las afecciones respiratorias. Actualmente su uso interno no se recomienda de forma continuada.',
    parte: 'Se recolectan las sumidades floridas (sus llamativas varas cubiertas de flores que cambian mágicamente de color rosa a azul intenso) durante los meses de verano.'
  }
])

const filteredPlantas = computed(() => {
  return plantas.value.filter(planta => {
    const query = searchQuery.value.toLowerCase()
    return (
      planta.nombre.toLowerCase().includes(query) ||
      planta.cientifico.toLowerCase().includes(query) ||
      (planta.euskera && planta.euskera.toLowerCase().includes(query)) ||
      planta.superpoder.toLowerCase().includes(query)
    )
  })
})
</script>

<style scoped>
.general-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  padding-top: 7rem;
  padding-left: 2rem;
  padding-right: 2rem;
  padding-bottom: 2rem;
}

.busqueda-filtros {
  margin-bottom: 2.5rem;
  width: 100%;
}

.input-busqueda {
  width: 100%;
  padding: 1rem 1.5rem;
  font-size: 1.1rem;
  border: 2px solid var(--shoftgreen);
  border-radius: 0.5rem;
  outline: none;
  background-color: #ffffff;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  transition: border-color 0.3s;
}

.input-busqueda:focus {
  border-color: #2e7d32; 
}

/* SISTEMA DE COLUMNAS PARA FICHAS DE PLANTAS */
.container {
  column-count: 3;
  column-gap: 2rem;
  width: 100%; 
  margin-bottom: 4rem; /* Separación antes de los anexos */
}

.card-planta {
  width: 100%;
  margin-bottom: 2rem;
  padding: 24px;
  background-color: var(--megashoftgreen);
  border: 1px solid var(--shoftgreen);
  border-radius: 0.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
  break-inside: avoid; 
  display: inline-block;
}

.info-planta h3 {
  margin-top: 1.2rem;
  margin-bottom: 0.4rem;
  font-size: 1.4rem;
  color: #1b5e20;
}

.nombre-cientifico {
  font-style: italic;
  font-size: 1.1rem;
  color: #555555;
  font-weight: normal;
}

.tag-euskera {
  font-size: 0.95rem;
  background-color: #e8f5e9;
  padding: 0.3rem 0.6rem;
  border-radius: 0.25rem;
  display: inline-block;
  margin-bottom: 1rem;
  color: #2e7d32;
}

.bloque-contenido {
  margin-top: 1.2rem;
}

.bloque-contenido h4 {
  font-size: 0.9rem;
  margin-bottom: 0.3rem;
  color: #333333;
  letter-spacing: 0.05em;
}

.bloque-contenido p {
  font-size: 1rem;
  line-height: 1.5;
  color: var(--darkgrey);
  margin: 0;
}

img {
  width: 100%;
  border-radius: 0.5rem;
  height: auto;
  display: block;
}

.no-results {
  text-align: center;
  padding: 3rem;
  color: #666666;
  font-size: 1.2rem;
}

/* ESTILOS PARA LOS ANEXOS DE SABIDURÍA ETNOBOTÁNICA */
.seccion-anexos {
  margin-top: 3rem;
  padding-top: 3rem;
  border-top: 2px dashed var(--shoftgreen);
}

.titulo-anexo {
  text-align: center;
  color: var(--darkgreen); /* Usa el color que tengas en root si prefieres */
  margin-bottom: 2rem;
  font-size: 2rem;
}

.anexo-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.anexo-tarjeta {
  background-color: #fcfcfc;
  border: 1px solid #e0e0e0;
  border-radius: 0.5rem;
  padding: 2rem;
  box-shadow: 0 4px 10px rgba(0,0,0,0.03);
}

.anexo-tarjeta h3 {
  color: #2e7d32;
  margin-top: 0;
  border-bottom: 2px solid var(--shoftgreen);
  padding-bottom: 0.5rem;
  margin-bottom: 1.5rem;
}

.anexo-tarjeta h4 {
  color: #333;
  margin-top: 1.5rem;
  margin-bottom: 0.5rem;
}

.ingredientes-box {
  background-color: var(--megashoftgreen);
  padding: 1rem;
  border-radius: 0.5rem;
  margin: 1rem 0;
}

.ingredientes-box h4 {
  margin-top: 0;
  color: #1b5e20;
}

.anexo-tarjeta ul, .anexo-tarjeta ol {
  padding-left: 1.5rem;
  color: var(--darkgrey);
  line-height: 1.6;
}

.anexo-tarjeta li {
  margin-bottom: 0.5rem;
}

.nota-alerta {
  margin-top: 1.5rem;
  padding: 1rem;
  background-color: #fff3e0;
  border-left: 4px solid #ff9800;
  border-radius: 4px;
  color: #e65100;
  font-size: 0.95rem;
}


/* RESPONSIVE FLUIDO */
@media (max-width: 900px) {
  .container {
    column-count: 2;
  }
  .anexo-grid {
    grid-template-columns: 1fr; /* Apila los anexos en tablet */
  }
}

@media (max-width: 600px) {
  .container {
    column-count: 1;
  }
  .general-container {
    padding-top: 5.5rem;
    padding-left: 1rem;
    padding-right: 1rem;
  }
  .card-planta {
    padding: 16px;
  }
  .info-planta h3 {
    font-size: 1.25rem;
  }
  .nombre-cientifico {
    display: block;
    font-size: 0.95rem;
    margin-top: 0.2rem;
  }
  .anexo-tarjeta {
    padding: 1.5rem;
  }
}
</style>