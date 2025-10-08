from fastapi import APIRouter

from . import (
    agendamentos_router,
    auth_router,
    clientes_router,
    dias_router,
    especialidades_router,
    horarios_router,
    indicadores_router,
    profissionais_router
)

api_router = APIRouter(prefix='/api')

api_router.include_router(agendamentos_router.router)
api_router.include_router(auth_router.router)
api_router.include_router(clientes_router.router)
api_router.include_router(dias_router.router)
api_router.include_router(especialidades_router.router)
api_router.include_router(horarios_router.router)
api_router.include_router(indicadores_router.router)
api_router.include_router(profissionais_router.router)
