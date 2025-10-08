from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

class ClienteBase(BaseModel):
    """
    Base pydantic model
    """
    nome: str = Field(
        max_length=60,
        examples=['Roberto'],
    )
    telefone: str = Field(
        max_length=11,
        examples=['85997735418'],
    )
    cpf: str = Field(
        max_length=11,
        examples=['72679346092'],
    )
    rua: str = Field(
        max_length=45,
        examples=['Rua 12'],
    )
    numero: int = Field(
        examples=['7789'],
    )
    email: str = Field(
        max_length=60,
        examples=['roberto.sa@gmail.com'],
    )

class ClienteCreate(ClienteBase):
    """
    Model para cadastro
    """
    senha: str

class ClienteOut(ClienteBase):
    """
    Model para envio de dados
    """
    model_config = ConfigDict(from_attributes=True)

    id_cliente: int

class ClienteOutMinimal(BaseModel):
    """
    Model utilizado para retornar informações mínimas sobre o cliente
    na resposta do token
    """
    model_config = ConfigDict(from_attributes=True)

    id_cliente: int
    nome: str
