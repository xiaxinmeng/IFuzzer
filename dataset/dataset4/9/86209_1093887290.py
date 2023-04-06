
class MyPath(zipfile.Path):
  pass


path = MyPath(zf)
path = path.joinpath('other')
assert isinstance(path, MyPath)  # Oups, type(path) is zipfile.Path
