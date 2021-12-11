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


class CartLocators:
    """Селекторы для корзины"""

    CART_BUTTON = (By.CSS_SELECTOR, "i.material-icons")
    CART_TITLE = (By.CSS_SELECTOR, "li.collection-item")
    CART_ADD_ITEM = (
        By.XPATH,
        ".//i[@class = 'material-icons basket-quantity' and contains(text(),'add')]",
    )
    CART_REMOVE_ITEM = (
        By.XPATH,
        ".//i[@class = 'material-icons basket-quantity' and contains(text(),'remove')]",
    )
    CART_DELETE_ITEM = (
        By.XPATH,
        ".//i[@class = 'material-icons basket-delete' and contains(text(),'close')]",
    )
    CART_BUY_BUTTON = (
        By.XPATH,
        ".//li/button[@class = 'btn red btn-small' and contains(text(),'Buy')]",
    )
    CART_DONE_POPUP = (
        By.XPATH,
        ".//div[@class = 'toast' and contains(text(),'Pay done!')]",
    )
