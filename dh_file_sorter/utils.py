"""Модуль вспомогательных утилит"""

__author__: str = "Digital Horizons"

from pathlib import Path


def get_path_inst(path: str | None) -> Path:
    """
    Получить экземпляр Path с проверкой существования пути и что он является директорией

    :param path: путь до папки
    :type path: str | None
    :return: экземпляр Path
    :rtype: Path

    :raise FileNotFoundError: переданный путь не существует
    :raise FileExistsError: переданный путь не является папкой

    .. code-block:: python
        from utils import get_path_inst

        get_path_inst("С:/Users") # Path до диска C
    """
    if path is None:
        raise ValueError('Не задан путь к файлам. Передайте путь при запуске с флагом "-p" или "--path""')

    path_inst: Path = Path(path)

    if not path_inst.exists():
        raise FileNotFoundError("Переданный путь не найден. Работа скрипта не возможна")

    if not path_inst.is_dir():
        raise FileExistsError("Переданный путь не является папкой. Работа скрипта невозможна")

    return path_inst


def get_or_create_if_not_exist_folder(path: str) -> Path:
    """
    Получение или создание папки, когда ее нет, по переданному пути

    :param path: путь до папки
    :type path: str
    :return: экземпляр Path с гарантией существования пути до переданной папки
    :rtype: Path

    :raise FileExistsError: переданный путь не является папкой

    .. code-block:: python
        from utils import get_or_create_if_not_exist_folder

        # Path до диска "С:/Users/NewUser". Если папки не было - создаст
        get_or_create_if_not_exist_folder("С:/Users/NewUser")
    """
    path_inst: Path = Path(path)

    if not path_inst.exists():
        path_inst.mkdir()
    elif path_inst.is_file():
        raise FileExistsError("Переданный путь является файлом, а должен быть папкой")

    return path_inst
