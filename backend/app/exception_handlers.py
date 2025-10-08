from functools import partial

from fastapi import FastAPI
from fastapi import status

from sqlalchemy.exc import IntegrityError

from .schemas.error_schema import SimpleMessageError
from .schemas.error_schema import FieldMessageError
from .utils.error_handling.content_factories import constant_message
from .utils.error_handling import add_exception_handler
from .services.exceptions import auth as aexc
from .services import exceptions as exc

def register_global_handlers(app: FastAPI):
    """
    Cria e registra todos os handlers globais da aplicação
    """
    _add_exc_handler = partial(add_exception_handler, app)

    _add_exc_handler(
        exc=exc.AlreadyExistsError,
        response_model=FieldMessageError,
        status_code=status.HTTP_409_CONFLICT,
    )

    _add_exc_handler(
        exc=exc.EntityNotFoundError,
        response_model=SimpleMessageError,
        status_code=status.HTTP_404_NOT_FOUND,
    )

    _add_exc_handler(
        exc=exc.ForbiddenOperationError,
        response_model=SimpleMessageError,
        status_code=status.HTTP_403_FORBIDDEN
    )

    _add_exc_handler(
        exc=aexc.InvalidCredentialsError,
        response_model=SimpleMessageError,
        status_code=status.HTTP_401_UNAUTHORIZED,
        headers={"WWW-Authenticate": "Bearer"}
    )

    _add_exc_handler(
        exc=IntegrityError,
        response_model=SimpleMessageError,
        status_code=status.HTTP_400_BAD_REQUEST,
        custom_content_factory=constant_message(
            "The values provided violate our constraints"
        )
    )
