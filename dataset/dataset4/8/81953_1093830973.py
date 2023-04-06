from zipfile import ZipFile, Path
import io

def recurse_print(parent):
    for child in parent.iterdir():
        if child.is_file():
            print(child, child.read_text())
        if child.is_dir():
            recurse_print(child)

data = io.BytesIO()
zf = ZipFile(data, "w")
zf.writestr("a.txt", "content of a")
zf.writestr("b/c.txt", "content of c")
zf.writestr("b/d/e.txt", "content of e")
zf.writestr("b/f.txt", "content of f")
zf.filename = "abcde.zip"
root = Path(zf)
recurse_print(root)