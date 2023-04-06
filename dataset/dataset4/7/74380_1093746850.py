from urllib.request import urlretrieve
from os import path
from zipfile import ZipFile

download_url = "https://www.dropbox.com/s/obiqvrt4m53pmoz/tesseract-4.0.0-alpha.zip?dl=1"


def setup_program():
    zip_name = urlretrieve(download_url)

    zip_file = ZipFile(zip_name, "r")
    zip_file.extractall(path.abspath("__tesseract/"))
    zip_file.close()

setup_program()  # REMOVE after test