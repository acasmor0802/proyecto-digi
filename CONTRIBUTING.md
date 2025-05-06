# Cómo contribuir

¡Gracias por tu interés en mejorar este proyecto de backups cifrados en formato ZIP con subida automática a Google Drive! Este documento describe cómo puedes colaborar con el código, reportar errores o proponer mejoras. Asegúrate de leerlo con atención para entender el proceso de contribución.

## Proceso de Contribución

Para contribuir al código, sigue estos pasos generales:

- **Haz un fork** del repositorio oficial en GitHub para tener tu copia personal.  
- **Clona tu fork** en tu máquina local (`git clone <tu-fork-url>`).  
- **Crea una rama (branch)** para tus cambios (`git checkout -b mi-nueva-funcionalidad`), con un nombre descriptivo.  
- **Realiza cambios** en esa rama siguiendo el estilo de código del proyecto. Asegúrate de probar y que tu código funcione correctamente.  
- **Agrega y haz commit** de tus cambios con mensajes claros y concisos (por ejemplo, “Añadir soporte para múltiples carpetas” o “Corregir error en cifrado de archivos”).  
- **Envía (push)** tu rama con los commits a tu repositorio remoto en GitHub (`git push origin mi-nueva-funcionalidad`).  
- **Abre un Pull Request (PR)** desde tu rama en tu fork hacia la rama principal (`main`) del proyecto original. En el PR, describe detalladamente los cambios que propones y por qué son útiles.  

Los mantenedores revisarán tu PR. Pueden pedirte cambios o mejoras antes de fusionarlo. Por favor responde amablemente a los comentarios y mantén el PR actualizado con nuevos commits si es necesario. Cuando tu PR sea aceptado, se integrará en el proyecto. 

## Estilo de Código

La consistencia del código es fundamental. Este proyecto sigue las convenciones de estilo de Python (PEP 8). Se recomienda usar herramientas como:

- **Black**: formateador automático (`black .`)
- **Flake8**: analizador estático (`flake8`)

Escribe nombres de variables, funciones y clases de manera descriptiva. Usa comentarios y docstrings explicativos en funciones nuevas.

## Reportar errores y sugerir mejoras

Usa la sección de *Issues* del repositorio para:

1. **Buscar si ya existe** un issue similar.
2. **Abrir uno nuevo** con título claro y descripción detallada.
3. Etiquetar como “bug” o “enhancement” si tienes permisos.

Sigue el código de conducta y mantén una comunicación respetuosa.

## Ideas para ampliar el proyecto

Algunas ideas de mejora:

- Soporte para múltiples carpetas.
- Archivo de configuración JSON/YAML.
- Interfaz web (Streamlit, Flask).
- Subida a otros servicios (Dropbox, S3, etc.).
- Notificaciones al finalizar backup.
- Backups incrementales.
- Tareas programadas internas.

Si tienes otras ideas, abre un issue o propón un PR.

## Agradecimientos

¡Gracias por tu interés en contribuir! Este proyecto mejora gracias a colaboradores como tú. Si tienes preguntas, abre un issue o contacta a los mantenedores.
