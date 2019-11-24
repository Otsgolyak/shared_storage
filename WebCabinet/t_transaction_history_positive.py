from selenium import webdriver
from PageObject.cabinet.login_page import LoginPage
from PageObject.cabinet.profile_page import ProfilePage
from PageObject.cabinet.trans_history_page import TransactionHistoryPage
import unittest


class TransHistoryPositiveTestSuite(unittest.TestCase):

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

    def setUp(self):
        self.driver.refresh() # Обновляем страницу
        profile_page = ProfilePage(self.driver)
        profile_page.transaction_history_lnk().click() # Переходим на страницу транзактион хистори
        trans = TransactionHistoryPage(self.driver)
        trans.page_is_loaded() # Проверка загрузки страницы

    def test_01_transaction_history_today(self):
        """Не корректно работает сайт, не грузится таблица, поэтому просто проходим тест без проверок, кроме ожиданий"""
        trans = TransactionHistoryPage(self.driver)
        trans.choice_acccount_slc().select_by_value("REAL-14714") # Выбираем аккаунт
        trans.choice_pariod_slc().select_by_value("Today") # Выбираем период
        trans.load_report_btn().click() # Кликаем на кнопку загрузить отчет
        assert trans.table_tbl().is_displayed(), "is not displayed" # Проверяем, что таблица загрузилась

    def test_02_transaction_history_last_week(self):
        """Тест проверки загрузки отчета за неделю"""
        trans = TransactionHistoryPage(self.driver)
        trans.choice_acccount_slc().select_by_value("REAL-14714") # Выбираем аккаунт
        trans.choice_pariod_slc().select_by_value("Last week") # Выбираем период
        trans.load_report_btn().click() # Кликаем на кнопку загрузить отчет
        assert trans.table_tbl().is_displayed(), "is not displayed" # Проверяем, что таблица загрузилась

    def test_03_transaction_history_last_month(self):
        """Тест проверки загрузки отчета за месяц"""
        trans = TransactionHistoryPage(self.driver)
        trans.choice_acccount_slc().select_by_value("REAL-14714") # Выбираем аккаунт
        trans.choice_pariod_slc().select_by_value("Last month") # Выбираем период
        trans.load_report_btn().click() # Кликаем на кнопку загрузить отчет
        assert trans.table_tbl().is_displayed(), "is not displayed" # Проверяем, что таблица загрузилась

    def test_04_transaction_history_last_year(self):
        """Тест проверки загрузки отчета за год"""
        trans = TransactionHistoryPage(self.driver)
        trans.choice_acccount_slc().select_by_value("REAL-14714") # Выбираем аккаунт
        trans.choice_pariod_slc().select_by_value("Last Year") # Выбираем период
        trans.load_report_btn().click() # Кликаем на кнопку загрузить отчет
        assert trans.table_tbl().is_displayed(), "is not displayed" # Проверяем, что таблица загрузилась

    def test_05_transaction_history_custom_period(self):
        """Тест проверки загрузки отчета за выбранный период"""
        import datetime
        date = datetime.datetime.now() # Получаем текущую дату
        trans = TransactionHistoryPage(self.driver)
        trans.page_is_loaded() # Проверка загрузки страницы
        trans.choice_acccount_slc().select_by_value("REAL-14714") # Выбираем аккаунт
        trans.choice_pariod_slc().select_by_value("Custom period") # Выбираем период
        trans.choice_custom_pariod_inp().click() # Кликаем для открытия формы ввода пользовательского периода
        trans.form_choice_custom_period_is_loaded() # Проверяем, что загрузилась форма для ввода пользовательского периода
        trans.typing(trans.choice_custom_pariod_start_inp(), '11-01-2019') # Начальный период
        trans.typing(trans.choice_custom_pariod_end_inp(), '{}-{}-{}'.format(date.month, date.day, date.year)) # Конечный период (подставляем текущую дату)
        assert trans.confirm_custom_pariod_btn().is_displayed(), "is not displayed" # Ждем пока станет видима кнопка подтверждения пользовательского периода
        trans.confirm_custom_pariod_btn().click() # Кликаем по кнопке подтверждения периода
        assert trans.load_report_btn().is_displayed(), "is not displayed" # Ждем пока станет видима кнопка загрузкить отчет
        trans.load_report_btn().click() # Кликаем на кнопку загрузить отчет
        assert trans.table_tbl().is_displayed(), "is not displayed" # Проверяем, что таблица загрузилась

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
