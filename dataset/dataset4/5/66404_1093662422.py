###################
import tarfile, io

tarFileIo = io.BytesIO()

tarFileObj = tarfile.open(fileobj=tarFileIo, mode="w:xz")

fileToAdd = io.BytesIO("hello world!".encode("utf-8"))

# fixes "AttributeError: '_io.BytesIO' object has no attribute 'name'"
fileToAdd.name="helloworld.txt"

# fails with 'io.UnsupportedOperation: fileno'
tarInfo = tarFileObj.gettarinfo(arcname="helloworld.txt", fileobj=fileToAdd)

# never runs
tarFileObj.addfile(tarInfo, fileobj=fileToAdd)
###################