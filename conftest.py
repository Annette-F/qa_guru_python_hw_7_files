import os.path
import shutil
import zipfile
import pytest
from import_os_path import FILES_DIR, ARCHIVE_DIR, ZIP_DIR


@pytest.fixture(scope='session', autouse=True)
def create_archive():
    if not os.path.exists(ARCHIVE_DIR):  # проверяем существует ли папка
        os.mkdir(ARCHIVE_DIR)  # создаем папку если её нет
    with zipfile.ZipFile(ZIP_DIR, 'w') as archive:  # создаем архив
        for file in os.listdir(FILES_DIR):  # добавляем файлы в архив
            archive.write(os.path.join(FILES_DIR, file), file)


    yield

    shutil.rmtree(ARCHIVE_DIR)  # удаляем файлы после архивации
