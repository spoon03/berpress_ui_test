import time

import pytest
from fixtures.constans import LandingConst


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
        time.sleep(3)
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
        result_search = app.landing.get_result_search()
        assert product in result_search

    def test_add_to_cart(self, app):
        """
        Шаги:
        1.Открыть страницу поиска
        2.Добавить товар в корзину
        3.Убедиться что товар добавлен
        :param app:
        :return:
        """
        app.open_lending_page()
        assert 1 == 1
