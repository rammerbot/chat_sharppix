import unicodedata
import re
import random

def normalizar_texto(texto):
    """Convierte texto a minúsculas y elimina tildes"""
    texto = texto.lower()
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    return texto

pairs = [

    # SALUDOS Y CONSULTAS GENERALES

    ((r"(.*)hola(.*)", r"(.*)buenos dias(.*)", r"(.*)buenas tardes(.*)"), 
    ["¡Hola! ¿Cómo puedo ayudarte?", "¡Hola! ¿Qué tal?"]),

    ((r"(.*)como estas(.*)", r"(.*)como te va(.*)", r"(.*)que tal estas(.*)"), 
    ["Estoy bien, gracias. ¿Y tú?", "¡Genial! ¿Cómo estás tú?"]),

    ((r"(.*)tu nombre(.*)", r"(.*)como te llamas(.*)"), 
    ["Soy Chat Norris, si me quedo sin respuestas, el problema es de la pregunta.",
    "Soy Chat Norris, el chatbot más rudo del oeste."]),


    # PREGUNTAS ESPECÍFICAS SOBRE SHARPPIXAI

    ((r"(.*)como (.*)duplicado(.*)", r"(.*)como(.*)repetido(.*)"), 
    ["SharpPixAI puede identificar automáticamente archivos duplicados mediante la composicion de la imagen. Para eliminarlos directamente desde la plataforma.\n Tanbien contamos con una funcion adicional que elimina los duplicados desde la cuenta premium"]),

    ((r"subir varias imagenes", r"lote", r"optimizar imagenes"), 
    ["Puedes subir varias imágenes a la vez y aplicar optimizaciones en lote."]),

    ((r"edi", r"ajust", r"color", r"retoque", r"filtro", r"correccion", r"brillo", r"contraste"), 
    ["SharpPixAI incluye herramientas básicas para edición, como ajustes de color."]),

    ((r"agua", r"personaliza", r"marca de agua", r"logotipo", r"prote"), 
    ["Puedes personalizar y aplicar marcas de agua en SharpPixAI."]),

    ((r"formato compatible", r"formatos compatibles", r"video", r"MP4", r"MOV", r"AVI", r"MKV"), 
    ["Los formatos de video compatibles incluyen MP4, MOV, AVI, MKV, entre otros."]),

    ((r"reduc", r"tamaño del video", r"tamaño de los videos", r"calidad", r"compr", r"resolucion", 
    r"peso", r"conv", r"liviano", r"compr"), 
    ["SharpPixAI usa compresión avanzada para reducir el tamaño de videos sin perder calidad."]),

    ((r"convertir imágenes", r"convertir a", r"convertir un imagen", r"formatos de imagen", r"jpeg", r"png", r"webp"), 
    ["Podés convertir imágenes a JPEG, PNG o WebP, y videos a MP4, MOV o AVI."]),

    ((r"guardar el audio", r"sonido", r"convertir audio", r"extraer el audio", r"descargar el audio", r"formato de audio", r"mp3", r"wav"), 
    ["Podés guardar solo el audio en formatos MP3 o WAV en SharpPixAI."]),

    ((r"aplicación",r"celular", r"aplicación movil", r"móvil", r"mobile", r"app", r"para celular", r"android", r"ios"), 
    ["La plataforma tiene aplicaciones para Android e iOS. Además, permite subir, optimizar y compartir archivos fácilmente."]),

    ((r"tarda en procesar",  r"velocidad de procesamiento", r"cuánto tiempo demora", r"cuánto tarda", r"cuánto demora", 
    r"cuánto tiempo toma", r"cuánto tiempo se demora"), 
    ["Depende del tamaño del archivo y la carga del servidor, pero generalmente el procesamiento es muy rápido gracias a optimizaciones en la nube."]),

    ((r"prote", r"segur", r"encripta"), 
    ["Todos los archivos se almacenan en servidores encriptados y seguros."]),

    ((r"conexion a internet", r"internet"), 
    ["Se necesita conexión a internet para usar las funciones de optimización y almacenamiento."]),

    ((r"espacio", r"almacenamiento", r"free", r"gratuita", r"almacenamiento", r"gratis", r"plan", r"gb"), 
    ["La versión gratuita ofrece 2 GB de almacenamiento inicial."]),

    ((r"compartir archivos", r"enlace", r"link", r"enviar archivos"), 
    ["Puedes generar enlaces de acceso o compartir directamente en redes sociales."]),

    ((r"registrar", r"cuenta", r"registro"), 
    ["Puedes registrarte con tu correo electrónico o usar una cuenta de Google/Apple."]),

    ((r"planes", r"familiares", r"plan familiar", r"varios usuarios", r"varias personas", r"plan", r"compartido"), 
    ["Hay opciones para planes compartidos con múltiples usuarios."]),

    ((r"eliminar archivos", r"elimina", r"archivos viejos"), 
    ["Puedes configurar reglas para limpiar archivos antiguos automáticamente."]),

    ((r"imagen", r"formatos compatibles", r"formatos soportados", r"formatos de imagen soportados", 
    r"JPEG", r"PNG", r"TIFF", r"BMP", r"RAW", r"NEF", r"CR2", r"ARW"), 
    ["JPEG, PNG, TIFF, BMP, y formatos RAW como NEF, CR2, y ARW."]),

    ((r"mejorar desenfoque",r"imagen borrosa", r"imagenes borrosas", r"desenfocada"), 
    ["SharpPixAI incluye una función para mejorar detalles y reducir desenfoques."]),

    ((r"fondo", r"borrar el fondo", r"remover el fondo", r"eliminar el fondo", r"quitar el fondo", r"extraer el fondo"), 
    ["Hay una herramienta para eliminar fondos con un solo clic."]),

    ((r"reduce la calidad", r"pierde calidad", r"afecta la calidad", r"calidad"), 
    ["La optimización está diseñada para mantener la calidad mientras reduce el tamaño."]),

    ((r"organizar", r"clasificar",r"ordenar"), 
    ["La plataforma tiene opciones de organización inteligente."]),

    ((r"jpeg", r"png", r"webp", r"guardar imágenes", r"formatos de imagen"), 
    ["Puedes convertir imágenes a formatos como JPEG, PNG o WebP."]),

    ((r"formatos de video", r"video", r"formatos compatibles", r"formatos admitidos"), 
    ["MP4, MOV, AVI, MKV, y más."]),

    ((r"tamaño del video", r"peso del video", r"comprimir videos", r"sin perder calidad", r"perder calidad", r"manteniendo la calidad", r"reducir el peso"), 
    ["SharpPixAI utiliza compresión avanzada que mantiene la calidad."]),

    ((r"recortar", r"video", r"seleccionar", r"segmento", r"cortar", r"parte", r"editar", r"longitud"), 
    ["Puedes seleccionar y recortar clips directamente en la plataforma."]),

    ((r"subtitulos", r"texto"), 
    ["Puedes cargar archivos de subtítulos o generarlos automáticamente y en varios idiomas."]),

    ((r"mejorar la calidad", r"ajustar la resolución", r"resolucion", r"pixelado"), 
    ["Cuenta con herramientas de mejora de resolución y reducción de ruido."]),

    ((r"tiempo", r"demora", r"tarda", r"velocidad"), 
    ["Depende de la resolución y la duración, pero generalmente es muy eficiente."]),

    ((r"dividir", r"dividir videos", r"cortar videos", r"recortar videos", r"segmentos", r"recortar", 
    r"separar videos", r"partes", r"separar", r"clips", r"fragmentar", r"secciones"), 
    ["Hay herramientas para dividir videos fácilmente."]),

    ((r"audio", r"WAV", r"mp3", r"separar", r"sonido", r"pista", r"extraer el audio", r"extraer el sonido"), 
    ["Puedes guardar solo el audio en formatos MP3 o WAV."]),

    ((r"4k", r"8k", r"ultra", r"hd"), 
    ["Soporta videos en alta resolución."]),

    ((r"extensiones de audio", r"formatos de audio", r"tipos de audio", r"mp3", r"WAV", r"FLAC", r"AAC"), 
    ["MP3, WAV, FLAC, AAC, y más."]),

    ((r"ruido", r"audios", r"interferencias", r"ruido de fondo", r"eliminar ruido", r"limpiar audio", r"claridad"), 
    ["SharpPixAI está desarrollando herramientas tiene una herramienta para limpiar audios, pero actualmente no disponemos de ellas en la plataforma."]),

    ((r"transcribir", r"transcripción"), 
    ["Aun no contamos con función de transcripción automática, pero se encuentra en desarrollo."]),

    ((r"volumen"), 
    ["Puede ajustar el volumen y mejorar la claridad."]),

    ((r"recortar archivos de audio", r"recortar audio", r"segmentos de audio", r"cortar audios"), 
    ["Actualmente la plataforma no te permite seleccionar y recortar segmentos."]),

    ((r"combinar audio", r"fusionar audio", r"unir audio", r"juntar audio"), 
    ["Aun no existe una función que te permita fusionar audios."]),

    ((r"optimización de audio", r"calidad de audio", r"audio original"), 
    ["La app está diseñada para mantener la calidad original del audio."]),

    ((r"silencios", r"pausas", r"eliminar silencios", r"quitar pausas", r"silenciar", r"pausar"), 
    ["Actualmente no existe una función que te permita configurar esta opción al procesar audios."]),

    ((r"audiolibros", r"libros", r"capítulos", r"autores"), 
    ["Puedes organizar libros por capítulos o autores en diferentes carpetas."]),

    ((r"audios grandes", r"audios pesados"), 
    ["No hay límites significativos en cuanto al tamaño."]),

    ((r"formatos de texto", r"texto", r"documentos", r"PDF", r"DOCX", r"TXT", r"ODT"), 
    ["PDF, DOCX, TXT, ODT, y más."]),

    ((r"imágenes a texto", r"imagen a texto", r"ocr", r"reconocimiento de texto", r"texto en imágenes"), 
    ["Actualmente se encuentra en desarrollo una OCR para reconocer texto en imágenes."]),

    ((r"palabras clave", r"clave", r"indexar", r"búsquedas", r"buscar documentos", r"buscar archivos"), 
    ["La función de la plataforma que indexa documentos para búsquedas rápidas se encuentra en desarrollo."]),

    ((r"combinar pdf", r"fusionar pdf", r"pdf", r"word", r"unir pdf"), 
    ["Actualmente la función para que puedas fusionar archivos PDF o Word se encuentra en desarrollo."]),

    ((r"editar texto", r"editar un documento", r"modificar texto", r"modificar un archivo", r"editar archivos"), 
    ["Puedes descargar cualquier archivo, editarlo y volver a subirlo."]),

    ((r"convertir documento", r" convertir pdf", r"convertir word", r"convertir un archivo de texto", r"convertir archivos de texto", 
    r"convertir pdf a word", r"convertir word a pdf"), 
    ["Actualmente la plataforma no te permite convertir de PDF a Word o viceversa."]),

    ((r"extraer imagenes", r"extraer fotos", r"extraer contenido visual", r"extraer imágenes de pdf"), 
    ["Actualmente la función para extraer contenido visual de archivos PDF se encuentra en desarrollo."]),

    ((r"límite", r"tamaño de documentos", r"tamaño de archivos", r"tamaño máximo", r"límite de tamaño"), 
    ["Admite documentos grandes siempre que no superen el límite del plan contratado."]),

    ((r"ofrece", r"ventajas", r"beneficios", r"características", r"funciones", r"opciones", r"posibilidades"), 
    ["Ofrece almacenamiento seguro, optimización masiva y herramientas de análisis."]),

    ((r"rastrear", r"acceso", r"monitor"), 
    ["Hay herramientas para auditar el acceso y los cambios."]),

    ((r"cuentas", r"usuarios", r"miembros", r"acceso", r"permisos", r"roles", r"privilegios"), 
    ["Los planes empresariales permiten múltiples usuarios con permisos personalizados."]),

    ((r"integrar API", r"erp", r"apis", r"vincular", r"api", r"integración"), 
    ["La plataforma admite integración con APIs externas."]),

    ((r"archivos confidenciales", r"seguridad", r"sensibles", r"protegida", r"privados", r"confidencial", r"privacidad"), 
    ["Garantiza alta seguridad y cumplimiento de normativas."]),

    ((r"copias de seguridad", r"backup", r"backups", r"respaldo"), 
    ["Puedes programar copias de seguridad periódicas."]),

    ((r"ajustar imagenes a", r"adaptar imagenes a", r"redes sociales", r"instagram", r"facebook", r"twitter", r"adapta imagenes para", 
    r"ajusta imagenes para"), 
    ["Incluye herramientas para ajustar imágenes, videos y audios según los estándares de las redes sociales."]),

    ((r"acceso a", r"permisos", r"asigna", r"roles", r"acceso para", r"permisos para", r"usuarios"), 
    ["Puedes asignar roles y permisos específicos a cada usuario."]),

    ((r"reportes", r"estadisticas", r"actividad", r"informe", r"movimientos"), 
    ["La plataforma genera reportes detallados."]),

    ((r"migrar", r"transferir", r"dropbox", r"drive", r"aws"), 
    ["Puedes utilizar las herramientas de importación masiva o las integraciones disponibles con plataformas como Google Drive, Dropbox o AWS."]),

    ((r"etiqueta", r"categori", r"tags"), 
    ["Puedes añadir etiquetas personalizadas a tus archivos."]),

    ((r"tiempo real", r"simultaneamente", r"colabora", r"equipo", r"comentar"), 
    ["Los equipos pueden comentar y realizar ajustes en ciertos archivos simultáneamente."]),

    ((r"zapier", r"automatiza", r"automatización"), 
    ["Puedes usar APIs o herramientas como Zapier para automatizar tareas."]),

    ((r"analizar", r"estadisticas", r"actividad", r"seguimiento"), 
    ["Puedes ver métricas sobre acceso, ediciones y descargas."]),

    ((r"raw"), 
    ["Incluye herramientas para procesar y mejorar imágenes RAW."]),

    ((r"álbumes", r"álbumes", r"contraseña", r"privados", r"compartir", r"enlaces protegidos", r"enlaces privados"), 
    ["Puedes crear enlaces privados o protegidos con contraseña para compartir álbumes."]),

    ((r"imágenes grandes", r"imágenes pesadas", r"imágenes de alta resolución", r"imágenes de alta calidad"), 
    ["Puedes editar fotos grandes sin pérdida de calidad."]),

    ((r"ediciones en lote", r"ajustes masivos", r"corrección de color", r"cambio de resolución"), 
    ["Puedes aplicar ajustes masivos como cambio de resolución o corrección de color."]),

    ((r"notifica", r"alerta"), 
    ["SharpPixAi alerta y da opciones para fusionar o eliminar duplicados."]),

    ((r"galerías", r"personalizadas", r"galerías personalizadas"), 
    ["Puedes personalizar la apariencia de las galerías compartidas."]),

    ((r"recuperar", r"papelera", r"eliminad", r"restaurar", r"accidental", r"temporales"), 
    ["Hay una papelera de reciclaje donde los archivos se almacenan temporalmente."]),

    ((r"ajustar la resolución", r"ajustar la duración", r"ajustar el formato"), 
    ["Puedes ajustar la resolución, duración y formato según los requisitos."]),

    ((r"agregar", r"efectos", r"videos", r"filtros", r"transiciones", r"editar", r"rápida", r"mejorar", r"aspecto"), 
    ["Puedes aplicar algunas ediciones rápidas directamente en la plataforma."]),

    ((r"almacenar", r"podcasts", r"audios extensos", r"audios largos", r"extensos", r"transcribir", r"audios pesados", r"audios grandes"), 
    ["Puedes almacenar, optimizar y transcribir audios extensos."]),

    ((r"organiza"r"carpetas", r"clasifica", r"categorías"), 
    ["La organización es completamente personalizable."]),

    ((r"ia", r"inteligencia artificial"), 
    ["Utiliza inteligencia artificial para detectar posibles optimizaciones."]),

    ((r"vista previa", r"visualizar", r"previsualizar", ), 
    ["Puedes visualizar cualquier archivo en la plataforma."]),

    ((r"análi", r"rendimiento", r"analizar los archivos", r"medir"), 
    ["Puedes exportar los archivos optimizados para usarlos en herramientas de análisis externas."]),

    ((r"seguras", r"almacenamiento", r"seguro", r"encriptar",r"familia"), 
    ["SharpPixAI ofrece almacenamiento seguro y encriptado."]),

    ((r"album", r"eventos", r"bodas", r"cumpleaños", r"fechas", r"temáticos"), 
    ["Puedes organizar tus fotos por eventos y fechas."]),

    ((r"collages", r"presentaciones", r"diapositivas", r"montajes"), 
    ["Puedes crear presentaciones básicas directamente en la plataforma."]),

    ((r"tamaño de las fotos", r"ajustar la calidad de las imágenes", r"optimizar las fotos", r"reducir el tamaño de las imágenes"), 
    ["La plataforma ajusta el tamaño y la calidad según lo necesites."]),

    ((r"inteligencia artificial", r"ia", r"ai"), 
    ["Utiliza inteligencia artificial para clasificar tus archivos."]),

    ((r"digitalizar", r"fotos antiguas", r"fotos viejas", r"escanear", r"papel"), 
    ["Puedes digitalizar fotos antiguas y mejorar su calidad automáticamente."]),

    ((r"liberar espacio", r"nube"), 
    ["Puedes subir archivos a la nube y eliminarlos del dispositivo."]),

    ((r"seguridad", r"encripta", r"autentica", r"dos factores", r"dos pasos"), 
    ["Utiliza encriptación de extremo a extremo y autenticación de dos factores."]),

    ((r"dura", r"conserva", r"tiempo duran", r"tiempo permanecen", r"tiempo se almacenan", r"tiempo se guardan", r"tiempo se conservan"), 
    ["Los archivos se almacenan indefinidamente mientras tengas una suscripción activa."]),

    

    # DESPEDIDA

    ((r"adios", r"hasta luego", r"nos vemos", r"bye"), 
    ["¡Adiós! Que tengas un buen día.", "Nos vemos, ¡cuídate!"]),

    ((r"ayuda", r"necesito ayuda", r"puedes ayudarme"), 
    ["Claro, dime, ¿cómo puedo ayudarte?", "Por supuesto, ¿qué necesitas?"]),
]

despedidas = ["¡Adiós! Que tengas un buen día.", "Nos vemos, ¡cuídate!"]

def obtener_respuesta(pregunta):
    pregunta = normalizar_texto(pregunta)

    for patrones, respuestas in pairs:
        if isinstance(patrones, tuple):
            for patron in patrones:
                if re.search(rf"\b{patron}\b", pregunta):  
                    return random.choice(respuestas)
        else:
            if re.search(rf"\b{patrones}\b", pregunta):
                return random.choice(respuestas)

    return "Disculpa, puedes reformular la pregunta?"


