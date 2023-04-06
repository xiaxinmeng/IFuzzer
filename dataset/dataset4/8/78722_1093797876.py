if path_that_doesnt_exist.is_dir():
    print("directory doesn't exist")
else:
    for path in children:
        print(path.stat().st_size)