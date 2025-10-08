from typing import Optional
from typing import TypeAlias
from typing import Annotated
from datetime import date

from pydantic import BaseModel
from pydantic import Field

from fastapi import Query
from fastapi import Depends

class PaginationModel(BaseModel):
    limit: int = Field(
        Query(
            100,
            description="O número máximo de entidades que serão listadas"
        )
    )

    offset: int = Field(
        Query(
            0,
            description=(
                "O número de entidades que serão puladas antes de listas"
            )
        )
    )

class ScheduleFilterModel(BaseModel):
    data: date = Field(
        Query(
            description="A data referente aos horários que serão listados"
        )
    )
    id_esp: Optional[int] = Field(
        Query(
            None,
            description=(
                "[Opcional] O id da especialidade que será aplicada para "
                "filtrar a listagem de profissionais"
            )
        )
    )
    id_hora: Optional[int] = Field(
        Query(
            None,
            description=(
                "[Opcional] O id da hora que será aplicada para filtrar "
                "a listagem de disponibilidades"
            )
        )
    )

PaginationParams: TypeAlias = Annotated[PaginationModel, Depends()]
ScheduleFilterParams: TypeAlias = Annotated[ScheduleFilterModel, Depends()]