from typing import Optional
from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

class IndicadorBase(BaseModel):
    """
    Base pydantic model
    """
    tipo: str = Field(
        max_length=45,
        examples=['Pressão'],
    )
    valor: str = Field(
        max_length=15,
        examples=['12/8'],
    )
    observacoes: Optional[str] = Field(
        default=None,
        examples=['Estava com dor no braço antes de medir a pressão'],
    )

# Não precisa de nenhum campo a mais além dos que foram declarados em
# IndicadorBase
class IndicadorCreate(IndicadorBase):
    """
    Model para registro
    """

class IndicadorOut(IndicadorBase):
    """
    Model para envio de dados
    """
    model_config = ConfigDict(from_attributes=True)

    id_indicador: int
    data_registro: datetime

class IndicadorUpdate(BaseModel):
    """
    Model para atualização de registros
    """
    tipo: Optional[str] = Field(
        default=None,
        max_length=45,
        examples=['Pressão'],
    )
    valor: Optional[str] = Field(
        default=None,
        max_length=15,
        examples=['12/8'],
    )
    observacoes: Optional[str] = Field(
        default=None,
        examples=['Estava com dor no braço antes de medir a pressão'],
    )
