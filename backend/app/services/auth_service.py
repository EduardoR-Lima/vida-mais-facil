from typing import Optional
import datetime as dt

import jwt

from .exceptions import EntityNotFoundError
from .exceptions.auth import InvalidCredentialsError
from .cliente_service import ClienteService
from ..utils.security import verify_password
from ..models import Cliente
from ..config import settings

class AuthService:
    """
    Classe para representar a lógica de negócio voltada ao processo de
    autenticação
    """

    def __init__(self, cliente_service: ClienteService):
        self._cliente_service = cliente_service

    def authenticate_cliente(self, email: str, senha: str):
        """
        Valida as credenciais informadas e retorna o cliente
        correspondente

        :raises InvalidCredentialsError:
            caso as crenciais não sejam válidas
        """
        try:
            model = self._cliente_service.get_by_email(email)
        except EntityNotFoundError as err:
            raise InvalidCredentialsError() from err

        if not verify_password(model.hash_senha, senha):
            raise InvalidCredentialsError()

        return model

    def generate_exp(self, minutes_to_expire: Optional[int] = None):
        """
        Gera a data de expiração do token
        """
        minutes = minutes_to_expire or settings.access_token_expire_time
        delta = dt.timedelta(minutes=minutes)

        return dt.datetime.now(dt.timezone.utc) + delta

    def generate_token(self, sub: str, exp: dt.datetime):
        """
        Produz um token de acesso
        """
        return jwt.encode(
            payload={'sub': sub, 'exp': exp},
            key=settings.secret_key,
            algorithm=settings.token_hash_algorithm
        )

    def generate_token_from_cliente(self, model: Cliente, exp: dt.datetime):
        """
        Produz um token de acesso a partir do model do cliente
        """
        return self.generate_token(str(model.id_cliente), exp)

    def validate_token(self, token: str):
        """
        Valida e decodifica o token fornecido

        :raises InvalidCredentialsError:
            caso o token tenha expirado ou não seja válido
        """
        try:
            return jwt.decode(
                jwt=token,
                key=settings.secret_key,
                algorithms=[settings.token_hash_algorithm]
            )
        except jwt.ExpiredSignatureError as err:
            raise InvalidCredentialsError('Token expired') from err
        except jwt.InvalidTokenError as err:
            raise InvalidCredentialsError() from err
