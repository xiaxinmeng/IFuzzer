from zipfile import ZipFile
import io

def foo():
    pass

data = io.BytesIO()
zf = ZipFile(data, "w")