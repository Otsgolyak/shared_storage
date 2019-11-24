from PageObject.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class DepositPage(BasePage):

    def choice_account_slc(self):
        """Возвращает элемент (select) выбора аккаунта"""
        return Select(self.element_by_css(By.CSS_SELECTOR, "#accounts select", name_rus='Выбор аккаунта'))

    def choice_payment_method_slc(self):
        """Возвращает элемент (select) выбора метода пополнения"""
        return Select(self.element_by_css(By.CSS_SELECTOR, "#paymethod select", name_rus='Выбор метода пополнения'))

    def choice_amount_inp(self):
        """Возвращает элемент сумма"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=Deposit__MiningServer__Amount] input", name_rus='Сумма 1')

    def choice_amount2_inp(self):
        """Возвращает элемент сумма 2, для не USD/EUR аккаунтов"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=Deposit__AmountConverted] input", name_rus='Сумма 2')

    def first_name_inp(self):
        """Возвращает элемент имя. Использовать для visa/master card (method 3)"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=Deposit__BillingInfo__FirstName] input", name_rus='Имя')

    def last_name_inp(self):
        """Возвращает элемент фамилия. Использовать для visa/master card (method 3)"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=Deposit__BillingInfo__LastName] input", name_rus='Фамилия')

    def first_name2_inp(self):
        """Возвращает элемент имя, использовать для visa/master card (method 4)"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=Deposit__FirstName] input", name_rus='Имя')

    def last_name2_inp(self):
        """Возвращает элемент фамилия, использовать для visa/master card (method 4)"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=Deposit__LastName] input", name_rus='Фамилия')

    def country_slc(self):
        """Возвращает элемент страна. Использовать для visa/master card (method 3, 4)"""
        return Select(self.element_by_css(By.CSS_SELECTOR, "#country select", name_rus='Страна'))

    def month_inp(self):
        """Возвращает элемент месяц, использовать для visa/master card (method 3, 4)"""
        return self.element_by_css(By.CSS_SELECTOR, "#month input", name_rus='Месяц')

    def year_inp(self):
        """Возвращает элемент год, использовать для visa/master card (method 3, 4)"""
        return self.element_by_css(By.CSS_SELECTOR, "#year input", name_rus='Год')

    def cvv_inp(self):
        """Возвращает элемент CVV, использовать для visa/master card (method 4)"""
        return self.element_by_css(By.CSS_SELECTOR, "#cvv input", name_rus='CVV') # Уточнить по name_rus

    def galka1_cbx(self):
        """Возвращает елемент input type=checkbox. Использовать для visa/master card (method 4)"""
        return self.element_by_css(By.CSS_SELECTOR, "input.DepositConfirmationBox__wrapper__input", name_rus='Галка 1', listed=True)[0] # Уточнить

    def galka2_cbx(self):
        """Возвращает елемент input type=checkbox. Использовать для visa/master card (method 4)"""
        return self.element_by_css(By.CSS_SELECTOR, "input.DepositConfirmationBox__wrapper__input", name_rus='Галка 2', listed=True)[1] # Уточнить

    def zip_code_inp(self):
        """Возвращает элемент zip code. Использовать для visa/master card (method 3, 4)"""
        return self.element_by_css(By.CSS_SELECTOR, "#country input", name_rus='Почтовый адрес')

    def city_inp(self):
        """Возвращает элемент город. Использовать для visa/master card (method 3, 4)"""
        return self.element_by_css(By.CSS_SELECTOR, "#city input", name_rus='Город')

    def address_inp(self):
        """Возвращает элемент адрес. Использовать для visa/master card (method 3, 4)"""
        return self.element_by_css(By.CSS_SELECTOR, "#address input", name_rus='Адрес')

    def email_inp(self):
        """Возвращает элемент емэйл. Использовать для visa/master card (method 3, 4)"""
        return self.element_by_css(By.CSS_SELECTOR, "#email input", name_rus='Почта')

    def phone_inp(self):
        """Возвращает элемент телефон. Использовать для visa/master card (method 3, 4)"""
        return self.element_by_css(By.CSS_SELECTOR, "#phone input", name_rus='Телефон')

    def phone_for_qiwi_and_yandex_money_inp(self):
        """Возвращает элемент телефон. Использовать для методов киви и яндекс деньги"""
        return self.element_by_css(By.CSS_SELECTOR, "input.form-control.phone-ar", name_rus='Телефон')

    def deposit_for_visa_master_method3_btn(self):
        """Возвращает элемент кнопки депозит. Использовать для visa/master card (method 3)"""
        return self.element_by_css(By.CSS_SELECTOR, "div.form-group.payment-block button", name_rus='Депозит')

    def deposit_for_visa_master_method4_btn(self):
        """Возвращает элемент кнопки депозит. Использовать для visa/master card (method 4)"""
        return self.element_by_css(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-block", name_rus='Депозит')

    def deposit_btn(self):
        """Возвращает элемент кнопки депозит. Использовать для всех кроме visa/master method 3,4"""
        return self.element_by_css(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-block.web-money-button", name_rus='Депозит')

    def valute_slc(self):
        """Возвращает (select) выбора валюты"""
        return Select(self.element_by_css(By.CSS_SELECTOR, "#amount select", name_rus='Вылюта'))

    def retry_on_page_visa_master_method3_btn(self):
        """'Возвращает элемент Кнопки Retry на странице платежной системы Visa/Master (method 3)'"""
        return self.element_by_css(By.CSS_SELECTOR, '#btnNext', name_rus='Кнопка Retry')

    def support_mail_lnk(self):
        """Возвращает элемент ссылки на почту супорта"""
        return self.element_by_css(By.CSS_SELECTOR, 'span[lang=en-US] a', name_rus='Ссылка на почту супорта')

    def visa_master_method_3_payment_sistem_btn(self):
        """Кнопка Pay, которая появляется на странице Visa/Master (method 3) при успешно введенных данных"""
        return self.element_by_css(By.CSS_SELECTOR, '#submitSelectPaymentType',
                                   name_rus='Кнопка Pay на странице метода')

    def qiwi_method2_payment_sistem_inp(self):
        """Возвращает элемент со страницы платежной системы метода qiwi 2"""
        return self.element_by_css(By.CSS_SELECTOR, '[name=account_id]', name_rus='Поле для ввода на странице метода')

    def page_is_loaded(self):
        """Проверка загрузки страницы"""
        assert self.choice_amount_inp().is_displayed, "is not displayed"

    def page_visa_master_method3_is_loaded(self):
        """Проверка загрузки страницы для Visa/Master method 3"""
        assert self.first_name_inp().is_displayed, "is not displayed"
        assert self.last_name_inp().is_displayed, "is not displayed"
        assert self.deposit_for_visa_master_method3_btn().is_displayed, "is not displayed"

    def page_visa_master_method4_is_loaded(self):
        """Проверка загрузки страницы для Visa/Master method 4"""
        assert self.first_name2_inp().is_displayed, "is not displayed"
        assert self.galka1_cbx().is_displayed, "is not displayed"
        assert self.deposit_for_visa_master_method4_btn().is_displayed, "is not displayed"
        assert self.cvv_inp().is_displayed, "is not displayed"

    def page_qiwi_or_yandex_money_is_loaded(self):
        """Проверка загрузки страницы для QIWI и Yandex money"""
        assert self.phone_for_qiwi_and_yandex_money_inp().is_displayed, "is not displayed"