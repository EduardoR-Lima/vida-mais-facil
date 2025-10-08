from sqlalchemy import select

from ._base import DatabaseRequiredService
from ..models import Dia

class DiaService(DatabaseRequiredService):
    """
    Classe para representar a lógica de negócio voltada a entidade
    'dia'
    """

    def get_all(self):
        """
        Retorna uma listagem contendo todos os dias disponíveis na 
        plataforma
        """
        return self._db_session.execute(
            select(Dia)
        ).scalars().all()
