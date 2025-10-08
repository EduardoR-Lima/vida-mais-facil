from fastapi import APIRouter

from ..dependencies import HoraServiceDep
from ..schemas.hora_schema import HoraOut

router = APIRouter(prefix='/horarios', tags=["Horarios"])

@router.get(
    '/',
    response_model=list[HoraOut]
)
def listar_horarios(service: HoraServiceDep):
    """
    Retorna uma lista contendo todos os horarios abrangidos pela
    plataforma
    """
    return service.get_all()
