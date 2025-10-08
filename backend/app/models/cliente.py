from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from ._base import ModelBase

if TYPE_CHECKING:
    from . import Agendamento, Indicador

class Cliente(ModelBase):
    """
    Classe de mapeamento da entidade 'cliente' do banco de dados
    """

    # Atributos da entidade
    id_cliente: Mapped[int] = mapped_column(
        primary_key=True
    )
    nome: Mapped[str]
    telefone: Mapped[str]
    cpf: Mapped[str]
    rua: Mapped[str]
    numero: Mapped[int]
    email: Mapped[str]
    hash_senha: Mapped[str]

    # Atributos de relacionamento
    agendamentos: Mapped[list[Agendamento]] = relationship(
        back_populates='cliente'
    )
    indicadores: Mapped[list[Indicador]] = relationship(
        back_populates='cliente'
    )
