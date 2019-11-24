from selenium import webdriver
from PageObject.cabinet.login_page import LoginPage
from PageObject.cabinet.profile_page import ProfilePage
from PageObject.cabinet.withdrawal_page import WithdrawalPage
from PageObject.cabinet.trans_history_page import TransactionHistoryPage
import unittest


class WithdrawalTestSuite(unittest.TestCase):

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
        login_page.login(username='shanterrr@yahoo.com', password='qweqwe321!') # Логинимся на сайте
        profile = ProfilePage(cls.driver)
        profile.page_is_loaded() # Проверка загрузки страницы

    def setUp(self):
        self.driver.refresh() # Обновляем страницу
        profile_page = ProfilePage(self.driver)
        profile_page.page_is_loaded() # Проверяем загрузку страницы
        profile_page.withdrawal_lnk().click() # Кликаем на страницу пополнения
        withdrawal = WithdrawalPage(self.driver)
        withdrawal.page_is_loaded() # Проверка загрузки страницы пополнения

    def test_01_withdrawal_visa(self):
        """Тест снятия, через метод VISA. Указывать значение в инпут choice_amount_inp, не менее 500"""
        withdrawal = WithdrawalPage(self.driver)
        withdrawal.choice_account_slc().select_by_value("REAL-14714") # Выбираем аккаунт
        withdrawal.choice_payment_method_slc().select_by_value('Visa') # Выбираем платежный метод
        withdrawal.page_visa_method_is_loaded() # Ждем загрузку страницы метода
        # Заполняем платежные данные
        withdrawal.card_number_inp().send_keys('1111222233334444') # Вводим данные в поле номер карты
        assert withdrawal.card_number_inp().get_attribute('value') == '1111-2222-3333-4444' # Проверяем введенные данные
        amount = '501' # Запоминаем какую сумму снятия ввели (для проверки)
        withdrawal.typing(withdrawal.choice_amount_inp(), amount)
        withdrawal.send_payment_btn().click() # Нажимаем отправить платеж
        trans = TransactionHistoryPage(self.driver)
        trans.page_is_loaded() # Дожидаемся загрузки страницы
        self.driver.get('https://trade.trademux.net/cabinet/clientarea/history') # Идем на страницу история транзакций
        assert trans.load_report_btn().is_displayed, "is not displayed" # дожидаемся видимости кнопки загрузить отчет
        trans.load_report_btn().click() # Нажимаем кнопку "загрузкить отчет"
        assert trans.table_tbl().is_displayed, "is not displayed" # Дожидаемся загрузки таблицы
        assert trans.last_string_tbl()[3].text.startswith('-' + amount) # Проверяем, что в верхней строке таблицы наша сумма со знаком "-"

    def test_02_withdrawal_wire_transfer(self):
        """Тест снятия через банковский перевод"""
        withdrawal = WithdrawalPage(self.driver)
        withdrawal.choice_account_slc().select_by_value("REAL-14714") # Выбираем аккаунт
        withdrawal.choice_payment_method_slc().select_by_value('Wire transfer') # Выбираем платежный метод
        withdrawal.page_wire_transfer_method_is_loaded() # Ждем загрузку страницы метода
        # Заполняем платежные данные
        amount = '80' # Запоминаем какую сумму снятия ввели (для проверки)
        withdrawal.typing(withdrawal.choice_amount_inp(), amount)
        withdrawal.typing(withdrawal.name_inp(), 'Ivan Ivanov')
        withdrawal.typing(withdrawal.iban_inp(), 'iban')
        withdrawal.typing(withdrawal.swift_inp(), 'swift')
        withdrawal.typing(withdrawal.bank_address_inp(), 'bank_address')
        withdrawal.typing(withdrawal.bank_phone_inp(), '+78005008888')
        withdrawal.send_payment_btn().click() # Нажимаем отправить платеж
        trans = TransactionHistoryPage(self.driver)
        trans.page_is_loaded() # Проверяем, что осуществился переход на страницу история транзакций
        self.driver.get('https://trade.trademux.net/cabinet/clientarea/history') # Идем на страницу история транзакций
        assert trans.load_report_btn().is_displayed, "is not displayed" # дожидаемся видимости кнопки загрузить отчет
        trans.load_report_btn().click() # Нажимаем кнопку "загрузкить отчет"
        assert trans.table_tbl().is_displayed, "is not displayed" # Дожидаемся загрузки таблицы
        assert trans.last_string_tbl()[3].text.startswith('-' + amount) # Проверяем, что в верхней строке таблицы наша сумма со знаком "-"

    def test_03_withdrawal_yandex_money(self):
        """Тест снятия через яндекс мани"""
        withdrawal = WithdrawalPage(self.driver)
        withdrawal.choice_account_slc().select_by_value("REAL-14714") # Выбираем аккаунт
        withdrawal.choice_payment_method_slc().select_by_value('Yandex.Money (Method 1)') # Выбираем платежный метод
        # Заполняем платежные данные
        withdrawal.page_yandex_money_method_is_loaded() # Проверка загрузки страницы метода
        withdrawal.typing(withdrawal.wallet_inp(), '12345')
        amount = '321'  # Запоминаем какую сумму снятия ввели (для проверки)
        withdrawal.typing(withdrawal.choice_amount_inp(), amount)
        withdrawal.send_payment_yandex_money_btn().click() # Нажимаем отправить платеж
        trans = TransactionHistoryPage(self.driver)
        trans.page_is_loaded() # Проверяем, что осуществился переход на страницу история транзакций
        self.driver.get('https://trade.trademux.net/cabinet/clientarea/history') # Идем на страницу история транзакций
        assert trans.load_report_btn().is_displayed, "is not displayed" # дожидаемся видимости кнопки загрузить отчет
        trans.load_report_btn().click() # Нажимаем кнопку "загрузкить отчет"
        assert trans.table_tbl().is_displayed, "is not displayed" # Дожидаемся загрузки таблицы
        assert trans.last_string_tbl()[3].text.startswith('-' + amount) # Проверяем, что в верхней строке таблицы наша сумма со знаком "-"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()