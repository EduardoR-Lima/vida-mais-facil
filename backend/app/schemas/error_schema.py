from pydantic import BaseModel
from pydantic import ConfigDict

class SimpleMessageError(BaseModel):
    """
    Model para mapear erros com uma mensagem simples
    """
    model_config=ConfigDict(from_attributes=True)

    message: str

class FieldMessageError(SimpleMessageError):
    """
    Model para mapear erros que especifiquem campos
    """
    model_config=ConfigDict(from_attributes=True)
    
    fields: list[str]
