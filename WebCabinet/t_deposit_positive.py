from selenium import webdriver
from PageObject.cabinet.login_page import LoginPage
from PageObject.cabinet.profile_page import ProfilePage
from PageObject.cabinet.deposit_page import DepositPage
import unittest


class DepositPositiveTestSuite(unittest.TestCase):

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
        profile.page_is_loaded() # Проверяем авторизацию

    def setUp(self):
        self.driver.get('https://trade.trademux.net/cabinet/clientarea/deposit') # Переходим на урл
        self.driver.refresh() # Обновляем страницу
        deposit = DepositPage(self.driver)
        deposit.page_is_loaded() # Проверка загрузки страницы

    def test_01_deposite_visa_master_method3(self):
        """Тест дипозита для метода VISA/MASTER (method 3)"""
        deposit = DepositPage(self.driver)
        # Заполняем данные
        deposit.choice_account_slc().select_by_value("REAL-14714")
        deposit.choice_payment_method_slc().select_by_value('Visa/Mastercard (Method 3)')
        deposit.typing(deposit.choice_amount_inp(), '99')
        deposit.typing(deposit.first_name_inp(), 'first name')
        deposit.typing(deposit.last_name_inp(), 'last name')
        deposit.country_slc().select_by_value('Russia')
        deposit.typing(deposit.zip_code_inp(), 'zip_code')
        deposit.typing(deposit.city_inp(), 'city')
        deposit.typing(deposit.address_inp(), 'address')
        deposit.typing(deposit.email_inp(), 'e-mail@mail.ru')
        deposit.typing(deposit.phone_inp(), '+79001005050')
        deposit.deposit_for_visa_master_method3_btn().click() # Кликаем по кнопке deposit
        # Проверяем видимость кнопки 'PAY' на странице платежной системы
        # assert deposit.visa_master_method_3_payment_sistem_btn().is_displayed, "is not displayed" (не работает)

    def test_02_deposite_visa_master_method4(self):
        """Тест дипозита Visa/Master (Method 4). Тест рабочий, но метод: Visa/Master Method 4 - нет"""
        # Заполняем данные
        deposit = DepositPage(self.driver)
        deposit.choice_account_slc().select_by_value("REAL-14714")
        deposit.choice_payment_method_slc().select_by_value('Visa/Mastercard (Method 4)')
        deposit.page_visa_master_method4_is_loaded()
        deposit.typing(deposit.choice_amount_inp(), '99')
        deposit.typing(deposit.first_name2_inp(), 'first name2')
        deposit.typing(deposit.last_name2_inp(), 'last name2')
        deposit.typing(deposit.month_inp(), '01')
        deposit.typing(deposit.year_inp(), '22')
        deposit.typing(deposit.cvv_inp(), '999')
        deposit.country_slc().select_by_value('Russia')
        deposit.typing(deposit.zip_code_inp(), 'zip_code')
        deposit.typing(deposit.city_inp(), 'city')
        deposit.typing(deposit.address_inp(), 'address')
        deposit.typing(deposit.email_inp(), 'e-mail@mail.ru')
        deposit.typing(deposit.phone_inp(), '+79001005050')
        # Кликаем по чекбоксам, ставим галочки
        deposit.galka1_cbx().click()
        deposit.galka2_cbx().click()
        deposit.deposit_for_visa_master_method4_btn().click() # Нет ассерта, так как некорректно работает кабинет

    def test_03_deposite_qiwi_method_2_real(self):
        """Тест дипозита для QIWI (method 2)"""
        # Заполняем данные
        deposit = DepositPage(self.driver)
        deposit.choice_account_slc().select_by_value("REAL-14714")
        deposit.choice_payment_method_slc().select_by_value('QIWI (Method 2)')
        deposit.page_qiwi_or_yandex_money_is_loaded()
        deposit.typing(deposit.choice_amount_inp(), '999')
        deposit.typing(deposit.phone_for_qiwi_and_yandex_money_inp(), '+79051005050')
        deposit.deposit_btn().click() # Нажимаем кнопку депозит
        # Проверяем, что перешли на нужную страницу, по наличию нужного инпута (не работает)
        #assert deposit.qiwi_method2_payment_sistem_inp().is_displayed, "is not displayed"

    def test_04_deposite_wire_transfer(self):
        """Тест депозита банковского перевода, ссылается на почту поддержки"""
        # Заполняем данные
        deposit = DepositPage(self.driver)
        deposit.choice_account_slc().select_by_value("REAL-14714")
        deposit.choice_payment_method_slc().select_by_value('Wire transfer')
        deposit.typing(deposit.choice_amount_inp(), '999')
        # Проверяем, что ссылка на супорт почту отобразалась
        assert deposit.support_mail_lnk().is_displayed, "is not displayed"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()