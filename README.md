![example workflow](https://github.com/spoon03/berpress_ui_test/actions/workflows/github-actions-demo.yml/badge.svg)

# berpress_ui_test
Selenium/Python


Use python 3.9 +
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

Test app https://berpress.github.io/online-grocery-store
```
https://berpress.github.io/online-grocery-store
```

Создание отчетов
```
pytest --alluredir=allure-results/
```

Просмотр отчетов
```
allure serve allure-results

*Предварительно установить allure serve
https://docs.qameta.io/allure/
```

Запуск CI
```
Для git actions подготовлен конфиг
github-actions-demo.yml
```

Цель и краткое описание проекта
```
berpress - магазин по продаже продуктов питания.
Необходимо покрыть:
1. Поиск товаров (негативный и позитивный сценарий)
2. Добавление товара в корзину
3. Работа с корзиной: удаление/добавление товара и покупка
```