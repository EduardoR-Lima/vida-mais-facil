from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from ._base import ModelBase

if TYPE_CHECKING:
    from . import Profissional

class Especialidade(ModelBase):
    """
    Classe de mapeamento da entidade 'especialidade' do banco de dados
    """

    # Atributos da entidade
    id_especialidade: Mapped[int] = mapped_column(
        primary_key=True,
    )
    nome: Mapped[str]

    # Atributos de relacionamento
    profissionais: Mapped[list[Profissional]] = relationship(
        back_populates='especialidade'
    )
