import time

from fixtures.constans import Url
from fixtures.pages.landing_page import LandingPage
from fixtures.pages.cart_page import CartPage
import logging

logger = logging.getLogger("press")


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.landing = LandingPage(self)
        self.cart = CartPage(self)

    def quit(self) -> None:
        """Закрытие окна браузера."""
        self.driver.quit()
        logger.info("Браузер закрыт")

    def open_lending_page(self) -> None:
        """Открытие страницы приложения"""
        logger.info(f"Открытие страницы {self.url+Url.LENDING_URL}")
        self.driver.get(self.url + Url.LENDING_URL)
        time.sleep(1)
