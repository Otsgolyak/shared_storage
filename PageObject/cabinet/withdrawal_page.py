from PageObject.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class WithdrawalPage(BasePage):

    def choice_account_slc(self):
        """Возвращает элемент (select) выбора аккаунта"""
        return Select(self.element_by_css(By.CSS_SELECTOR, "#accounts select", name_rus="Выбор аккаунта"))

    def choice_payment_method_slc(self):
        """Возвращает элемент (select) выбора платежных средств"""
        return Select(self.element_by_css(By.CSS_SELECTOR, "#paymethod select", name_rus="Выбор метода снятия"))

    def choice_amount_inp(self):
        """Возвращает элемент сумма"""
        return self.element_by_css(By.CSS_SELECTOR, "#amount input", name_rus='Сумма')

    def choice_amount2_inp(self):
        """Возвращает элемент сумма 2"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=Withdrawal__PayMethod__amountConverted] input",
                                   name_rus='Сумма 2')

    def phone_inp(self):
        """Возвращает элемент телефон"""
        return self.element_by_css(By.CSS_SELECTOR, "input.form-control.wallet-input.phone-ar", name_rus='Телефон')

    def send_payment_btn(self):
        """Возвращает элемент кнопки отправить платеж"""
        return self.element_by_css(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-block",
                                   name_rus='Отправить платеж')

    def send_payment_yandex_money_btn(self):
        """Возвращает элемент кнопки отправить платеж (для яндекс мани метода)"""
        return self.element_by_css(By.CSS_SELECTOR, "button.btn.btn-.lg.btn-primary.btn-block.no-margin."
                                                    "withdrawal-block", name_rus='Отправить платеж(Янд.М)')

    def name_inp(self):
        """Возвращает элемент имя, для метода 'банковский перевод'"""
        return self.element_by_css(By.CSS_SELECTOR, "#Name input", name_rus='Имя')

    def iban_inp(self):
        """Возвращает элемент iban, для метода 'банковский перевод'"""
        return self.element_by_css(By.CSS_SELECTOR, "#Iban input", name_rus='IBAN')

    def swift_inp(self):
        """Возвращает элемент swift, для метода 'банковский перевод'"""
        return self.element_by_css(By.CSS_SELECTOR, "#Swift input", name_rus='SWIFT')

    def bank_address_inp(self):
        """Возвращает элемент адрес банка, для метода 'банковский перевод'"""
        return self.element_by_css(By.CSS_SELECTOR, "#BankAddress input", name_rus='Адрес банка')

    def bank_phone_inp(self):
        """Возвращает элемент телефон банка, для метода 'банковский перевод'"""
        return self.element_by_css(By.CSS_SELECTOR, "#BankPhone input", name_rus='Телефон банка')

    def wallet_inp(self):
        """Возвращает элемент кошелек, для yandex money"""
        return self.element_by_css(By.CSS_SELECTOR, "input.form-control.wallet-input", name_rus='Кошелек')

    def card_number_inp(self):
        """Возвращает элемент номер карты для VISA"""
        return self.wait_visibility_of_element_by_css("#cardnumber input")

    def page_is_loaded(self):
        """Проверяем загрузку страницы"""
        assert self.choice_amount_inp().is_displayed, "is not displayed"

    def page_visa_method_is_loaded(self):
        """Проверяем загрузку страницы для Visa"""
        assert self.card_number_inp().is_displayed, "is not displayed"

    def page_wire_transfer_method_is_loaded(self):
        """Проверяем загрузку страницы для банковского перевода"""
        assert self.swift_inp().is_displayed, "is not displayed"
        assert self.bank_address_inp().is_displayed, "is not displayed"
        assert self.iban_inp().is_displayed, "is not displayed"

    def page_yandex_money_method_is_loaded(self):
        """Проверяем загрузку страницы для ундекс моней"""
        assert self.wallet_inp().is_displayed, "is not displayed"
        assert self.send_payment_yandex_money_btn().is_displayed, "is not displayed"


class UploadFilesWithdrawalPage(BasePage):

    def upload_identity_inp(self):
        """Возвращает элемент подтверждение личности"""
        return self.element_by_css(By.CSS_SELECTOR, "#identity-docs", name_rus='Подтверждение личности')

    def upload_proof_of_residence_inp(self):
        """Возвращает элемент подтверждение адреса"""
        return self.element_by_css(By.CSS_SELECTOR, "#address-docs", name_rus='Подтверждение адреса')

    def upload_credit_card_inp(self):
        """Возвращает элемент кредитная карта"""
        return self.element_by_css(By.CSS_SELECTOR, "#card-docs", name_rus='Кредитная карта')

    def upload_other_inp(self):
        """Другое"""
        return self.element_by_css(By.CSS_SELECTOR, "#other-docs", name_rus='Другое')

    def page_is_loaded(self):
        """Проверяем загрузку страницы"""
        assert self.upload_identity_inp().is_displayed, "is not displayed"
        assert self.upload_proof_of_residence_inp().is_displayed, "is not displayed"
        assert self.upload_credit_card_inp().is_displayed, "is not displayed"

