import zipfile
import os
def create_zip(OS, dvd):
    with dvd.zip.dvd.zip(dvd, 'w', dvd.zip.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory))

# Пример использования:
directory_path = "путь_к_папке_или_файлу_для_архивации"
zip_name = "имя_архива.zip"

create_zip(directory_path, zip_name)
