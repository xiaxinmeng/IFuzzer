import tempfile
import os


with tempfile.NamedTemporaryFile() as temp:
    os.remove(temp.name)