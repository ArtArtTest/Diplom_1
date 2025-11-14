import pytest
from unittest.mock import Mock
import allure
from praktikum.burger import Burger


class TestBurger:

    @allure.title("Проверка установки булочки")
    def test_set_buns_sets_correct_bun(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title("Проверка добавления ингридиента")
    def test_add_ingredient_adds_to_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    @allure.title("Проверка, что ингредиент удаляется по индексу")
    @pytest.mark.parametrize("initial_count, remove_index, expected_count", [
        (3, 0, 2),
        (3, 1, 2),
        (3, 2, 2),
    ])
    def test_remove_ingredient_removes_correctly(self, initial_count, remove_index, expected_count):
        burger = Burger()
        mock_ingredients = [Mock() for _ in range(initial_count)]
        burger.ingredients = mock_ingredients[:]
        burger.remove_ingredient(remove_index)
        assert len(burger.ingredients) == expected_count
        assert mock_ingredients[remove_index] not in burger.ingredients

    @allure.title("Проверка, ингредиент перемещается с индекса на индекс")
    @pytest.mark.parametrize("from_idx, to_idx, expected_order", [
        (0, 2, [1, 2, 0]),
        (2, 0, [2, 0, 1]),
        (1, 1, [0, 1, 2]),  
    ])
    def test_move_ingredient_moves_correctly(self, from_idx, to_idx, expected_order):
        burger = Burger()
        ingredients = []
        for i in range(3):
            mock = Mock()
            mock.id = i  
            ingredients.append(mock)
        burger.ingredients = ingredients

        burger.move_ingredient(from_idx, to_idx)

        actual_order = [ing.id for ing in burger.ingredients]
        assert actual_order == expected_order

    @allure.title("Проверка расчета стоимости бургера")
    def test_get_price_calculates_correctly(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        mock_ing1, mock_ing2, mock_ing3 = Mock(), Mock(), Mock()
        mock_ing1.get_price.return_value = 50.0
        mock_ing2.get_price.return_value = 75.0
        mock_ing3.get_price.return_value = 25.0

        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        burger.add_ingredient(mock_ing3)

        expected_price = 100.0 * 2 + 50.0 + 75.0 + 25.0  # = 350.0
        assert burger.get_price() == expected_price

    @allure.title("Проверка генерации чека")
    def test_get_receipt_returns_correct_string(self):

        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        burger.set_buns(mock_bun)

        mock_sauce = Mock()
        mock_sauce.get_type.return_value = "SAUCE"
        mock_sauce.get_name.return_value = "sour cream"

        mock_filling = Mock()
        mock_filling.get_type.return_value = "FILLING"
        mock_filling.get_name.return_value = "cutlet"

        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        mock_bun.get_price.return_value = 100.0
        mock_sauce.get_price.return_value = 50.0
        mock_filling.get_price.return_value = 100.0

        receipt = burger.get_receipt()

        expected_lines = [
            "(==== black bun ====)",
            "= sauce sour cream =",
            "= filling cutlet =",
            "(==== black bun ====)",  
            "",                       
            "Price: 350.0"
        ]
        expected_receipt = "\n".join(expected_lines)
        assert receipt == expected_receipt

        