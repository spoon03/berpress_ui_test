Что тестируем: https://berpress.github.io/online-grocery-store/
Инструменты для тестирования: Python, pytest, allure/html-report
Проект должен быть расположен на GitHub


Что должно быть сделано (минимум):
1. Отчеты  Allure / html-report
2. Полная инструкция и описание того, как установить и запустить тесты
3. В проекте необходимо иметь линтер
4. В проект необходимо добавить CI/CD (какой именной на ваше усмотрение)
5. Тесты
6. Добавить в проект логгирование
7. Использовать Page Object

Минимум тестов:
1.  Поиск товаров (негативный и позитивный сценарий)
2. Добавление товара в корзину
3. Работа с корзиной: удаление/добавление товара и покупка

[![Build Status](https://app.travis-ci.com/berpress/moodle_ui_test.svg?branch=main)](https://app.travis-ci.com/berpress/moodle_ui_test)
# moodle_ui_test
Selenium/Python


Use python 3.8 +
Create and activate virtual environments

```
python3 -m venv env
source env/bin/activate
```

Run in terminal

```
pip install -r requirements.txt
```

pre-commit https://pre-commit.com
```
pre-commit run --all-files
```

Test app
```
https://qacoursemoodle.innopolis.university
```


pytest --alluredir=allure-results/
