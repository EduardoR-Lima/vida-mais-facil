from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

class EspecialidadeOut(BaseModel):
    """
    Model para envio de dados
    """
    model_config = ConfigDict(from_attributes=True)

    id_especialidade: int
    nome: str = Field(
        examples=['Otorrinolaringologia'],
    )
