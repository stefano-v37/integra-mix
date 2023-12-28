from typing import List

from pydantic import BaseModel, Field

from integra_mix.quantities import Quantity


class Ingredient(Quantity):
    source: str = Field(
        default=None,
        description="source of the ingredient, to evaluate the quality",
    )


class Integrator(BaseModel):
    name: str = Field(default=[], description="name of the integrator")
    nutritional_table: List[Ingredient] = Field(
        default=[], description="list of ingredients of the integrator"
    )
    cost: float = Field(default=None, description="cost of the integrator")
    vendor: str = Field(default=None, description="vendor associated to the cost")
