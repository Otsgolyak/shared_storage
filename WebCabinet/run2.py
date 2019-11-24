# -*- coding: utf-8 -*-
import inspect
import subprocess
import os
import time
import logging
import sys
import json
import imp
import shutil
from importlib.machinery import SourceFileLoader


class RunTests:

    def __init__(self):

        self._init_log()
        self.options = sys.argv[1:]
        self.test_files = {}
        self.streams_number = 40
        self.delay_run_tests = 1

    def _init_log(self):
        """Инициализируем лог"""

        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        logger = logging.getLogger('run_tests')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        logger.setLevel(logging.INFO)
        self.log = logger.info

    def _generate_list_of_file_for_run(self):
        """Создаем список файлов для запуска"""

        self.log("Получаем список файлов в текущей директории")
        self.log("Запускаются только скрипты test*.py")
        all_file = os.listdir(os.getcwd())
        for file in all_file:
            if os.path.isfile(file) and file.startswith('t') \
                    and os.path.splitext(file)[1] == '.py':
                self.test_files[file] = dict(tests=[], run=False, exec_time=0, process=None)

    def _run_test(self, test):
        """Запускает тестовый набор"""

        self.log("Запускаем файл: %s" % test)
        file_run = os.path.join(os.getcwd(), test)
        commands = ['python', file_run]
        if self.options:
            commands.extend(self.options)
        self.log(commands)
        return subprocess.Popen(commands)

    def _check_files(self):
        bad_files = []
        for test_file in self.test_files:
            try:
                imp.load_source(os.path.join(os.getcwd(), test_file), test_file)
            except Exception as error:
                bad_files.append('\n\tФайл - %s\n\tПричина - %s' % (test_file, error))
        assert not bad_files, 'Не смогли запустить%s' % '\n'.join(bad_files)

    def run_tests(self):
        """Метод для запуска тестов"""

        run_test_method = self._run_tests

        start = time.time()
        run_test_method()
        exec_time = round(time.time() - start, 0)

    def _is_not_running_files(self):
        return any(filter(lambda v: not v['run'], self.test_files.values()))

    def _run_tests(self):
        """Метод для запуска и мониторинга тестов"""

        py_process = []  # В списке храняться запущенные питоновские процессы

        self._generate_list_of_file_for_run()
        self._check_files()

        self.log("Запускаем тесты")
        while self._is_not_running_files() or len(py_process) > 0:
            if (self.streams_number > len(py_process)) and self._is_not_running_files():
                test, value = next(filter(lambda v: not v[1]['run'], self.test_files.items()))
                process = self._run_test(test)
                self.test_files[test]['run'] = True
                py_process.append(process)
            else:
                # Ждем пока освободятся слоты, удаляем завершенные
                py_process = [proc for proc in py_process if proc.poll() is None]
            time.sleep(self.delay_run_tests)

    def _running_files_number(self):
        """Количестов запущенных файлов"""

        return len([value for value in self.test_files.values() if value['run'] is True])
