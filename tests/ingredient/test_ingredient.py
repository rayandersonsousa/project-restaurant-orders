from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("camarão")

    assert ingredient == Ingredient("camarão")

    assert ingredient.name == "camarão"

    assert repr(ingredient) == f"Ingredient('camarão')"

    assert hash(ingredient) == hash(Ingredient("camarão"))
    assert hash(ingredient) != hash(Ingredient("carne"))

    assert ingredient.restrictions == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
    }
