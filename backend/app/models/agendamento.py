from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from ._base import ModelBase

if TYPE_CHECKING:
    from . import Profissional, Cliente, Hora, Dia

class Agendamento(ModelBase):
    """
    Classe de mapeamento da entidade 'agendamento' do banco de dados
    """

    # Atributos da entidade
    id_agendamento: Mapped[int] = mapped_column(
        primary_key=True
    )
    id_profissional: Mapped[int] = mapped_column(
        ForeignKey('profissional.id_profissional')
    )
    id_cliente: Mapped[int] = mapped_column(
        ForeignKey('cliente.id_cliente')
    )
    id_hora: Mapped[int] = mapped_column(
        ForeignKey('hora.id_hora')
    )
    id_dia: Mapped[int] = mapped_column(
        ForeignKey('dia.id_dia')
    )
    data: Mapped[date]

    # Atributos de relacionamento
    profissional: Mapped[Profissional] = relationship(
        back_populates='agendamentos'
    )
    cliente: Mapped[Cliente] = relationship(
        back_populates='agendamentos'
    )
    dia: Mapped[Dia] = relationship(
        back_populates='agendamentos'
    )
    hora: Mapped[Hora] = relationship(
        back_populates='agendamentos'
    )
