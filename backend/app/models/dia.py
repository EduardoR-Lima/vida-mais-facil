from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from ._base import ModelBase
from ._associations import dia_disponivel_m2m

if TYPE_CHECKING:
    from . import Profissional, Agendamento

class Dia(ModelBase):
    """
    Classe de mapeamento da entidade 'dia' do banco de dados
    """

    # Atributos da entidade
    id_dia: Mapped[int] = mapped_column(
        primary_key=True
    )
    nome: Mapped[str]

    # Atributos de relacionamento
    profissionais: Mapped[list[Profissional]] = relationship(
        secondary=dia_disponivel_m2m,
        back_populates='dias'
    )
    agendamentos: Mapped[list[Agendamento]] = relationship(
        back_populates='dia'
    )
