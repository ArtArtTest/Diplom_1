import pytest
import allure
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.fixture(params=[
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 50.0),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100.0),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300.0),
    ])
    def ingredient_params(self, request):
        return request.param

    @allure.title("Проверка, что возвращается корректный тип")
    def test_get_type_returns_correct_type(self, ingredient_params):
        ing_type, name, price = ingredient_params
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_type() == ing_type

    @allure.title("Проверка, что возвращается корректное название")
    def test_get_name_returns_correct_name(self, ingredient_params):
        ing_type, name, price = ingredient_params
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_name() == name

    @allure.title("Проверка, что возвращается корректная цена")
    def test_get_price_returns_correct_price(self, ingredient_params):
        ing_type, name, price = ingredient_params
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_price() == price
