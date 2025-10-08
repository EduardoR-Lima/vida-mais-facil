from fastapi import APIRouter

from ..schemas.token_schema import Token
from ..dependencies import AuthServiceDep
from ..dependencies import OAuthFormDep
from ..services.exceptions.auth import InvalidCredentialsError
from ..utils.error_handling import raises

router = APIRouter(prefix='/auth', tags=["Auth"])

@router.post(
    '/token',
    response_model=Token,
    **raises(InvalidCredentialsError)
)
def request_access_token(
    service: AuthServiceDep,
    form: OAuthFormDep
):
    """
    Retorna um token de acesso com um tempo de validade caso as credenciais
     sejam válidas
    """

    cliente = service.authenticate_cliente(form.username, form.password)

    exp = service.generate_exp()

    return Token(
        token_type="bearer",
        access_token=service.generate_token_from_cliente(cliente, exp),
        exp=exp,
        cliente=cliente
    )
