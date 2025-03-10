import unicodedata
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

def normalizar_texto(texto):
    # Convierte texto a minúsculas y elimina tildes
    texto = texto.lower()
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    return texto

pairs = [
    (r"hola|buenos dias|buenas tardes|que tal", ["¡Hola! ¿Cómo puedo ayudarte?", "¡Hola! ¿Qué tal?"]),
    (r"como estas", ["Estoy bien, gracias. ¿Y tú?", "¡Genial! ¿Cómo estás tú?"]),
    (r"tu nombre", ["Soy Chat Norris, si me quedo sin respuestas, el problema es de la pregunta."]),
    (r"como te llamas", ["Soy Chat Norris, el chatbot más rudo del oeste.", "Me llamo Chat Norris, si no encuentro la respuesta, el problema es de la pregunta."]),
    (r"adios|hasta luego", ["¡Adiós! Que tengas un buen día.", "Nos vemos, ¡cuídate!"]),
    (r"ayuda", ["Claro, dime, ¿cómo puedo ayudarte?", "Por supuesto, ¿qué necesitas?"]),
    

#Preguntas específicas sobre SharpPixAI

    (r"(?=.*\b(duplicado(.*))\b)(?=.*\b(elimina(.*))\b).*",                                     
    ["Para eliminar duplicados, SharpPixAI te permite fusionarlos o eliminarlos directamente desde la plataforma."]),

    (r"(?=.*\b(identifica(.*)|detec(.*)|reconoc(.*))\b)(?=.*\b(duplicad(.*)|repetid(.*))\b).*", 
    ["SharpPixAI puede identificar automáticamente archivos duplicados."]),

    (r"(.*)procesa(.*)|(.*)lote(.*)", 
    ["Puedes subir varias imágenes a la vez y aplicar optimizaciones en lote."]),

    (r"(.*)edi(.*)|(.*)ajust(.*)|(.*)color(.*)", 
    ["SharpPixAI incluye herramientas básicas para edición, como ajustes de color."]),

    (r"(.*)agua(.*)|(.*)personaliza(.*)", 
    ["Podés personalizar y aplicar marcas de agua en SharpPixAI."]),

    (r"(?=.*\bformato\b)(?=.*\bcompatib\b)(?=.*\bvideo\b).*", 
    ["Los formatos de video compatibles incluyen MP4, MOV, AVI, MKV, entre otros."]),

    (r"(?=.*\breduc\b)(?=.*\btamaño\b)(?=.*\bvideo\b)(?=.*\bcalidad\b).*", 
    ["SharpPixAI usa compresión avanzada para reducir el tamaño de videos sin perder calidad."]),

    (r"(?=.*\bconver\b)(?=.*\bformato\b)(?=.*\bvideo\b)(?=.*\bimagen\b).*", 
    ["Podés convertir imágenes a JPEG, PNG o WebP, y videos a MP4, MOV o AVI."]),

    (r"(?=.*\b(extra|guarda)\b)(?=.*\b(audio)\b)(?=.*\b(mp3|wav)\b).*", 
    ["Podés guardar solo el audio en formatos MP3 o WAV en SharpPixAI."]),

    (r"(?=.*\b(audio|texto)\b)(?=.*\b(transcri.*)\b).*", 
    ["SharpPixAI todavía no tiene función de transcripción automática, pero está en desarrollo."]),

    (r"(.*)(volumen)(.*)(audio)(.*)(aumentar|mejorar|ajustar)(.*)",                                                               
    ["Podés ajustar el volumen y mejorar la claridad del audio en SharpPixAI."]),

    (r"(.*)(recortar|seleccionar)(.*)(audio)(.*)",                                                               
    ["Por ahora, no es posible seleccionar y recortar segmentos de audio en SharpPixAI."]),

    (r"(.*)(combinar|fusionar)(.*)(audios)(.*)",                                            
    ["Actualmente, no hay una función para fusionar audios en SharpPixAI."]),

    (r"(.*)(ruido)(.*)", 
    ["SharpPixAI está desarrollando herramientas para limpiar audios, pero todavía no están disponibles."]),

    (r"(.*)(calidad)(.*)(audio|original)(.*)",                           
    ["SharpPixAI mantiene la calidad original del audio, incluso después de la optimización."]),

    (r"(.*)(silencio)(.*)", 
    ["Actualmente, SharpPixAI no permite configurar la eliminación automática de silencios en los audios."]),

    (r"(.*)(audiolibros)(.*)", 
    ["Puedes organizar audiolibros en SharpPixAI por capítulos o autores."]),

    (r"(.*)(tamaño|grande)(.*)",                                              
    ["SharpPixAI no impone límites significativos en cuanto al tamaño de los archivos."]),

    (r"(.*)transcri(.*)|(.*)optimiza(.*)|(.*)largo(.*)|(.*)extens(.*)audio(.*)",                                                              
    ["En SharpPixAI puedes almacenar, optimizar y transcribir audios extensos."]),

    (r"(.*)recort(.*)|(.*)clip(.*)", 
    ["Puedes seleccionar y recortar clips de video directamente en la plataforma."]),

    (r"(.*)subtitulo(.*)", 
    ["Puedes cargar archivos de subtítulos o generarlos automáticamente en varios idiomas."]),

    (r"(.*)pixela(.*)", 
    ["SharpPixAI incluye herramientas para mejorar la resolución y reducir el pixelado."]),

    (r"(.*)grandes(.*)|(.*)pesad(.*)", 
    ["La optimización de SharpPixAI es eficiente incluso con archivos de gran tamaño."]),

    (r"(.*)divid(.*)|(.*)segmento(.*)|(.*)fragment(.*)", 
    ["Puedes dividir videos en segmentos más pequeños dentro de SharpPixAI."]),

    (r"(.*)HD(.*)|(.*)4K(.*)|(.*)8K(.*)|(.*)alta(.*)|(.*)resolucion(.*)", 
    ["SharpPixAI soporta videos en alta resolución, incluyendo 4K y 8K."]),

    (r"(?=.*\bformatos\b)(?=.*\btexto\b)|(?=.*\bcompatibles\b).*", 
    ["Los formatos de texto compatibles con SharpPixAI incluyen PDF, DOCX, TXT y ODT."]),

    (r"(?=.*\bconver\b)(?=.*\b(imagenes|texto|ocr)\b).*", 
    ["SharpPixAI todavía no cuenta con OCR para reconocer texto en imágenes, pero está en desarrollo."]),

    (r"(.*)imagenes(.*)redes sociales(.*)optimizacion(.*)|(.*)adapta(.*)|(.*)ajusta(.*)|(.*)tamaño(.*)|(.*)formato(.*)|(.*)instagram(.*)|(.*)facebook(.*)",                               
    ["Puedes ajustar el tamaño y formato de imágenes para redes sociales en SharpPixAI."]),

    (r"(.*)palabra(.*)|(.*)clave(.*)|(.*)busca(.*)|(.*)indexa(.*)", 
    ["La función de indexación de documentos para búsquedas rápidas en SharpPixAI está en desarrollo."]),

    (r"(.*)cuenta(.*)|(.*)multi(.*)|(.*)empresa(.*)", 
    ["SharpPixAI ofrece cuentas individuales y planes empresariales con múltiples usuarios."]),

    (r"(.*)limite(.*)|(.*)documento(.*)", 
    ["SharpPixAI admite documentos grandes siempre que no superen el límite del plan contratado."]),

    (r"(.*)volumen(.*)", 
    ["SharpPixAI ofrece almacenamiento seguro, optimización masiva y herramientas de análisis."]),

    (r"(.*)apis(.*)", 
    ["La plataforma admite integración con APIs externas para conectar con otros sistemas."]),

    (r"(.*)copia(.*)|(.*)backup(.*)", 
    ["Puedes programar copias de seguridad periódicas en SharpPixAI."]),

    (r"(.*)nivel|(.*)permiso", 
    ["Puedes asignar roles y permisos específicos a cada usuario en SharpPixAI."]),

    (r"(.*)reporte(.*)", 
    ["SharpPixAI genera reportes detallados sobre el uso del almacenamiento y la actividad de los archivos."]),

    (r"(.*)migra(.*)", 
    ["Puedes migrar archivos a SharpPixAI utilizando herramientas de importación masiva o integraciones con Google Drive, Dropbox o AWS."]),

    (r"(.*)etiqueta(.*)|(.*)label(.*)", 
    ["Puedes añadir etiquetas personalizadas a tus archivos para facilitar la organización y búsqueda."]),

    (r"(.*)colabora(.*)|(.*)tiempo real(.*)|(.*)simultaneo(.*)|(.*)vivo(.*)", 
    ["Los equipos pueden colaborar en SharpPixAI comentando y realizando ajustes en archivos en tiempo real."]),

    (r"(.*)flujo|(.*)automatiza(.*)", 
    ["Puedes automatizar tareas en SharpPixAI utilizando APIs o herramientas como Zapier."]),

    (r"(.*)analis(.*)|(.*)metrica(.*)|(.*)KPI(.*)", 
    ["SharpPixAI permite ver métricas detalladas sobre acceso, ediciones y descargas."]),

    (r"(.*)raw(.*)|(.*)crud(.*)", 
    ["SharpPixAI incluye herramientas para procesar y mejorar imágenes RAW."]),

    (r"(.*)fecha(.*)|(.*)ubicacion(.*)", 
    ["SharpPixAI ofrece opciones avanzadas de organización basadas en fecha y ubicación."]),

    (r"(.*)galeria(.*)", 
    ["Podés personalizar la apariencia de las galerías en SharpPixAI."]),

    (r"(.*)recupera(.*)|(.*)restaura(.*)|(.*)papelera(.*)", 
    ["Los archivos eliminados se almacenan temporalmente en la papelera de reciclaje."]),

    (r"(.*)resolucion(.*)|(.*)duracion(.*)", 
    ["Podés ajustar la resolución, duración y formato de archivos en SharpPixAI."]),

    (r"(.*)clips(.*)", 
    ["SharpPixAI permite seleccionar y recortar segmentos de video fácilmente."]),

    (r"(.*)compr(.*)", 
    ["La compresión avanzada de SharpPixAI reduce el tamaño de los archivos sin afectar la calidad."]),

    (r"(.*)efecto(.*)|(.*)filtro(.*)", 
    ["Podés aplicar efectos y filtros básicos directamente en la plataforma."]),

    (r"(.*)inteligencia(.*)|(.*)artificial(.*)|(.*)ia(.*)|(.*)clasifica(.*)", 
    ["SharpPixAI usa inteligencia artificial para detectar optimizaciones y clasificar archivos automáticamente."]),

    (r"(.*)vista previa(.*)", 
    ["Podés visualizar cualquier archivo en SharpPixAI antes de compartirlo o editarlo."]),

    (r"(.*)rendimiento(.*)|(.*)anali(.*)", 
    ["SharpPixAI no ofrece análisis de rendimiento directamente, pero permite exportar archivos optimizados para herramientas externas."]),

    (r"(.*)collage(.*)|(.*)presentacion(.*)", 
    ["Podés crear presentaciones y collages básicos en SharpPixAI."]),

    (r"(.*)ajust(.*)", 
    ["SharpPixAI permite ajustar el tamaño y la calidad de archivos según tus necesidades."]),

    (r"(.*)ajust(.*)(.*)masiv(.*)|(.*)lote(.*)|(.*)grup(.*)", 
    ["Podés aplicar ajustes masivos como cambios de resolución o corrección de color."]),

    (r"(.*)personaliz(.*)organiza", 
    ["La organización en SharpPixAI es completamente personalizable."]),

    (r"(.*)enlace(.*)|(.*)prote(.*)|(.*)compart(.*)|(.*)segur(.*)album(.*)",                                               
    ["Podés crear enlaces privados o protegidos con contraseña para compartir álbumes en SharpPixAI."]),

    (r"(.*)pdf(.*)|(.*)word(.*)convert(.*)", 
    ["Actualmente, SharpPixAI no permite convertir de PDF a Word o viceversa."]),

    (r"(.*)empresa(.*)plan(.*)",                                                                                                                                                                                                
    ["Los planes empresariales de SharpPixAI pueden ajustarse a necesidades específicas y permiten múltiples usuarios con permisos personalizados."]),

    (r"(.*)combinar(.*)|(.*)fusionar(.*)documentos(.*)|(.*)archivos(.*)|(.*)pdf(.*)|(.*)word(.*)",                                       
    ["La función para fusionar archivos PDF o Word en SharpPixAI está en desarrollo."]),

    (r"(.*)edita(.*)app(.*)", 
    ["Actualmente, SharpPixAI no permite editar archivos dentro de la plataforma, pero podés descargarlos, editarlos y volver a subirlos."]),

    (r"(.*)protege(.*)|(.*)encripta(.*)contraseña(.*)", 
    ["SharpPixAI no cuenta con opciones para encriptar archivos en este momento."]),

    (r"(.*)garnti(.*)segur(.*)",                                                                           
    ["SharpPixAI garantiza alta seguridad y cumplimiento de normativas."]),

    (r"(.*)audita(.*)|(.*)acceso(.*)|(.*)cambio(.*)",                                                               
    ["SharpPixAI ofrece herramientas para auditar el acceso y los cambios en los archivos."]),

    (r"(.*)PDF(.*)extrae(.*)",                                                                
    ["La función para extraer contenido visual de archivos PDF en SharpPixAI está en desarrollo."]),



    (r"(.*)", ["No estoy seguro de entenderte, ¿puedes reformularlo?"])
]

#  Forzar normalización
class ChatNormalizado(Chat):
    def respond(self, input_text):
        input_text = normalizar_texto(input_text)  # Normaliza ANTES de comparar
        return super().respond(input_text)

chatbot = ChatNormalizado(pairs, reflections)

def iniciar_chat():
    print("Hola, ¿en qué puedo ayudarte?")
    while True:
        entrada_usuario = input("> ")  # Se pasa el texto sin normalizar
        respuesta = chatbot.respond(entrada_usuario)  
        print(respuesta)

if __name__ == "__main__":
    iniciar_chat()
