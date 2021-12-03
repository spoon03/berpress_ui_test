from selenium.webdriver.common.by import By


class LandingLocators:
    """Класс для описания локаторов главной страницы"""

    SEARCH_INPUT = (By.ID, "email_inline")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.search-btn")
    RESULT_SEARCH = (By.CLASS_NAME, "card-title")
    NO_RESULT_SEARCH = (By.CSS_SELECTOR, "h3")

    @staticmethod
    def BUY_BUTTON(goods: str):
        selector = (
            By.XPATH,
            f".//div/span[@class = 'card-title' and contains(text(),"
            f"'{goods}')]/following::div[1]/button",
        )
        return selector

    CART_BUTTON = (By.CSS_SELECTOR, "i.material-icons")
    CART_TITLE = (By.CSS_SELECTOR, "li.collection-item")
