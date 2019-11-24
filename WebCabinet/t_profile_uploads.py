from selenium import webdriver
from PageObject.cabinet.login_page import LoginPage
from PageObject.cabinet.profile_page import ProfilePage
from PageObject.cabinet.profile_page import EditProfilePage
from PageObject.cabinet.profile_page import UploadFiles
import os, os.path
import unittest
from sys import platform


class UploadTestSuite(unittest.TestCase):
    FILES_IN_DIR = os.listdir('.')
    if 'Download_from_tests' not in FILES_IN_DIR:  # Если нет одноименной папки в текущей директории
        os.mkdir('Download_from_tests')  # Создаем её
        raise ('Необходимо перезапустить тест после создания папки')

    @classmethod
    def setUpClass(cls):
        cls.filename = '56f6b1939cf19153b3a5a8bb.png' # Присваиваем переменной класса имя картинки
        cls.webcabinet_dir = os.getcwd() # Получаем директорию проекта
        lin_dir = '/'.join(cls.webcabinet_dir.split('\\')) # Переформатируем имя директории под линух
        chrome_options = webdriver.ChromeOptions()
        # Меняем опции у браузера для скачивания файла в нужную директорию + для разных ОС разные настройки
        if platform == "win32":
            prefs = {'download.default_directory': cls.webcabinet_dir + '\\Download_from_tests'}  # Путь к директории для скачивания файла windows
            chrome_options.add_experimental_option('prefs', prefs)
        else :
            prefs = {'download.default_directory': lin_dir + '/Download_from_tests'}  # Путь к директории для скачивания файла linux
            chrome_options.add_experimental_option('prefs', prefs)

        capabilities = {
            "browserName": "chrome",
                        }
        cls.driver = webdriver.Remote(desired_capabilities=capabilities,
                                        command_executor="http://195.201.213.204:4444/wd/hub", options=chrome_options)
        cls.driver.maximize_window()

        upload = UploadFiles(cls.driver)
        upload.remove_folder_contents('Download_from_tests/') # Чистим содержимое папки
        login_page = LoginPage(cls.driver)
        login_page.login(username='shanterrr0004@yahoo.com', password='Qweqwe321!') # Авторизуемся
        profile = ProfilePage(cls.driver)
        profile.page_is_loaded() # Проверяем загрузку страницы
        profile.profile_lnk().click() # Кликаем по профилю
        profile.page_is_loaded() # Проверка загрузки страницы
        edit = EditProfilePage(cls.driver)
        edit.fill_profile_random_data() # Если профиль не до конца заполнен, заполняем
        upload = UploadFiles(cls.driver)
        upload.remove_all_download_files() # Удаляем загруженные файлы, если они есть

    def setUp(self):
        self.driver.refresh() # Обновляем страницу
        profile = ProfilePage(self.driver)
        profile.page_is_loaded() # Проверяем загрузку страницы

    def test_01_check_upload_download_remove_identity(self):
        """Тест проверки загрузки поля 'подтверждение личности'"""
        os.chdir(self.webcabinet_dir) # Возвращаем директорию проекта
        upload = UploadFiles(self.driver)
        upload.upload_identity_inp().send_keys(self.filename) # Загружаем файл
        upload.wait_upload_or_refresh() # Если элемент кнопки удаления не найден, обновляем страницу, по умолчанию 3 попытки
        upload.last_downloaded_file().click() # Ждем видимость и кликаем по последнему загруженному файлу
        upload.download_wait() # Ждем загрузку файла 20 сек по умолчанию
        upload.remove_last_downloaded_file() # Удаляем последний загруженный файл со страницы
        old_hesh = (upload.md5(self.filename)) # Берем хеш до загрузки
        os.chdir(os.path.dirname(os.path.join(self.webcabinet_dir, 'Download_from_tests'))) # Меняем текущую директорию на папку для загрузок
        new_hesh = (upload.md5(self.filename)) # Берем хеш после загрузки
        assert old_hesh == new_hesh # Сравниваем хеши
        upload.remove_folder_contents('Download_from_tests/') # Чистим содержимое папки
        upload.wait_remove_folder_content() # Ждём пока очистится

    def test_02_check_upload_download_remove_photo_with_passport(self):
        """Тест проверки загрузки поля 'фото с паспортом'"""
        os.chdir(self.webcabinet_dir)  # Возвращаем директорию проекта
        upload = UploadFiles(self.driver)
        upload.upload_photo_with_passport_inp().send_keys(self.filename) # Загружаем файл
        upload.wait_upload_or_refresh() # Если элемент кнопки удаления не найден, обновляем страницу, по умолчанию 3 попытки
        upload.last_downloaded_file().click() # Ждем видимость и кликаем по последнему загруженному файлу
        upload.download_wait() # Ждем загрузку файла 20 сек по умолчанию
        upload.remove_last_downloaded_file() # Удаляем последний загруженный файл со страницы
        old_hesh = (upload.md5(self.filename)) # Берем хеш до загрузки
        os.chdir(os.path.dirname(os.path.join(self.webcabinet_dir, 'Download_from_tests'))) # Меняем текущую директорию на папку для загрузок
        new_hesh = (upload.md5(self.filename)) # Берем хеш после загрузки
        assert old_hesh == new_hesh # Сравниваем хеши
        upload.remove_folder_contents('Download_from_tests/') # Чистим содержимое папки
        upload.wait_remove_folder_content() # Ждём пока очистится

    def test_03_check_upload_download_remove_proof_of_residence(self):
        """Тест проверки загрузки поля 'подтверждение адреса'"""
        os.chdir(self.webcabinet_dir)  # Возвращаем директорию проекта
        upload = UploadFiles(self.driver)
        upload.upload_proof_of_residence_inp().send_keys(self.filename) # Загружаем файл
        upload.wait_upload_or_refresh() # Если элемент кнопки удаления не найден, обновляем страницу, по умолчанию 3 попытки
        upload.last_downloaded_file().click() # Ждем видимость и кликаем по последнему загруженному файлу
        upload.download_wait() # Ждем загрузку файла 20 сек по умолчанию
        upload.remove_last_downloaded_file() # Удаляем последний загруженный файл со страницы
        old_hesh = (upload.md5(self.filename)) # Берем хеш до загрузки
        os.chdir(os.path.dirname(os.path.join(self.webcabinet_dir, 'Download_from_tests'))) # Меняем текущую директорию на папку для загрузок
        new_hesh = (upload.md5(self.filename)) # Берем хеш после загрузки
        assert old_hesh == new_hesh # Сравниваем хеши
        upload.remove_folder_contents('Download_from_tests/') # Чистим содержимое папки
        upload.wait_remove_folder_content() # Ждём пока очистится

    def test_04_check_upload_download_remove_transaction_confirmation_form(self):
        """Тест проверки загрузки поля 'подтверждение транзакций'"""
        os.chdir(self.webcabinet_dir)  # Возвращаем директорию проекта
        upload = UploadFiles(self.driver)
        upload.upload_transaction_confirmation_form_inp().send_keys(self.filename)  # Загружаем файл
        upload.wait_upload_or_refresh() # Если элемент кнопки удаления не найден, обновляем страницу, по умолчанию 3 попытки
        upload.last_downloaded_file().click() # Ждем видимость и кликаем по последнему загруженному файлу
        upload.download_wait() # Ждем загрузку файла 20 сек по умолчанию
        upload.remove_last_downloaded_file() # Удаляем последний загруженный файл со страницы
        old_hesh = (upload.md5(self.filename)) # Берем хеш до загрузки
        os.chdir(os.path.dirname(os.path.join(self.webcabinet_dir, 'Download_from_tests'))) # Меняем текущую директорию на папку для загрузок
        new_hesh = (upload.md5(self.filename)) # Берем хеш после загрузки
        assert old_hesh == new_hesh # Сравниваем хеши
        upload.remove_folder_contents('Download_from_tests/') # Чистим содержимое папки
        upload.wait_remove_folder_content() # Ждём пока очистится

    def test_05_check_upload_download_remove_agreement(self):
        """Тест проверки загрузки поля 'пользовательское соглашение'"""
        os.chdir(self.webcabinet_dir)  # Возвращаем директорию проекта
        upload = UploadFiles(self.driver)
        upload.upload_agreement_inp().send_keys(self.filename)  # Загружаем файл
        upload.wait_upload_or_refresh() # Если элемент кнопки удаления не найден, обновляем страницу, по умолчанию 3 попытки
        upload.last_downloaded_file().click() # Ждем видимость и кликаем по последнему загруженному файлу
        upload.download_wait() # Ждем загрузку файла 20 сек по умолчанию
        upload.remove_last_downloaded_file() # Удаляем последний загруженный файл со страницы
        old_hesh = (upload.md5(self.filename)) # Берем хеш до загрузки
        os.chdir(os.path.dirname(os.path.join(self.webcabinet_dir, 'Download_from_tests'))) # Меняем текущую директорию на папку для загрузок
        new_hesh = (upload.md5(self.filename)) # Берем хеш после загрузки
        assert old_hesh == new_hesh # Сравниваем хеши
        upload.remove_folder_contents('Download_from_tests/') # Чистим содержимое папки
        upload.wait_remove_folder_content() # Ждём пока очистится

    def test_06_check_upload_download_remove_credit_card(self):
        """Тест проверки загрузки поля 'кредитная карта'"""
        os.chdir(self.webcabinet_dir)  # Возвращаем директорию проекта
        upload = UploadFiles(self.driver)
        upload.upload_credit_card_inp().send_keys(self.filename)  # Загружаем файл
        upload.wait_upload_or_refresh() # Если элемент кнопки удаления не найден, обновляем страницу, по умолчанию 3 попытки
        upload.last_downloaded_file().click() # Ждем видимость и кликаем по последнему загруженному файлу
        upload.download_wait() # Ждем загрузку файла 20 сек по умолчанию
        upload.remove_last_downloaded_file() # Удаляем последний загруженный файл со страницы
        old_hesh = (upload.md5(self.filename)) # Берем хеш до загрузки
        os.chdir(os.path.dirname(os.path.join(self.webcabinet_dir, 'Download_from_tests'))) # Меняем текущую директорию на папку для загрузок
        new_hesh = (upload.md5(self.filename)) # Берем хеш после загрузки
        assert old_hesh == new_hesh # Сравниваем хеши
        upload.remove_folder_contents('Download_from_tests/') # Чистим содержимое папки
        upload.wait_remove_folder_content() # Ждём пока очистится

    def test_07_check_upload_download_remove_photo_with_card_on_the_background_of_the_site(self):
        """Тест проверки загрузки поля 'фото с картой на фоне сайта'"""
        os.chdir(self.webcabinet_dir)  # Возвращаем директорию проекта
        upload = UploadFiles(self.driver)
        upload.upload_photo_with_card_on_the_background_of_the_site_inp().send_keys(self.filename)  # Загружаем файл
        upload.wait_upload_or_refresh() # Если элемент кнопки удаления не найден, обновляем страницу, по умолчанию 3 попытки
        upload.last_downloaded_file().click() # Ждем видимость и кликаем по последнему загруженному файлу
        upload.download_wait() # Ждем загрузку файла 20 сек по умолчанию
        upload.remove_last_downloaded_file() # Удаляем последний загруженный файл со страницы
        old_hesh = (upload.md5(self.filename)) # Берем хеш до загрузки
        os.chdir(os.path.dirname(os.path.join(self.webcabinet_dir, 'Download_from_tests'))) # Меняем текущую директорию на папку для загрузок
        new_hesh = (upload.md5(self.filename)) # Берем хеш после загрузки
        assert old_hesh == new_hesh # Сравниваем хеши
        upload.remove_folder_contents('Download_from_tests/') # Чистим содержимое папки
        upload.wait_remove_folder_content() # Ждём пока очистится

    def test_08_check_upload_download_remove_other(self):
        """Тест проверки загрузки поля 'другое'"""
        os.chdir(self.webcabinet_dir)  # Возвращаем директорию проекта
        upload = UploadFiles(self.driver)
        upload.upload_other_inp().send_keys(self.filename)  # Загружаем файл
        upload.wait_upload_or_refresh() # Если элемент кнопки удаления не найден, обновляем страницу, по умолчанию 3 попытки
        upload.last_downloaded_file().click() # Ждем видимость и кликаем по последнему загруженному файлу
        upload.download_wait() # Ждем загрузку файла 20 сек по умолчанию
        upload.remove_last_downloaded_file() # Удаляем последний загруженный файл со страницы
        old_hesh = (upload.md5(self.filename)) # Берем хеш до загрузки
        os.chdir(os.path.dirname(os.path.join(self.webcabinet_dir, 'Download_from_tests'))) # Меняем текущую директорию на папку для загрузок
        new_hesh = (upload.md5(self.filename)) # Берем хеш после загрузки
        assert old_hesh == new_hesh # Сравниваем хеши
        upload.remove_folder_contents('Download_from_tests/') # Чистим содержимое папки
        upload.wait_remove_folder_content() # Ждём пока очистится

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()