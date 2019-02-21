from tests.methods import *


class TestMobile:

    def test_unsuccess_auth(self, driver):
        start_activity(driver)
        open_page_for_sign_in(driver)
        enter_login_password(driver, 'tgdj@gmail.com', 'qqqqqqqq')
        result = check_authorisation(driver, 'Account does not exist. Please register an account to start shopping.')
        assert result
        driver.quit()
