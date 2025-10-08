"""Модуль модели файла"""

from pathlib import Path
from dataclasses import dataclass

from consts import FOLDER_NAME, FILE_EXTENSIONS_BY_TYPE, FileType


@dataclass
class FileModel:
    """
    Модель файла

    :ivar path: полный путь до файла
    """

    def __init__(self, path: str) -> None:
        self.path: Path = Path(path)

        if not self.path.is_file():
            raise ValueError(f'Переданный путь "{self.path}" не является файлом')

    @property
    def extension(self) -> str:
        """Расширение файла"""
        return self.path.suffix.lower()

    @property
    def is_image(self) -> bool:
        """Флаг, что файл является изображением"""
        return self.extension in FILE_EXTENSIONS_BY_TYPE[FileType.IMAGE]

    @property
    def is_video(self) -> bool:
        """Флаг, что файл является видео"""
        return self.extension in FILE_EXTENSIONS_BY_TYPE[FileType.VIDEO]

    @property
    def is_audio(self) -> bool:
        """Флаг, что файл является аудио"""
        return self.extension in FILE_EXTENSIONS_BY_TYPE[FileType.AUDIO]

    @property
    def is_document(self) -> bool:
        """Флаг, что файл является документом"""
        return self.extension in FILE_EXTENSIONS_BY_TYPE[FileType.DOCUMENT]

    @property
    def is_archive(self) -> bool:
        """Флаг, что файл является архивом"""
        return self.extension in FILE_EXTENSIONS_BY_TYPE[FileType.ARCHIVE]

    @property
    def is_install(self) -> bool:
        """Флаг, что файл является установочным"""
        return self.extension in FILE_EXTENSIONS_BY_TYPE[FileType.INSTALL]

    @property
    def is_other(self) -> bool:
        """Флаг, что файл не подходит под известные типы"""
        return not any(
            (
                self.is_image,
                self.is_video,
                self.is_audio,
                self.is_document,
                self.is_archive,
                self.is_install,
            )
        )

    @property
    def file_type(self) -> FileType:
        """Тип файла по его расширению"""
        match True:
            case self.is_image:
                return FileType.IMAGE
            case self.is_video:
                return FileType.VIDEO
            case self.is_audio:
                return FileType.AUDIO
            case self.is_document:
                return FileType.DOCUMENT
            case self.is_archive:
                return FileType.ARCHIVE
            case self.is_install:
                return FileType.INSTALL
            case _:
                return FileType.OTHER

    @property
    def sort_folder_name(self) -> str:
        """Название папки сортировки для файла"""
        return FOLDER_NAME.get(self.file_type) or FileType.OTHER
