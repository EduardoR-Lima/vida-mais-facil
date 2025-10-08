from fastapi import APIRouter
from fastapi import status

from ._query_params import PaginationParams
from ._query_params import ScheduleFilterParams
from ..dependencies import ProfissionalServiceDep
from ..schemas.profissional_schema import ProfissionalOut
from ..schemas.profissional_schema import ProfissionalCreate
from ..schemas.profissional_schema import ProfissionalOutSchedule
from ..services.exceptions import AlreadyExistsError
from ..utils.error_handling import raises

router = APIRouter(prefix='/profissionais', tags=["Profissionais"])

@router.get(
    "/",
    response_model=list[ProfissionalOut]
)
def listar_profissionais(
    service: ProfissionalServiceDep,
    pag_params: PaginationParams
):
    """
    Retorna uma lista de profissionais cadastrados na plataforma
    """

    return service.get_all(
        **pag_params.model_dump()
    )

@router.post(
    "/",
    response_model=ProfissionalOut,
    status_code=status.HTTP_201_CREATED,
    **raises(AlreadyExistsError)
)
def cadastrar_novo_profissional(
    create_date: ProfissionalCreate,
    service: ProfissionalServiceDep
):
    """
    Cadastra um novo profissional no banco de dados
    """

    return service.create(
        **create_date.model_dump()
    )

@router.get(
    "/disponibilidade",
    response_model=list[ProfissionalOutSchedule]
)
def listar_disponibilidades(
    service: ProfissionalServiceDep,
    filter_params: ScheduleFilterParams,
    pag_params: PaginationParams
):
    """
    Retorna uma lista de profissionais e seus respectivos horários
    disponíveis para agendamento a partir da data e dos filtros aplicados
    """

    return service.get_schedule(
        **pag_params.model_dump(),
        **filter_params.model_dump()
    )
