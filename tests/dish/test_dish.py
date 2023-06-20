from src.models.dish import Dish, Ingredient  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    pudim = Dish("pudim", 5.50)
    ingredient = Ingredient("leite")

    assert pudim == Dish("pudim", 5.50)
    assert pudim != Dish("bolo", 7.50)

    assert pudim.name == "pudim"

    assert hash(pudim) == hash(repr(pudim))
    assert repr(pudim) == "Dish('pudim', R$5.50)"

    pudim.add_ingredient_dependency(ingredient, 1)

    assert pudim.get_ingredients() == {ingredient}
    assert pudim.get_restrictions() == ingredient.restrictions

    with pytest.raises(TypeError):
        Dish("pudim", "5.50")

    with pytest.raises(ValueError):
        Dish("pudim", -5)
