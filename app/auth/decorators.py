from functools import wraps
from flask_jwt_extended import jwt_required
from extensions import api

def jwt_and_doc(func):
    @api.doc(security='Bearer')
    @jwt_required()
    @wraps(func)
    def decorated(*args, **kwargs):
        return func(*args, **kwargs)
    return decorated