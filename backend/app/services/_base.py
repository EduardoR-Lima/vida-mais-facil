from abc import ABC

from sqlalchemy import select
from sqlalchemy import exists
from sqlalchemy.orm import Session

class DatabaseRequiredService(ABC):
    """
    Classe abstrata para representar services que dependem diretamente 
    do banco de dados
    """

    def __init__(self, session: Session):
        self._db_session = session

    def _exists(self, *clauses):
        return self._db_session.execute(
            select(exists().where(*clauses))
        ).scalar()
