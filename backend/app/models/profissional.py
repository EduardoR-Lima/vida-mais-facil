from __future__ import annotations
from typing import TYPE_CHECKING
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from ._base import ModelBase
from ._associations import dia_disponivel_m2m
from ._associations import horario_disponivel_m2m

if TYPE_CHECKING:
    from . import Especialidade, Agendamento, Dia, Hora

class Profissional(ModelBase):
    """
    Classe de mapeamento da entidade 'profissional' do banco de dados
    """

    # Atributos da entidade
    id_profissional: Mapped[int] = mapped_column(
        primary_key=True
    )
    id_especialidade: Mapped[int] = mapped_column(
        ForeignKey('especialidade.id_especialidade')
    )
    nome: Mapped[str]
    telefone: Mapped[str]
    descricao: Mapped[str]
    registro_profissional: Mapped[Optional[str]]

    # Atributos de relacionamento
    especialidade: Mapped[Especialidade] = relationship(
        back_populates='profissionais'
    )
    agendamentos: Mapped[list[Agendamento]] = relationship(
        back_populates='profissional'
    )
    dias: Mapped[list[Dia]] = relationship(
        secondary=dia_disponivel_m2m,
        back_populates='profissionais'
    )
    horarios: Mapped[list[Hora]] = relationship(
        secondary=horario_disponivel_m2m,
        back_populates='profissionais'
    )
