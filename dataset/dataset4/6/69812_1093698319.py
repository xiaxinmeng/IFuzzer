from gzip import GzipFile
from io import BytesIO
file = BytesIO()
writer = GzipFile(fileobj=file, mode="wb")
writer.write(b"data")
writer.close()
file.seek(0)
reader = GzipFile(fileobj=file, mode="rb")
data = reader.read(2**32)  # Ideally this should return b"data"