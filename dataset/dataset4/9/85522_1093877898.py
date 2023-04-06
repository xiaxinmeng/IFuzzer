import io
from zipfile import ZipFile

bytes_io = io.BytesIO()
zip_file = ZipFile(bytes_io, mode="w")
bytes_io.close()
zip_file.close()  # throws ValueError