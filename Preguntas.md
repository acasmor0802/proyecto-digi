# Respuestas Proyecto 2: Automatización de copias de seguridad en la nube

## Ciclo de vida del dato (5b)
**1. ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?**  
Los datos pasan por varias etapas: primero se generan las copias de seguridad comprimiendo y cifrando la carpeta seleccionada. Luego, el archivo cifrado se sube a Google Drive. Para evitar que se acumulen demasiadas copias, el script elimina automáticamente las más antiguas cuando se supera el límite definido (cinco backups).  

**2. ¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?**  
Verifico que el archivo comprimido y cifrado se cree correctamente antes de subirlo a la nube. Uso una clave de cifrado única para proteger los datos, lo que evita que puedan ser alterados o leídos sin autorización.  

**3. Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?**  
Como el proyecto ya trabaja con datos, una mejora podría ser añadir un historial detallado de los respaldos o notificaciones automáticas en caso de errores.  

---

## Almacenamiento en la nube (5f)
**1. Si tu software utiliza almacenamiento en la nube, ¿cómo garantizas la seguridad y disponibilidad de los datos?**  
La seguridad se garantiza cifrando los archivos antes de subirlos a Google Drive. La disponibilidad está asegurada por la infraestructura de Google Drive, que ofrece alta redundancia y acceso constante.  

**2. ¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual?**  
Consideré usar AWS S3 o Dropbox, pero elegí Google Drive porque es fácil de integrar con Python y ofrece almacenamiento gratuito para usuarios individuales.  

**3. Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?**  
En futuras versiones podría agregar soporte para servicios como AWS S3 o Azure Blob Storage, especialmente para entornos más empresariales.  

---

## Seguridad y regulación (5i)
**1. ¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?**  
La principal medida es el cifrado de los archivos antes de subirlos a la nube, lo que garantiza que nadie pueda leerlos sin la clave de cifrado. Además, la autenticación de Google asegura que solo el usuario autorizado puede acceder a los archivos.  

**2. ¿Qué normativas podrían afectar el uso de tu software y cómo las has tenido en cuenta?**  
El Reglamento General de Protección de Datos (GDPR) es una normativa clave si se gestionan datos personales. Aunque este proyecto no procesa datos sensibles, si lo hiciera, el usuario tendría control sobre sus datos y podría eliminarlos fácilmente.  

**3. ¿Qué riesgos potenciales identificas y cómo los abordarías en el futuro?**  
Un riesgo importante es la pérdida de la clave de cifrado, lo que haría imposible recuperar los datos. Una solución sería almacenar la clave de forma segura en servicios como AWS Secrets Manager o Vault.  

---

## Implicación de las THD en negocio y planta (2e)
**1. ¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial?**  
Este software automatiza la creación de copias de seguridad para sistemas críticos, reduciendo el riesgo de pérdida de datos y liberando tiempo para otras tareas importantes.  

**2. ¿Cómo podría mejorar procesos operativos o la toma de decisiones?**  
Facilita la recuperación rápida de datos en caso de fallos y asegura que siempre haya respaldos actualizados, lo que mejora la continuidad del negocio y la toma de decisiones basada en datos recientes.  

**3. Si no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?**  
Este software sería útil para pequeñas empresas, profesionales independientes y usuarios particulares que quieran proteger sus documentos importantes de forma automática.  

---

## Mejoras en IT y OT (2f)
**1. ¿Cómo puede tu software facilitar la integración entre entornos IT y OT?**  
Podría servir como puente para proteger datos generados por dispositivos OT (como logs o configuraciones), haciéndolos accesibles para su análisis en entornos IT.  

**2. ¿Qué procesos específicos podrían beneficiarse en términos de automatización o eficiencia?**  
Procesos de almacenamiento de datos históricos, respaldo de configuraciones de dispositivos IoT y protección de logs operativos a largo plazo.  

**3. Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos?**  
Se podría adaptar para sincronizar información directamente desde dispositivos IoT y hacer respaldos automáticos en la nube.  

---

## Tecnologías Habilitadoras Digitales (THD) (2g)
**1. ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?**  
Las principales tecnologías utilizadas son **Cloud Computing** (Google Drive) y **cifrado de datos** para proteger la información. Además, la **automatización de procesos** es clave en este proyecto.  

**2. ¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software?**  
El almacenamiento en la nube asegura que las copias de seguridad estén siempre accesibles, el cifrado protege la confidencialidad de los datos y la automatización reduce el trabajo manual.  

**3. Si no has utilizado THD, ¿cómo podrías implementarlas para enriquecer tu solución?**  
Podría integrar Machine Learning para anticipar posibles fallos o recomendar acciones, como eliminar archivos duplicados o comprimir más datos.  
