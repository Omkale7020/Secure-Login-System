from flask_bcrypt import Bcrypt
from models import create_user, get_user

bcrypt = Bcrypt()

def register_user(username, password):
    hashed = bcrypt.generate_password_hash(password).decode('utf-8')
    create_user(username, hashed)

def login_user(username, password):
    user = get_user(username)
    if user and bcrypt.check_password_hash(user["password"], password):
        return True
    return False