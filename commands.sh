docker-compose up -d # up containers with docker-compose
docker-compose down  # down containers 
docker-compose down --volumes --remove-orphans

docker-compose up --build # modificar los archivos de la aplicación localmente y ver los cambios reflejados sin necesidad de reconstruir los contenedores