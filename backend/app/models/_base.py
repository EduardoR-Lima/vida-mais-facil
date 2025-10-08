import re

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import MappedAsDataclass

class ModelBase(DeclarativeBase, MappedAsDataclass, init=False, repr=False):
    """
    Base class from where all models will inherit
    """

    @classmethod
    def _generate_tablename(cls):
        return re.sub(
            # Não captura todos os casos, mas é o suficiente
            r"(?!^)([A-Z])",
            r"_\1",
            cls.__name__
        ).lower()

    def __init_subclass__(cls, **kw):
        # Gera o nome da tabela automaticamente, convertendo o nome
        # da classe do padrão CamelCase para snake_case
        if not hasattr(cls, '__tablename__'):
            cls.__tablename__ = cls._generate_tablename()

        return super().__init_subclass__(**kw)
