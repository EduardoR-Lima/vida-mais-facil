from bcrypt import hashpw
from bcrypt import checkpw
from bcrypt import gensalt

_DEFAULT_ENCODING = 'utf-8'

def generate_password_hash(password: str):
    """
    Produz e retorna o hash da senha fornecida

    :param password:
        `str` contendo a senha que será utilizada para produzir o hash
    """
    pw_bytes = password.encode(_DEFAULT_ENCODING)
    salt = gensalt(rounds=12)

    return hashpw(pw_bytes, salt).decode(_DEFAULT_ENCODING)

def verify_password(hashed_password: str, password: str):
    """
    Retorna verdadeiro ou falso a depender se a senha fornecida
    corresponde ao hash informado

    :param hashed_password:
        `str` contendo o hash da senha que será comparada

    :param password:
        `str` contendo a senha que será comparada
    """
    h_bytes = hashed_password.encode(_DEFAULT_ENCODING)
    pw_bytes = password.encode(_DEFAULT_ENCODING)

    return checkpw(pw_bytes, h_bytes)
