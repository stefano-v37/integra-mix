import unittest

import pytest

from integra_mix.models import Ingredient, Integrator, Quantity

qt1_dict = {"name": "test_qt_1", "quantity": 3, "measurement_unit": "g"}
qt2_dict = {"name": "test_qt_2", "quantity": 300, "measurement_unit": "mg"}

ing1_dict = {**qt1_dict, **{"name": "test_ingredient_1", "source": "100% CreaPURE"}}
ing2_dict = {**qt1_dict, **{"name": "test_ingredient_2"}}
ing3_dict = {**qt1_dict, **{"name": "test_ingredient_1"}}

integ1_dict = {
    "name": "test_integrator_1",
    "cost": 50,
    "vendor": "Yamamoto website",
    "nutritional_table": [ing1_dict, ing2_dict],
}

integ2_dict = {
    "name": "test_integrator_1",
    "cost": 50,
    "vendor": "Yamamoto website",
    "nutritional_table": [ing1_dict, ing3_dict],
}


class TestModels(unittest.TestCase):
    def test_quantity(self):
        qt1 = Quantity(**qt1_dict)
        self.assertEqual(qt1.quantity, 3)

    def test_ingredient(self):
        ing1 = Ingredient(**ing1_dict)
        self.assertEqual(ing1.name, "test_ingredient_1")
        self.assertEqual(ing1.quantity, 3)
        self.assertEqual(ing1.source, "100% CreaPURE")

    def test_integrator(self):
        integ1 = Integrator(**integ1_dict)
        self.assertEqual(integ1.name, "test_integrator_1")
        self.assertEqual(integ1.cost, 50)

        self.assertEqual(
            integ1.get_ingredients(["test_ingredient_1", "test_ingredient_2"])
            .get("test_ingredient_1")
            .quantity,
            3,
        )

    def test_failure_integrator(self):
        with pytest.raises(ValueError, match="Ingredient names must be unique"):
            Integrator(**integ2_dict)
