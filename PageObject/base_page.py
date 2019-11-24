from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def wait_url(self, url):
        """Ждем пока текущий урл не стал = указанному"""
        return self.wait.until(EC.url_to_be(url))

    def wait_invisibility_of_element_by_css(self, locator):
        """Ожидание проверки того, что элемент либо невидим, либо отсутствует в DOM"""
        return self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, locator)))

    def wait_visibility_of_element_by_css(self, locator):
        """Ожидание для проверки того, что элемент присутствует в DOM страницы и виден"""
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))

    def wait_visibility_of_elements_by_css(self, locator):
        """Ожидание проверки того, что все элементы присутствуют в DOM страницы и являются видимыми"""
        return self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, locator)))

    def wait_visibility_of_any_elements_located_by_css(self, locator):
        return self.wait.until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, locator)))

    def element_by_css(self, how, locator, listed=False, name_rus=None):
        e = self.wait.until(lambda e: self.driver.find_elements(how, locator))
        if listed:
            return e
        else:
            return e[0]

    @staticmethod
    def typing(elem, text):
        """Чистим текстовое поле до переедачи в него текста, посимвольно вводим текст, и проверяем что ввели"""
        elem.click()
        elem.send_keys(Keys.CONTROL + "a" + Keys.BACK_SPACE)
        for symbol in text:
            elem.send_keys(symbol)
        try:
            tx = elem.get_attribute('value')
            assert tx == text, 'Incorrect text'
        except ValueError:
            raise ValueError('Значение в строке с перданным текстом не совпадает с ожидаемым')



