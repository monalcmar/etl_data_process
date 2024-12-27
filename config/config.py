import os
from dotenv import load_dotenv
from pathlib import Path

# Cargar las variables de entorno desde el archivo .env
dotenv_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path)

# Asignar las credenciales a variables
db_user = os.getenv('DATABASE_USER')
db_password = os.getenv('DATABASE_PASSWORD')
db_host = os.getenv('DATABASE_HOST')
db_name = os.getenv('DATABASE_NAME')
# db_schema = os.getenv('DATABASE_SCHEMA')
