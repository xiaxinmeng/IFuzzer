import zipfile

test_zip = "time_test.zip"
test_name = "test_name.txt"

with zipfile.ZipFile(test_zip, "w") as zf:
    zf.writestr(test_name, "Hi there! " * 300)

with zipfile.ZipFile(test_zip) as zf:
    for i in range(100000):
        zf.read(test_name)