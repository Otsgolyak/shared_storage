from PageObject.base_page import BasePage
import hashlib
import os, os.path
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):

    def profile_lnk(self):
        """Возвращает элемент профиль"""
        return self.element_by_css(By.CSS_SELECTOR, "li[utl-loc=Profile]", name_rus='Профиль')

    def deposit_lnk(self):
        """Возвращает элемент депозит"""
        return self.element_by_css(By.CSS_SELECTOR, "li[utl-loc=Deposit]", name_rus='Пополнение')

    def withdrawal_lnk(self):
        """Возвращает элемент снятие/withdrawal"""
        return self.element_by_css(By.CSS_SELECTOR, "li[utl-loc=Withdraw]", name_rus='Снятие')

    def bonus_offers_lnk(self):
        """Возвращает элемент бонус офферс"""
        return self.element_by_css(By.CSS_SELECTOR, "li[utl-loc=Bonusoffers]", name_rus='Бонусы')

    def transaction_history_lnk(self):
        """Возвращает элемент история транзакций/transaction history"""
        return self.element_by_css(By.CSS_SELECTOR, "li[utl-loc=History]", name_rus='История операций')

    def logo_lnk(self):
        """Возвращает элемент лого, верхняя панель"""
        return self.element_by_css(By.CSS_SELECTOR, "img[alt='TradeMUX']", name_rus='Лого')

    def my_client_aria_lnk(self):
        """Возвращает элемент мой кабинет/my client aria, верхняя панель"""
        return self.element_by_css(By.CSS_SELECTOR, "li[utl-loc=NavClientarea]", name_rus='Мой кабинет')

    def platforms_lnk(self):
        """Возвращает элемент платформа/platforms, верхняя панель"""
        return self.element_by_css(By.CSS_SELECTOR, "li[utl-loc=NavPlatforms]", name_rus='Платформа')

    def affiliate_aria_lnk(self):
        """Возвращает элемент партнёрский кабинет/affiliate aria, верхняя панель"""
        return self.element_by_css(By.CSS_SELECTOR, "li[utl-loc=NavReferral]", name_rus='Партнерский кабинет')

    def trading_btn(self):
        """Возвращает элемент трайдинг, верхняя панель"""
        return self.element_by_css(By.CSS_SELECTOR, '#bs-navbar-collapse-1 [class="form-horizontal navbar-form navbar-'
                                                'right"] .btn.btn-default.navbar-btn.btn-margin', name_rus="Торговать")
        #return self.wait_visibility_of_any_elements_located_by_css("[utl-loc=NavbarForm] .btn.btn-default.navbar-btn.btn-margin") Уточнить как лучше

    def mining_btn(self):
        """Возвращает элемент майнинг, верхняя панель"""
        return self.element_by_css(By.CSS_SELECTOR, "#bs-navbar-collapse-1 button", name_rus='Майнинг', listed=True)[1] # Уточнить

    def diposit_on_top_panel_btn(self):
        """Возвращает элемент депозит, верхняя панель"""
        return self.element_by_css(By.CSS_SELECTOR, '#bs-navbar-collapse-1 [class="form-horizontal navbar-form navbar-'
                                                  'right"] .btn.btn-default.navbar-btn.btn-yellow', name_rus='Депозит')

    def logout_lnk(self):
        """Возвращает элемент кнопки выход"""
        return self.element_by_css(By.CSS_SELECTOR,'[utl-loc="NavbarForm"] a.exit-menu', name_rus='Выход')

    def two_factor_auth_cbx(self):
        return self.element_by_css(By.CSS_SELECTOR, 'input.switch_1', name_rus='Двухфакторная аутентификация')

    def page_is_loaded(self):
        assert self.profile_lnk().is_displayed, "is not displayed"
        assert self.deposit_lnk().is_displayed, "is not displayed"
        assert self.my_client_aria_lnk().is_displayed, "is not displayed"


class EditProfilePage(BasePage):

    def edit_btn(self):
        """Возвращает элемент кнопки редактировать на странице профиля, нужно кликнуть,
         чтобы появились остальные элементы внутри формы редактирования"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=Profile__Edit__btn]", name_rus='Редактировать')

    def edit_first_name_inp(self):
        """Возвращает элемент имя"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=EditProfile__FirstName] input", name_rus='Имя')

    def edit_last_name_inp(self):
        """Возвращает элемент фамилия"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=EditProfile__LastName] input", name_rus='Фамилия')

    def edit_birth_inp(self):
        """Возвращает элемент дата рождения"""
        return self.element_by_css(By.CSS_SELECTOR, "#birthday", name_rus='Дата рождения')

    def edit_country_slc(self):
        """Возвращает элемент страна"""
        return Select(self.element_by_css(By.CSS_SELECTOR, "dd select", name_rus='Страна'))

    def edit_zip_code_inp(self):
        """Возвращает элемент zip code"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=EditProfile__ZipCode] input", name_rus='Почтовый индекс')

    def edit_city_inp(self):
        """Возвращает элемент город"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=EditProfile__City] input", name_rus='Город')

    def edit_address_inp(self):
        """Возвращает элемент адрес"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=EditProfile__Address] input", name_rus='Адрес')

    def save_btn(self):
        """Возвращает элемент кнопки сохранить"""
        return self.element_by_css(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-block", name_rus='Сохранить')

    def list_with_profile_data(self):
        """Возвращает список элементов, в тексте которых содержатся данные профиля, 7 элементов:
        0 - First Name
        1 - Last Name
        2 - Date of Birth
        3 - City
        4 - Country
        5 - Address
        6 - Zip code
        """
        return self.wait_visibility_of_elements_by_css('div.profile-regular-field a')

    def fill_profile_random_data(self, firstname=None, lastname=None, birth=None, country=None, zip_code=None,
                                 city=None, address=None):
        """Заполняет данные профиля, если не заполнены"""
        import random
        a = self.list_with_profile_data() # Получаем список данных профиля и ждем загрузки страницы
        if len(a) != 7: # Если есть незаполненные поля (a = 7, если все заполнены)
            random_string = str(random.randrange(0, 9999)) # Создаем случайную строку
            self.edit_btn().click() # Нажимаем кнопку редактировать
            self.form_is_loaded()  # Проверяем загрузку формы профиля
            # Заполняем данные
            self.fill_profile(firstname=random_string, lastname=random_string, birth=('04', '29', '1976'),
                              country='Panama', zip_code='zip_code',  city='city', address='address')


    def fill_profile(self, firstname=None, lastname=None, birth=None, country=None, zip_code=None,
                                 city=None, address=None):
        """Заполняет данные профиля, сохраняет и проверяет, что данные корректно сохранились"""
        # Заполняем данные если таковые были переданы в функцию
        if firstname:
            self.typing(self.edit_first_name_inp(), firstname)
        if lastname:
            self.typing(self.edit_last_name_inp(), lastname)
        if birth:
            self.typing(self.edit_birth_inp(), '{}{}{}'.format(birth(0), birth(1), birth(2))) # Месяц День Год
        self.edit_first_name_inp().click() # Кликаем по верхнему инпуту, чтобы убраласть форма для выбора даты
        if country:
            self.edit_country_slc().select_by_value(country)
        if zip_code:
            self.typing(self.edit_zip_code_inp(), zip_code)
        if city:
            self.typing(self.edit_city_inp(), city)
        if address:
            self.typing(self.edit_address_inp(), address)
        self.save_btn().click() # Нажимаем сохранить
        self.wait_invisibility_of_element_by_css("button.btn.btn-lg.btn-primary.btn-block") # Ждем пока не исчезнет кнопка сохранить
        self.page_is_loaded() # Проверяем загрузку страницы
        self.driver.refresh() # Обновляем страницу
        profile_data = self.list_with_profile_data() # ждем загрузку страницы и получаем список данных профиля

        # Сравниваем введенные данные с тем, что написано на странице профиля
        if firstname:
            assert profile_data[0].text == firstname
        if lastname:
            assert profile_data[1].text == lastname
        if birth:
            assert birth[0] in profile_data[2].text
            assert birth[1] in profile_data[2].text
            assert birth[2] in profile_data[2].text
        if country:
            assert profile_data[4].text == country
        if zip_code:
            assert profile_data[6].text == zip_code
        if city:
            assert profile_data[3].text == city
        if address:
            assert profile_data[5].text == address

    def form_is_loaded(self):
        """Проверка загрузки страницы"""
        assert self.edit_first_name_inp().is_displayed, "is not displayed"
        assert self.edit_last_name_inp().is_displayed, "is not displayed"
        assert self.edit_birth_inp().is_displayed, "is not displayed"

    def page_is_loaded(self):
        assert self.edit_btn().is_displayed, "is not displayed"

    def form_closing_check(self):
        """Проверка закрытия формы"""
        self.wait_invisibility_of_element_by_css("button.btn.btn-lg.btn-primary.btn-block") # Ждем пока не исчезнет
                                                                                                # кнопка сохранить


class UploadFiles(BasePage):

    currdir = os.getcwd() # Создаем переменную с текущей директорией

    def upload_identity_inp(self):
        """Возвращает элемент подтверждение личности"""
        return self.element_by_css(By.CSS_SELECTOR, "#identity-docs", name_rus='Логин')

    def upload_photo_with_passport_inp(self):
        """Возвращает элемент фото с паспортом"""
        return self.element_by_css(By.CSS_SELECTOR, "#photo-with-passport", name_rus='Логин')

    def upload_proof_of_residence_inp(self):
        """Возвращает элемент подтверждение адреса"""
        return self.element_by_css(By.CSS_SELECTOR, "#address-docs", name_rus='Логин')

    def upload_transaction_confirmation_form_inp(self):
        """Возвращает элемент подтверждение транзакций"""
        return self.element_by_css(By.CSS_SELECTOR, "#questionnaire-1", name_rus='Логин')

    def upload_agreement_inp(self):
        """Возвращает элемент пользовательское соглашение"""
        return self.element_by_css(By.CSS_SELECTOR, "#questionnaire-2", name_rus='Логин')

    def upload_credit_card_inp(self):
        """Возвращает элемент кредитная карта"""
        return self.element_by_css(By.CSS_SELECTOR, "#card-docs", name_rus='Логин')

    def upload_photo_with_card_on_the_background_of_the_site_inp(self):
        """Возвращает элемент фото с картой на фоне сайта"""
        return self.element_by_css(By.CSS_SELECTOR, "#photo-card-background-site", name_rus='Логин')

    def upload_other_inp(self):
        """Возвращает элемент другое"""
        return self.element_by_css(By.CSS_SELECTOR, "#other-docs", name_rus='Логин')

    def last_downloaded_file(self):
        """Возвращает элемент 1го загруженного файла, если виден"""
        return self.wait_visibility_of_elements_by_css("div.col-xs-6.uploaded-file a")[0] # Список

    def get_all_downloaded_files(self):
        """Возвращает список загруженных файлов"""
        return self.wait_visibility_of_elements_by_css("div.col-xs-6.uploaded-file")

    def last_downloaded_file_remove_circle(self):
        """Возвращает кнопку удаления последнего загруженного файла, если видима"""
        return self.wait_visibility_of_elements_by_css("span.glyphicon.glyphicon-remove-circle")[0]

    def confirm_delete_btn(self):
        """Возвращает кнопку подтверждения удаления, если видна"""
        return self.wait_visibility_of_any_elements_located_by_css('button.btn.btn-danger')[0]

    def cancellation_delete_btn(self):
        """Возвращает кнопку отмены удаления, если видна"""
        return self.wait_visibility_of_any_elements_located_by_css('button.btn.btn-danger')[1]

    def remove_last_downloaded_file(self):
        """Удаляет последний загруженный файл. Ожидается, что он единственный загруженный на странице, так как
        после загрузки будем сразу удалять файл в кейсе"""
        # Получаем элемент последнего загруженного файла и кликаем по элементу удалить
        self.last_downloaded_file_remove_circle().click()
        self.confirm_delete_btn().click() # Получаем кнопку для подтверждения удаления
        self.wait_invisibility_of_element_by_css('div.modal-content') # Ждем пока не исчезнет форма

    def remove_all_download_files(self):
        """Удаляет все загруженные файлы, если они есть"""
        try:
            a = self.get_all_downloaded_files()
            while a:
                self.remove_last_downloaded_file()
                a = a[1:]
                self.driver.refresh()
        except:
            pass

    def wait_upload_or_refresh(self, tryes=3):
        while tryes > 0: # Пока не закончились попытки
            try:
                self.last_downloaded_file_remove_circle() # Ищем элемент кнопки удаления, иначе TimeoutExcepton
                break # Прерываем, если не было исключения
            except:
                tryes -= 1 # Уменьшаем количство попыток
                self.driver.refresh() # Обновляем страницу

    def download_wait(self, second=20):
        """Ждет пока в нужной папке не появятся загруженные до конца файлы"""
        import time
        flag = True # Создаем флажок
        start = time.time()  # Создаем переменную для стартового времени
        cur_time = time.time() # Создаем переменную для текущего времени
        stop = time.time() + second # Создаем переменную со временем окончания загрузки
        while flag and cur_time < stop: # Пока флаг и не вышло время
            time.sleep(1) # Ждем секунду
            cur_time = time.time() # Обновляем текущее время
            flag = False # Обнуляем флаг
            for filename in os.listdir('Download_from_tests'): # Для каждого файла в директории
                if filename.endswith('.crdownload') or filename.endswith('.tmp'): # Если есть недогруженные файлы
                    flag = True # Возвращаем флаг, продолжаем цикл
        if cur_time > stop: # Если время вышло
            raise ('Не найден элемент за {} сек'.format((str(second)))) # Кидаем ошибку
        return (cur_time - start) # Возвращает потраченное время

    def wait_remove_folder_content(self, path=currdir + '/Download_from_tests', second=10):
        """Ждет очистки содержимого папки"""
        import time
        flag = True # Создаем флажок
        start = time.time() # Создаем переменную для стартового времени
        cur_time = time.time() # Создаем переменную для текущего времени
        stop = time.time() + second # Создаем переменную со временем окончания загрузки
        while flag and cur_time < stop: # Пока флаг и не вышло время
            if not self.is_empty_folder(path): # Если папка не пуста
                time.sleep(1) # Ждем секунду
                cur_time = time.time()  # Обновляем текущее время
            else: # Иначе
                flag = False # Прекращаем цикл, так как папка пуста
        if cur_time > stop: # Если время вышло
            raise ('Не найден элемент за {} сек'.format(str(second))) # Кидаем ошибку
        return (cur_time - start) # Возвращает потраченное время

    def is_empty_folder(self, path):
        """Проверяет что папка пустая"""
        if not os.listdir(path):
            return True
        else:
            return False

    def remove_folder_contents(self, path):
        """Удаляет содержимое папок для загрузки"""
        start_dir = self.currdir # Сохраняем первоначальную директорию
        folder_inside_current_folder = os.path.dirname(os.path.join(self.currdir, path)) # Получаем нужную директорию
        os.chdir(folder_inside_current_folder) # Меняем текущую директорию, на новую
        files = (os.listdir('.')) # Получаем список файлов директории
        for f in files: # Проходим циклом по каждому файлу
            os.remove(f) # и удаляем файл
        os.chdir(start_dir) # Возвращаем директорию на стартовую

    def md5(self, fname):
        """Берет хеш файла"""
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def page_is_loaded(self):
        """Проверка загрузки страницы"""
        assert self.upload_identity_inp().is_displayed, "is not displayed"
        assert self.upload_photo_with_passport_inp().is_displayed, "is not displayed"
        assert self.upload_proof_of_residence_inp().is_displayed, "is not displayed"


class CreateAccount(BasePage):

    def create_account_btn(self):
        """Возвращает элемент кнопки создать аккаунт, нужно кликнуть, чтобы появились остальные элементы"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=Profile__CreateAccount__btn]",
                                   name_rus='Кнопка: создать аккаунт')

    def leverage_slc(self):
        """Возвращает элемент плечо (select)"""
        return Select(self.element_by_css(By.CSS_SELECTOR, "[utl-loc=CreateAccount__Leverage] select",
                                          name_rus='Плечо'))

    def currency_slc(self):
        """Возвращает элемент валюта (select)"""
        return Select(self.element_by_css(By.CSS_SELECTOR, "[utl-loc=CreateAccount__Currency] select",
                                          name_rus='Валюта'))

    def deposit_inp(self):
        """Возвращает элемент размер депозита"""
        return self.element_by_css(By.CSS_SELECTOR, "#deposit input", name_rus='Размер депозита')

    def galka_1_cbx(self):
        """Возвращает элемент input type=checkbox"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=CreateAccount__risk_disclosure_notice] input",
                                   name_rus='Заявление о раскрытии рисков')

    def galka_2_cbx(self):
        """Возвращает элемент input type=checkbox"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=CreateAccount__user_agreement] input",
                                   name_rus='Пользовательское соглашение')

    def galka_3_cbx(self):
        """Возвращает элемент input type=checkbox"""
        return self.element_by_css(By.CSS_SELECTOR, "[utl-loc=CreateAccount__privacy_policy] input",
                                   name_rus='Заявление о конфеденциальности')

    def create_btn(self):
        """Возвращает элемент кнопики создать, которая внутри формы создания"""
        return self.element_by_css(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-block", name_rus='Создать')

    def form_is_loaded(self):
        """Проверяет загрузку формы создания аккаунта"""
        assert self.deposit_inp().is_displayed, "is not displayed"
        assert self.galka_1_cbx().is_displayed, "is not displayed"
        assert self.create_btn().is_displayed, "is not displayed"

    def form_closing_check(self):
        """Ждет пока форма создания аккаунта перестанет быть visible"""
        # Проверяем по кнопке "создать", если не исчезнет за wait, то TimeOutException
        self.wait_invisibility_of_element_by_css("button.btn.btn-lg.btn-primary.btn-block")


class FooterPage(BasePage):


    def term_of_website_use_lnk(self):
        """Возвращает элемент подвала: 'Условия доступа к сайту'"""
        return self.element_by_css(By.CSS_SELECTOR, '[utl-loc=AppView__FOOTER_TERMS] a',
                                   name_rus='Условия доступа к сайту')

    def provacy_policy_lnk(self):
        """Возвращает элемент подвала: 'Заявление о конфиденциальности'"""
        return self.element_by_css(By.CSS_SELECTOR, '[utl-loc=AppView__FOOTER_PRIVACY] a',
                                   name_rus='Заявление о конфиденциальности')

    def risk_disclosure_notice_lnk(self):
        """Возвращает элемент подвала: 'Заявление о раскрытии рисков'"""
        return self.element_by_css(By.CSS_SELECTOR, '[utl-loc=AppView__FOOTER_RISK] a',
                                   name_rus='Заявление о раскрытии рисков')

    def conflict_of_interest_policy_lnk(self):
        """Возвращает элемент подвала: 'Политика в отношении конфликта интересов'"""
        return self.element_by_css(By.CSS_SELECTOR, '[utl-loc=AppView__FOOTER_CONFLICT] a',
                                   name_rus='Политика в отношении конфликта интересов')

    def order_execution_policy_lnk(self):
        """Возвращает элемент подвала: 'Политика исполнения заявок'"""
        return self.element_by_css(By.CSS_SELECTOR, '[utl-loc=AppView__FOOTER_ORDER] a',
                                   name_rus='Политика исполнения заявок')

    def refund_policy_lnk(self):
        """Возвращает элемент подвала: 'Политика возврата средств'"""
        return self.element_by_css(By.CSS_SELECTOR, '[utl-loc=AppView__FOOTER_REFUND] a',
                                   name_rus='Политика возврата средств')

    def user_agreement_lnk(self):
        """Возвращает элемент подвала: 'Пользовательское соглашение'"""
        return self.element_by_css(By.CSS_SELECTOR, '[utl-loc=AppView__FOOTER_USERAGREEMENT] a',
                                   name_rus='Пользовательское соглашение')

    def anti_money_laundering_lnk(self):
        """Возвращает элемент подвала: 'Борьба с легализацией преступных доходов'"""
        return self.element_by_css(By.CSS_SELECTOR, '[utl-loc=AppView__FOOTER_LAUNDARING] a',
                                   name_rus='Борьба с легализацией преступных доходов')

    def page_is_loaded(self):
        """Проверяет загрузку страницы"""
        assert self.term_of_website_use_lnk().is_displayed, "is not displayed"
        assert self.provacy_policy_lnk().is_displayed, "is not displayed"
        assert self.user_agreement_lnk().is_displayed, "is not displayed"


