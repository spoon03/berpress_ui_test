import logging

from fixtures.pages.base_page import BasePage
from fixtures.locators.landing import LandingLocators

logger = logging.getLogger("press")


class LandingPage(BasePage):
    """Класс с описанием методов главной страницы."""

    def search(self, text: str, is_submit: bool = True) -> None:
        """
        Поиск товара на главной странице.
        :param text: Текст для поиска
        :param is_submit: Нажать кнопку поиска
        """
        logger.info(f"Поиск продукта {text} в магазине")
        self.fill_element(data=text, locator=LandingLocators.SEARCH_INPUT)
        if is_submit:
            self.click_element(locator=LandingLocators.SEARCH_BUTTON)

    def get_result_search(self) -> str:
        """Возвращает результат поиска"""
        logger.info("Отображение результатов поиска")
        text = self.get_text(locator=LandingLocators.RESULT_SEARCH)
        return text

    def buy(self, goods: str = "bananas") -> None:
        """
        Добавление товара в корзину.
        :param goods: покупаемый товар
        :return:
        """
        logger.info(f"Добавление товара {goods} в корзину")
        self.click_element(locator=LandingLocators.BUY_BUTTON(goods=goods))
