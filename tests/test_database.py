import pytest
import allure
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    @pytest.fixture
    def db(self):
        return Database()

    @allure.title("Проверка, что список состоит из 3 булочек")
    def test_available_buns_returns_three_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    @allure.title("Проверка, что возвращается 6 ингредиентов")
    def test_available_ingredients_returns_six_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    @pytest.mark.parametrize(
        "index,name,price",
        [
            (0, "black bun", 100.0),
            (1, "white bun", 200.5),
            (2, "red bun", 0.0),
        ],
    )

    @allure.title("Проверка, что индекс возвращает корректное имя булочки")     
    def test_buns_parametrization(self, index, name, price):

        database = Database()
        buns = database.available_buns()
        bun = buns[index]

        assert bun.name == name

    @pytest.mark.parametrize(
        "index,ingredient_type,name,price",
        [
            (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
        ],
    )

    @allure.title("Проверка, что индекс возвращает корректное имя ингридиента")     
    def test_ingredients_parametrization(self, index,ingredient_type,name,price):
        database = Database()

        ingredients = database.available_ingredients()
        ingredient = ingredients[index]

        assert ingredient.name == name
        
