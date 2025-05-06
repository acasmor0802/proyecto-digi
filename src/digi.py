import os  # Importing the os module for interacting with the operating system
import zipfile  # Importing the zipfile module for creating and handling ZIP files
from cryptography.fernet import Fernet  # Importing Fernet for encryption and decryption
from pydrive.auth import GoogleAuth  # Importing GoogleAuth for Google Drive authentication
from pydrive.drive import GoogleDrive  # Importing GoogleDrive for file management on Google Drive

# ----------------------- CONFIGURATION ------------------------
FOLDER_TO_BACKUP = "./mi_carpeta"  # Path of the folder to back up
BACKUP_FOLDER = "./backups"  # Folder where compressed backups will be stored
MAX_BACKUPS = 5  # Maximum number of backups to keep
ENCRYPTION_KEY = Fernet.generate_key()  # Generates a key for encrypting files
fernet = Fernet(ENCRYPTION_KEY)  # Initializes a Fernet object with the generated key

# -------------------- MAIN FUNCTIONS -------------------
def create_backup(folder_path, backup_folder):
    """
    Creates a zip file of the specified folder and encrypts it.

    @param {str} folder_path - The path of the folder to back up.
    @param {str} backup_folder - The folder where the backup will be stored.
    @return {str} - The path of the encrypted backup file.
    @raises OSError: If there is an error creating the backup folder or ZIP file.
    """
    if not os.path.exists(backup_folder):  # Check if the backup folder exists
        os.makedirs(backup_folder)  # Create the backup folder if it doesn't exist
    
    zip_filename = os.path.join(backup_folder, "backup.zip")  # Define the name for the ZIP file
    encrypted_filename = os.path.join(backup_folder, "backup_encrypted.zip")  # Define the name for the encrypted file
    
    # Create the zip file
    with zipfile.ZipFile(zip_filename, 'w') as backup_zip:  # Open a new ZIP file for writing
        for foldername, subfolders, filenames in os.walk(folder_path):  # Walk through the folder
            for filename in filenames:  # Iterate over all files
                file_path = os.path.join(foldername, filename)  # Get the full file path
                backup_zip.write(file_path, os.path.relpath(file_path, folder_path))  # Write the file to the ZIP archive
    
    # Encrypt the zip file
    with open(zip_filename, 'rb') as file:  # Open the ZIP file in binary read mode
        encrypted_data = fernet.encrypt(file.read())  # Encrypt the contents of the ZIP file
    
    with open(encrypted_filename, 'wb') as encrypted_file:  # Open a new file for writing the encrypted data
        encrypted_file.write(encrypted_data)  # Write the encrypted data to the file
    
    os.remove(zip_filename)  # Remove the unencrypted ZIP file
    print(f"Backup created and encrypted: {encrypted_filename}")  # Print confirmation message
    return encrypted_filename  # Return the path of the encrypted file

def upload_to_google_drive(file_path):
    """
    Uploads the encrypted backup file to Google Drive.

    @param {str} file_path - The path of the encrypted file to upload.
    @raises FileNotFoundError: If the client secrets file is not found.
    @raises Exception: If there is an error during the upload process.
    """
    client_secrets_path = 'client_secrets.json'  # Path to the client secrets JSON file
    
    if not os.path.exists(client_secrets_path):  # Check if the client secrets file exists
        raise FileNotFoundError(f"Error: '{client_secrets_path}' not found. Please place it in the script directory.")
    
    gauth = GoogleAuth()  # Create a GoogleAuth instance
    gauth.CommandLineAuth()  # Authenticate using command line (avoids localhost issues)
    drive = GoogleDrive(gauth)  # Create a GoogleDrive instance with authenticated credentials
    
    file = drive.CreateFile({'title': os.path.basename(file_path)})  # Create a new file in Google Drive
    file.SetContentFile(file_path)  # Set the content of the file to be uploaded
    file.Upload()  # Upload the file to Google Drive
    print(f"File uploaded to Google Drive: {file_path}")  # Print confirmation message
    
def manage_backup_history(backup_folder):
    """
    Manages the backup history by removing older backups if the limit is exceeded.

    @param {str} backup_folder - The folder where backups are stored.
    @raises OSError: If there is an error deleting backup files.
    """
    backups = sorted(  # Get a sorted list of backup files by creation time
        [os.path.join(backup_folder, f) for f in os.listdir(backup_folder)], 
        key=os.path.getctime
    )
    
    while len(backups) > MAX_BACKUPS:  # Check if the number of backups exceeds the maximum allowed
        oldest_backup = backups.pop(0)  # Remove the oldest backup from the list
        os.remove(oldest_backup)  # Delete the oldest backup file
        print(f"Backup deleted: {oldest_backup}")  # Print confirmation message

# ------------------------ EXECUTION --------------------------
if __name__ == "__main__":  # Check if the script is being run directly
    print("Iniciando proceso de copia de seguridad...")  # Print starting message
    backup_file = create_backup(FOLDER_TO_BACKUP, BACKUP_FOLDER)  # Create a backup
    upload_to_google_drive(backup_file)  # Upload the backup to Google Drive
    manage_backup_history(BACKUP_FOLDER)  # Manage the backup history
    print("Proceso de copia de seguridad completado.")  # Print completion message
    print(f"Tu clave de seguridad para el backup es: {ENCRYPTION_KEY}")  # Print the encryption key