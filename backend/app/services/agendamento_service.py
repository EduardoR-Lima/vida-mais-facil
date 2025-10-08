from sqlalchemy import select
from sqlalchemy import func

from .exceptions import AlreadyExistsError
from ._base import DatabaseRequiredService
from ..models import Agendamento
from ..utils.date import weekday_from_date

#pylint: disable=not-callable
class AgendamentoService(DatabaseRequiredService):
    """
    Classe para representar a lógica de negócio voltada a entidade
    'agendamento'
    """

    def get_all_by_cliente_id(self, id_cliente: int, limit: int, offset: int):
        """
        Retorna uma lista de agendamentos pendentes 
        """

        return self._db_session.execute(
            select(Agendamento)
            .where(Agendamento.id_cliente == id_cliente)
            .filter(Agendamento.data >= func.current_timestamp())
            .offset(offset)
            .limit(limit)
        ).scalars().all()

    def create(self, id_cliente: int, **model_kwargs):
        """
        Registra um novo agendamento no banco de dados

        :raises AlreadyExistsError:
            caso já exista um agendamento para o profissional, dia e
            horário fornecidos
        """
        model = Agendamento(id_cliente=id_cliente, **model_kwargs)
        model.id_dia = weekday_from_date(model.data)

        if self._exists(
            Agendamento.id_profissional == model.id_profissional,
            Agendamento.id_hora == model.id_hora,
            Agendamento.data == model.data
        ):
            raise AlreadyExistsError(
                Agendamento.id_profissional.name,
                Agendamento.id_hora.name,
                Agendamento.data.name,
                message=(
                    "The combination of the listed fields has already been "
                    "taken"
                )
            )

        self._db_session.add(model)
        self._db_session.commit()

        return model

    def total(self, id_cliente: int):
        """
        Retorna o total de agendamentos realizados pelo cliente informado
        """
        return self._db_session.execute(
            select(func.count("*"))
            .where(Agendamento.id_cliente == id_cliente)
        ).scalar()
