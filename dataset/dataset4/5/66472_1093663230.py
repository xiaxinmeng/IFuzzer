dir = Path("/a/directory/")
file = Path("/a/file")
print(dir.match("*/")) # True
print(file.match("*/")) # True