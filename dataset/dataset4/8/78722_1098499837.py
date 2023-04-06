try:
    children = list(path_that_doesnt_exist.iterdir())
except FileNotFoundError:
    print("directory doesn't exist")
for path in children:
    print(path.stat().st_size)