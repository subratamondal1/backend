"""python class models to create sql tables"""

from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field

class GemClarity(str, Enum):
    SI = "SI"
    VS = "VS"
    VVS = "VVS"
    FL = "FL"

class GemColor(str, Enum):
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"

class GemType(str, Enum):
    DIAMOND = "DIAMOND"
    RUBY = "RUBY"
    EMERALD = "EMERALD"

class GemProperties(SQLModel, table=True):
    # the primary key needs to be optional, according to SqlModel
    id: Optional[int] = Field(primary_key=True, index=True)
    size:float = 1.0
    gem_clarity:Optional[GemClarity] = None
    gem_color:Optional[GemColor] = None

class Gem(SQLModel, table=True):
    # the primary key needs to be optional, according to SqlModel
    id:Optional[int] = Field(primary_key=True, index=True)
    price:float
    available:bool = True
    gem_type:Optional[GemType] = GemType.DIAMOND

    gem_properties_id:Optional[int] = Field(default=None, foreign_key="gemproperties.id")
