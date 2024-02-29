"""enter data """

import string
import random

from sqlmodel import Session

from models.gem_models import Gem, GemProperties, GemClarity
from main import ENGINE

COLOR_GRADES:str = string.ascii_uppercase[3:9]

def create_gem_properties() -> GemProperties:
    size:float = random.randint(a=3, b=70)/10
    color:str= COLOR_GRADES[random.randint(a=0,b=5)]
    clarity:str=[clarity.value for clarity in GemClarity][random.randint(a=0,b=3)]
    gem_properties = GemProperties(
        size=size,
        gem_clarity=clarity,
        gem_color=color
    )
    return gem_properties

def create_gem(gem_properties) -> Gem:
    gem = Gem(
        price=1000, 
        gem_properties_id=gem_properties
    )
    return gem

def create_gem_db():
    gem_properties:GemProperties = create_gem_properties()
    print(gem_properties)

    with Session(bind=ENGINE) as session:
        session.add(instance=gem_properties)
        session.commit()
        gem:Gem = create_gem(gem_properties=gem_properties.id)
        session.add(gem)
        session.commit()

create_gem_db()