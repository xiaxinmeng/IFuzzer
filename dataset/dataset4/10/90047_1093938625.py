path = pl.Path("foo/bar")
print(path.match("bar"))
print(path.match(str(pl.Path("bar"))))
print(path.match(str(pl.Path("*"))))