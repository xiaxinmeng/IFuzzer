import io
from zipfile import ZipFile, Path

def make_zip():
    """Make zip file and return bytes."""
    bytes_io = io.BytesIO()
    zip_file = ZipFile(bytes_io, mode="w")
    zip_path = Path(zip_file, "file-a")
    
    # use zipp.Path.open
    with zip_path.open(mode="w") as fp:
        fp.write(b"contents of file-a")

    zip_file.close()

    data = bytes_io.getvalue()

    bytes_io.close()
    
    return data

zip_data = make_zip()
# Exception ignored in: <function ZipFile.__del__ at 0x10922e670>
# Traceback (most recent call last):
#   File "/Users/nick/.pyenv/versions/3.8.3/lib/python3.8/zipfile.py", line 1820, in __del__
#     self.close()
#   File "/Users/nick/.pyenv/versions/3.8.3/lib/python3.8/zipfile.py", line 1837, in close
#     self.fp.seek(self.start_dir)
# ValueError: I/O operation on closed file.