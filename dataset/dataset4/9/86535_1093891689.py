import multiprocessing.pool, zipfile

# Create a ZipFile with two files and same content
with zipfile.ZipFile("test.zip", "w", zipfile.ZIP_STORED) as z:
    z.writestr("file1", b"0"*10000)
    z.writestr("file2", b"0"*10000)

# Read file1  with two threads at once
with zipfile.ZipFile("test.zip", "r") as z:
    pool = multiprocessing.pool.ThreadPool(2)
    while True:
        pool.map(z.read, ["file1", "file1"])