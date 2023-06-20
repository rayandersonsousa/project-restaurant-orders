import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path) as file:
            data = csv.DictReader(file)
            dishes_dict = {}

            for row in data:
                dish_name = row["dish"]
                dish_price = float(row["price"])
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                ingredient = Ingredient(ingredient_name)
                dish = dishes_dict.get(dish_name)

                if dish is None:
                    dish = Dish(dish_name, dish_price)
                    dishes_dict[dish_name] = dish
                    self.dishes.add(dish)

                dish.add_ingredient_dependency(ingredient, recipe_amount)
