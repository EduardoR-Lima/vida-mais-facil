from sqlalchemy import select

from .exceptions import EntityNotFoundError
from .exceptions import ForbiddenOperationError
from ._base import DatabaseRequiredService
from ..models import Indicador

class IndicadorService(DatabaseRequiredService):
    """
    Classe para representar a lógica de negócio voltada a entidade
    'indicador'
    """

    def get_all_by_cliente_id(self, id_cliente: int, limit: int, offset: int):
        """
        Retorna uma lista de indicadores atrelados ao id fornecido
        """
        return self._db_session.execute(
            select(Indicador)
            .where(Indicador.id_cliente == id_cliente)
            .order_by(Indicador.data_registro)
            .offset(offset)
            .limit(limit)
        ).scalars().all()

    def create(self, id_cliente: int, **model_kwargs):
        """
        Registra um novo indicador no banco de dados atrelado ao id
        fornecido
        """
        model = Indicador(id_cliente=id_cliente, **model_kwargs)

        self._db_session.add(model)
        self._db_session.commit()

        return model

    def delete(self, id_cliente: int, id_indicador: int):
        """
        Remove o registro do indicador atavés do id fornecido

        :raises EntityNotFoundError:
            caso o id informado não aponte para nenhum id

        :raises ForbiddenOperationError:
            caso o id_cliente não corresponda com a registro do indicador
        """
        model = self._db_session.get(Indicador, id_indicador)

        if not model:
            raise EntityNotFoundError(
                f"Could not find 'Indicador' for id {id_indicador}"
            )

        if model.id_cliente != id_cliente:
            raise ForbiddenOperationError()

        self._db_session.delete(model)
        self._db_session.commit()

    def update(self, id_cliente: int, id_indicador: int, **model_kwargs):
        """
        Atualiza o registro do indicador no banco de dados a partir
        dos ids fornecidos
        
        :raises EntityNotFoundError:
            caso o id informado não aponte para nenhum id

        :raises ForbiddenOperationError:
            caso o id_cliente não corresponda com a registro do indicador
        """
        model = self._db_session.get(Indicador, id_indicador)

        if not model:
            raise EntityNotFoundError(
                f"Could not find 'Indicador' for id {id_indicador}"
            )

        if model.id_cliente != id_cliente:
            raise ForbiddenOperationError()

        for name, value in model_kwargs.items():
            setattr(model, name, value)

        self._db_session.commit()

        return model
