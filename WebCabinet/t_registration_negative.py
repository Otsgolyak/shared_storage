from selenium import webdriver
from PageObject.cabinet.login_page import RegistrationPage
import unittest


class RegistrationNegativeTestSuite(unittest.TestCase):

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

    def test_01_registration_negative(self):
        """Регистрация с невалидным емэйлом"""
        reg_page = RegistrationPage(self.driver)
        # Заполняем данные
        reg_page.page_is_loaded() # Проверка загрузки страницы
        reg_page.typing(reg_page.name_inp(), 'Denis')
        reg_page.typing(reg_page.login_inp(), '@trademux.net')
        reg_page.typing(reg_page.password_inp(), 'Qweqwe321!')
        reg_page.typing(reg_page.confirm_password_inp(), 'Qweqwe321!')
        reg_page.typing(reg_page.tel_inp(), '+12345678')
        reg_page.typing(reg_page.promokod_inp(), '')
        # Кликаем на галочки
        reg_page.galka_1_cbx_click()
        reg_page.galka_2_cbx_click()
        reg_page.galka_3_cbx_click()
        reg_page.registration_btn().click() # Нажимаем кнопку регистрация
        assert reg_page.validation_massage_txt() == 'Email is not valid.' # Проверка валидирующего сообщения

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()

