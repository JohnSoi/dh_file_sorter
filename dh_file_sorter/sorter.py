"""Модуль сортера"""

__author__: str = "Digital Horizons"

from os import listdir
from shutil import move
from os.path import join, isfile
from pathlib import Path
from argparse import Namespace, ArgumentParser, BooleanOptionalAction
from functools import cached_property

from utils import get_path_inst, get_or_create_if_not_exist_folder
from file_model import FileModel
from console_manager import ConsoleManager


class FileSorter:
    """
    Класс сортера

    :ivar _dir_path: путь до папки с файлами для сортировки
    :type _dir_path: Path
    :ivar _console_manager: экземпляр для работы с выводом в консоль
    :type _console_manager: ConsoleManager
    """

    def __init__(self) -> None:
        self._dir_path, verbose = self._get_sorter_params()
        self._console_manager: ConsoleManager = ConsoleManager(verbose)

    @cached_property
    def files(self) -> list[str]:
        """Список файлов в папке"""
        return [file_name for file_name in listdir(self._dir_path) if isfile(join(self._dir_path, file_name))]

    def process(self) -> None:
        """Основной процесс сортировки файлов"""
        self._console_manager.permanent_print(f"Будет обработано файлов: {len(self.files)}")

        for file_name in self.files:
            self._console_manager.dynamic_print(f'-- Обрабатываем файл - "{file_name}"')
            file_model: FileModel = FileModel(join(self._dir_path, file_name))
            move(
                file_model.path,
                get_or_create_if_not_exist_folder(join(self._dir_path, file_model.sort_folder_name)),
            )

        self._console_manager.permanent_print("Работа скрипта завершена")

    @staticmethod
    def _get_sorter_params() -> tuple[Path, bool]:
        """
        Получение параметров сортера из вызова в консоли

        :return: путь по папки с фалами, нужен ли консольный вывод
        """
        parser: ArgumentParser = ArgumentParser(description="Сортирует файлы в определенной папке по типам")
        parser.add_argument(
            "-p",
            "--path",
            type=str,
            help="Путь к папке с файлами для сортировки"
        )
        parser.add_argument(
            "-v", "--verbose",
            type=bool,
            help="Выводить информацию о работе процесса",
            action=BooleanOptionalAction
        )
        arguments: Namespace = parser.parse_args()

        return get_path_inst(arguments.path), arguments.verbose
