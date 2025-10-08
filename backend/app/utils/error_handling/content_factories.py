from typing import Callable
from typing import TypeAlias
from typing import TypeVar

from pydantic import BaseModel

T = TypeVar('T')
_ContentFactory: TypeAlias = Callable[[T], dict]

def from_pydantic_model(model: type[BaseModel]) -> _ContentFactory:
    """
    Retorna um factory que converte exceções em dicionários a partir
    de um modelo pydantic via `.model_validate`

    :param model:
        um modelo do `pydantic` que será utilizado para produzir o
        objeto a partir da exceção
    """
    def factory(exc: Exception):
        return model.model_validate(exc).model_dump()

    return factory

def constant_message(msg: str):
    """
    Retorna um factory que produz a mesma mensagem independente da
    exceção passada.

    O dicionário retornado pelo factory é do tipo {'message': msg}

    :param msg:
        uma `str` contendo a mensagem que será retornada pelo factory
    """
    def factory(exc: Exception):    #pylint: disable=unused-argument
        return {'message': msg}

    return factory
