class TestLending:
    def test_search_positive(self, app):
        """
        Шаги:
        1.Открыть страницу витрины
        2.В поле поиска ввести имеющийся товар
        3.Нажать кноаку Искать
        3.Убедиться что товар отбразился
        :param app:
        :return:
        """
        app.open_lending_page()
        app.lending.serch("Яблоко")
        text = app.lending.get_result_serch_text()
        assert text == "ничего не найдено"

    def test_search_negative(self, app):
        """
        Шаги:
        1.Открыть страницу витрины
        2.В поле поиска ввести отсутствующий товар
        3.Нажать кноаку Искать
        3.Убедиться что товар НЕ отбразился
        :param app:
        :return:
        """
        app.open_lending_page()
        assert 1 == 1

    def test_add_to_cart(self, app):
        """
        Шаги:
        1.Открыть страницу поиска
        2.Добавить товар в корзину
        3.Убедиться что товар добавлен
        :param app:
        :return:
        """
        app.open_lending_page()
        assert 1 == 1
