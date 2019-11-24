from selenium import webdriver
from PageObject.cabinet.login_page import LoginPage
from PageObject.cabinet.profile_page import ProfilePage
from PageObject.cabinet.profile_page import CreateAccount
from PageObject.cabinet.deposit_page import DepositPage
from PageObject.cabinet.profile_page import EditProfilePage
import unittest


class CreateAccTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        capabilities = {
            "browserName": "chrome",
                        }
        cls.driver = webdriver.Remote(desired_capabilities=capabilities,
                                        command_executor="http://195.201.213.204:4444/wd/hub")
        cls.driver.maximize_window()

        login_page = LoginPage(cls.driver)
        login_page.login(username='shanterrr@yahoo.com', password='qweqwe321!') # Авторизуемся
        profile = ProfilePage(cls.driver)
        profile.page_is_loaded() # Проверка загрузки страницы
        profile.profile_lnk().click() # Кликаем по профилю
        edit = EditProfilePage(cls.driver)
        edit.fill_profile_random_data() # Дожидаемся элементов профиля, если профиль не до конца заполнен, заполняем случайными данными

    def test_01_check_create_account(self):
        """Проверяет создание аккаунта"""
        # Сначала получаем количество уже созданных аккаунтов для будущей проверки
        profile = ProfilePage(self.driver)
        profile.deposit_lnk().click() # Переходим на вкладку deposit
        deposit = DepositPage(self.driver)
        deposit.page_is_loaded() # Проверка загрузки страницы
        count_of_acc = len(deposit.choice_account_slc().options) # Количество созданных аккаунтов на данный момент
        profile.profile_lnk().click() # Переходим на вкладку profile
        create = CreateAccount(self.driver)
        create.create_account_btn().click() # Кликаем по кнопке создать аккаунт
        create.form_is_loaded() # Ждем загрузку формы
        # Заполняем данные аккаунта
        create.leverage_slc().select_by_value('1:5')
        create.currency_slc().select_by_value('EUR')
        create.typing(create.deposit_inp(), '4567')
        create.galka_1_cbx().click()
        create.galka_2_cbx().click()
        create.galka_3_cbx().click()
        create.create_btn().click() # Нажимаем создать аккаунт
        create.form_closing_check() # Проверяем, что форма закрылась за wait
        deposit = DepositPage(self.driver)
        new_count_of_acc = len(deposit.choice_account_slc().options) # Количество созданных аккаунтов на данный момент
        assert count_of_acc + 1 == new_count_of_acc # Сравниваем количество до и после создания

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()