# DEVELOPER.md

This document explains the internals of the backup/encrypt/upload tool (`digi.py`) and its companion decryptor (`decrypt.py`).

---

## 🔧 Technologies & Libraries

- **Python 3.x**  
- **zipfile** — ZIP compression  
- **cryptography.fernet** — AES-based symmetric encryption  
- **PyDrive2** — Google Drive API client  
- **os, shutil, logging** — filesystem operations & logging  

---

## 🚀 Workflow Overview

### 1. `digi.py` (Backup & Upload)

1. **Configuration**  
   - `FOLDER_TO_BACKUP` (hardcoded or via env var)  
   - `BACKUP_FOLDER` (./backups)  
   - `MAX_BACKUPS` (5)  
   - `client_secrets.json` for Drive auth  

2. **`create_backup()`**  
   - Walks the folder tree of `FOLDER_TO_BACKUP`  
   - Packs into `backup.zip` in `BACKUP_FOLDER`  
   - Encrypts with a newly generated Fernet key  
   - Writes `backup_encrypted.zip`, deletes the plaintext ZIP  

3. **`upload_to_google_drive()`**  
   - Authenticates via `PyDrive2` using `client_secrets.json`  
   - Uploads `backup_encrypted.zip` to your Drive  

4. **`manage_backup_history()`**  
   - Lists all files in `BACKUP_FOLDER`  
   - Keeps newest `MAX_BACKUPS`, deletes older  

5. **Output**  
   - Prints progress and final Fernet key to STDOUT  
   - Encrypted files live in `backups/` and on Drive  

### 2. `decrypt.py` (Decrypt & Extract)

1. Prompts for **the same** Fernet key used in `digi.py`.  
2. Reads `backups/backup_encrypted.zip`, decrypts to `backups/backup.zip`.  
3. Extracts `backup.zip` into `extracted_files/`.  
4. Prints confirmation messages.

---

## 🔐 Security Notes

- **Keep your Fernet key secret** — do NOT commit it.  
- Protect `client_secrets.json` (`chmod 600`).  
- The key printed by `digi.py` should be captured and stored securely (e.g., vault).

---

## 🧪 Usage

```bash
# Run a backup & upload
python src/digi.py

# Decrypt & extract
python src/decrypt.py