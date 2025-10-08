from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import time

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from ._base import ModelBase
from ._associations import horario_disponivel_m2m

if TYPE_CHECKING:
    from . import Profissional, Agendamento

class Hora(ModelBase):
    """
    Classe de mapeamento da entidade 'hora' do banco de dados
    """

    # Atributos da entidade
    id_hora: Mapped[int] = mapped_column(
        primary_key=True,
    )
    valor: Mapped[time]

    # Atributos de relacionamento
    profissionais: Mapped[list[Profissional]] = relationship(
        secondary=horario_disponivel_m2m,
        back_populates='horarios'
    )
    agendamentos: Mapped[list[Agendamento]] = relationship(
        back_populates='hora'
    )
