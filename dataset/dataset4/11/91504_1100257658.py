
from urllib.request import url2pathname
from pathlib import Path

def path_from_uri(uri):
    return Path(url2pathname(uri.removeprefix('file:')))
