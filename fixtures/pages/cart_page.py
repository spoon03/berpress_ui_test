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
        pass

    def remove_item(self) -> None:
        """
        Уменьшить количество товаров.
        :return:
        """
        pass
