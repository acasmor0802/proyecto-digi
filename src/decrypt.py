import os  # Importing the os module for interacting with the operating system
import zipfile  # Importing the zipfile module for handling ZIP files
from cryptography.fernet import Fernet  # Importing Fernet for encryption and decryption

# ----------------------- CONFIGURATION ------------------------

# Prompt the user to enter the encryption key
user_input_key = input("Introduce tu clave de cifrado: ")  # Request the encryption key from the user
ENCRYPTION_KEY = user_input_key.encode()  # Convert the string key to bytes
fernet = Fernet(ENCRYPTION_KEY)  # Initialize a Fernet object with the provided key

# -------------------- MAIN FUNCTIONS -------------------
def decrypt_file(encrypted_file_path, decrypted_file_path):
    """
    Decrypts the encrypted file.

    @param {str} encrypted_file_path - The path of the encrypted file to be decrypted.
    @param {str} decrypted_file_path - The path where the decrypted file will be saved.
    @raises InvalidToken: If the provided key is invalid or the file is corrupted.
    """
    with open(encrypted_file_path, 'rb') as encrypted_file:  # Open the encrypted file in binary read mode
        encrypted_data = encrypted_file.read()  # Read the encrypted data
    
    decrypted_data = fernet.decrypt(encrypted_data)  # Decrypt the data using the Fernet object
    
    with open(decrypted_file_path, 'wb') as decrypted_file:  # Open a new file for writing the decrypted data
        decrypted_file.write(decrypted_data)  # Write the decrypted data to the file
    
    print(f"Archivo descifrado: {decrypted_file_path}")  # Print confirmation message

def unzip_file(zip_file_path, extract_to_folder):
    """
    Extracts the contents of the specified ZIP file.

    @param {str} zip_file_path - The path of the ZIP file to extract.
    @param {str} extract_to_folder - The folder where the files will be extracted.
    @raises FileNotFoundError: If the ZIP file does not exist.
    """
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:  # Open the ZIP file for reading
        zip_ref.extractall(extract_to_folder)  # Extract all contents to the specified folder
    print(f"Archivos descomprimidos en: {extract_to_folder}")  # Print confirmation message

# ------------------------ EXECUTION --------------------------
if __name__ == "__main__":  # Check if the script is being run directly
    encrypted_file_path = './backups/backup_encrypted.zip'  # Path to the encrypted file
    decrypted_file_path = './backups/backup.zip'  # Path where the decrypted file will be saved
    extract_to_folder = './extracted_files'  # Folder where the files will be extracted

    # Ensure that the extraction folder exists
    if not os.path.exists(extract_to_folder):  # Check if the extraction folder exists
        os.makedirs(extract_to_folder)  # Create the extraction folder if it doesn't exist

    decrypt_file(encrypted_file_path, decrypted_file_path)  # Call the function to decrypt the file
    unzip_file(decrypted_file_path, extract_to_folder)  # Call the function to unzip the decrypted file
