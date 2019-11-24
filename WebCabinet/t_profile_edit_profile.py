from selenium import webdriver
from PageObject.cabinet.login_page import LoginPage
from PageObject.cabinet.profile_page import ProfilePage
from PageObject.cabinet.profile_page import EditProfilePage
import unittest


class EditProfileTestSuite(unittest.TestCase):

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
        profile.profile_lnk().click() # Кликаем по профилю
        edit = EditProfilePage(cls.driver)
        edit.page_is_loaded() # Проверка загрузки страницы (по кнопке редактировать)

    def test_01_edit_profile_positive(self):
        edit = EditProfilePage(self.driver)
        edit.edit_btn().click() # Нажимаем кнопку редактировать
        edit.form_is_loaded()  # Проверяем загрузку формы профиля
        # fillProfile Заполняет данные профиля, сохраняет и проверяет, что данные корректно сохранились
        edit.fill_profile(firstname='name', lastname='lastname', birth=('04', '29', '1976'), country='Panama',
                          zip_code='zip code', city='city', address='address')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()









