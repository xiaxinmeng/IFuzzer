@contextmanager
def in_directory(path):
    pwd = str(Path().absolute())
    if not path.is_dir():
        path = path.parent
    os.chdir(str(path))
    yield path.absolute()
    os.chdir(pwd)