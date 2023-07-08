docker-compose up -d # up containers with docker-compose
docker-compose down  # down containers 
docker-compose down --volumes --remove-orphans

 # modificar los archivos de la aplicación localmente y ver los
 # cambios reflejados sin necesidad de reconstruir los contenedores
docker-compose up --build

# información sobre posibles problemas dentro del contenedor
docker logs docker-compose-crud-web
docker logs docker-compose-crud-db

# ejecutar shell en contenedor web
docker exec -it docker-compose-crud-web bash

# Para inicializar Alembic, ejecuta este comando:
docker-compose exec docker-compose-crud-web alembic init alembic

# Para copiar archivos alembic desde el contenedor a la máquina local 
docker cp docker-compose-crud-web:/alembic ./alembic
docker cp docker-compose-crud-web:/alembic.ini ./alembic.ini

# Generación de una migración
docker-compose exec web alembic revision --autogenerate -m "Added new column"
#Aplicar las migraciones
docker-compose exec web alembic upgrade head -x


# ejecutar comandos en bash del container
docker-compose exec web bash -c "alembic revision --autogenerate -m 'Added new column to users table'"



# Display the current revision for a database: 
alembic current
# View migrations history: 
alembic history --verbose
# Revert all migrations:
alembic downgrade base
# Revert migrations one by one: 
alembic downgrade -1
# Apply all migrations:
alembic upgrade head
# Apply migrations one by one: 
alembic upgrade +1
# Display all raw SQL: 
alembic upgrade head --sql
# Reset the database: 
alembic downgrade base && alembic upgrade head