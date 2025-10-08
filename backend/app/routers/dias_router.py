from fastapi import APIRouter

from ..dependencies import DiaServiceDep
from ..schemas.dia_schema import DiaOut

router = APIRouter(prefix='/dias', tags=["Dias"])

@router.get(
    '/',
    response_model=list[DiaOut]
)
def listar_dias(service: DiaServiceDep):
    """
    Retorna uma lista contendo todos os dias abrangidos pela plataforma
    """
    return service.get_all()
