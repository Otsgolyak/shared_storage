from selenium import webdriver
from PageObject.cabinet.login_page import LoginPage
from PageObject.cabinet.profile_page import ProfilePage
import unittest


class LoginPositiveTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        capabilities = {
            "browserName": "chrome",
                        }
        cls.driver = webdriver.Remote(desired_capabilities=capabilities,
                                      command_executor="http://195.201.213.204:4444/wd/hub", options=chrome_options)
        cls.driver.maximize_window()

    def test_01_auth_positive(self):
        """Заходит на сайт https://trade.trademux.net/cabinet/login и авторизуется на нем, ждем проверки авторизации"""
        login_page = LoginPage(self.driver)
        login_page.login(username='shanterrr@yahoo.com', password='qweqwe321!') # Авторизуемся на сайте и логинимся
        profile = ProfilePage(self.driver)
        profile.page_is_loaded() # Проверка загрузки страницы

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()









