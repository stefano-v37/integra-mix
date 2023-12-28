from typing import Literal

from pydantic import BaseModel, Field

measurement_units = Literal["g", "mg"]
measurement_units_to_standard = {"g": 10**-3, "mg": 10**-6}


class Quantity(BaseModel):
    name: str = Field(default=None, description="name of the quantity")
    quantity: float = Field(default=None, description="numeric value of the quantity")
    measurement_unit: measurement_units = Field(
        default=None, description="measurement unit of the quantity"
    )
