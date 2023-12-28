from typing import List

from pydantic import BaseModel, Field, model_validator

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

    @model_validator(mode="after")
    def check_unique_ingredient_names(cls, values):
        names = [ingredient.name for ingredient in values.nutritional_table]
        if len(names) != len(set(names)):
            raise ValueError("Ingredient names must be unique")
        return values

    def get_ingredients(self, ingredient_list: List[str] = []) -> dict[str, Ingredient]:
        return {
            key: [
                ingredient
                for ingredient in self.nutritional_table
                if ingredient.name == key
            ][0]
            for key in ingredient_list
        }
