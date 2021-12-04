import random
from fixtures.constans import LandingConst


class TestCart:
    def test_add_item(self, app):
        """
        Шаги:
        1.Открыть страницу поиска
        2.Добавить товар в корзину
        3.Открыть корзину.
        4.Увеличить кол-во товаров на 1 шт
        5. Проверить что пересчиталась сумма
        :param app:
        :return:
        """
        app.open_lending_page()
        app.landing.buy(random.choice(LandingConst.TEST_EXIST_GOODS))
        app.cart.open_cart()
        # cart_text = app.landing.get_text(locator=CartLocators.CART_TITLE)
        app.cart.add_item()
        # cart_text2 = app.landing.get_text(locator=CartLocators.CART_TITLE)
        assert 1 == 1

    def test_remove_item(self, app):
        """
        Шаги:
        1.Открыть страницу поиска
        2.Добавить товар в корзину
        3.Открыть корзину.
        4.Уменьшить кол-во товаров на 1 шт
        5. Проверить что пересчиталась сумма
        :param app:
        :return:
        """
        app.open_lending_page()
        app.landing.buy(random.choice(LandingConst.TEST_EXIST_GOODS))
        app.cart.open_cart()
        app.cart.remove_item()
        assert 1 == 1

    def test_del(self, app):
        """
        Шаги:
        1.Открыть страницу поиска
        2.Добавить товар в корзину
        3.Убедиться что товар добавлен
        4.Открыть корзину
        4.Удалить товар из корзины
        5.Убедиться что товар удален
        :param app:
        :return:
        """
        app.open_lending_page()
        assert 1 == 1

    def test_buy(self, app):
        """
        Шаги:
        1.Открыть страницу поиска
        2.Добавить товар в корзину
        3.Убедиться что товар добавлен
        4.Открыть корзину
        5.Нажать кнопку Купить
        6.Убедиться что покупка прошла успешно
        :param app:
        :return:
        """
        app.open_lending_page()
        assert 1 == 1
