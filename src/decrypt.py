import os
import zipfile
from cryptography.fernet import Fernet

# ----------------------- CONFIGURACIÓN ------------------------

# Solicitar al usuario que introduzca la clave de cifrado
user_input_key = input("Introduce tu clave de cifrado: ")
ENCRYPTION_KEY = user_input_key.encode()  # Convertir la clave de texto a bytes
fernet = Fernet(ENCRYPTION_KEY)

# -------------------- FUNCIONES PRINCIPALES -------------------
def decrypt_file(encrypted_file_path, decrypted_file_path):
    """Descifra el archivo cifrado."""
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    
    print(f"Archivo descifrado: {decrypted_file_path}")

def unzip_file(zip_file_path, extract_to_folder):
    """Descomprime el archivo ZIP."""
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_folder)
    print(f"Archivos descomprimidos en: {extract_to_folder}")

# ------------------------ EJECUCIÓN --------------------------
if __name__ == "__main__":
    encrypted_file_path = './backups/backup_encrypted.zip'  # Ruta del archivo cifrado
    decrypted_file_path = './backups/backup.zip'  # Ruta donde se guardará el archivo descifrado
    extract_to_folder = './extracted_files'  # Carpeta donde se descomprimirán los archivos

    # Asegúrate de que la carpeta de extracción exista
    if not os.path.exists(extract_to_folder):
        os.makedirs(extract_to_folder)

    decrypt_file(encrypted_file_path, decrypted_file_path)
    unzip_file(decrypted_file_path, extract_to_folder)
