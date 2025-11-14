import allure
import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize("name,price", [
        ("black bun", 100.0),
        ("white bun", 200.5),
        ("red bun", 0.0),
    ])
    @allure.title("Проверка, что булочка корректно возвращает название")
    def test_bun_get_name_returns_correct_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name,price", [
        ("black bun", 100.0),
        ("white bun", 200.5),
        ("red bun", 0.0),
    ])
    @allure.title("Проверка, что булочка корректно возвращает цену")
    def test_bun_get_price_returns_correct_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

