
import os
import pathlib
import tempfile

with tempfile.TemporaryDirectory(prefix="path_test_") as path:
    new_path = pathlib.Path(path, "A"*255, "B"*255)
    extended_path = "\\\\?\\%s" % new_path
    os.makedirs(extended_path)
    print(len(extended_path), extended_path)
