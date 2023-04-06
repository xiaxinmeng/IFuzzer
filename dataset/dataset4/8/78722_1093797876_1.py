children = iter(path_that_doesnt_exist.iterdir())
while True:
    try:
        path = next(children)
    except FileNotFoundError:
        print("directory doesn't exist")
        break
    print(path.stat().st_size)