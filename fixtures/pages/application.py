from fixtures.constans import Url
import logging

logger = logging.getLogger("moodle")


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def quit(self):
        self.driver.quit()
        logger.info("Close browser")

    def open_lending_page(self):
        logger.info(f"Open page {self.url+Url.LENDING_URL}")
        self.driver.get(self.url + Url.LENDING_URL)
