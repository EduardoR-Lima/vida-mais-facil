from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

class DiaOut(BaseModel):
    """
    Model para envio de dados
    """
    model_config = ConfigDict(from_attributes=True)

    id_dia: int
    nome: str = Field(
        examples=['Segunda'],
    )
