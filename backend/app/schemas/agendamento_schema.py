from datetime import date

from pydantic import BaseModel
from pydantic import ConfigDict

from .profissional_schema import ProfissionalOut
from .hora_schema import HoraOut

class AgendamentoBase(BaseModel):
    """
    Base pydantic model
    """
    data: date

class AgendamentoCreate(AgendamentoBase):
    """
    Model para registro
    """
    id_profissional: int
    id_hora: int

class AgendamentoOut(AgendamentoBase):
    """
    Model para envio de dados
    """
    model_config = ConfigDict(from_attributes=True)

    id_agendamento: int
    hora: HoraOut
    profissional: ProfissionalOut

class AgendamentoTotal(BaseModel):
    """
    Model para representar o total de agendamentos cadastrados 
    """
    total: int
