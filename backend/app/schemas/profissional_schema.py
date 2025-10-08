from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from .especialidade_schema import EspecialidadeOut
from .hora_schema import HoraOut

class ProfissionalBase(BaseModel):
    """
    Base pydantic model
    """
    nome: str = Field(
        max_length=60,
        examples=['Carlos Eduardo'],
    )
    telefone: str = Field(
        max_length=11,
        examples=['85995329065'],
    )
    descricao: str = Field(
        examples=['Sou formado pela UFC e tenho 10 anos de experiência'],
    )

class ProfissionalCreate(ProfissionalBase):
    """
    Model para registro
    """
    id_especialidade: int
    horarios_ids: set[int]
    dias_ids: set[int]
    registro_profissional: Optional[str] = Field(
        default=None,
        max_length=15,
        examples=['135462CRM/CE'],
    )

class ProfissionalOut(ProfissionalBase):
    """
    Model para envio de dados
    """
    model_config = ConfigDict(from_attributes=True)

    id_profissional: int
    especialidade: EspecialidadeOut

class ProfissionalOutSchedule(ProfissionalOut):
    """
    Model para listagem de disponibilidade
    """
    horarios: list[HoraOut]
