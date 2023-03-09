#!/bin/bash

# Criar um ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate

python3 -m pip install --upgrade pip

# Instalar as dependências do requirements.txt
pip install -r requirements.txt

# Desativar o ambiente virtual
deactivate