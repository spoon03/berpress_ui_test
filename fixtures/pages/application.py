from fixtures.constans import Url
from fixtures.pages.landing_page import LandingPage
import logging

logger = logging.getLogger("press")


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.landing = LandingPage(self)
        # self.register = RegisterPage(self)

    def quit(self):
        self.driver.quit()
        logger.info("Close browser")

    def open_lending_page(self):
        logger.info(f"Open page {self.url+Url.LENDING_URL}")
        self.driver.get(self.url + Url.LENDING_URL)
