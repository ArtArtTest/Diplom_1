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

    @allure.title("Проверка, что имена булочек называются как нужно")
    def test_available_buns_have_correct_names(self):
        db = Database()
        expected_names = {"black bun", "white bun", "red bun"}
        actual_names = {bun.get_name() for bun in db.available_buns()}
        assert actual_names == expected_names

    @allure.title("Проверка, что возвращается 6 ингредиентов")
    def test_available_ingredients_returns_six_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    @allure.title("Проверка, что доступно 3 соуса")
    def test_database_has_three_sauces(self):
        db = Database()
        sauces = [ing for ing in db.available_ingredients() if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

    @allure.title("Проверка, что доступно 3 начинки")
    def test_database_has_three_fillings(self):
        db = Database()
        fillings = [ing for ing in db.available_ingredients() if ing.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3

    @allure.title("Проверка, что имена соусов называются как нужно")
    def test_sauce_names_are_correct(self):
        db = Database()
        sauce_names = {ing.get_name() for ing in db.available_ingredients() if ing.get_type() == INGREDIENT_TYPE_SAUCE}
        expected = {"hot sauce", "sour cream", "chili sauce"}
        assert sauce_names == expected

    @allure.title("Проверка, что имена начинок называются как нужно")
    def test_filling_names_are_correct(self):
        db = Database()
        filling_names = {ing.get_name() for ing in db.available_ingredients() if ing.get_type() == INGREDIENT_TYPE_FILLING}
        expected = {"cutlet", "dinosaur", "sausage"}
        assert filling_names == expected
        
