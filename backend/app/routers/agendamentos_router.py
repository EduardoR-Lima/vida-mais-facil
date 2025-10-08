from fastapi import APIRouter
from fastapi import status

from ._query_params import PaginationParams
from ..dependencies import AgendamentoServiceDep
from ..dependencies import CurrentUserDep
from ..services.exceptions import AlreadyExistsError
from ..services.exceptions.auth import InvalidCredentialsError
from ..schemas.agendamento_schema import AgendamentoOut
from ..schemas.agendamento_schema import AgendamentoCreate
from ..schemas.agendamento_schema import AgendamentoTotal
from ..utils.error_handling import raises

router = APIRouter(prefix='/agendamentos', tags=["Agendamentos"])

@router.get(
    "/",
    response_model=list[AgendamentoOut],
    **raises(InvalidCredentialsError)
)
def listar_agendamentos(
    service: AgendamentoServiceDep,
    token_data: CurrentUserDep,
    pag_params: PaginationParams
):
    """
    Retorna uma lista de agendamentos pendentes do cliente atualmente
    autenticado
    """

    return service.get_all_by_cliente_id(
        id_cliente=int(token_data.sub),
        **pag_params.model_dump()
    )

@router.post(
    "/",
    response_model=AgendamentoOut,
    status_code=status.HTTP_201_CREATED,
    **raises(InvalidCredentialsError, AlreadyExistsError)
)
def registrar_novo_agendamento(
    create_data: AgendamentoCreate,
    service: AgendamentoServiceDep,
    token_data: CurrentUserDep
):
    """
    Registra um novo agendamento para o cliente atualmente autenticado
    """

    return service.create(
        id_cliente=int(token_data.sub),
        **create_data.model_dump()
    )

@router.get(
    "/total",
    response_model=AgendamentoTotal
)
def total_de_agendamentos(
    token_data: CurrentUserDep,
    service: AgendamentoServiceDep
):
    """
    Retorna uma contagem do total de agendamentos realizados pelo cliente
    atualmente autenticado
    """
    return AgendamentoTotal(
        total=service.total(
            int(token_data.sub)
        )
    )
