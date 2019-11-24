from selenium import webdriver
from PageObject.cabinet.login_page import LoginPage
from PageObject.cabinet.profile_page import ProfilePage
from PageObject.cabinet.trans_history_page import TransactionHistoryPage
import unittest


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        capabilities = {
            "browserName": "chrome",
                        }
        cls.driver = webdriver.Remote(desired_capabilities=capabilities,
                                        command_executor="http://195.201.213.204:4444/wd/hub", options=chrome_options)
        cls.driver.maximize_window()

        login_page = LoginPage(cls.driver)
        login_page.login(username='shanterrr@yahoo.com', password='qweqwe321!') # Авторизуемся
        profile_page = ProfilePage(cls.driver)
        profile_page.page_is_loaded() # Проверка загрузки страницы
        profile_page.transaction_history_lnk().click() # Переходим в раздел история транзакций
        trans = TransactionHistoryPage(cls.driver)
        trans.page_is_loaded() # Проверка загрузки страницы

    def test_01_transaction_history_custom_period_negative(self):
        """Негативный тест. Выбираем пустой пользовательский перод и проверяем, что кнопка недоступна"""
        trans = TransactionHistoryPage(self.driver)
        trans.choice_acccount_slc().select_by_value("REAL-14714") # Выбираем аккаунт
        trans.choice_pariod_slc().select_by_value("Custom period") # Выбираем период
        trans.choice_custom_pariod_inp().click() # Кликаем для открытия формы ввода пользовательского периода
        trans.form_choice_custom_period_is_loaded() # Проверяем загрузку формы выбора периода
        trans.typing(trans.choice_custom_pariod_end_inp(), '') # Очищаем поле "конечный период"
        trans.typing(trans.choice_custom_pariod_start_inp(), '') # Очищаем поле "начальный период"
        assert trans.confirm_custom_pariod_btn().get_attribute('disabled') # Проверяем недоступность кнопки

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
