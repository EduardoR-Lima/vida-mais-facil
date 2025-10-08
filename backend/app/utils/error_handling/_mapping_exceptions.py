from typing import Optional

from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from pydantic import BaseModel

from .content_factories import _ContentFactory
from .content_factories import from_pydantic_model
from ..logging import logger

# Para o escopo desse projeto, essa abordagem com uma variável global é
# o suficiente e não apresenta muitos riscos
_EXCEPTIONS_MAP = {}

# Produz o handler que será repassado para o app.add_exception_handler.
def _get_exc_handler(
    content_factory: _ContentFactory,
    status_code: int,
    **response_kwargs
):

    # O Request faz parte da assinatura obrigatória dos handlers, mesmo
    # que não seja utilizado
    def handler(req: Request, exc: Exception):  #pylint: disable=unused-argument
        return JSONResponse(
            content_factory(exc),
            status_code,
            **response_kwargs
        )

    return handler

def add_exception_handler[T: Exception](
    app: FastAPI,
    exc: type[T],
    response_model: type[BaseModel],
    status_code: int,
    custom_content_factory: Optional[_ContentFactory[T]] = None,
    **response_kwargs
):
    """
    Adiciona um handler global que automaticamente mapeia o erro para uma
    `JSONResponse` válida a partir do `response_model` e `status_code`

    :param app:
        a instância da aplicação na qual serão adicionados os handlers
    
    :param exc:
        a exceção que deve ser capturada pelo handler

    :param response_model:
        um modelo do `pydantic` para representar a estrutura de `exc`
    
    :param status_code:
        um inteiro representando o status da resposta

    :param custom_content_factory:
        uma função opcional que recebe uma instância de `exc` e retorna
        um dicionário que será passado para `JSONResponse.content`. 
        `.content_factories.from_pydantic_model` é utilizado, por padrão,
        caso nenhum valor tenha sido fornecido
        
    :param response_kwargs:
        qualquer extra `kwarg` será repassado para o método de construção
        do `JSONResponse`
    """
    _EXCEPTIONS_MAP[exc] = {
        status_code: {'model': response_model}
    }

    _cf = custom_content_factory or from_pydantic_model(response_model)

    app.add_exception_handler(
        exc,
        _get_exc_handler(
            _cf,
            status_code,
            **response_kwargs
        )
    )

# Basicamente um get aprimorado para realizar logs caso a exceção não
# tenha sido devidamente mapeada
def _possible_response_from_exc(exc: type[Exception]) -> dict:
    # Objeto que vai descrever a possível resposta
    exc_info = _EXCEPTIONS_MAP.get(exc, {})

    if not exc_info:
        logger.warning(
            "Unable to map %s to a possible response. Skipping the map process"
        )

    return exc_info

def raises(*exceptions: type[Exception]):
    """
    Criado para ser utilizado durante o mapeamento das rotas. Retorna um
    dicionário mapeando as possíveis respostas da rota a partir das
    exceções especificadas

    Para que essa função possa ser utilizada, a exceção deve ter sido
    previamente mapeada a partir da função `add_exception_mapper`

    :param exceptions:
        exceções que serão utilizadas para produzir as possíveis
        respostas
    """
    responses = {}

    for exc in exceptions:
        responses.update(_possible_response_from_exc(exc))

    return {'responses': responses}
