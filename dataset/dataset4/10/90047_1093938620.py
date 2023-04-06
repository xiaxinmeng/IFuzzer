import pathlib as pl

path = pl.Path("foo/bar")
print(path.match("bar"))
print(path.match(pl.Path("bar")))