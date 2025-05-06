## Motivación

En los entornos empresariales modernos, la integridad y disponibilidad de los datos son críticas para la continuidad operativa y el cumplimiento normativo. Este proyecto ofrece una solución de backup automatizada y cifrada que comprime una carpeta objetivo, la cifra usando Fernet y la sube a Google Drive. Esto garantiza que los datos sensibles estén seguros en tránsito y en reposo, al tiempo que permite una restauración sencilla cuando sea necesario.

## Inicio Rápido

### Prerrequisitos

- Python 3.7 o superior  
- Un proyecto en Google Cloud con la API de Drive habilitada  
- `client_secrets.json` desde la Consola de Google Cloud  

### Instalación

1. Clona el repositorio:  
   ```bash
   git clone https://github.com/acasmor0802/proyecto-digi.git
   ```
2. Crea y activa un entorno virtual
   ```bash
    python -m venv venv
    venv\Scripts\activate
   ```
3. Instala las dependencias necesarias:
   ```bash
    pip install -r requirements.txt
   ```
4. Asegúrate de colocar tu archivo `client_secrets.json` dentro del directorio `src/`.
   Este archivo contiene las credenciales de Google necesarias para subir los respaldos a Google Drive.

### Ejecución

Desde la raíz del proyecto, navega al directorio src y ejecuta el script principal:
   ```bash
    cd src
    python digi.py
   ```
Esto iniciará el proceso de copia de seguridad, cifrado y subida automática a Google Drive.
