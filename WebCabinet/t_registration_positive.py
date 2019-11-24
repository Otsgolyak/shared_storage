from selenium import webdriver
from PageObject.cabinet.login_page import RegistrationPage
import unittest


class RegistrationPositiveTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        capabilities = {
            "browserName": "chrome",
                        }
        cls.driver = webdriver.Remote(desired_capabilities=capabilities,
                                      command_executor="http://195.201.213.204:4444/wd/hub", options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.get('https://trade.trademux.net/cabinet/signup') # Переходим на сайт
        reg_page = RegistrationPage(cls.driver)
        reg_page.page_is_loaded() # Проверка загрузки страницы

    def test_01_registration_positive(self):
        """Тест успешной регистрации, добавлять 1 к номеру при успешном выполнении"""
        reg_page = RegistrationPage(self.driver)
        # Заполняем данные
        reg_page.typing(reg_page.name_inp(), 'Denis')
        reg_page.typing(reg_page.login_inp(), 'shanterrr0017@yahoo.com') # Нужно добавлять 1 при успешном выполнении
        reg_page.typing(reg_page.password_inp(), 'Qweqwe321!')
        reg_page.typing(reg_page.confirm_password_inp(), 'Qweqwe321!')
        reg_page.typing(reg_page.tel_inp(), '+12345678')
        reg_page.typing(reg_page.promokod_inp(), '12345qwer')
        # Кликаем на галочки
        reg_page.galka_1_cbx_click()
        reg_page.galka_2_cbx_click()
        reg_page.galka_3_cbx_click()
        reg_page.registration_btn().click() # Нажимаем кнопку регистрация
        assert reg_page.deposit_on_trade_page_btn().is_displayed, "is not displayed" # Ждем загрузку элемента с торговой страницы

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()









