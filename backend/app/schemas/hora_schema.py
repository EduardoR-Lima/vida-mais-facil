from datetime import time

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

class HoraOut(BaseModel):
    """
    Model para envio de dados
    """
    model_config = ConfigDict(from_attributes=True)

    id_hora: int
    valor: time = Field(
        examples=['07:00:00'],
    )
