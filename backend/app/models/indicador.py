from __future__ import annotations
from typing import TYPE_CHECKING
from typing import Optional
from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from ._base import ModelBase

if TYPE_CHECKING:
    from . import Cliente

class Indicador(ModelBase):
    """
    Classe de mapeamento da entidade 'indicador' do banco de dados
    """

    # Atributos da entidade
    id_indicador: Mapped[int] = mapped_column(
        primary_key=True
    )
    id_cliente: Mapped[int] = mapped_column(
        ForeignKey('cliente.id_cliente')
    )
    tipo: Mapped[str]
    valor: Mapped[str]
    data_registro: Mapped[datetime] = mapped_column(
        server_default=func.current_timestamp() #pylint: disable=not-callable
    )
    observacoes: Mapped[Optional[str]]

    # Atributos de relacionamento
    cliente: Mapped[Cliente] = relationship(
        back_populates='indicadores'
    )
