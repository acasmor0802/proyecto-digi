## Criterio 6a) Objetivos estratégicos

**¿Qué objetivos estratégicos específicos de la empresa aborda tu software?**  
- **Continuidad de negocio**: Garantiza que siempre exista una copia recuperable de datos críticos (documentación, bases de datos, configuraciones).  
- **Seguridad de la información**: Protege los backups mediante cifrado simétrico fuerte (Fernet), reduciendo riesgo de filtraciones.  
- **Automatización de procesos**: Elimina tareas manuales de archivado y envío, liberando recursos internos.  

**¿Cómo se alinea el software con la estrategia general de digitalización?**  
- Facilita la transición de procesos de respaldo manuales (papel, discos físicos) a un flujo 100 % digitalizado y reproducible por cron/CI.  
- Conecta con servicios Cloud (Google Drive), alineándose con la adopción de infraestructuras en la nube.  

---

## Criterio 6b) Áreas de negocio y comunicaciones

**¿Qué áreas de la empresa (producción, negocio, comunicaciones) se ven más beneficiadas con tu software?**  
- **Producción / TI**: Hostings, servidores y aplicaciones disponen de copias diarias automáticas.  
- **Negocio / Operaciones**: Equipos de soporte recuperan rápidamente datos en caso de fallo.  
- **Comunicaciones / Compliance**: Se genera registro de actividad (logs), facilitando auditorías y reportes.  

**¿Qué impacto operativo esperas en las operaciones diarias?**  
- Reducción de incidencias por pérdida de datos; mayor rapidez en recuperación (RTO).  
- Menor carga de trabajo en tareas repetitivas de backup, permitiendo al equipo centrarse en mejoras o desarrollo.  

---

## Criterio 6c) Áreas susceptibles de digitalización

**¿Qué áreas de la empresa son más susceptibles de ser digitalizadas con tu software?**  
- **Gestión documental**: archivos de texto, facturas, contratos.  
- **Configuraciones de sistemas**: archivos de configuración de servidores, scripts de despliegue.  

**¿Cómo mejorará la digitalización las operaciones en esas áreas?**  
- Acceso centralizado y versionado implícito gracias al timestamp en los backups.  
- Trazabilidad y recuperación automática sin intervención manual.  

---

## Criterio 6d) Encaje de áreas digitalizadas (AD)

**¿Cómo interactúan las áreas digitalizadas con las no digitalizadas?**  
- Los datos digitalizados (backups cifrados) pueden compartirse con departamentos no técnicos mediante Google Drive.  
- El flujo manual (por ejemplo, firmar impresiones) se ve limitado a casos de excepción, acelerando procesos.  

**¿Qué soluciones o mejoras propondrías para integrar estas áreas?**  
- Portal web interno donde usuarios no técnicos consulten backups antiguos (previo descifrado con roles).  
- Notificaciones automáticas (email/Slack) tras cada backup, integradas en los canales de comunicación existentes.  

---

## Criterio 6e) Necesidades presentes y futuras

**¿Qué necesidades actuales de la empresa resuelve tu software?**  
- Protección contra borrados accidentales o ataques ransomware.  
- Almacenamiento externo (Cloud) para catástrofes in situ (incendio, robo).  

**¿Qué necesidades futuras aborda?**  
- Escalabilidad a múltiples carpetas/proyectos.  
- Integración con otros proveedores cloud (AWS S3, Azure Blob) vía adaptadores.  

---

## Criterio 6f) Relación con tecnologías

**¿Qué tecnologías habilitadoras has empleado y cómo impactan en las áreas de la empresa?**  
- **Fernet (Cryptography)**: cifrado simétrico fuerte, aporta confidencialidad sin complejidad.  
- **PyDrive / Google Drive API**: facilita almacenamiento remoto, elimina infraestructura local de backup.  
- **Python + zipfile + argparse**: scripting sencillo y portable.  

**¿Qué beneficios específicos aporta la implantación de estas tecnologías?**  
- **Seguridad**: cifrado de extremo a extremo.  
- **Disponibilidad**: datos accesibles globalmente.  
- **Mantenibilidad**: código Python ampliamente soportado.  

---

## Criterio 6g) Brechas de seguridad

**¿Qué posibles brechas de seguridad podrían surgir al implementar tu software?**  
- **Exposición de la clave**: si se guarda sin permisos, un tercero podría descifrar backups.  
- **Acceso no autorizado a Drive**: si las credenciales OAuth se filtran.  
- **Riesgo de script injection**: ejecutar sin validar rutas o nombres de fichero.  

**¿Qué medidas concretas propondrías para mitigarlas?**  
- Almacenar la clave en un vault o fichero con `chmod 600`, nunca en repositorio.  
- Usar service account con permisos mínimos y rotación periódica de credenciales.  
- Validar y sanear rutas; no usar `os.system` ni comandos dinámicos.  

---

## Criterio 6h) Tratamiento de datos y análisis

**¿Cómo se gestionan los datos en tu software y qué metodologías utilizas?**  
- Lectura/escritura en bloque de los ZIP cifrados, sin procesar contenido interno.  
- Logs de operaciones (fecha, éxito/fracaso, rutas) que luego pueden analizarse.  

**¿Qué haces para garantizar la calidad y consistencia de los datos?**  
- Comprobación de integridad: al extraer, validar que `zipfile` no arroje excepciones y el número de archivos coincide con el listado.  
- Versionado con timestamps: evita sobrescrituras accidentales.  
- (Futuro) Añadir hashes (SHA-256) antes y después de cifrar para detectar corrupción.  
