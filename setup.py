import os
import subprocess

# Nome do ambiente virtual que será criado
VENV_NAME = "venv"

# Caminho para o arquivo requirements.txt
REQ_FILE = "requirements.txt"

# Comando para criar o ambiente virtual
CREATE_CMD = f"python -m venv {VENV_NAME}"

# Comando para ativar o ambiente virtual
ACTIVATE_CMD = f"source {VENV_NAME}/bin/activate"

# Comando para instalar os pacotes listados no arquivo requirements.txt
INSTALL_CMD = f"pip install -r {REQ_FILE}"

# Cria o ambiente virtual
subprocess.run(CREATE_CMD.split())

# Ativa o ambiente virtual
os.system(ACTIVATE_CMD)

# Instala os pacotes listados no arquivo requirements.txt
subprocess.run(INSTALL_CMD.split())
