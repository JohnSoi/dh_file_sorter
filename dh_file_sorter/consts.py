"""Модуль констант сортера"""

__author__: str = "Digital Horizons"

from enum import StrEnum


class FileType(StrEnum):
    """
    Типы файлов для сортировки

    :cvar IMAGE: изображения
    :cvar VIDEO: видео
    :cvar AUDIO: аудио
    :cvar DOCUMENT: документы, таблицы, презентации
    :cvar ARCHIVE: архивы
    :cvar INSTALL: установочные файлы
    :cvar OTHER: остальные
    """

    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    DOCUMENT = "document"
    ARCHIVE = "archive"
    INSTALL = "install"
    OTHER = "other"


# Название папок по типам файлов
FOLDER_NAME: dict[FileType, str] = {
    FileType.IMAGE: "Image",
    FileType.AUDIO: "Audio",
    FileType.VIDEO: "Video",
    FileType.DOCUMENT: "Document",
    FileType.ARCHIVE: "Archive",
    FileType.INSTALL: "Install",
    FileType.OTHER: "Others",
}

# Список расширений файлов по типам
FILE_EXTENSIONS_BY_TYPE: dict[FileType, tuple[str, ...]] = {
    FileType.IMAGE: (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff"),
    FileType.AUDIO: (".mp3", ".wav", ".aiff", ".aiff"),
    FileType.VIDEO: (".mp4", ".avi"),
    FileType.DOCUMENT: (".doc", ".docx", ".pptx", ".ppt", ".xls", ".xlsx", ".txt"),
    FileType.ARCHIVE: (".zip", ".7z", ".rar"),
    FileType.INSTALL: (".exe", ".msi"),
}
