import os.path

CURRENT_FILE = os.path.abspath(__file__) # получаем абсолютный путь к текущему файлу
CURRENT_DIR = os.path.dirname(CURRENT_FILE) # получаем абсолютный путь к текущей директории где находится файл с которым работаем
FILES_DIR = os.path.join(CURRENT_DIR, 'files') # делаем склейку пути к текущей директории и папки files
ARCHIVE_DIR = os.path.join(CURRENT_DIR, 'resources')
ZIP_DIR = os.path.join(ARCHIVE_DIR, 'new_archive.zip')
