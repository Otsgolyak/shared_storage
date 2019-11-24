from PageObject.base_page import BasePage
from selenium.webdriver.common.by import By


class InfoPage(BasePage):

    def info_lnk(self):
        """Возвращает элемент инфо"""
        return self.element_by_css(By.CSS_SELECTOR, "a.info-menu svg", name_rus='Инфо')

    def faq_lnk(self):
        """Возвращает элемент инфо"""
        return self.element_by_css(By.CSS_SELECTOR, 'div.main div.info.row [utl-loc=INFO_FAQ_ITEM]', name_rus='Чаво?')

    def terms_and_conditions_lnk(self):
        """Возвращает элемент инфо"""
        return self.element_by_css(By.CSS_SELECTOR, 'div.main div.info.row [utl-loc=INFO_TERMS_ITEM]',
                                   name_rus='Правила и условия')

    def help_and_support_lnk(self):
        """Возвращает элемент инфо"""
        return self.element_by_css(By.CSS_SELECTOR, 'div.main div.info.row [utl-loc=INFO_SUPPORT_ITEM]',
                                   name_rus='Помощь и поддержка')

    def terms_of_bonuses_lnk(self):
        """Возвращает элемент инфо"""
        return self.element_by_css(By.CSS_SELECTOR, 'div.main div.info.row [utl-loc=INFO_BONUS_ITEM]',
                                   name_rus='Условия бонусов')

    def get_link_in_contents(self):
        """Возвращает элемент с содержимым контента"""
        return self.wait_visibility_of_elements_by_css('div.content a')

    def get_content_lst(self):
        """Возвращает элементы ссылок страницы"""
        return self.wait_visibility_of_element_by_css('div.content')

    def page_is_loaded(self):
        assert self.faq_lnk().is_displayed, 'is not displayed'
        assert self.terms_and_conditions_lnk().is_displayed, 'is not displayed'
        assert self.help_and_support_lnk().is_displayed, 'is not displayed'

    def logo_in_sourse_page_lnk(self):
        """Возвращает элемент logo а странице загружаемого ресурса"""
        return self.element_by_css(By.CSS_SELECTOR, '#rt-logo', name_rus='Лого на странице')