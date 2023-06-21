docker-compose up -d # up containers with docker-compose
docker-compose down  # down containers 
docker-compose down --volumes --remove-orphans

 # modificar los archivos de la aplicación localmente y ver los
 # cambios reflejados sin necesidad de reconstruir los contenedores
docker-compose up --build

# información sobre posibles problemas dentro del contenedor
docker logs docker-compose-crud-web
docker logs docker-compose-crud-db