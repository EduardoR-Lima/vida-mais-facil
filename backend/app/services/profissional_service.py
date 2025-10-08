from typing import Optional
from typing import Iterable
from datetime import date

from sqlalchemy import select
from sqlalchemy import exists
from sqlalchemy import not_
from sqlalchemy.orm import contains_eager

from .exceptions import AlreadyExistsError
from ._base import DatabaseRequiredService
from ..utils.date import weekday_from_date
from ..models import Profissional
from ..models import Agendamento
from ..models import Dia
from ..models import Hora

class ProfissionalService(DatabaseRequiredService):
    """
    Classe para representar a lógica de negócio voltada a entidade
    'profissional'
    """

    def get_all(self, limit: int, offset: int):
        """
        Retorna uma lista contendo todos os profissionais cadastrados
        na plataforma
        """
        return self._db_session.execute(
            select(Profissional)
            .offset(offset)
            .limit(limit)
        ).scalars().all()

    def get_schedule(
        self,
        data: date,
        limit: int,
        offset: int,
        id_esp: Optional[int] = None,
        id_hora: Optional[int] = None
    ):
        """
        Lista todos os horários disponíveis a partir da data, da especialidade
        e da hora
        """
        id_dia = weekday_from_date(data)

        stmt = (
            select(Profissional)
            .join(Profissional.dias)
            .join(Profissional.horarios)
            .where(
                Dia.id_dia == id_dia,
                not_(exists().where(
                    Agendamento.id_profissional == Profissional.id_profissional,
                    Agendamento.id_hora == Hora.id_hora,
                    Agendamento.data == data
                ))
            )
            # Garante que Profissional.horarios seja preenchido de acordo
            # com os resultados dessa query inicial
            .options(contains_eager(Profissional.horarios))
            .execution_options(populate_existing=True)
            .offset(offset)
            .limit(limit)
        )

        if id_esp:
            stmt = stmt.where(Profissional.id_especialidade == id_esp)

        if id_hora:
            stmt = stmt.where(Hora.id_hora == id_hora)

        return self._db_session.execute(stmt).unique().scalars().all()

    def create(
        self,
        horarios_ids: Iterable[int],
        dias_ids: Iterable[int],
        **model_kwargs 
    ):
        """
        Registra um novo profissional no banco de dados
        
        :raises AlreadyExistsError:
            caso o registro_profissional já tenha sido cadastrado no banco
        """
        model = Profissional(**model_kwargs)

        if model.registro_profissional and self._exists(
            Profissional.registro_profissional == model.registro_profissional
        ):
            raise AlreadyExistsError(Profissional.registro_profissional.name)

        model.dias.extend(
            self._db_session.execute(
                select(Dia)
                .filter(Dia.id_dia.in_(dias_ids))
            ).scalars().all()
        )
        model.horarios.extend(
            self._db_session.execute(
                select(Hora)
                .filter(Hora.id_hora.in_(horarios_ids))
            ).scalars().all()
        )

        self._db_session.add(model)
        self._db_session.commit()

        return model