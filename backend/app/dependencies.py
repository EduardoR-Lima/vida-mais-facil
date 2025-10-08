from typing import TypeAlias, Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from . import services as s
from .config import settings
from .schemas.token_schema import TokenData

_engine = create_engine(settings.sqlalchemy_database_uri)

def get_database_session():
    with Session(_engine, autocommit=False, autoflush=False) as sess:
        yield sess

DbSessionDep: TypeAlias = Annotated[
    Session,
    Depends(get_database_session)
]

def service_di_factory[T](service: type[T]):
    def di(session: DbSessionDep) -> T:
        return service(session)

    return di

AgendamentoServiceDep: TypeAlias = Annotated[
    s.AgendamentoService,
    Depends(service_di_factory(s.AgendamentoService))
]
ClienteServiceDep: TypeAlias = Annotated[
    s.ClienteService,
    Depends(service_di_factory(s.ClienteService))
]
DiaServiceDep: TypeAlias = Annotated[
    s.DiaService,
    Depends(service_di_factory(s.DiaService))
]
EspecialidadeServiceDep: TypeAlias = Annotated[
    s.EspecialidadeService,
    Depends(service_di_factory(s.EspecialidadeService))
]
HoraServiceDep: TypeAlias = Annotated[
    s.HoraService,
    Depends(service_di_factory(s.HoraService))
]
IndicadorServiceDep: TypeAlias = Annotated[
    s.IndicadorService,
    Depends(service_di_factory(s.IndicadorService))
]
ProfissionalServiceDep: TypeAlias = Annotated[
    s.ProfissionalService,
    Depends(service_di_factory(s.ProfissionalService))
]

def get_auth_service(cliente_service: ClienteServiceDep):
    return s.AuthService(cliente_service)

AuthServiceDep: TypeAlias = Annotated[
    s.AuthService,
    Depends(get_auth_service)
]

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/api/auth/token')

def get_current_user(
    service: AuthServiceDep,
    token: Annotated[str, Depends(oauth_scheme)]
):
    return TokenData.model_validate(service.validate_token(token))

CurrentUserDep: TypeAlias = Annotated[
    TokenData,
    Depends(get_current_user)
]
OAuthFormDep: TypeAlias = Annotated[
    OAuth2PasswordRequestForm,
    Depends()
]
