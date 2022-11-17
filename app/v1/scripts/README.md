Para adregar las tablas a postgresql primero cree la base de datos en postgresql posterior a esto en un archivo con nombre ".env" agregue las siguientes lineas de codigo:

DB_NAME = "Nombre de la base de datos"
DB_USER = "Usuario de postgresql"
DB_PASS = "Clave de postgresql"
DB_HOST = "Host de postgresql"
DB_PORT = "Puerto de postgresql"

Por su seguridad agregue a ".env" a su ".gitignore"

Posterior a esto ejecute los siguientes comandos:

from app.v1.scripts.create_tables import create_tables
create_tables()