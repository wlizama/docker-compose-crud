from users.model import Base
from users.services import createUser, getAllUsers, updateUser, deleteUser
from db import engine

# Crea todas las tablas definidas en el Base
Base.metadata.create_all(engine)

# Operaciones de prueba
# crear_usuario('Juan', 'juan@example.com')
# usuarios = obtener_usuarios()
# print(usuarios)

# actualizar_usuario('Juan', 'Pedro')
# borrar_usuario('Pedro')
