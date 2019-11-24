from selenium import webdriver
from PageObject.cabinet.login_page import LoginPage
from PageObject.cabinet.profile_page import ProfilePage
from PageObject.cabinet.info_page import InfoPage
import unittest


class InfoTestSuite(unittest.TestCase):

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
        profile = ProfilePage(cls.driver)
        profile.page_is_loaded() # Проверяем загрузку страницы

    def setUp(self):
        self.driver.get('https://trade.trademux.net/cabinet/info/faq') # Переходим в раздел инфо
        self.driver.refresh() # Обновляем страницу
        info = InfoPage(self.driver)
        info.page_is_loaded() # Дожидаемся загрузки страницы

    def test_01_check_links_in_info_page_en(self):
        """Проверка ссылок раздела инфо"""
        info = InfoPage(self.driver)
        info.faq_lnk().click() # Кликаем по ссылке "Чаво"
        assert info.get_content_lst().is_displayed, 'is not displayed'
        assert info.get_content_lst().text.startswith('FAQ') # Проверяем, начало содержимого контента страницы
        assert info.get_content_lst().text.endswith('For technical support go to: support@trademux.net') # ... окончание ...
        info.terms_and_conditions_lnk().click() # Кликаем по ссылке "Правила и условия"
        assert info.get_content_lst().is_displayed, 'is not displayed' # Проверяем, что контент отобразился
        assert info.get_content_lst().text.startswith('Trading') # Проверяем, начало содержимого контента страницы
        assert info.get_content_lst().text.endswith('into trading platform.') # ... окончание ...
        info.help_and_support_lnk().click() # Кликаем по ссылке "Правила и условия"
        assert info.get_content_lst().is_displayed, 'is not displayed' # Проверяем, что контент отобразился
        assert info.get_content_lst().text.startswith('Help and Support') # Проверяем, начало содержимого контента страницы
        assert info.get_content_lst().text.endswith('support@trademux.net') # ... окончание ...
        info.terms_of_bonuses_lnk().click() # Кликаем по ссылке "Правила и условия"
        assert info.get_content_lst().is_displayed, 'is not displayed' # Проверяем, что контент отобразился
        assert info.get_content_lst().text.startswith('Regulation of') # Проверяем, начало содержимого контента страницы
        assert info.get_content_lst().text.endswith('observing this regulation.') # ... окончание ...

    def test_02_check_links_in_content_faq(self):
        """Проверка ссылок из содержимого раздела 'Чаво'"""
        info = InfoPage(self.driver)
        info.faq_lnk().click() # Кликаем по ссылке "Чаво"
        assert info.get_link_in_contents()[1].text == "support@trademux.net" # Проверка текста ссылки на почту
        info.get_link_in_contents()[0].click() # Кликаем по ссылке на профиль
        profile = ProfilePage(self.driver)
        profile.page_is_loaded() # ПРоверяем загрузку страницы

    def test_03_check_links_in_content_help_and_supp(self):
        """Проверка ссылок из содержимого раздела 'Помощь'"""
        info = InfoPage(self.driver)
        info.help_and_support_lnk().click() # Кликаем по ссыдке "ПОмощь и поддержка"
        assert info.get_link_in_contents()[0].text == "support@trademux.net" # Проверка текста ссылки на почту

    def test_04_check_links_in_content_terms_of_bonuses_1(self):
        """Проверка ссылок из содержимого раздела 'Условия бонусов'"""
        info = InfoPage(self.driver)
        info.terms_of_bonuses_lnk().click() # Кликаем по ссылке "Условия бонусов"
        info.get_link_in_contents()[0].click() # Дожидаемся ссылки и кликаем по ней
        assert info.logo_in_sourse_page_lnk().is_displayed, 'is not displayed' # Дожидаемся видимости и проверяем

    def test_05_check_links_in_content_terms_of_bonuses_2(self):
        """Проверка ссылок из содержимого раздела 'Условия бонусов'"""
        info = InfoPage(self.driver)
        info.terms_of_bonuses_lnk().click() # Кликаем по ссылке "Условия бонусов"
        info.get_link_in_contents()[1].click() # Дожидаемся ссылки
        profile = ProfilePage(self.driver)
        profile.page_is_loaded() # Проверяем загрузку страницы

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()