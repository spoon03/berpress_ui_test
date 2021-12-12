import logging
import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger("press")


class BasePage:
    def __init__(self, app):
        self.app = app

    def custom_find_elements(self, locator, wait_time=10) -> list:
        """
        Поиск всех элементов на странице с указанным локатором.
        :param locator: Локатор
        :param wait_time: Время ожидания
        :return: Список вебэлементов
        """
        elements = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Не найден элемент с локатором {locator}",
        )
        return elements

    def click_element(self, locator, wait_time=10) -> None:
        """
        Клик по элементу.
        :param locator: Локатор элемента
        :param wait_time: Время ожидания
        :return:
        """
        elements = self.custom_find_elements(locator, wait_time)
        element = elements[0]
        logger.info(f"Нажатие на элемент с локатором {locator}")
        timestamp = time.time() + wait_time
        while time.time() < timestamp:
            try:
                element.click()
                break
            except ElementClickInterceptedException:
                time.sleep(0.5)

    def fill_element(self, data, locator, wait_time=10) -> None:
        """
        Ввод текста в поле.
        :param wait_time:Ожидание элемента
        :param locator:Локатор
        :param data: Данные для ввода
        """
        element = self.custom_find_elements(locator, wait_time)[0]
        logger.info(f"Заполняем {element} данными {data}")
        if data:
            element.send_keys(data)

    def get_text(self, locator, wait_time=10) -> list:
        """
        Получение текста всех элементов найденных по локатору.
        :param locator: Локатор
        :param wait_time: Ожидание
        :return: Текст на элементе
        """
        result_text = []
        elements = self.custom_find_elements(locator, wait_time)
        time.sleep(0.5)
        for element in elements:
            logger.info(f"Для  {element} получен текст {element.text}")
            result_text.append(element.text)
        return result_text
