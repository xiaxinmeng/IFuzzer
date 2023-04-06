data = io.BytesIO()
zf = ZipFile(data, "w")
zf.writestr("a.txt", "content of a")
zf.writestr("b/d/e.txt", "content of e")
zf.filename = "abcde.zip"
root = Path(zf)
recurse_print(root)