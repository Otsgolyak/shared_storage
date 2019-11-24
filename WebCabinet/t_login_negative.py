from selenium import webdriver
from PageObject.cabinet.login_page import LoginPage
import unittest


class LoginNegativeTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        capabilities = {
            "browserName": "chrome",
                        }
        cls.driver = webdriver.Remote(desired_capabilities=capabilities,
                                        command_executor="http://195.201.213.204:4444/wd/hub", options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.get('https://trade.trademux.net/cabinet/login')  # Перехаодим на нужный урл
        login_page = LoginPage(cls.driver)
        login_page.page_is_loaded() # Проверка загрузки страницы

    def setUp(self):
        self.driver.refresh() # Обновляем страницу
        login_page = LoginPage(self.driver)
        login_page.page_is_loaded() # Проверка загрузки страницы

    def test_01_auth_negative(self):
        """Проверяет авторизацию с некорректными данными"""
        login_page = LoginPage(self.driver)
        # Вводим данные пользователя и кликаем "логин"
        login_page.typing(login_page.login_inp(), '@yahoo.com') #Correct
        login_page.typing(login_page.password_inp(), '12345') # Incorrect
        login_page.login_btn().click()
        assert login_page.heading_txt() == 'Invalid login or password, try again' # Проверяем заголовок

    def test_02_auth_negative(self):
        """Проверяет авторизацию с некорректными данными"""
        login_page = LoginPage(self.driver)
        # Вводим данные пользователя и кликаем "логин"
        login_page.typing(login_page.login_inp(), '123@trademux.net') # Incorrect
        login_page.typing(login_page.password_inp(), '12345') # Incorrect
        login_page.login_btn().click()
        assert login_page.heading_txt() == 'Invalid login or password, try again' # Проверяем заголовок

    def test_03_auth_negative(self):
        """Проверяет авторизацию с некорректными данными"""
        login_page = LoginPage(self.driver)
        # Вводим данные пользователя и кликаем "логин"
        login_page.typing(login_page.login_inp(), '123@trademux.net') # Incorrect
        login_page.typing(login_page.password_inp(), '') # Empty
        login_page.login_btn().click()
        assert login_page.heading_txt() == 'Login to account' # Проверяем заголовок

    def test_04_auth_negative(self):
        """Проверяет авторизацию с некорректными данными"""
        login_page = LoginPage(self.driver)
        # Вводим данные пользователя и кликаем "логин"
        login_page.typing(login_page.login_inp(), 'shanterrr@yahoo.com') # Correct
        login_page.typing(login_page.password_inp(), '') # Empty
        login_page.login_btn().click()
        # Проверяем сообщение о незаполненном текстовом поле
        assert login_page.password_inp().get_attribute('placeholder') == '* This field is required'

    def test_05_auth_negative(self):
        """Проверяет авторизацию с некорректными данными"""
        login_page = LoginPage(self.driver)
        # Вводим данные пользователя и кликаем "логин"
        login_page.typing(login_page.login_inp(), '') # Empty
        login_page.typing(login_page.password_inp(), '') # Empty
        login_page.login_btn().click()
        # Проверяем сообщение о незаполненных текстовых полях
        assert login_page.login_inp().get_attribute('placeholder') == '* This field is required'
        assert login_page.password_inp().get_attribute('placeholder') == '* This field is required'

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()