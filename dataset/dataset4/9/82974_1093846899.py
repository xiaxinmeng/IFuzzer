import pathlib
p = pathlib.Path(".", "a", "b", "c")
p
WindowsPath('a/b/c')
p.resolve(strict=False)
WindowsPath('C:/Python36/Scripts/a')