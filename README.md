## Motivation

In modern business environments, data integrity and availability are critical for operational continuity and regulatory compliance. This project provides an automated and encrypted backup solution that compresses a target folder, encrypts it using Fernet, and uploads it to Google Drive. This ensures that sensitive data is secure both in transit and at rest, while allowing for easy restoration when needed.

## Quick Start

### Prerequisites

- Python 3.7 or higher  
- A Google Cloud project with the Drive API enabled  
- `client_secrets.json` downloaded from the Google Cloud Console  

### Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/acasmor0802/proyecto-digi.git
   ```
2. Create and activate a virtual environment:
   ```bash
    python -m venv venv
    venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
    pip install -r requirements.txt
   ```
4. Make sure to place your `client_secrets.json` file inside the `src/` directory.
This file contains the necessary Google credentials to upload the backups to Google Drive.

### Execution
From the project root, navigate to the src directory and run the main script:
   ```bash
    cd src
    python digi.py
   ```
This will start the backup process, including encryption and automatic upload to Google Drive.

## 📄 Licencia

Este proyecto está licenciado bajo los términos de la [Licencia MIT](./LICENSE).
