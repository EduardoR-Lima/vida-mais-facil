from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey

from ._base import ModelBase

dia_disponivel_m2m = Table(
    'dia_disponivel',
    ModelBase.metadata,
    Column(
        'id_dia',
        ForeignKey('dia.id_dia'),
        primary_key=True
    ),
    Column(
        'id_profissional',
        ForeignKey('profissional.id_profissional'),
        primary_key=True
    )
)

horario_disponivel_m2m = Table(
    'horario_disponivel',
    ModelBase.metadata,
    Column(
        'id_hora',
        ForeignKey('hora.id_hora'),
        primary_key=True
    ),
    Column(
        'id_profissional',
        ForeignKey('profissional.id_profissional'),
        primary_key=True
    )
)