from sqlalchemy import select

from ._base import DatabaseRequiredService
from ..models import Especialidade

class EspecialidadeService(DatabaseRequiredService):
    """
    Classe para representar a lógica de negócio voltada a entidade
    'especialidade'
    """

    def get_all(self):
        """
        Retorna uma listagem contendo todos os especialidades disponíveis na 
        plataforma
        """
        return self._db_session.execute(
            select(Especialidade)
        ).scalars().all()
