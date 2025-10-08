from fastapi import APIRouter

from ..dependencies import EspecialidadeServiceDep
from ..schemas.especialidade_schema import EspecialidadeOut

router = APIRouter(prefix='/especialidades', tags=["Especialidades"])

@router.get(
    '/',
    response_model=list[EspecialidadeOut]
)
def listar_especialidades(service: EspecialidadeServiceDep):
    """
    Retorna uma lista contendo todas as especialidades abrangidas pela
    plataforma
    """
    return service.get_all()
