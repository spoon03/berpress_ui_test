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
        logger.info(f"Search product {text} in the store")
        self.fill_element(data=text, locator=LandingLocators.SEARCH_INPUT)
        if is_submit:
            self.click_element(locator=LandingLocators.SEARCH_BUTTON)

    def get_result_search(self) -> str:
        """Возвращает результат поиска"""
        logger.info("Search result")
        text = self.get_text(locator=LandingLocators.SEARCH_RESULT)
        return text
