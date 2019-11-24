from selenium.webdriver.common.action_chains import ActionChains
from PageObject.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def login_inp(self):
        """Возвращает элемент логин"""
        return self.element_by_css(By.CSS_SELECTOR, "#login input", name_rus='Логин')

    def password_inp(self):
        """Возвращает элемент пароль"""
        return self.element_by_css(By.CSS_SELECTOR, "#loginpass", name_rus='Пароль')

    def login_btn(self):
        """Возвращает элемент кнопки логин"""
        return self.element_by_css(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-block", name_rus='Кнопка логин')

    def registration_lnk(self):
        """Возвращает элемент кнопки регистрация"""
        return self.element_by_css(By.CSS_SELECTOR, "div.login__form__body.fields-login a", name_rus='Регистрация')

    def forgot_password_lnk(self):
        """Возвращает элемент кнопки забыли пароль"""
        return self.element_by_css(By.CSS_SELECTOR, "div.pull-right a", name_rus='Забыли пароль?')

    def heading_txt(self):
        """Возвращает сообщение, которе выводится при неверном вводе логина или пароля"""
        return self.element_by_css(By.CSS_SELECTOR, "h2", name_rus='Сообщение в заголовке').text

    def lang_slc(self):
        """Возвращает элемент выбора языка (select)"""
        return Select(self.element_by_css(By.CSS_SELECTOR, 'select.app-lang-select.form-control', name_rus='Выбор языка'))

    def login(self, username, password, url='https://trade.trademux.net/cabinet/login'):
        """Логинимся, проверяем что залогинились"""
        self.driver.get(url) # Перехаодим на нужный урл
        self.wait_url(url) # Ждем, пока осуществится переход
        # Вводим данные пользователя и кликаем "логин"
        self.typing(self.login_inp(), username)
        self.typing(self.password_inp(), password)
        self.login_btn().click()

    def page_is_loaded(self):
        assert self.login_inp().is_displayed, "is not displayed"
        assert self.password_inp().is_displayed, "is not displayed"
        assert self.login_btn().is_displayed, "is not displayed"

class PasswordReminderPage(BasePage):

    def login_inp(self):
        """Возвращает элемент кнопки логин"""
        return self.element_by_css(By.CSS_SELECTOR, "input.form-control", name_rus='Логин')

    def send_password_btn(self):
        """Возвращает элемент кнопки отправить пароль"""
        return self.element_by_css(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-block", name_rus='Кнопка: ввести пароль')

    def alredy_have_an_account_lnk(self):
        """Возвращает элемент кнопки уже есть учетная запись?"""
        return self.element_by_css(By.CSS_SELECTOR, "#form-reminder-id a", name_rus='Уже есть учетная запись?')

    def registration_lnk(self):
        """Возвращает элемент кнопки регистрация"""
        return self.element_by_css(By.CSS_SELECTOR, "div.pull-right a", name_rus='Регистрация')

    def page_is_loaded(self):
        assert self.login_inp().is_displayed, "is not displayed"
        assert self.send_password_btn().is_displayed, "is not displayed"



class RegistrationPage(BasePage):

    def name_inp(self):
        """Возвращает элемент имя"""
        return self.element_by_css(By.CSS_SELECTOR, "input.form-control", name_rus='Имя')

    def login_inp(self):
        """Возвращает элемент логин"""
        return self.element_by_css(By.CSS_SELECTOR, "#login input.form-control", name_rus='Логин')

    def password_inp(self):
        """Возвращает элемент пароль"""
        return self.element_by_css(By.CSS_SELECTOR, "#signpass", name_rus='Пароль')

    def confirm_password_inp(self):
        """Возвращает элемент подтверждение пароля"""
        return self.element_by_css(By.CSS_SELECTOR, "#signpassconfirm", name_rus='Подтверждение пароля')

    def tel_inp(self):
        """Возвращает элемент телефон"""
        return self.element_by_css(By.CSS_SELECTOR, "input.PhoneInput__input.form-control", name_rus='Телефон')

    def promokod_inp(self):
        """Возвращает элемент промокод"""
        return self.element_by_css(By.CSS_SELECTOR, "#promo input.form-control", name_rus='Промокод')

    def galka_1_cbx_click(self):
        """Наводит мышку на чекбокс, кликает и ставит галку"""
        expandables = self.element_by_css(By.CSS_SELECTOR, "[for=confirmation]", name_rus="Клик на галку 1")
        ActionChains(self.driver).move_to_element_with_offset(expandables, 0, 0).click().perform()

    def galka_2_cbx_click(self):
        """Наводит мышку на чекбокс, кликает и ставит галку"""
        expandables = self.element_by_css(By.CSS_SELECTOR, "[for=agreement]", name_rus="Клик на галку 2")
        ActionChains(self.driver).move_to_element_with_offset(expandables, 0, 0).click().perform()

    def galka_3_cbx_click(self):
        """Наводит мышку на чекбокс, кликает и ставит галку """
        expandables = self.element_by_css(By.CSS_SELECTOR, "[for=policy]", name_rus="Клик на галку 3")
        ActionChains(self.driver).move_to_element_with_offset(expandables, 0, 0).click().perform()

    def registration_btn(self):
        """Возвращает элемент кнопки регистрация"""
        return self.element_by_css(By.CSS_SELECTOR, "div.signup-btn", name_rus='Кнопка: регистрация')

    def forgot_password_lnk(self):
        """Возвращает элемент кнопки забыли пароль"""
        return self.element_by_css(By.CSS_SELECTOR, "#form-signin-id a", name_rus='Забыли пароль?')

    def alredy_have_an_account_lnk(self):
        """Возвращает элемент кнопки уже есть учетная запись"""
        return self.element_by_css(By.CSS_SELECTOR, "div.pull-right a", name_rus='Уже есть учетная запись?')

    def validation_massage_txt(self):
        """Возвращает валидирующее сообщение"""
        return self.element_by_css(By.CSS_SELECTOR, 'div.form-signin__validation-message p', name_rus='Валидирующее сообщение').text

    def deposit_on_trade_page_btn(self):
        """Возвращает элемент кнопки депозит на торговой странице"""
        return self.element_by_css(By.CSS_SELECTOR, '[utl-loc=HeaderButtons__Deposit]', name_rus='Депозит')

    def page_is_loaded(self):
        """Проверка загрузки страницы"""
        assert self.name_inp().is_displayed, "is not displayed"
        assert self.login_inp().is_displayed, "is not displayed"
        assert self.password_inp().is_displayed, "is not displayed"



