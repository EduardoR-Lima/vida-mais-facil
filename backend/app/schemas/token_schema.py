from datetime import datetime

from pydantic import BaseModel

from .cliente_schema import ClienteOutMinimal

class Token(BaseModel):
    """
    Model para representar a resposta da rota de autenticação
    """
    token_type: str
    access_token: str
    exp: datetime
    cliente: ClienteOutMinimal

class TokenData(BaseModel):
    """
    Model para representar os dados contidos no token
    """
    sub: str
