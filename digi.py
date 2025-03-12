import os
import zipfile
from cryptography.fernet import Fernet
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# ----------------------- CONFIGURACIÓN ------------------------
FOLDER_TO_BACKUP = "./mi_carpeta"  # Ruta de la carpeta a respaldar
BACKUP_FOLDER = "./backups"  # Carpeta donde se guardarán las copias comprimidas
MAX_BACKUPS = 5  # Número máximo de copias de seguridad a conservar
ENCRYPTION_KEY = Fernet.generate_key()  # Genera una clave para cifrar los archivos
fernet = Fernet(ENCRYPTION_KEY)

# -------------------- FUNCIONES PRINCIPALES -------------------
def create_backup(folder_path, backup_folder):
    """Crea un archivo zip de la carpeta y lo cifra."""
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    
    zip_filename = os.path.join(backup_folder, "backup.zip")
    encrypted_filename = os.path.join(backup_folder, "backup_encrypted.zip")
    
    # Crear el archivo zip
    with zipfile.ZipFile(zip_filename, 'w') as backup_zip:
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                backup_zip.write(file_path, os.path.relpath(file_path, folder_path))
    
    # Cifrar el archivo zip
    with open(zip_filename, 'rb') as file:
        encrypted_data = fernet.encrypt(file.read())
    
    with open(encrypted_filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    
    os.remove(zip_filename)  # Eliminar el archivo zip sin cifrar
    print(f"Backup creado y cifrado: {encrypted_filename}")
    return encrypted_filename

def upload_to_google_drive(file_path):
    """Sube el archivo cifrado a Google Drive."""
    client_secrets_path = 'client_secrets.json'
    
    if not os.path.exists(client_secrets_path):
        print(f"Error: No se encontró el archivo '{client_secrets_path}'. Por favor, colócalo en el directorio del script.")
        return
    
    gauth = GoogleAuth()
    gauth.CommandLineAuth()  # Cambiado para evitar problemas con localhost:8080
    drive = GoogleDrive(gauth)
    
    file = drive.CreateFile({'title': os.path.basename(file_path)})
    file.SetContentFile(file_path)
    file.Upload()
    print(f"Archivo subido a Google Drive: {file_path}")

def manage_backup_history(backup_folder):
    """Elimina las copias de seguridad más antiguas si se supera el límite."""
    backups = sorted(
        [os.path.join(backup_folder, f) for f in os.listdir(backup_folder)], 
        key=os.path.getctime
    )
    
    while len(backups) > MAX_BACKUPS:
        oldest_backup = backups.pop(0)
        os.remove(oldest_backup)
        print(f"Backup eliminado: {oldest_backup}")

# ------------------------ EJECUCIÓN --------------------------
if __name__ == "__main__":
    print("Iniciando proceso de copia de seguridad...")
    backup_file = create_backup(FOLDER_TO_BACKUP, BACKUP_FOLDER)
    upload_to_google_drive(backup_file)
    manage_backup_history(BACKUP_FOLDER)
    print("Proceso de copia de seguridad completado.")
    print(f"Tu clave de seguridad para el backip es: {ENCRYPTION_KEY}")
