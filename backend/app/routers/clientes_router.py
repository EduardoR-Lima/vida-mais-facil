from fastapi import APIRouter
from fastapi import status

from ..dependencies import ClienteServiceDep
from ..dependencies import CurrentUserDep
from ..schemas.cliente_schema import ClienteOut
from ..schemas.cliente_schema import ClienteCreate
from ..services.exceptions import AlreadyExistsError
from ..services.exceptions.auth import InvalidCredentialsError
from ..utils.error_handling import raises

router = APIRouter(prefix='/clientes', tags=["Clientes"])

@router.post(
    "/",
    response_model=ClienteOut,
    status_code=status.HTTP_201_CREATED,
    **raises(AlreadyExistsError)
)
def cadastrar_novo_cliente(
    create_data: ClienteCreate,
    service: ClienteServiceDep
):
    """
    Cadastra um novo cliente no banco de dados
    """
    return service.create(
        **create_data.model_dump()
    )

# Teoricamente, get_by_id pode levantar EntityNotFound, mas, nesse
# caso, como o id é inferido através do token, para que o id seja
# inválido, o token também deverá ser. Portanto apenas InvalidCredentials
# foi mapeado
@router.get(
    "/me",
    response_model=ClienteOut,
    **raises(InvalidCredentialsError)
)
def cliente_atual(
    service: ClienteServiceDep,
    token_data: CurrentUserDep
):
    """
    Retorna as informações do cliente atualmente autenticado
    """
    return service.get_by_id(
        id_cliente=int(token_data.sub)
    )
