class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def quit(self):
        self.driver.quit()

    def open_login_page(self):
        self.driver.get(self.url)

    def open_register_page(self):
        self.driver.get(self.url)
