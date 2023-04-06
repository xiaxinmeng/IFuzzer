
import zipfile


class TestClass:
    def __init__(self, path):
        self.zip_file = zipfile.ZipFile(path)

    def iter_dir(self):
        return [each.name for each in zipfile.Path(self.zip_file).iterdir()]

    def read(self, filename):
        with self.zip_file.open(filename) as file:
            print(file.read())

root = "zipfile.zip"
test = TestClass(root)
files = test.iter_dir()
test.read(files[0])
