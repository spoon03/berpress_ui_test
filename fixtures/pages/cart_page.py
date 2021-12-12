import logging

from fixtures.pages.base_page import BasePage
from fixtures.locators.landing import CartLocators

logger = logging.getLogger("press")


class CartPage(BasePage):
    """Класс с описанием методов корзины."""

    def open_cart(self) -> None:
        """
        Открыть корзину.
        :return:
        """
        logger.info("Переход в корзину")
        self.click_element(locator=CartLocators.CART_BUTTON)

    def add_item(self) -> None:
        """
        Увеличить количество товаров.
        :return:
        """
        logger.info("Увеличиваем количество товара на 1ед.")
        self.click_element(locator=CartLocators.CART_ADD_ITEM)

    def remove_item(self) -> None:
        """
        Уменьшить количество товаров.
        :return:
        """
        logger.info("Уменьшаем количество товара на 1ед.")
        self.click_element(locator=CartLocators.CART_REMOVE_ITEM)

    def get_product_total_price(self, product: str) -> float:
        """
        Ищем итоговую стоимость для заданного продукта
        :param product: Имя продукта
        :return: Значение стоимости
        """
        cart_text = self.get_text(locator=CartLocators.CART_TITLE)
        product_price_string = ""
        for line in cart_text:
            if line.find(product) != -1:
                product_price_string = line
                break
        if product_price_string == "":
            assert False, f"В корзине не найден продукт {product}"
        product_total_price = product_price_string[
            (product_price_string.find("= ") + 2) : product_price_string.find(" руб")
        ]
        return float(product_total_price)

    def delete(self) -> None:
        """
        Удалить товар.
        :return:
        """
        logger.info("Удаление товара")
        self.click_element(locator=CartLocators.CART_DELETE_ITEM)

    def buy(self) -> None:
        """
        Покупка всех товаров из корзины.
        :return:
        """
        logger.info("Покупка товаров")
        self.click_element(locator=CartLocators.CART_BUY_BUTTON)
