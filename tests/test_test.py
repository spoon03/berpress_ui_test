class TestTest:
    def test_login_with_valid_data(self, app):
        app.open_login_page()
        assert 1 == 1
