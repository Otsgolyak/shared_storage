from PageObject.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from PageObject.cabinet.profile_page import ProfilePage


class TransactionHistoryPage(BasePage):

    def choice_acccount_slc(self):
        """Возвращает элемент выбора аккаунта (select)"""
        return Select(self.element_by_css(By.CSS_SELECTOR, "#accounts select", name_rus='Выбор аккаунта'))

    def choice_pariod_slc(self):
        """Возвращает элемент выбора периода (select)"""
        return Select(self.element_by_css(By.CSS_SELECTOR, "#paymethod select", name_rus='Выбор периода'))

    def choice_custom_pariod_inp(self):
        """Возвращает элемент выбора пользовательского периода (инпут по которому надо кликнуть)"""
        return self.element_by_css(By.CSS_SELECTOR, "#daterange", name_rus='Выбор пользовательского периода')

    def choice_custom_pariod_start_inp(self):
        """Возвращает элемент выбора пользовательского периода. Начальная дата"""
        return self.element_by_css(By.CSS_SELECTOR, "[name=daterangepicker_start]", name_rus='Начальная дата')

    def choice_custom_pariod_end_inp(self):
        """Возвращает элемент выборапользовательского периода. Конечная дата"""
        return self.element_by_css(By.CSS_SELECTOR, "[name=daterangepicker_end]", name_rus='Конечная дата')

    def confirm_custom_pariod_btn(self):
        """Возвращает элемент кнопки подверждения выбора даты"""
        return self.element_by_css(By.CSS_SELECTOR, "button.applyBtn.btn.btn-sm.btn-success",
                                   name_rus='Кнопка подтверждения выбора периода')

    def load_report_btn(self):
        """Возвращает элемент кнопки загрузить отчет"""
        return self.element_by_css(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-block",
                                   name_rus='Кнопка загрузить отчет')

    def table_tbl(self):
        """Возвращает элемент таблицы"""
        return self.element_by_css(By.CSS_SELECTOR, "table.table.table--history.table-desk", name_rus='Таблица')

    def last_string_tbl(self):
        """Возвращает значение поля 'сумма' последней операции в таблице"""
        return self.element_by_css(By.CSS_SELECTOR, 'table.table-desk tr td',
                                   name_rus='Последняя операция в таблице, поле сумма', listed=True)[:4]

    def page_is_loaded(self):
        """Проверка загрузки страницы"""
        profile = ProfilePage(self.driver) # Подтягиваем элемент со страницы профиля для доп проверки
        assert profile.transaction_history_lnk().is_displayed, "is not displayed"
        assert self.load_report_btn().is_displayed, "is not displayed"

    def form_choice_custom_period_is_loaded(self):
        """Проверка загрузки формы выбора пользовательского периода"""
        assert self.choice_custom_pariod_inp().is_displayed, "is not displayed"
        assert self.choice_custom_pariod_start_inp().is_displayed, "is not displayed"


