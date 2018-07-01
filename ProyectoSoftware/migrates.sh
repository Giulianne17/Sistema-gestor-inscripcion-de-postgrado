# Borrar la base de datos anterior
rm -r db.sqlite3 InscripcionPostgrado/migrations

# Crear script de migrates
python3 manage.py makemigrations InscripcionPostgrado

# Realizar migraciones
python3 manage.py migrate

# Cargar elementos a la base de datos
python3 manage.py shell -c "from script import *;addtoDB()"