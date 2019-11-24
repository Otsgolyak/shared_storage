from selenium import webdriver
from PageObject.cabinet.login_page import LoginPage
from PageObject.cabinet.profile_page import FooterPage
import unittest


class FooterTestSuite(unittest.TestCase):

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
        footer = FooterPage(cls.driver)
        footer.page_is_loaded() # Проверяем загрузку страницы

    def setUp(self):
        self.driver.refresh() # Обновляем страницу
        footer = FooterPage(self.driver)
        footer.page_is_loaded() # Проверяем загрузку страницы

    def test_01_check_footer_term_of_website_use_lnk(self):
        """Проверка ссылок подвала"""
        footer = FooterPage(self.driver)
        footer.term_of_website_use_lnk().click() # Переходим по ссылке
        self.driver.switch_to_window(self.driver.window_handles[1]) # Меняем действующее окно браузера
        assert self.driver.current_url == 'https://trademux.net/docs/terms_of_use.html'

    def test_02_check_footer_provacy_policy_lnk(self):
        """Проверка ссылок подвала"""
        footer = FooterPage(self.driver)
        footer.provacy_policy_lnk().click() # Переходим по ссылке
        self.driver.switch_to_window(self.driver.window_handles[1]) # Меняем действующее окно браузера
        assert self.driver.current_url == 'https://trademux.net/docs/privacy_policy.html'

    def test_03_check_footer_risk_disclosure_notice_lnk(self):
        """Проверка ссылок подвала"""
        footer = FooterPage(self.driver)
        footer.risk_disclosure_notice_lnk().click() # Переходим по ссылке
        self.driver.switch_to_window(self.driver.window_handles[1]) # Меняем действующее окно браузера
        assert self.driver.current_url == 'https://trademux.net/docs/risk_disclosure_notice.html'

    def test_04_check_footer_conflict_of_interest_policy_lnk(self):
        """Проверка ссылок подвала"""
        footer = FooterPage(self.driver)
        footer.conflict_of_interest_policy_lnk().click() # Переходим по ссылке
        self.driver.switch_to_window(self.driver.window_handles[1]) # Меняем действующее окно браузера
        assert self.driver.current_url == 'https://trademux.net/docs/conflict_of_interest_policy_statement.html'

    def test_05_check_footer_order_execution_policy_lnk(self):
        """Проверка ссылок подвала"""
        footer = FooterPage(self.driver)
        footer.order_execution_policy_lnk().click() # Переходим по ссылке
        self.driver.switch_to_window(self.driver.window_handles[1])
        assert self.driver.current_url == 'https://trademux.net/docs/order_execution_policy.html'

    def test_06_check_footer_refund_policy_lnk(self):
        """Проверка ссылок подвала"""
        footer = FooterPage(self.driver)
        footer.refund_policy_lnk().click() # Переходим по ссылке
        self.driver.switch_to_window(self.driver.window_handles[1]) # Меняем действующее окно браузера
        assert self.driver.current_url == 'https://trademux.net/docs/refund_cancellation_policy.html'

    def test_07_check_footer_user_agreement_lnk(self):
        """Проверка ссылок подвала"""
        footer = FooterPage(self.driver)
        footer.user_agreement_lnk().click() # Переходим по ссылке
        self.driver.switch_to_window(self.driver.window_handles[1]) # Меняем действующее окно браузера
        assert self.driver.current_url == 'https://trademux.net/docs/user_agreement.html'

    def test_08_check_footer_anti_money_laundering_lnk(self):
        """Проверка ссылок подвала"""
        footer = FooterPage(self.driver)
        footer.anti_money_laundering_lnk().click() # Переходим по ссылке
        self.driver.switch_to_window(self.driver.window_handles[1]) # Меняем действующее окно браузера
        assert self.driver.current_url == 'https://trademux.net/docs/anti_money_laundering.html'

    def tearDown(self):
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0]) # Меняем действующее окно браузера

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()