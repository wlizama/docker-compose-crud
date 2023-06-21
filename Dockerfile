FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

# Agregar estas líneas para exponer el puerto 5001 y establecer la variable de entorno FLASK_RUN_PORT
EXPOSE 5003
ENV FLASK_RUN_PORT=5003

COPY . .

CMD ["python", "main.py"]
