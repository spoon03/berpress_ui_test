import pytest
from fixtures.constans import LandingConst
from fixtures.locators.landing import LandingLocators
from fixtures.locators.landing import CartLocators


class TestLending:
    @pytest.mark.parametrize("product", LandingConst.TEST_EXIST_GOODS)
    def test_search_positive(self, app, product):
        """
        Шаги:
        1.Открыть страницу витрины
        2.В поле поиска ввести имеющийся товар
        3.Нажать кноаку Искать
        3.Убедиться что товар отбразился
        :param app:
        :return:
        """
        app.open_lending_page()
        app.landing.search(product)
        result_search = app.landing.get_result_search()
        assert product in result_search

    @pytest.mark.parametrize("product", LandingConst.TEST_NON_EXIST_GOODS)
    def test_search_negative(self, app, product):
        """
        Шаги:
        1.Открыть страницу витрины
        2.В поле поиска ввести отсутствующий товар
        3.Нажать кноаку Искать
        3.Убедиться что товар НЕ отбразился
        :param app:
        :return:
        """
        app.open_lending_page()
        app.landing.search(product)
        result = app.landing.get_text(LandingLocators.NO_RESULT_SEARCH)[0]
        assert result == LandingConst.NO_RESULT_TEXT

    @pytest.mark.parametrize("product", LandingConst.TEST_EXIST_GOODS)
    def test_add_to_cart(self, app, product):
        """
        Шаги:
        1.Открыть страницу поиска
        2.Добавить товар в корзину
        3.Открыть корзину
        4.Убедиться что товар добавлен
        :param app:
        :return:
        """
        app.open_lending_page()
        app.landing.buy(product)
        app.cart.open_cart()
        cart_text = app.landing.get_text(locator=CartLocators.CART_TITLE)
        cart_title = cart_text[0]
        assert cart_title == "Корзина"
        add_goods = cart_text[1]
        assert add_goods.find(product) != -1
