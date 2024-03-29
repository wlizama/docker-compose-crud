FROM python:3.9

WORKDIR /docker-compose-crud

COPY requirements.txt .

RUN pip install -r requirements.txt

# Agregar estas líneas para exponer el puerto 5003 y establecer la variable de entorno FLASK_RUN_PORT
EXPOSE 5003
ENV FLASK_RUN_PORT=5003
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=dc-crud-db
ENV POSTGRES_HOST=host.docker.internal
ENV POSTGRES_PORT=5432
ENV PYTHONPATH=/docker-compose-crud
ENV FLASK_APP=run:create_app

COPY . .

CMD ["python", "run.py", "--host=0.0.0.0"]