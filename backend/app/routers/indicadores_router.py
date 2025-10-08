from fastapi import APIRouter
from fastapi import status
from fastapi.responses import Response

from ._query_params import PaginationParams
from ..dependencies import IndicadorServiceDep
from ..dependencies import CurrentUserDep
from ..schemas.indicador_schema import IndicadorCreate
from ..schemas.indicador_schema import IndicadorUpdate
from ..schemas.indicador_schema import IndicadorOut
from ..services.exceptions import ForbiddenOperationError
from ..services.exceptions import EntityNotFoundError
from ..services.exceptions.auth import InvalidCredentialsError
from ..utils.error_handling import raises

router = APIRouter(prefix='/indicadores', tags=["Indicadores"])

@router.get(
    "/",
    response_model=list[IndicadorOut],
    **raises(InvalidCredentialsError)
)
def listar_indicadores(
    service: IndicadorServiceDep,
    token_data: CurrentUserDep,
    pag_params: PaginationParams
):
    """
    Retorna uma lista de indicadores atrelados ao cliente atualmente
    autenticado
    """

    return service.get_all_by_cliente_id(
        id_cliente=int(token_data.sub),
        **pag_params.model_dump()
    )

@router.post(
    "/",
    response_model=IndicadorOut,
    status_code=status.HTTP_201_CREATED,
    **raises(InvalidCredentialsError)
)
def regitrar_novo_indicador(
    create_data: IndicadorCreate,
    service: IndicadorServiceDep,
    token_data: CurrentUserDep
):
    """
    Registra um novo indicador para o cliente atualmente autenticado
    """

    return service.create(
        id_cliente=int(token_data.sub),
        **create_data.model_dump()
    )

@router.delete(
    "/{id_indicador}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    **raises(ForbiddenOperationError, EntityNotFoundError)
)
def remover_indicador(
    id_indicador: int,
    service: IndicadorServiceDep,
    token_data: CurrentUserDep
):
    """
    Remove um indicador a partir do id fornecido caso esse indicador
    pertença ao cliente atualmente autenticado
    """

    service.delete(
        id_cliente=int(token_data.sub),
        id_indicador=id_indicador
    )

@router.put(
    "/{id_indicador}",
    response_model=IndicadorOut,
    **raises(ForbiddenOperationError, EntityNotFoundError)
)
def atualizar_indicador(
    id_indicador: int,
    update_data: IndicadorUpdate,
    service: IndicadorServiceDep,
    token_data: CurrentUserDep
):
    """
    Atualiza um indicador a partir do id fornecido caso esse indicador
    pertença ao cliente atualmente autenticado
    """

    return service.update(
        id_cliente=int(token_data.sub),
        id_indicador=id_indicador,
        **update_data.model_dump(exclude_unset=True)
    )
