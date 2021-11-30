from selenium.webdriver.common.by import By


class LandingLocators:
    """Класс для описания локаторов главной страницы"""

    SEARCH_INPUT = (By.ID, "email_inline")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.search-btn")
    SEARCH_RESULT = (By.CLASS_NAME, "card-title")
    NO_RESULT_SEARCH = (By.CSS_SELECTOR, "h3")
