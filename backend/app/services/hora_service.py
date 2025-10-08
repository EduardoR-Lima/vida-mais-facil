from sqlalchemy import select

from ._base import DatabaseRequiredService
from ..models import Hora

class HoraService(DatabaseRequiredService):
    """
    Classe para representar a lógica de negócio voltada a entidade
    'hora'
    """

    def get_all(self):
        """
        Retorna uma listagem contendo todos os horarios disponíveis na 
        plataforma
        """
        return self._db_session.execute(
            select(Hora)
        ).scalars().all()